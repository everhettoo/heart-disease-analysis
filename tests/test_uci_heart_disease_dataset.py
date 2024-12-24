from unittest import TestCase

from models.uci_heart_disease_dataset import (UCIHeartDiseaseData,
                                              get_standard_features,
                                              get_reduced_features,
                                              get_original_standard_features)

class TestUCIHeartDiseaseDataset(TestCase):
    def test_get_original_features(self):

        expected_columns = []
        expected_columns.append(UCIHeartDiseaseData.age)
        expected_columns.append(UCIHeartDiseaseData.gender)
        expected_columns.append(UCIHeartDiseaseData.chest_pain)
        expected_columns.append(UCIHeartDiseaseData.bp_systolic)
        expected_columns.append(UCIHeartDiseaseData.cholesterol)
        expected_columns.append(UCIHeartDiseaseData.blood_sugar)
        expected_columns.append(UCIHeartDiseaseData.rest_ecg)
        expected_columns.append(UCIHeartDiseaseData.exe_max_heartrate)
        expected_columns.append(UCIHeartDiseaseData.exe_induced_angina)
        expected_columns.append(UCIHeartDiseaseData.exe_st_depression)
        expected_columns.append(UCIHeartDiseaseData.exe_st_segment_slope)
        expected_columns.append(UCIHeartDiseaseData.major_vessels)
        expected_columns.append(UCIHeartDiseaseData.thalassemia)
        expected_columns.append(UCIHeartDiseaseData.target)

        self.assertListEqual(expected_columns, get_standard_features())

    def test_get_reduced_features(self):

        expected_columns = []
        expected_columns.append(UCIHeartDiseaseData.age)
        expected_columns.append(UCIHeartDiseaseData.chest_pain)
        expected_columns.append(UCIHeartDiseaseData.bp_systolic)
        expected_columns.append(UCIHeartDiseaseData.cholesterol)
        expected_columns.append(UCIHeartDiseaseData.rest_ecg)
        expected_columns.append(UCIHeartDiseaseData.exe_max_heartrate)
        expected_columns.append(UCIHeartDiseaseData.exe_induced_angina)
        expected_columns.append(UCIHeartDiseaseData.exe_st_depression)
        expected_columns.append(UCIHeartDiseaseData.major_vessels)
        expected_columns.append(UCIHeartDiseaseData.thalassemia)
        expected_columns.append(UCIHeartDiseaseData.target)

        self.assertListEqual(expected_columns, get_reduced_features())

    def test_get_original_standard_features(self):
        expected_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca','thal', 'num']

        self.assertListEqual(expected_columns, get_original_standard_features())



