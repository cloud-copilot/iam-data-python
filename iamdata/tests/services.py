import unittest

from iamdata.services import Services

class ServicesTest(unittest.TestCase):
    def test_get_service_keys(self):
        services = Services()
        result = services.get_service_keys()
        self.assertIsInstance(result, list)

    def test_get_service_name_exists(self):
        services = Services()
        result = services.get_service_name("s3")
        self.assertEqual(result, "Amazon S3")

    def test_get_service_name_not_exists(self):
        services = Services()
        with self.assertRaises(Exception) as context:
            services.get_service_name("nonexistent_service")
        self.assertEqual(str(context.exception), "Service key nonexistent_service found")

    def test_service_exists(self):
        services = Services()
        result = services.service_exists("s3")
        self.assertTrue(result)

    def test_service_not_exists(self):
        services = Services()
        result = services.service_exists("nonexistent_service")
        self.assertFalse(result)