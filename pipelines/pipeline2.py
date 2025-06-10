from codebase.merge_job_simple import MergeJobSimple
from codebase.transformer import Transform
import pandas as pd
from utils.file_utils import write_csv

if __name__ == "__main__":
    config_path = "conf/config2.json"
    job2 = MergeJobSimple(config_path)

    df = job2.run()
    output_file = job2.config['output_file']

    write_csv(df, output_file['location'])
