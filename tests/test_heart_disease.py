from unittest import TestCase
from models.heart_disease import HeartDisease, get_hd_columns

class TestHeartDisease(TestCase):
    def test_get_columns(self):

        expected = []
        expected.append(HeartDisease.AGE)
        expected.append(HeartDisease.GENDER)
        expected.append(HeartDisease.CHEST_PAIN)
        expected.append(HeartDisease.BP_SYSTOLIC)
        expected.append(HeartDisease.CHOLESTEROL)
        expected.append(HeartDisease.BLOOD_SUGAR)
        expected.append(HeartDisease.REST_ECG)
        expected.append(HeartDisease.EXE_MAX_HEARTRATE)
        expected.append(HeartDisease.EXE_ANGINA)
        expected.append(HeartDisease.EXE_ST_DEPRESSION)
        expected.append(HeartDisease.EXE_ST_SEGMENT_SLOPE)
        expected.append(HeartDisease.MAJOR_VESSELS)
        expected.append(HeartDisease.THALASSEMIA)
        expected.append(HeartDisease.TARGET)

        self.assertListEqual(expected, get_hd_columns())

