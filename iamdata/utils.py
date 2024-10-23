import json
import os

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, 'data')

_cache = {}

def load_json(*file_path_parts):
    file_path = os.path.join(data_dir, *file_path_parts)
    if file_path in _cache:
        return _cache[file_path]
    with open(file_path, 'r') as f:
        content = json.load(f)
        _cache[file_path] = content
        return content