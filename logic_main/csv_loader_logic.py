from xml.etree.ElementTree import tostring

import pandas as pd
from schema_manager_logic import create_schema_record
from db_modifier import modify_sql_db

def upload_data(table_path):
    # Step 1: Convert csv file into a df
    print("the table path is", table_path)
    try:
        df = pd.read_csv(table_path)
        # TODO: these should be specific types of exceptions
        print('success')
    except Exception:
        raise

    # Step 2: call schema manager. SM will make a new schema record for this uploaded data.
    # Will compare to directory of schemas and return command to add to existing table or create new table
    create_table_str = create_schema_record(df, table_path)

    placeholder_path = 'sample_db.db'
    modify_sql_db(create_table_str, placeholder_path)


