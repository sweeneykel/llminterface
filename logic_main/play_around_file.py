import pandas as pd

df = pd.read_csv('../test/example_table.csv')

col_list = ['id', 'INTEGER PRIMARY KEY AUTOINCREMENT,']

# def convert(orig):
#     if orig
#
#     return converted


# Chat GPT generated code ---------*
def pandas_dtype_to_sql(dtype) -> str:
    dtype_str = str(dtype)
    if "int" in dtype_str:
        return "INTEGER"
    elif "float" in dtype_str:
        return "REAL"
    elif "bool" in dtype_str:
        return "INTEGER"
    elif "datetime" in dtype_str:
        return "TEXT"
    elif "timedelta" in dtype_str:
        return "REAL"
    elif dtype_str == "category":
        return "TEXT"
    else:
        return "TEXT"
# Chat GPT generated code ---------*


# df.columns creates an Index object
# df.dtypes creates a Series object (accessed with help of Index object)
data_types = df.dtypes
for col_key in df.columns:
    col_df_type = data_types.loc[col_key]
    sql_translation = pandas_dtype_to_sql(col_df_type)








#for i in df.dtypes:
    #print(i)

print(col_list)