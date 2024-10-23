# IAM Data In Python Package

This is a simple package for utilizing AWS IAM data for Services, Actions, Resources, and Condition Keys. Data is embedded in the python package.

New data is checked against the AWS IAM documentation and updated daily if there are changes.

## Installation
```bash
pip install iam-data
```

## Usage
```python
from iamdata import IAMData

iam_data = IAMData()
print(f"Data Version {iam_data.data_version()} updated at {iam_data.data_updated_at()}")
for service_key in iam_data.services.get_service_keys():
    service_name = iam_data.services.get_service_name(service_key)
    print(f"Getting Actions for {service_name}")
    for action in iam_data.actions.get_actions_for_service(service_key):
        action_details = iam_data.actions.get_action_details(service_key, action)
        print(f"{service_key}:{action} => {action_details}")
```

## API
### Services
* `services.get_service_keys()` - Returns a list of all service keys such as 's3', 'ec2', etc.
* `services.get_service_name(service_key)` - Returns the service name for a given service key.
* `services.service_exists(service_key)` - Returns True if the service key exists.

### Actions
* `actions.get_actions_for_service(service_key)` - Returns an array of all actions for a given service key.
* `actions.get_action_details(service_key, action_key)` - Returns an object with the action details such as `description`, `resourceTypes`, and `conditionKeys`.
* `actions.action_exists(service_key, action_key)` - Returns true if the action exists.

### Resources
* `resources.get_resource_types_for_service(service_key)` - Returns an array of all resource types for a given service key.
* `resources.get_resource_type_details(service_key, resource_type_key)` - Returns an object with the resource type details such as `description`, `arnFormat`, and `conditionKeys`.
* `resources.resource_type_exists(service_key, resource_type_key)` - Returns true if the resource type exists.

### Conditions Keys
* `conditions.get_condition_keys_for_service(service_key)` - Returns an array of all condition keys for a given service key.
* `conditions.get_condition_key_details(service_key, condition_key)` - Returns an object with the condition key details such as `description`, `conditionValueTypes`, and `conditionOperators`.
* `conditions.condition_key_exists(service_key, condition_key)` - Returns true if the condition key exists.

### Version Info
The version is number is formatted as `major.minor.updatedAt`. The updatedAt is the date the data was last updated in the format `YYYYMMDDX` where `X` is a counter to enable publishing more than once per day if necessary. For example version `0.1.202408291` has data updated on August 29th, 2024.

The version can be accessed using the `data_version()` method.

There is also `date_updated_at()` which returns the date the data was last updated.

