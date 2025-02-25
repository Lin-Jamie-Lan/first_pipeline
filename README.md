# Pipeline Framework

This is a Python-based pipeline framework designed to process JSON and CSV files, validate their schemas, and save the results either as CSV files or in an SQLite database. The framework follows software engineering best practices and is organized into modular components for easy maintenance and extensibility.

## Features
- **Input Formats**: Supports JSON and CSV files.
- **Schema Validation**: Validates input data against a JSON schema.
- **Output Options**: Saves processed data as CSV files or in an SQLite database.
- **Modular Design**: Organized into separate modules for jobs, utilities, and database operations.
- **Testing**: Includes unit tests for schema validation, primary key uniqueness, and configuration completeness.

## Folder Structure
pipeline_framework/
│
├── codebase/ # Core job classes, functions: base_job, full_replace_job, merge_job_simple, merge_job_update, transformer. 
├── conf/ # Configuration file for each pipeline. 
├── database/ # SQLite connection and management, connector, manager. 
├── input # input folder for csv or json data. 
├── output/ # output folder for csv or json data. 
├── pipelines/ # Pipeline script for each pipeline. 
├── schema/ # JSON schema files. 
├── tests/ # Unit tests. 
├── utils/ # Utility functions. 
├── README.md # Project documentation. 
└── requirements.txt # Python dependencies. 

## Prerequisites
- Python 3.7 or higher
- SQLite (preinstalled on macOS)
pip install -r requirements.txt

## SQLite configuration
### Add the following lines to your ~/.zshrc (or ~/.bashrc):
export SQLITE_DB_PATH="$HOME/my_databases/pipeline_data.db"
export SQLITE_TABLE_NAME="processed_data"
### Reload the shell:
source ~/.zshrc
### command to connect to sqlite
sqlite3 ~/my_databases/pipeline_data.db
select * from sample;
.exit
### create table is optional

## command to run pipeline and test
python pipelines/pipeline4.py\
pytest tests/\



# Here's how the components are connected:

1. pipelines/: 
Contains the pipeline scripts that orchestrate the workflow.

Depends on:
codebase/ for job classes.
conf/ for configuration files.
schema/ for schema validation.

2. codebase/: 
Contains the core job classes (BaseJob, FullReplaceJob, MergeJob).

Depends on:
utils/ for utility functions.
database/ for SQLite operations.

3. utils/: Contains utility functions for file handling and schema validation.

Used by:
codebase/ for common functionality.

4. database/: 
Handles SQLite connections and database operations.

Used by:
codebase/ for saving data to SQLite.

5. conf/: 
Contains configuration files (JSON) for input/output settings.

Used by:
pipelines/ to configure jobs.

6. schema/: 
Contains JSON schema files for input validation.

Used by:
codebase/ for schema validation.

7. tests/: 
Contains unit tests for the framework.

Tests:
codebase/, utils/, and database/.

## Diagram
+-----------------+       +-----------------+       +-----------------+
|   pipelines/    |       |    codebase/    |       |     utils/      |
|-----------------|       |-----------------|       |-----------------|
| - pipeline1.py  |<------| - base_job.py   |<------| - file_utils.py |
| - pipeline2.py  |       | - full_replace_job.py | - schema_utils.py |
| - pipeline3.py  |       | - merge_job.py  |       +-----------------+
| - pipeline4.py  |       +-----------------+
+-----------------+               ^
        |                         |
        v                         |
+-----------------+       +-----------------+
|     conf/       |       |   database/     |
|-----------------|       |-----------------|
| - config1.json  |       | - connector.py  |
| - config2.json  |       | - manager.py    |
| - config3.json  |       +-----------------+
| - config4.json  |               ^
+-----------------+               |
        |                         |
        v                         |
+-----------------+       +-----------------+
|    schema/      |       |     tests/      |
|-----------------|       |-----------------|
| - schema1.json  |       | - test_base_job.py |
| - schema2.json  |       | - test_full_replace_job.py |
| - schema3.json  |       | - test_merge_job.py |
| - schema4.json  |       +-----------------+
+-----------------+

# Mermaid
erDiagram
    pipelines ||--o{ codebase : "call"
    pipelines ||--o{ database : "call"
    pipelines ||--o{ conf : "read"
    conf ||--o{ schema : "read"
    codebase ||--o{ utils : "call"
    codebase ||--o{ schema : "validate"
### https://mermaid-js.github.io/mermaid-live-editor/