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
├── codebase/ # Core job classes, functions: base_job, full_replace_job, merge_job_simple, merge_job_update, transformer
├── conf/ # Configuration file for each pipeline
├── database/ # SQLite connection and management, connector, manager
├── input # input folder for csv or json data
├── output/ # output folder for csv or json data 
├── pipelines/ # Pipeline script for each pipeline
├── schema/ # JSON schema files
├── tests/ # Unit tests
├── utils/ # Utility functions
├── README.md # Project documentation
└── requirements.txt # Python dependencies

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
python pipelines/pipeline4.py 
pytest tests/

