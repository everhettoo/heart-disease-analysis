"""
Acknowledgement : Code was referenced from Prof. Mafas Raheem's AML labs.
Description     : This helper module is to provide necessary parameters and functions for seamless model
                  validation.
"""
import warnings
from collections import Counter

import matplotlib.pyplot as plt
import seaborn as sns
import math as math
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# # Dictionary to store global model's accuracies for result comparisons.
# global_accuracies = {}

# Dictionary to store accuracies for result comparisons.
accuracies = {}

# Randomness to reproduce same splits for comparisons.
random_state = 1

# K-fold split for cv.
kfold_n_split =5

# K-fold shuffle for cv.
kfold_shuffle =True


"""
There are two datasets used, and each has three types of evaluations:
Datasets:
- Standard          - a preprocessed dataset.
- Over sampled      - the preprocessed dataset was oversampled for class balancing.
 
Evaluations:
- base model        - without hyperparameter tuning and cross validation.
- grid-search-cv    - used for hyperparameter tuning and cross-validation.
- random-search-cv  - used for hyperparameter tuning and cross-validation. 

"""
class EvaluationType:
    # Standard data with base model.
    std_base                = "std-base"
    # Standard data with grid search cv.
    std_grid_search_cv      = "std-grid-scv"
    # Standard data with random search cv.
    std_random_search_cv    = "std-rand-scv"

    # Over sampled data with base model.
    os_base                = "os-base"
    # Over sampled data with grid search cv.
    os_grid_search_cv      = "os-grid-scv"
    # Over sampled data with random search cv.
    os_random_search_cv    = "os-rand-scv"


"""
Description     : A function to display classification-report, confusion-matrix and ROC curve for model 
                  result analysis. Returns accuracy from classification report.
"""
def display_validation_report(y_test, y_pred, x_test, classifier):
    # Manually calculate accuracy in % of the test-set and prediction result.
    # acc_score = accuracy_score(y_test, y_pred) * 100
    # accuracies[test_name] = math.ceil(acc_score)

    # Display the classification report for test-set vs prediction.
    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    # Retrieve accuracy from classification-report.
    acc_result = classification_report(y_test, y_pred, output_dict=True)
    accuracy = acc_result['accuracy'] * 100

    # Display the confusion matrix for test-set vs prediction.
    print("\nConfusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize = (3, 3))
    sns.heatmap(cm, annot=True, linewidths = .5, square = True, cmap = 'Blues', cbar = False)
    plt.ylabel('Truth')
    plt.xlabel('Predicted')

    # Display ROC Curve.
    RocCurveDisplay.from_estimator(estimator = classifier, X = x_test, y = y_test);

    return math.ceil(accuracy)


"""
Description     : A function to scale and do train and test splits.
"""
def scale_and_split(x_set, y_set):
    # Some algo like SVM is very slow with unscaled/normalized data.
    scaler = StandardScaler()
    x_set = scaler.fit_transform(x_set)

    # The random-state ensures to split is deterministic (same set for reproducing same results).
    # Meanwhile, stratify ensures the classes are evenly split for train and test.
    return train_test_split(x_set, y_set, test_size = 0.20, stratify=y_set, random_state=random_state)