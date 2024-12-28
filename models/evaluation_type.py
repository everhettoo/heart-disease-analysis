"""
There are two datasets used, and each has three types of evaluations:

Datasets:
- Standard          - a preprocessed dataset.
- Over sampled      - the preprocessed dataset was oversample for class balancing.

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
    os_base                 = "os-base"
    # Over sampled data with grid search cv.
    os_grid_search_cv       = "os-grid-scv"
    # Over sampled data with random search cv.
    os_random_search_cv     = "os-rand-scv"