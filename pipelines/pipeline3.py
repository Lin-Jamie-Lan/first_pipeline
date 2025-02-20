from codebase.full_replace_job import FullReplaceJob
from codebase.merge_job_update import MergeJobUpdate
from codebase.transformer import transform
import pandas as pd
from utils.file_utils import write_csv

if __name__ == "__main__":
    config_path = "conf/config3.json"
    job3 = MergeJobUpdate(config_path)

    df = job3.run()
    output_file = job3.config['output_file']

    write_csv(df, output_file['location'])
