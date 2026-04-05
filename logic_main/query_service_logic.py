from schema_manager_logic import get_all_schema_strings
from llm_interface_logic import ask_LLM
from sql_db_validator_logic import validate_LLM_output
from db_modifier import query_only_db

def get_query(user_query_natural_syntax):
    # call schema manager: schema manager will provide schema context to the LLM
    placeholder_path = 'sample_db.db'
    schema_context = get_all_schema_strings(placeholder_path)

    # call LLM Interface: LLM Interface will provide a translation from natural structured language
    # to SQLite syntax
    llm_sql_syntax = ask_LLM(user_query_natural_syntax, schema_context)

    # call SQL/DB Validator: SQL/DB Validator will conduct verification on LLM Interface's translation
    if validate_LLM_output(llm_sql_syntax):
        # call SQLite DB
        query_only_db(llm_sql_syntax, placeholder_path)


    return 0