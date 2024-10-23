import unittest

from iamdata.conditions import Conditions

class ConditionsTest(unittest.TestCase):
    def test_get_condition_keys_for_service(self):
        conditions = Conditions()
        result = conditions.get_condition_keys_for_service("s3")
        self.assertIsInstance(result, list)

    def test_get_condition_key_details(self):
        conditions = Conditions()
        result = conditions.get_condition_key_details("s3", "s3:AccessGrantsInstanceArn")
        self.assertIsInstance(result, dict)

    def test_condition_key_exists(self):
        conditions = Conditions()
        result = conditions.condition_key_exists("s3", "s3:AccessGrantsInstanceArn")
        self.assertTrue(result)

    def test_condition_key_not_exists(self):
        conditions = Conditions()
        result = conditions.condition_key_exists("s3", "nonexistent_condition_key")
        self.assertFalse(result)

    def test_get_condition_key_details_not_exists(self):
        conditions = Conditions()
        with self.assertRaises(Exception) as context:
            conditions.get_condition_key_details("s3", "nonexistent_condition_key")
        self.assertEqual(str(context.exception), "Condition key 'nonexistent_condition_key' not found for service 's3'")