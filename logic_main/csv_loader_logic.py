import pandas as pd
from schema_manager_logic import create_schema_record
from db_modifier import add_table_to_db

def upload_data(table_path):
    # Step 1: Convert csv file into a df
    try:
        df = pd.read_csv(table_path)
        # TODO: these should be specific types of exceptions
        print('success')
    except Exception:
        raise

    # Step 2: call schema manager. SM will make a new schema record for this uploaded data.
    # Will compare to directory of schemas and return command to add to existing table or create new table
    create_table_str = create_schema_record(df)

    placeholder_path = 'sample_db.db'
    add_table_to_db(create_table_str, placeholder_path)


