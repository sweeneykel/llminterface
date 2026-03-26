import pandas as pd
df = pd.read_csv('../tests/example_table.csv')
print(df.head())


def add_new_table(table):
    # TODO : code for adding a table to a db
    # call schema manager: schema manager will decide whether to append to create a table
    # use pandas.read_csv() to load data
    # manually create and insert data into SQlite
    return "This is a placeholder"