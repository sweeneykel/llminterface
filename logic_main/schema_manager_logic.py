
# Schema Manager Part 1
def create_schema_record(df):
    # Creates a Schema record for all CSVs uploaded.


    # LLM: code review on df.dtypes.to_dict() https://chatgpt.com/g/g-p-69c84b135ed48191b95908e323c125fd-ec530-llm-interface-project/c/69cfc71c-2f1c-8331-a5e4-1000b37ff97a
    col_label_dtype = df.dtypes.to_dict()

    # Checks against db of existing objects from tables that were already added to db


    # If exact match, delete newly created record and instruct csv_loader_logic.py to add to an existing table


    # Else, store newly created record for future comparison and help with queries and instruct csv_loader_logic to create a new table in the db


    return 'create'






