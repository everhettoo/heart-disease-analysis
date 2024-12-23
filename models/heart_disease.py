class HeartDisease():
    AGE                     = "Age"                     # age
    GENDER                  = "Gender"                  # sex
    CHEST_PAIN              = "Chest Pain"              #cp
    BP_SYSTOLIC             = "BP Systolic"             # trestbps
    CHOLESTEROL             = "Cholesterol"             # chol
    BLOOD_SUGAR             = "Blood Sugar"             # fbs
    REST_ECG                = "Rest ECG"                # restecg
    EXE_MAX_HEARTRATE        = "Exe. Max Heartrate"      # thalach
    EXE_ANGINA              = "Exercise Exe. Angina"    # exang
    EXE_ST_DEPRESSION       = "Exe. ST Depression"      # old[peak
    EXE_ST_SEGMENT_SLOPE    = "Exe. ST Segment Slope"   # slope
    MAJOR_VESSELS           = "Major Vessels"           # ca
    THALASSEMIA             = "Thalassemia"             # thal
    TARGET                  = "Target"                  # num

def get_standard_features():
    result = []
    result.append(HeartDisease.AGE)
    result.append(HeartDisease.GENDER)
    result.append(HeartDisease.CHEST_PAIN)
    result.append(HeartDisease.BP_SYSTOLIC)
    result.append(HeartDisease.CHOLESTEROL)
    result.append(HeartDisease.BLOOD_SUGAR)
    result.append(HeartDisease.REST_ECG)
    result.append(HeartDisease.EXE_MAX_HEARTRATE)
    result.append(HeartDisease.EXE_ANGINA)
    result.append(HeartDisease.EXE_ST_DEPRESSION)
    result.append(HeartDisease.EXE_ST_SEGMENT_SLOPE)
    result.append(HeartDisease.MAJOR_VESSELS)
    result.append(HeartDisease.THALASSEMIA)
    result.append(HeartDisease.TARGET)
    return result

def get_reduced_features():
    result = []
    result.append(HeartDisease.AGE)
    result.append(HeartDisease.CHEST_PAIN)
    result.append(HeartDisease.BP_SYSTOLIC)
    result.append(HeartDisease.CHOLESTEROL)
    result.append(HeartDisease.REST_ECG)
    result.append(HeartDisease.EXE_MAX_HEARTRATE)
    result.append(HeartDisease.EXE_ANGINA)
    result.append(HeartDisease.EXE_ST_DEPRESSION)
    result.append(HeartDisease.MAJOR_VESSELS)
    result.append(HeartDisease.THALASSEMIA)
    result.append(HeartDisease.TARGET)
    return result



