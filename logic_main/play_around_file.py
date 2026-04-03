import pandas as pd

df = pd.read_csv('example_table.csv')

print(type(df.columns))
print(type(df.dtypes))

# df.columns creates an Index object
# df.dtypes creates a Series object (accessed with help of Index object)
data_types = df.dtypes
for k in df.columns:
    print("column name: ", k)
    print(data_types.loc[k])



#for i in df.dtypes:
    #print(i)