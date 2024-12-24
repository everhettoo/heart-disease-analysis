class UCIHeartDiseaseOriginalData:
    # The original (raw) dataset has 76 variables.
    headers = [
        'id',
        'ccf',
        'age',
        'sex',
        'painloc',
        'painexer',
        'relrest',
        'pncaden',
        'cp',
        'trestbps',
        'htn',
        'chol',
        'smoke',
        'cigs',
        'years',
        'fbs',
        'dm',
        'famhist',
        'restecg',
        'ekgmo',
        'ekgday',
        'ekgyr',
        'dig',
        'prop',
        'nitr',
        'pro',
        'diuretic',
        'proto',
        'thaldur',
        'thaltime',
        'met',
        'thalach',
        'thalrest',
        'tpeakbps',
        'tpeakbpd',
        'dummy',
        'trestbpd',
        'exang',
        'xhypo',
        'oldpeak',
        'slope',
        'rldv5',
        'rldv5e',
        'ca',
        'restckm',
        'exerckm',
        'restef',
        'restwm',
        'exeref',
        'exerwm',
        'thal',
        'thalsev',
        'thalpul',
        'earlobe',
        'cmo',
        'cday',
        'cyr',
        'num',
        'lmt',
        'ladprox',
        'laddist',
        'diag',
        'cxmain',
        'ramus',
        'om1',
        'om2',
        'rcaprox',
        'rcadist',
        'lvx1',
        'lvx2',
        'lvx3',
        'lvx4',
        'lvf',
        'cathef',
        'junk',
        'name'
    ]

class UCIHeartDiseaseData:
    age                     = "Age"                     # age
    gender                  = "Gender"                  # sex
    chest_pain              = "Chest Pain"              # cp
    bp_systolic             = "BP Systolic"             # trestbps
    cholesterol             = "Cholesterol"             # chol
    blood_sugar             = "Blood Sugar"             # fbs
    rest_ecg                = "Rest ECG"                # restecg
    exe_max_heartrate       = "Exe. Max Heartrate"      # thalach
    exe_induced_angina      = "Exe. Induced Angina"     # exang
    exe_st_depression       = "Exe. ST Depression"      # old[peak
    exe_st_segment_slope    = "Exe. ST Segment Slope"   # slope
    major_vessels           = "Major Vessels"           # ca
    thalassemia             = "Thalassemia"             # thal
    target                  = "Target"                  # num

class UCIHeartDiseaseDataFile:
    cleveland_standard          = 'data/uci-heart-disease/processed.cleveland.data'
    hungarian_standard          = 'data/uci-heart-disease/processed.hungarian.data'
    longbeach_standard          = 'data/uci-heart-disease/processed.va.data'
    switzerland_standard        = 'data/uci-heart-disease/processed.switzerland.data'
    salvaged_standard           = 'data/uci-heart-disease/processed.salvaged.data'
    cleveland_cleansed          = 'data/uci-heart-disease/processed.cleveland-cleansed.data'
    cleveland_preprocessed      = 'data/uci-heart-disease/processed.cleveland-cleansed-preprocessed.data'
    hungarian_recovered         = 'data/uci-heart-disease/recovered-hungarian.data'
    longbeach_recovered         = 'data/uci-heart-disease/recovered-va.data'
    switzerland_recovered       = 'data/uci-heart-disease/recovered-switzerland.data'

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

def get_original_features():
    return UCIHeartDiseaseOriginalData.headers



