# iam_data_lib/resources.py
from .utils import load_json

class Resources:

    def _get_resources(self, service_key):
        """Load resources from a JSON file."""
        return load_json("resourceTypes",f"{service_key.lower()}.json")

    def get_resource_types_for_service(self, service_key):
        """Returns a list of all resource types for a given service key."""
        return [r['key'] for r in self._get_resources(service_key).values()]

    def get_resource_type_details(self, service_key, resource_type_key):
        """Returns the details of a specific resource type."""
        data = self._get_resources(service_key)
        lower_resource_type_key = resource_type_key.lower()
        if lower_resource_type_key in data:
            return data[lower_resource_type_key]
        raise Exception(f"Resource type '{resource_type_key}' not found for service '{service_key}'")

    def resource_type_exists(self, service_key, resource_type_key):
        """Checks if a resource type exists for a given service key."""
        lower_resource_type_key = resource_type_key.lower()
        return lower_resource_type_key in self._get_resources(service_key)