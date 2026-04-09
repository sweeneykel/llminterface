
from schema_manager import create_schema_record
import pandas as pd

'''
#if condition returns False, AssertionError is raised:
assert x == "goodbye"
#if condition returns False, AssertionError is raised:
assert x != "welcome", "x should not be 'welcome'"
'''

'''
import pytest
def test_zero_division():
    with pytest.raises(<SPECIFIC EXCEPTION YOU WANT THROWN>):
        # function you want to test
'''

'''
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    '''


def test_SQL_output():
    df = pd.read_csv('customers.csv')
    assert create_schema_record(df, 'customers') == (f'CREATE TABLE "customers" '
                                                     f'("primary_key_index" INTEGER PRIMARY KEY AUTOINCREMENT, '
                                                     f'"customer_id" INTEGER, '
                                                     f'"name" TEXT, '
                                                     f'"email" TEXT, '
                                                     f'"city" TEXT, '
                                                     f'"signup_date" TEXT);')

#def test_SQL_all_tables():
