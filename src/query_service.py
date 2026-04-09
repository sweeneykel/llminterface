from schema_manager import get_list_table_names, add_col_names
from llm_interface import ask_llm
from sql_db_validator import validate_LLM_output
from db_modifier import query_only_db
from human_itl import human_itl_confirms
from schema_manager import get_list_table_names, add_col_names

def get_query(user_query_natural_syntax: str, database_path: str):
    # call schema manager: schema manager will provide schema context to the LLM
    # OLD schema_context = get_all_schema_strings(database_path)
    schema_context = add_col_names(database_path, get_list_table_names(database_path))

    # call LLM Interface: LLM Interface will provide a translation to SQL syntax
    llm_sql_syntax = ask_llm(user_query_natural_syntax, schema_context)

    # call SQL/DB Validator: SQL/DB Validator will conduct verification on LLM Interface's translation
    if validate_LLM_output(llm_sql_syntax, schema_context):
        if human_itl_confirms("Do you want to proceed with this query?", llm_sql_syntax):
            # call SQLite DB
            print(query_only_db(llm_sql_syntax, database_path))
