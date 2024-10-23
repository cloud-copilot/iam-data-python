from .utils import load_json

class Services:

    def get_service_keys(self):
        """Returns a list of all service keys."""
        return load_json('services.json')

    def get_service_name(self, service_key):
        """Get the name of a service by its key."""
        data = load_json('serviceNames.json')
        lower_key = service_key.lower()
        if(lower_key in data):
            return data[lower_key]
        raise Exception(f"Service key {service_key} found")

    def service_exists(self, service_key):
        """Checks if a service key exists."""
        data = load_json('serviceNames.json')
        lower_key = service_key.lower()
        return lower_key in data