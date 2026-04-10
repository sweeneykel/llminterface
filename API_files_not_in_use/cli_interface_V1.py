import argparse
from csv_loader import upload_data
from query_service import get_query

# LLM Usage: Used chatgpt to clarify argparse concepts and consider different options for user input.

# this module will only be able to call: csv_loader.py (to upload new data) or query_service.py (submit a query)

# Make parser
parser = argparse.ArgumentParser(
                    prog='LLM Interface',
                    description='This program allows you to 1) upload a csv file into a database and 2) make natural language queries to retrieve data',
                    epilog='Text at the bottom of help')

# Define commands with user input
parser.add_argument('--addcsv', help='include the path to the file that you want to add to the db')
parser.add_argument('--query', nargs='+', type=str, help='in plain spoken text, write your query')

# Interpret input
args = parser.parse_args()

if args.query:
    # Begin query routine. Call csv_loader_logic
    # args.query is list
    get_query(args.query)

if args.addcsv:
    # Begin addcsv routine. Call query_service_logic
    # args.addcsv is str
    upload_data(args.addcsv)