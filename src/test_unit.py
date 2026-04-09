import pytest
import pandas as pd
from csv_loader import upload_data
from schema_manager import create_schema_record, get_list_table_names, add_col_names
from human_itl import human_itl_confirms

# test csv_loader
def test_read_csv():
    with pytest.raises(UnicodeDecodeError):
        upload_data('sqlite_test_input.xlsx', 'jftdb')

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

# Unit Tests for schema_manager.py
def test_create_schema_record():
    df = pd.read_csv('customers.csv')
    assert create_schema_record(df, 'customers') == 'CREATE TABLE "customers" ("customer_id" INTEGER, "name" TEXT, "email" TEXT, "city" TEXT, "signup_date" TEXT);'

def test_get_list_table_names():
    assert get_list_table_names('tq') == {"customers":[], "order_items":[], "orders":[], "products":[]}

def test_add_col_names():
    df = {"customers":[], "order_items":[], "orders":[], "products":[]}
    assert add_col_names('tq', df) == {"customers":['customer_id', 'name', 'email', 'city', 'signup_date'], "order_items":['order_item_id', 'order_id', 'product_id', 'quantity', 'unit_price'], "orders":['order_id', 'customer_id', 'order_date', 'status', 'total_amount'], "products":['product_id', 'product_name', 'category', 'price', 'stock_quantity']}

