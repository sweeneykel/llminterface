from query_service_logic import get_all_schema_strings
from llm_interface_logic import ask_LLM

print(get_all_schema_strings('sample_db.db'))

# specifically tests ask_LLM(natural syntax, all schemas)
def test_LLM_translation(user_query_natural_syntax):


    # call schema manager: schema manager will provide schema context to the LLM
    placeholder_path = 'sample_db.db'
    schema_context = get_all_schema_strings(placeholder_path)

    # call LLM Interface: LLM Interface will provide a translation from natural structured language
    # to SQLite syntax
    llm_sql_syntax = ask_LLM(user_query_natural_syntax, schema_context)