import pytest
from codebase.merge_job_simple import MergeJobSimple

def test_merge_job_run():
    config_path = "conf/config2.json"
    job = MergeJobSimple(config_path)
    job.run()