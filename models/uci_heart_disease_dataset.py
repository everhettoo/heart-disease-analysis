class UCIHeartDiseaseData:
    age                     = "Age"                     # age
    gender                  = "Gender"                  # sex
    chest_pain              = "Chest Pain"              #cp
    bp_systolic             = "BP Systolic"             # trestbps
    cholesterol             = "Cholesterol"             # chol
    blood_sugar             = "Blood Sugar"             # fbs
    rest_ecg                = "Rest ECG"                # restecg
    exe_max_heartrate       = "Exe. Max Heartrate"      # thalach
    exe_induced_angina      = "Exe. induced Angina"     # exang
    exe_st_depression       = "Exe. ST Depression"      # old[peak
    exe_st_segment_slope    = "Exe. ST Segment Slope"   # slope
    major_vessels           = "Major Vessels"           # ca
    thalassemia             = "Thalassemia"             # thal
    target                  = "Target"                  # num

def get_standard_features():
    result = []
    result.append(UCIHeartDiseaseData.age)
    result.append(UCIHeartDiseaseData.gender)
    result.append(UCIHeartDiseaseData.chest_pain)
    result.append(UCIHeartDiseaseData.bp_systolic)
    result.append(UCIHeartDiseaseData.cholesterol)
    result.append(UCIHeartDiseaseData.blood_sugar)
    result.append(UCIHeartDiseaseData.rest_ecg)
    result.append(UCIHeartDiseaseData.exe_max_heartrate)
    result.append(UCIHeartDiseaseData.exe_induced_angina)
    result.append(UCIHeartDiseaseData.exe_st_depression)
    result.append(UCIHeartDiseaseData.exe_st_segment_slope)
    result.append(UCIHeartDiseaseData.major_vessels)
    result.append(UCIHeartDiseaseData.thalassemia)
    result.append(UCIHeartDiseaseData.target)
    return result

def get_reduced_features():
    result = []
    result.append(UCIHeartDiseaseData.age)
    result.append(UCIHeartDiseaseData.chest_pain)
    result.append(UCIHeartDiseaseData.bp_systolic)
    result.append(UCIHeartDiseaseData.cholesterol)
    result.append(UCIHeartDiseaseData.rest_ecg)
    result.append(UCIHeartDiseaseData.exe_max_heartrate)
    result.append(UCIHeartDiseaseData.exe_induced_angina)
    result.append(UCIHeartDiseaseData.exe_st_depression)
    result.append(UCIHeartDiseaseData.major_vessels)
    result.append(UCIHeartDiseaseData.thalassemia)
    result.append(UCIHeartDiseaseData.target)
    return result



