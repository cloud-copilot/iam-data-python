from .utils import load_json

class Actions:
    def _get_actions(self, service_key):
        """Load actions from a JSON file."""
        return load_json("actions",f"{service_key.lower()}.json")

    def get_actions_for_service(self, service_key):
        """Returns a list of all actions for a given service key."""
        return [action['name'] for action in self._get_actions(service_key).values()]

    def get_action_details(self, service_key, action_key):
        """Returns the details of a specific action."""
        lower_action = action_key.lower()
        data = self._get_actions(service_key)
        if lower_action in data:
            return data[lower_action]
        raise Exception(f"Action '{action_key}' not found for service '{service_key}'")

    def action_exists(self, service_key, action_key):
        """Checks if an action exists for a given service key."""
        lower_action = action_key.lower()
        return lower_action in self._get_actions(service_key)