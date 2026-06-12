# ETL-Pipeline

A learning-focused ETL pipeline project demonstrating CSV extraction, data transformation, and PostgreSQL loading. The repository includes a simple Airflow DAG wrapper for orchestration and an early dashboard folder for future UI integration.

## Project Overview

This project is built as an educational ETL pipeline that:
- extracts customer data from a CSV file
- transforms the data with simple cleaning and renaming rules
- loads the cleaned data into a PostgreSQL database
- can be orchestrated via Apache Airflow using a BashOperator

## Repository Structure

- `data/`
  - `customers_data.csv` — sample source dataset used by the pipeline
- `dags/`
  - `etl_dag.py` — Airflow DAG definition that runs `src/main.py`
  - `etl_dag_trial.py` — experimental or alternate DAG file
- `dashboard/`
  - `app.py`, `appy.py` — dashboard-related files for future visualization or UI work
- `src/`
  - `main.py` — pipeline entry point
  - `database/`
    - `config.py` — reads PostgreSQL connection settings from `database.ini`
    - `connect.py` — helper for PostgreSQL connectivity
    - `database.ini` — database credentials configuration file
    - `sql_table.sql` — database table DDL or reference SQL
  - `scripts/`
    - `extract.py` — reads CSV data into a pandas DataFrame
    - `transform.py` — cleans and normalizes data
    - `load.py` — inserts rows into PostgreSQL and handles duplicates
- `requirements.txt` — Python dependencies
- `simple_auth_manager_passwords.json.generated` — generated auth/password file

## Setup

1. Create and activate a Python virtual environment in the repo root:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure PostgreSQL connection:
   - Edit `src/database/database.ini`
   - Confirm the `[postgresql]` section contains your database host, port, database, user, and password

## Usage

### Run locally

From the project root, run:
```bash
python src/main.py
```

The pipeline will:
1. extract `data/customers_data.csv`
2. transform the DataFrame
3. load the records into the PostgreSQL table configured by `table_name` in `src/main.py`

### Airflow

The Airflow DAG is defined in `dags/etl_dag.py`. It uses a BashOperator to execute:
```bash
.venv/bin/python src/main.py
```

To use this DAG:
1. Ensure Apache Airflow is installed and configured
2. Place the `dags/` folder in your Airflow home or point `dags_folder` to this repo
3. Start the scheduler and webserver

> Note: On non-macOS or non-Unix systems, adjust the `bash_command` path in `dags/etl_dag.py`.

## ETL Pipeline Details

- `src/scripts/extract.py` reads the CSV and validates that the DataFrame is not empty.
- `src/scripts/transform.py` standardizes column names, combines `city` and `country` into `location`, and drops unused columns.
- `src/scripts/load.py` connects to PostgreSQL, inserts rows, and skips duplicate entries.

## Notes

- `src/main.py` currently uses hard-coded values for `file_name` and `table_name`.
- Error handling exists in extract/transform/load, but the pipeline can be improved with more robust validation and logging.
- `dashboard/` is included for future dashboard or UI extensions.

## Future Improvements

- parameterize input file and destination table
- add tests for ETL functions
- improve transformation logic and data validation
- build a dashboard or Airflow monitoring UI
- support additional data sources and destinations

## License

This project is intended for learning and experimentation. Add a license file if you want to publish under a specific open source license.
