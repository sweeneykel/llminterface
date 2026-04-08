import pandas as pd

df = pd.read_csv('customers.csv')

placeholders = f"({', '.join('?' for _ in df.columns)})"
print(placeholders)

print(df)

print(df.loc[1:])