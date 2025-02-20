import pandas as pd
from codebase.base_job import BaseJob
from utils.file_utils import write_csv
from codebase.transformer import transform

class MergeJobSimple(BaseJob):
    def run(self):
        self.validate_input_schema()

        output_file = self.config['output_file']

        new_data = pd.DataFrame(self.input_data)
        transform.timeStamp(self, new_data, timestamp_type='update_timestamp')
        try:
            existing_data = pd.read_csv(output_file['location'])
        except pd.errors.EmptyDataError:
            existing_data=new_data
            transform.timeStamp(self, existing_data, timestamp_type='ingest_timestamp')
            transform.timeStamp(self, existing_data, timestamp_type='update_timestamp')
        
        print(existing_data)
        print(new_data)
        # concated_data = pd.concat([existing_data, new_data], ignore_index=False
        #                         ).drop_duplicates(subset=[self.config['output_file']['primary_key']])
        
        # joined_data = existing_data.join(new_data, on=id_column, how="outer", lsuffix="_x", rsuffix="_y")

        print("check the pk: ", output_file['primary_key'])
        print("check again:", [self.config['output_file']['primary_key']])
        # check the pk:  id
        # check again: ['id']

        merged_data = existing_data.merge(new_data, how="outer", 
                                          on=[self.config['output_file']['primary_key']], 
                                          suffixes=('_e', '_n') )

        pd.set_option('display.max_columns', None)

        # print(merged_data)
        newdf=pd.DataFrame()
        for col in merged_data.columns:
            if col in [self.config['output_file']['primary_key']]:
                newdf[col]=merged_data[col]
            elif 'ingest_timestamp' in col:
                newdf['ingest_timestamp']=merged_data['ingest_timestamp'].fillna(merged_data['update_timestamp_n'])
            elif 'update_timestamp' in col:
                newdf['update_timestamp']=merged_data['update_timestamp_n']
            elif "_n" in col and 'timestamp' not in col:
                basecol=col.split("_n")[0]
                newdf[basecol]=merged_data[basecol+'_n']
        return(newdf)