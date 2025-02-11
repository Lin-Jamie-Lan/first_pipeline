import json
import pandas as pd

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(data, file_path):
    if isinstance(data, dict):
        data = pd.DataFrame(data)
    data.to_json(file_path, index=False)

def read_csv(file_path):
    return pd.read_csv(file_path)

def write_csv(data, file_path):
    if isinstance(data, dict):
        data = pd.DataFrame(data)
    data.to_csv(file_path, index=False)