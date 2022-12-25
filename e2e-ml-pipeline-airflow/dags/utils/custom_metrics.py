import mlflow
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, \
    r2_score, confusion_matrix, classification_report, accuracy_score, \
    precision_score, recall_score, f1_score


def log_confusion_matrix(y_test: list, y_pred: list):
    cm = confusion_matrix(y_test, y_pred)
    ax = sns.heatmap(cm, annot=True, cmap='Blues')
    ax.set_title('Confusion Matrix with labels\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ')
    fig = ax.get_figure()
    mlflow.log_figure(fig, 'conf_matrix.png')


def log_classification_report(y_test: list, y_pred: list):
    cr = classification_report(y_test, y_pred, output_dict=True)
    cr_metrics = pd.json_normalize(cr, sep='_').to_dict(orient='records')[0]
    mlflow.log_metrics(cr_metrics)

def eval_metrics(y_test: list, y_pred: list):
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)
    mlflow.log_metric("mae", mae)


def log_all_eval_metrics(y_test: list, y_pred: list):
    
    # Classification Report
    log_classification_report(y_test, y_pred)

    # Confusion Matrix
    log_confusion_matrix(y_test, y_pred)

