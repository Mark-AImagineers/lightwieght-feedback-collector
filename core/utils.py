import json
import os

def get_full_version_data(BASE_DIR):
    """
    Load and return the entire version.json contents as a dict
    """
    version_path = os.path.join(BASE_DIR, 'version.json')
    try:
        with open(version_path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"version.json not found in {BASE_DIR}")
    except json.JSONDecodeError:
        raise ValueError("version.json is not valid JSON")

def get_version_data(BASE_DIR, variable):
    """
    Return a specific variable from version.json
    """
    data = get_full_version_data(BASE_DIR)
    if variable not in data:
        raise KeyError(f"{variable} not found in version.json")
    return data[variable]