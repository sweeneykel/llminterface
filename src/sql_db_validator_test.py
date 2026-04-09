from query_service import get_list_table_names, add_col_names
from llm_interface import ask_llm
from db_modifier import query_only_db

tuq1 = "What is the average cost of a product that is available for sale?"
tuq2 = "How many orders are still being processed?"
tuq3 = "How many orders are completed?"
tuq4 = "What is the most expensive item available for sale?"

# specifically test ask_LLM(natural syntax, all schemas)
def test_LLM_translation(user_query_natural_syntax):

    # call schema manager: schema manager will provide schema context to the LLM
    schema_context = add_col_names('tq',get_list_table_names('tq'))
    # OLD schema_context = get_all_schema_strings('tq.db')
    print(schema_context)

    # call LLM Interface: LLM Interface will provide a translation from natural structured language
    # to SQLite syntax
    llm_sql_syntax = ask_llm(user_query_natural_syntax, schema_context)


test_LLM_translation(tuq1)