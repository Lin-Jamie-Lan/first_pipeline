import pytest
from codebase.full_replace_job import FullReplaceJob

def test_full_replace_job_run():
    config_path = "conf/config1.json"
    job = FullReplaceJob(config_path)
    job.run()