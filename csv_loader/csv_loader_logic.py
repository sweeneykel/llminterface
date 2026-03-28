import pandas as pd

# test
# df = pd.read_csv('../tests/example_table.csv')
# print(df.head())

def add_new_table(table):
    # use pandas.read_csv() to load data
    df = pd.read_csv(table)

    # call schema manager: schema manager will decide whether to append to create a table

    # based off of results from schema manager, either create new DB or append DB
    # no match. create DB


    # match. append DB to existing.

    # return results to callee if success or failure

    return "This is a placeholder"