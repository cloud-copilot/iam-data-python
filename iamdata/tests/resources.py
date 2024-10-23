import unittest

from iamdata.resources import Resources

class ResourcesTest(unittest.TestCase):
    def test_get_resource_types_for_service(self):
        resources = Resources()
        result = resources.get_resource_types_for_service("s3")
        self.assertIsInstance(result, list)

    def test_get_resource_type_details(self):
        resources = Resources()
        result = resources.get_resource_type_details("s3", "Bucket")
        self.assertIsInstance(result, dict)

    def test_get_resource_type_details_not_exists(self):
        resources = Resources()
        with self.assertRaises(Exception) as context:
            resources.get_resource_type_details("s3", "nonexistent_resource")
        self.assertEqual(str(context.exception), "Resource type 'nonexistent_resource' not found for service 's3'")

    def test_resource_type_exists(self):
        resources = Resources()
        result = resources.resource_type_exists("s3", "Bucket")
        self.assertTrue(result)

    def test_resource_type_not_exists(self):
        resources = Resources()
        result = resources.resource_type_exists("s3", "nonexistent_resource")
        self.assertFalse(result)