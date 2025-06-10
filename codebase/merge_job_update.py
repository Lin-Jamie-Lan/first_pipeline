import pandas as pd
from codebase.base_job import BaseJob
from utils.file_utils import write_csv
from codebase.transformer import Transform

class MergeJobUpdate(BaseJob):
    def run(self):
        self.validate_input_schema()

        output_file = self.config['output_file']

        new_data = pd.DataFrame(self.input_data)
        Transform.timeStamp(self, new_data, timestamp_type='ingest_timestamp')
        Transform.timeStamp(self, new_data, timestamp_type='update_timestamp')
        try:
            existing_data = pd.read_csv(output_file['location'])
        except pd.errors.EmptyDataError:
            existing_data=new_data
        

        merged_data = existing_data.merge(new_data, how="outer", 
                                          on=[self.config['output_file']['primary_key']], 
                                          suffixes=('_e', '_n') )

        pd.set_option('display.max_columns', None)

        newdf=pd.DataFrame()
        print(merged_data)

  # Loop through each row and each column
        for index, row in merged_data.iterrows():
            if pd.isnull(row['update_timestamp_e']):
                newdf.at[index, 'update_timestamp']=row['update_timestamp_n']
                newdf.at[index, 'ingest_timestamp']=row['ingest_timestamp_n']
            else:
                newdf.at[index, 'update_timestamp']=row['update_timestamp_e']
                newdf.at[index, 'ingest_timestamp']=row['ingest_timestamp_e']
            for column_name in merged_data.columns:
                if column_name in [self.config['output_file']['primary_key']]:
                    newdf.at[index, column_name]=row[column_name]
                elif 'ingest_timestamp' not in column_name and 'update_timestamp' not in column_name:
                    basecol=column_name.replace("_e","_n").split("_n")[0]
                    cell_value_e = row[basecol+'_e']
                    cell_value_n = row[basecol+'_n']
                    if cell_value_e != cell_value_n:
                        newdf.at[index, basecol]=row[basecol+'_n']
                        newdf.at[index, 'update_timestamp']=row['update_timestamp_n']
                    else:
                        newdf.at[index, basecol]=row[basecol+'_e']       

                # print(f"Row {index}, Column '{column_name}': {cell_value}")
        return(newdf)