import pandas as pd
from schema_manager_logic import create_table_record
from sqlite_db_logic import create_new_table

def add_new_table(table_path):
    # Step 1: Convert csv file into a df
    try:
        df = pd.read_csv(table_path)
        # TODO: these should be specific types of exceptions
        print('success')
    except Exception:
        raise

    # Step 2: call schema manager. SM will make a new schema record for this uploaded data.
    # Will compare to directory of schemas and return command to add to existing table or create new table
    append_or_create = create_table_record(df)

    if append_or_create == 'create':
        # Create brand-new table in db
        create_new_table(df)

    else:
        # Append data to existing table in db
        print(0)

    # return results to callee if success(new table, appended table) or failure
    return 0