"""
Acknowledgement : Code was referenced from Prof. Mafas Raheem's AML labs.
Description     : Most steps for building a classifier is repeating. The code from different labs were refactored to
                  provide seamless steps for building classifiers and testing.
"""
from collections import Counter

from sklearn.metrics import classification_report, confusion_matrix, RocCurveDisplay
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
import pandas as pd
import models.global_data as gd
from sklearn.model_selection import GridSearchCV

"""
Description: 
"""
def get_class_counters(y_set, y_train, y_test):
    data = [['Entire', Counter(y_set).get(0), Counter(y_set).get(1)],
            ['Train', Counter(y_train).get(0), Counter(y_train).get(1)],
            ['Test', Counter(y_test).get(0), Counter(y_test).get(1)], ]
    # print(data)
    return pd.DataFrame(data, columns=['Set','0','1'])


"""
Description: Performs scaling on the dataset first, and then split according to the supplied. parameters. 
"""
def scale_and_split(x_set, y_set, test_size, stratify, random_state):
    # Some classifiers are very slow with unscaled/normalized data (E.g. SVM).
    scaler = StandardScaler()
    x_set = scaler.fit_transform(x_set)

    # The random-state does deterministic split (same sets for reproducing results across model evaluations).
    # Meanwhile, stratify ensures the classes are evenly split for both train and test sets.
    if stratify:
        return train_test_split(x_set, y_set, test_size = test_size, stratify=y_set, random_state=random_state)
    else:
        return train_test_split(x_set, y_set, test_size = test_size, random_state=random_state)


"""
Description: A function to display classification-report, confusion-matrix and ROC curve for model 
                  result analysis.
"""
def create_validation_report(y_test, y_pred, x_test, classifier, test_name, verbose=False):
    # Dictionary for storing evaluation results.
    result = {}

    # Creates classification report for test-set vs prediction.
    print(f"\nCreating classification-report for [{test_name}] ...")

    if verbose:
        print(classification_report(y_test, y_pred))

    # Stores few metrics from classification-reports. Accuracy is one of then and can be accessed result['accuracy'].
    result[gd.ValidationReportKey.classification_report] = classification_report(y_test, y_pred, output_dict=True)

    # Stores the confusion matrix for test-set vs prediction.
    print(f"\nCreating confusion-matrix for [{test_name}] ...")

    if verbose:
        print(confusion_matrix(y_test, y_pred))

    result[gd.ValidationReportKey.confusion_matrix] = confusion_matrix(y_test, y_pred)

    print(f"\nEvaluation result was created for [{test_name}] ...")

    return result

"""
Description: Builds a basic model using the x-sets, and predicts using the y-train set. 
"""
def fine_tune_with_grid_search_cv(cls, x_train, y_train, x_test, parameters, folds, test_name):
    print(f'\nEvaluation name: [{test_name}]. Fine tuning model...')

    grid_scv = GridSearchCV(cls, parameters, scoring='accuracy', cv=folds)

    # Train the model with training set.
    # Without the random-state, DT is producing different result despite the random-state in sample split for training-set.
    grid_scv.fit(x_train, y_train)

    # Display the best hyperparameters and score. The best score is mean of CV scores for train-set.
    print(f'Best params          :{grid_scv.best_params_}.')
    print(f'Best score (*mean)   :{grid_scv.best_score_}.')

    # Do prediction with the trained model.
    return grid_scv.predict(x_test)

# """
# Description: Builds a basic model using the x-sets, and predicts using the y-train set.
# """
# def fine_tune_and_predict(cls, x_train, y_train, x_test, test_name):
#     print(f'\nEvaluation name: [{test_name}]. Fine-tuning model and cross-validating ...')
#     # Train the model with training set.
#     # Without the random-state, DT is producing different result despite the random-state in sample split for training-set.
#     cls.fit(x_train, y_train)
#
#     if fine_tune:
#         # Display the best hyperparameters and score. The best score is mean of CV scores for train-set.
#         print(f'Best params          :{cls.best_params_}.')
#         print(f'Best score (*mean)   :{cls.best_score_}.')
#     else:
#         # Display the best hyperparameters used.
#         print(f'Params:{ cls.get_params()}.')
#
#     # Do prediction with the trained model.
#     return cls.predict(x_test)
# #     # Do prediction with the trained model.
# #     return cls.predict(x_test)


