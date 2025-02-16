import pandas as pd
from codebase.base_job import BaseJob
from utils.file_utils import write_csv
from codebase.transformer import transform

class MergeJob(BaseJob):
    def run(self):
        self.validate_input_schema()

        output_file = self.config['output_file']

        new_data = pd.DataFrame(self.input_data)
        transform.timeStamp(self, new_data)
        try:
            existing_data = pd.read_csv(output_file['location'])
        except:
            existing_data=new_data
        print(existing_data)
        
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
        print(merged_data)
        newdf=pd.DataFrame()


        for col in merged_data.columns:
            if col in [self.config['output_file']['primary_key']]:
                newdf[col]=merged_data[col]
            elif "_e" in col :
                basecol=col.split("_e")[0]
                # print(basecol)
                newdf[basecol]=merged_data[basecol+'_n']
        return newdf