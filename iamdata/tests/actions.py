import unittest

from iamdata.actions import Actions

class ActionsTest(unittest.TestCase):
    def test_get_actions_for_service(self):
        actions = Actions()
        result = actions.get_actions_for_service("s3")
        self.assertIsInstance(result, list)

    def test_get_action_details_exists(self):
        actions = Actions()
        result = actions.get_action_details("s3", "GetObject")
        self.assertIsInstance(result, dict)

    def test_get_action_details_not_exists(self):
        actions = Actions()
        with self.assertRaises(Exception) as context:
            actions.get_action_details("s3", "nonexistent_action")
        self.assertEqual(str(context.exception), "Action 'nonexistent_action' not found for service 's3'")

    def test_action_exists(self):
        actions = Actions()
        result = actions.action_exists("s3", "GetObject")
        self.assertTrue(result)

    def test_action_not_exists(self):
        actions = Actions()
        result = actions.action_exists("s3", "nonexistent_action")
        self.assertFalse(result)