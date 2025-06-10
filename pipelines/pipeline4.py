from codebase.full_replace_job import FullReplaceJob
from codebase.transformer import Transform
import pandas as pd
from utils.file_utils import write_csv
from database.manager import DatabaseManager

if __name__ == "__main__":
    config_path = "conf/config4.json"
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
    transforming = Transform(config_path) #need config_path, because def __init__(self, config_path) in the class

    # Instantiate the transformer
    marital_status_transformer = transforming.maritalStatus(df, id_column='id')
    df_timestamp=transforming.timeStamp(marital_status_transformer, timestamp_type='injest_timestamp')
    df_timestamp=transforming.timeStamp(df_timestamp, timestamp_type='update_timestamp')
    
    output=DatabaseManager()
    output.save_dataframe(df_timestamp, 'sample2')