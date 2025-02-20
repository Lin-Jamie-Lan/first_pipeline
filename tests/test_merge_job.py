import pytest
from codebase.merge_job_update import MergeJob

def test_merge_job_run():
    config_path = "conf/config2.json"
    job = MergeJob(config_path)
    job.run()