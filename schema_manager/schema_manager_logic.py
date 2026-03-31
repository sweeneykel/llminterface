# discover existing tables in the db
# represent table schemas as structured objects
# compare schemas to determine compatibility (append vs create)
# provide schema info to other components like Query Service, CSV Loader, LLM

# schema class
# list of tuples [(column_name,column_type),( , )]
# can compare regardless of order set(list_a) == set(list_c)
# if match, then delete schema class. Return command to append only.
# if no match, keep schema class. Return command to add new.


# determine if append or create a new df
def append_or_create(df):

    df.columns()
    return 0

def create_schema_record(df):

    return 0

def find_schema_context(table):
    return 0