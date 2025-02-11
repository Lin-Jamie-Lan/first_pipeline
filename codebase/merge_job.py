import pandas as pd
from codebase.base_job import BaseJob
from utils.file_utils import write_csv

class MergeJob(BaseJob):
    def run(self):
        self.validate()
        output_file = self.config['output_file']
        existing_data = pd.read_csv(output_file['location'])
        new_data = pd.DataFrame(self.input_data)
        merged_data = pd.concat([existing_data, new_data]).drop_duplicates(subset=[self.config['output_file']['primary_key']])
        write_csv(merged_data, output_file['location'])