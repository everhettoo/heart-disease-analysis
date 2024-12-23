from unittest import TestCase
from models.heart_disease import HeartDisease, get_standard_features, get_reduced_features

class TestHeartDisease(TestCase):
    def test_get_original_features(self):

        expected_columns = []
        expected_columns.append(HeartDisease.AGE)
        expected_columns.append(HeartDisease.GENDER)
        expected_columns.append(HeartDisease.CHEST_PAIN)
        expected_columns.append(HeartDisease.BP_SYSTOLIC)
        expected_columns.append(HeartDisease.CHOLESTEROL)
        expected_columns.append(HeartDisease.BLOOD_SUGAR)
        expected_columns.append(HeartDisease.REST_ECG)
        expected_columns.append(HeartDisease.EXE_MAX_HEARTRATE)
        expected_columns.append(HeartDisease.EXE_ANGINA)
        expected_columns.append(HeartDisease.EXE_ST_DEPRESSION)
        expected_columns.append(HeartDisease.EXE_ST_SEGMENT_SLOPE)
        expected_columns.append(HeartDisease.MAJOR_VESSELS)
        expected_columns.append(HeartDisease.THALASSEMIA)
        expected_columns.append(HeartDisease.TARGET)

        self.assertListEqual(expected_columns, get_standard_features())

    def test_get_reduced_features(self):

        expected_columns = []
        expected_columns.append(HeartDisease.AGE)
        expected_columns.append(HeartDisease.CHEST_PAIN)
        expected_columns.append(HeartDisease.BP_SYSTOLIC)
        expected_columns.append(HeartDisease.CHOLESTEROL)
        expected_columns.append(HeartDisease.REST_ECG)
        expected_columns.append(HeartDisease.EXE_MAX_HEARTRATE)
        expected_columns.append(HeartDisease.EXE_ANGINA)
        expected_columns.append(HeartDisease.EXE_ST_DEPRESSION)
        expected_columns.append(HeartDisease.MAJOR_VESSELS)
        expected_columns.append(HeartDisease.THALASSEMIA)
        expected_columns.append(HeartDisease.TARGET)

        self.assertListEqual(expected_columns, get_reduced_features())

