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

    # Step 2: call schema manager. schema manager will decide whether to append to create a new table
    # TODO: change from method to API once logic is ready
    append_or_create(df)

    # based off of results from schema manager, either create new DB or append DB
    # no match. create DB


    # match. append DB to existing.


    # return results to callee if success or failure
    return "This is a placeholder"