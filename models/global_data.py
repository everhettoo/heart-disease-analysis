# Dictionary to store local model's accuracies for result comparisons.
accuracies = {}

# Randomness to reproduce same splits for comparisons.
random_state = 1

# K-fold split for cv.
k_fold_n_split =5

# K-fold shuffle for cv.
k_fold_shuffle =True

class ValidationReportKey:
    classification_report   = "classification_report"
    confusion_matrix        = "confusion_matrix"
    roc_curve               = "roc_curve"

class DataSplitStrategy:
    test_size       = 0.20
    stratify        = True
    random_state    = 1