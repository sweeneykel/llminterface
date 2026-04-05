from schema_manager_logic import get_all_schema_strings
from llm_interface_logic import ask_chat_gpt

def get_query(user_query):
    # call schema manager: schema manager will provide schema context to the LLM
    placeholder_path = 'sample_db.db'
    schema_context = get_all_schema_strings(placeholder_path)

    print("this is schema: ", schema_context)
    # call LLM Interface: LLM Interface will provide a translation from natural structured language
    # to SQLite syntax
    print("chats response: ", ask_chat_gpt(user_query, schema_context))

    # call SQL/DB Validator: SQL/DB Validator will conduct validation and verification on LLM Interface's translation
    # call SQLite DB
    # return results of query request or error message

    return 0