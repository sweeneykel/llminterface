import pandas as pd
from schema_manager.schema_manager_logic import append_or_create

def convert_csv_df(path):
    try:
        return pd.read_csv(path)
        # TODO: these should be specific types of exceptions
    except Exception:
        raise

def add_new_table(table_path):
    # Step 1: use pandas.read_csv() to load data into df
    df = convert_csv_df(table_path)

    # Step 2: call schema manager. SM will make a new schema for this uploaded data. Will compare to directory of schemas.
    # If match, then delete new schema, return command to append.
    # If no match, then keep new schema, return command to add.
    decision = append_or_create(df)

    # based off of decision from schema manager, either create new DB or append DB
    # no match. create DB by call sqlite_db

    # match. append DB to existing by call sqlite_db


    # return results to callee if success(new table, appended table) or failure
    return "This is a placeholder"