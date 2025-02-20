from codebase.full_replace_job import FullReplaceJob
from codebase.merge_job_update import MergeJob
from codebase.transformer import transform
import pandas as pd
from utils.file_utils import write_csv

if __name__ == "__main__":
    config_path = "conf/config1.json"
    # create an object
    # you call a class to create an instance (or object) of that class
    job = FullReplaceJob(config_path) #need config_path, because def __init__(self, config_path) in the class

    # Run the FullReplaceJob to get the initial DataFrame
    # If the function is a method inside a class, you need to call it on an instance of the class
    df = job.run()  # Assuming job.run() returns a DataFrame

    # Debug: Check if df is None
    if df is None:
        raise ValueError("The DataFrame returned by job.run() is None. Check the FullReplaceJob implementation.")
    
    # Create an instance of the transformer and specify the id_column
    transforming = transform(config_path) #need config_path, because def __init__(self, config_path) in the class

    # Instantiate the transformer
    marital_status_transformer = transforming.maritalStatus(df, id_column='id')
    df_timestamp=transforming.timeStamp(df)
    # # Apply the transformer to the DataFrame
    # transformed_df = marital_status_transformer.execute(df)

    write_csv(df_timestamp, "output/sample_data_output1.csv")