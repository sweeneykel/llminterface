import pandas as pd
df = pd.read_csv('../tests/example_table.csv')
print(df.head())

def add_new_table(table):
    # use pandas.read_csv() to load data
    # call schema manager: schema manager will decide whether to append to create a table
    # based off of results from schema manager, either create new DB or append DB
    # return results to callee if success or failure
    return "This is a placeholder"