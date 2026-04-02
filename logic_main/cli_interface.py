import argparse
# Resources: Used chatgpt to clarify argparse concepts and consider different options for user input

# This will only be able to call:
# upload new data
# calls csv_loader_logic.py

# get stored data
# calls query_service_logic.py

# Make parser
parser = argparse.ArgumentParser(
                    prog='LLM Interface',
                    description='This program allows you to 1) upload a csv file into a database and 2) make natural language queries to retrieve data',
                    epilog='Text at the bottom of help')
# Define commands
parser.add_argument('--addcsv', help='include the path to the file that you want to add to the db')
parser.add_argument('--query', nargs='+', type=str, help='in plain spoken text, write your query')
# Interpret
args = parser.parse_args()

if args.query:
    # Begin query routine. Call csv_loader_logic
    print(" ")

if args.addcsv:
    # Begin addcsv routine
    print(" ")



