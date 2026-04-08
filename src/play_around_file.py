import pandas as pd

goal = "SELECT name FROM sqlite_master WHERE name='spam'"

table_name = "'spam'"
confirm_modify_db = f"SELECT name FROM sqlite_master WHERE name={table_name}"

print(goal)
print(confirm_modify_db)

if goal == confirm_modify_db:
    print('yes')