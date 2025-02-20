import pandas as pd
from codebase.base_job import BaseJob
from utils.file_utils import write_csv
from datetime import datetime

class transform(BaseJob):
    def maritalStatus(self, df, id_column='id'):
        df['marital_status'] = df[id_column].apply(lambda x: True if len(str(x)) == 4 else False)
        if id_column not in df.columns:
            raise ValueError(f"Column '{id_column}' not found in DataFrame!!!!!")
        return df
    
    def timeStamp(self, df, timestamp_type):
        now=datetime.now()
        df[timestamp_type] = now
        return df