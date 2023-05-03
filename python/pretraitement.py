import pandas as pd
import numpy as np

def get_item_make_arrays(df,nb_colonnes):
    ''' 
        Retourne toutes les catégories et les marques présentes dans le DataFrame df
        nb_colonnes correspond au nombre d'objets sur lequel on se limite 
        (la plupart des paniers safes et frauduleux sont à 4objets et il n'y a pas d'augmentation de la fraude au dessus de 5objets)
    '''
    items = []
    marques = []
    for i in range(1, nb_colonnes+1):
        items.append(df['item'+str(i)].astype(str).unique())
        marques.append(df['make'+str(i)].astype(str).unique())

    tableau_des_items = np.unique(np.concatenate(items))
    tableau_des_marques = np.unique(np.concatenate(marques))

    return tableau_des_items, tableau_des_marques


def dataframe_make(df, tab_make,nb_colonnes):
    ''' 
        Fait un one-hot encoding sur les marques du Dataframe df
        
        Args:
            - df (pd.DataFrame): Dataframe avec au moins 24 colonnes "make" & "item"
            - tab_make (Numpy array): tableau qui contient toutes les marques qui serviront de colonne
            
        Returns:
            df_make : DataFrame 'ID' + une colonne par marque
        '''
    col = ['ID'] + tab_make
    df_make = pd.DataFrame(columns=col, index=df.index)

    for row in df.index:
        for i in range(1, nb_colonnes+1):
            marque = df[f'make{i}'][row]
            nb_items = df[f"Nbr_of_prod_purchas{i}"][row]

            if type(marque) == float: # Stop si valeur nulle. J'ai essayé de retirer cette partie mais ça plante. Dans le doute, on laisse
                break
        
            make_column = f"{marque}"
            if make_column in df_make.columns:
                df_make[make_column][row] = nb_items

    return df_make


def dataframe_item(df, tab_item, nb_colonnes):
    ''' 
        Fait un one-hot encoding sur les catégories du Dataframe df
        
        Args:
            - df (pd.DataFrame): Dataframe avec au moins 24 colonnes "make" & "item"
            - tab_item (Numpy array): tableau qui contient toutes les catégories qui serviront de colonne
            
        Returns:
            df_item : DataFrame 'ID' + une colonne par catégorie
        '''
    df_item = pd.DataFrame(columns=tab_item, index=df.index)

    for row in df.index:
        for i in range(1, nb_colonnes+1):
            item_column = f"{df[f'item{i}'][row]}"
            nb_items = df[f"Nbr_of_prod_purchas{i}"][row]

            if item_column in df_item.columns:
                df_item[item_column][row] = nb_items

    return df_item


    
            