import json
import os

def load_packing_templates():
    try:
        with open(os.path.join("data", "packing_templates.json"), "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
