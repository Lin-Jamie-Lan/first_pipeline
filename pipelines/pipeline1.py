from codebase.full_replace_job import FullReplaceJob
from codebase.transformer import Transform
import pandas as pd
from utils.file_utils import write_csv

if __name__ == "__main__":
    config_path = "conf/config1.json"
    # create an object/instance (2 words used interchangably)
    # you call a class to create an instance (or object) of that class
    # If the function is a method inside a class, you need to call it on an instance of the class
    job = FullReplaceJob(config_path) #need config_path, because def __init__(self, config_path) in the class

    # Run the FullReplaceJob to get the initial DataFrame
    df = job.run()  # Assuming job.run() returns a DataFrame

    # Debug: Check if df is None
    if df is None:
        raise ValueError("The DataFrame returned by job.run() is None. Check the FullReplaceJob implementation.")
    
    # Create an instance of the transformer and specify the id_column
    # Instantiate the transformer
    transforming = Transform(config_path) #need config_path, because def __init__(self, config_path) in the class

    # call the function insider of the instance
    # If the function is a method inside a class, you need to call it on an instance of the class
    transforming.maritalStatus(df, id_column='id')
    df_timestamp=transforming.timeStamp(df, 'ingest_timestamp')


    write_csv(df_timestamp, "output/sample_data_output1.csv")