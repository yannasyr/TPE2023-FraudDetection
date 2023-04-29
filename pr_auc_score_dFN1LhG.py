import numpy as np
import sklearn

from sklearn.metrics import average_precision_score



def pr_auc_score(y_true, y_pred_proba):
    ''' 
    Return the area under the Precision-Recall curve.
    
    Args:
        - y_true (pd.DataFrame): Dataframe with a unique identifier for each observation (first column) and the ground truth observations (second column).
        - y_pred_proba (pd.DataFrame): Dataframe with a unique identifier for each observation (first column) and the predicted probabilities estimates for the minority class (second column).
        
    Returns:
        float
    '''
    
    y_true_sorted = y_true.sort_values(by='ID').reset_index(drop=True)
    y_pred_proba_sorted = y_pred_proba.sort_values(by='ID').reset_index(drop=True)
    pr_auc_score = average_precision_score(np.ravel(y_true_sorted.iloc[:, 1]), np.ravel(y_pred_proba_sorted.iloc[:, 1]))

    return pr_auc_score



# The following lines show how the csv files are read
if __name__ == '__main__':
    import pandas as pd
    y_true_path = 'Y_test.csv'  # path of the y_true csv file
    y_pred_proba_path = 'Y_test_benchmark.csv'  # path of the y_pred csv file
    y_true = pd.read_csv(y_true_path, index_col=0)
    y_pred_proba = pd.read_csv(y_pred_proba_path, index_col=0)
    print(pr_auc_score(y_true, y_pred_proba))



