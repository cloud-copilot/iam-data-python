from .utils import load_json

class Conditions:
    def _get_conditions(self, service_key):
        """Load conditions from a JSON file."""
        return load_json("conditionKeys",f"{service_key.lower()}.json")

    def get_condition_keys_for_service(self, service_key):
        """Returns a list of all condition keys for a given service key."""
        return [key['key'] for key in self._get_conditions(service_key).values()]

    def get_condition_key_details(self, service_key, condition_key):
        """Returns the details of a specific condition key."""
        data = self._get_conditions(service_key)
        lower_condition_key = condition_key.lower()
        if lower_condition_key in data:
            return data[lower_condition_key]
        raise Exception(f"Condition key '{condition_key}' not found for service '{service_key}'")

    def condition_key_exists(self, service_key, condition_key):
        """Checks if a condition key exists for a given service key."""
        data = self._get_conditions(service_key)
        lower_condition_key = condition_key.lower()
        return lower_condition_key in data