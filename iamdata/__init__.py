# iam_data_lib/__init__.py
from .utils import load_json
from .services import Services
from .actions import Actions
from .resources import Resources
from .conditions import Conditions

from datetime import datetime

class IAMData:
    def __init__(self):
        self.services = Services()
        self.actions = Actions()
        self.resources = Resources()
        self.conditions = Conditions()

    def _get_metadata(self):
        """Load metadata from a JSON file."""
        return load_json("metadata.json")

    def data_version(self):
        """Returns the version of the IAM data."""
        return self._get_metadata()['version']

    def data_updated_at(self):
        """Returns the last updated timestamp of the IAM data."""
        return datetime.strptime(self._get_metadata()['updatedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')