# HRxRecruiting-AI Project

## Project Overview

The **HRxRecruiting-AI** project focuses on discovering data to provide a data-driven solution to optimize and enhance the recruitment process. This repository contains data, scripts, and code that facilitate the analysis and management of recruitment data, aiming to streamline hiring and recruitment practices.

### Repository Structure

This repository contains three main components:

1. **Raw Data**
2. **Cleaned Data**
3. **Code (Python, SQL, and others)**

---

## 1. Raw Data

The `raw_data/` directory contains the original, unprocessed data files used in this project. These datasets may include information on candidates, applications, job postings, interview schedules, and more.

- **Formats**: CSV, Excel, and other structured data formats
- **Data**: Contains unmodified data as received from various sources, without any cleaning or preprocessing.

**Location**: `/raw_data`

---

## 2. Cleaned Data

The `cleaned_data/` directory contains data that has been processed and cleaned to remove errors, inconsistencies, and missing values. This data is ready for analysis and further processing.

- **Formats**: CSV and Excel files
- **Modifications**: Duplicates removed, missing values handled, data reformatted for consistency, and any necessary corrections applied.

**Location**: `/cleaned_data`

---

## 3. Code

The `code/` directory contains scripts and queries used to clean, process, and analyze the recruitment data. These files are organized based on the language used and their specific function.

### Python Code

Python scripts are used for various data analysis tasks, including data cleaning, visualization, and basic statistical analysis.

- **File Location**: `/code/python`
- **Main Files**:
  - `data_cleaning.py`: Script for cleaning raw data.
  - `data_analysis.py`: Contains functions for analyzing recruitment trends.
  - `visualization.py`: Generates basic plots and charts from the data.

### SQL Queries

SQL scripts are used to extract, transform, and manipulate data stored in relational databases. These queries are designed to manage recruitment data, track applicants, and generate reports.

- **File Location**: `/code/sql`
- **Main Files**:
  - `create_tables.sql`: Contains SQL queries to set up the database schema.
  - `data_extraction.sql`: Queries for extracting relevant data from the database.
  - `reports.sql`: Queries for generating recruitment and hiring reports.

### Other Formats

Additional code files that may be included in other languages or formats, such as shell scripts or configuration files for database connections.

- **File Location**: `/code/others`
- **Main Files**:
  - `config.sh`: Example shell script for setting up the environment.
  - `database_config.json`: Configuration file for database connection parameters.

---

## How to Use

1. **Data**: Start by exploring the `raw_data/` or `cleaned_data/` folders to understand the structure of the available datasets.
2. **Python Scripts**: Use the Python scripts to perform data analysis or visualization. Run the scripts in any Python environment with necessary dependencies (e.g., Pandas, Matplotlib).
3. **SQL Queries**: Use the SQL queries to manage and analyze recruitment data stored in relational databases. Ensure your database schema matches the one provided in the `create_tables.sql` file.
4. **Contributions**: Feel free to contribute by submitting issues or pull requests if you find any bugs or want to enhance the project.

---

## Requirements

- **Python**: Version 3.6 or higher
- **SQL**: Compatible with MySQL, PostgreSQL, or other common database systems
- **Libraries** (Python):
  - Pandas
  - Matplotlib
  - NumPy

---

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more details.

---

## Contact

For any questions or support, please reach out to the project maintainer at **monasloanelab@gmail.com**.
