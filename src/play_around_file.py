from schema_manager import get_list_table_names, add_col_names

import re

def extract_tables(query: str) -> set[str]:
    q = query.lower()

    tables = set()
    tables.update(re.findall(r"\bfrom\s+(\w+)", q))
    tables.update(re.findall(r"\bjoin\s+(\w+)", q))

    return tables

def extract_columns(query: str) -> set[str]:
    q = query.lower()

    match = re.search(r"select\s+(.*?)\s+from", q)
    if not match:
        return set()

    cols_part = match.group(1)

    if cols_part.strip() == "*":
        return {"*"}

    columns = set()

    for col in cols_part.split(","):
        col = col.strip()

        # remove aliases (AS or implicit)
        col = col.split()[0]

        # handle table.column
        if "." in col:
            col = col.split(".")[1]

        columns.add(col)

    return columns

def validate_query(query: str, schema_map: dict[str, set[str]]) -> bool:
    tables = extract_tables(query)
    columns = extract_columns(query)

    # --- validate tables ---
    for table in tables:
        if table not in schema_map:
            print(f"[ERROR] Unknown table: {table}")
            return False

    # --- validate columns ---
    if "*" not in columns:
        valid_columns = set()
        for table in tables:
            valid_columns.update(schema_map[table])

        for col in columns:
            if col not in valid_columns:
                print(f"[ERROR] Unknown column: {col}")
                return False

    return True


db_dictionary = get_list_table_names('tq')
add_col_names('tq', db_dictionary)
schema = db_dictionary

schema_map = {k: set(v) for k, v in schema.items()}

query = "SELECT name, email FROM customers"
print(validate_query(query, schema_map))


query2 = 'SELECT AVG(total_amount) AS average_order_value FROM orders;'
print(validate_query(query2, schema_map))

query3 = 'SELECT product_name, price FROM products ORDER BY price DESC LIMIT 1;'
print(validate_query(query3, schema_map))



