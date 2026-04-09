from schema_manager import get_list_table_names, add_col_names


db_dictionary = get_list_table_names('tq')
print(db_dictionary)
add_col_names('tq', db_dictionary)
print(db_dictionary)