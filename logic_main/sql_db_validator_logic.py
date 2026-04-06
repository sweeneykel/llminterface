from schema_manager_logic import get_all_schema_strings


#placeholder_path = 'sample_db.db'
#schema_context = get_all_schema_strings(placeholder_path)
#print(schema_context)

def validate_LLM_output(llm_sql_syntax):
    # TODO: come back to this after
    # no destructive querys (drop, inject, corrupt)
    #if "drop" in llm_sql_syntax.lower():

    print("This is the SQL syntax the LLM provided and that is being analyzed: ", llm_sql_syntax)
    # VALIDATION
    # only allow SELECT queries or alternatively allow read only sql connection
    if not llm_sql_syntax.startswith("SELECT"):
        # LLM help line below
        raise ValueError("Invalid input")

    # Reject queries referencing unknown tables


    # Reject queries referencing unknown columns

    return True

