from codebase.full_replace_job import FullReplaceJob
from codebase.merge_job import MergeJob
from codebase.transformer import transform
import pandas as pd
from utils.file_utils import write_csv

if __name__ == "__main__":
    config_path = "conf/config2.json"
    job2 = MergeJob(config_path)

    df=job2.run()
    output_file = job2.config['output_file']
    
    write_csv(df, output_file['location'])
