import json
import pandas as pd
from utils.file_utils import read_json, read_csv, write_csv, write_json
from utils.schema_utils import validate_schema
from database.manager import DatabaseManager

class BaseJob:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self.schema = self._load_schema(self.config['schema_file'])
        self.input_data = self._load_input_data()

    def _load_config(self, config_path):
        with open(config_path, 'r') as f:
            return json.load(f)

    def _load_schema(self, schema_path):
        with open(schema_path, 'r') as f:
            return json.load(f)

    def _load_input_data(self):
        input_file = self.config['input_file']
        if input_file['type'] == 'json':
            return read_json(input_file['location'])
        elif input_file['type'] == 'csv':
            return read_csv(input_file['location'])
        else:
            raise ValueError("Unsupported file type")
        
    def _output_data(self):
        input_file = self.config['input_file']
        if input_file['type'] == 'json':
            output_file = self.config['output_file']
            return write_json(self.input_data, output_file['location'])
        elif input_file['type'] == 'csv':
            output_file = self.config['output_file']
            return write_csv(self.input_data, output_file['location'])
        else:
            raise ValueError("Unsupported file type")
        
    def validate_input_schema(self):
        validate_schema(self.input_data, self.schema)

    def run(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def save_output(self, data: pd.DataFrame):
        """Save data to CSV or SQLite based on config."""
        output_config = self.config['output_file']
        
        if output_config['type'] == 'csv':
            write_csv(data, output_config['location'])
        elif output_config['type'] == 'sqlite':
            db_manager = DatabaseManager()
            table_name = output_config.get('table_name')  # Get table name from config
            db_manager.save_dataframe(data, table_name=table_name)
        else:
            raise ValueError("Unsupported output type")