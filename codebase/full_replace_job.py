from codebase.base_job import BaseJob
from utils.file_utils import read_csv, write_csv

class FullReplaceJob(BaseJob):
    def run(self):
        self.validate_input_schema()
        return self.input_data
        # print(self.input_data)
        # existing_data = pd.read_csv(input_file['location'])
        # input_file = self.config['input_file']
        # self._output_data()


# class FullReplaceJob(BaseJob):
#     def run(self):
#         self.validate()
#         output_file = self.config['output_file']
#         write_csv(self.input_data, output_file['location'])