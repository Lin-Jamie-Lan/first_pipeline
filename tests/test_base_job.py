import pytest
from codebase.base_job import BaseJob

def test_base_job_initialization():
    config_path = "conf/config1.json"
    job = BaseJob(config_path)
    assert job.config is not None
    assert job.schema is not None
    assert job.input_data is not None

def test_base_job_validate():
    config_path = "conf/config1.json"
    job = BaseJob(config_path)
    job.validate_input_schema()