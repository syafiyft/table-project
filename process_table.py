import pandas as pd

# load CSV file
file_path = "Table_Input.csv"  
df = pd.read_csv(file_path)

# display df
print("Loaded DataFrame:")
print(df)

# extract values
a5 = df.loc[df['Index #'] == 'A5', 'Value'].values[0]
a20 = df.loc[df['Index #'] == 'A20', 'Value'].values[0]
a15 = df.loc[df['Index #'] == 'A15', 'Value'].values[0]
a7 = df.loc[df['Index #'] == 'A7', 'Value'].values[0]
a13 = df.loc[df['Index #'] == 'A13', 'Value'].values[0]
a12 = df.loc[df['Index #'] == 'A12', 'Value'].values[0]

# for calculations
alpha = a5 + a20
beta = a15 / a7 if a7 != 0 else "Error (division by zero)"
charlie = a13 * a12

# create a new df for Table 2
table_2 = pd.DataFrame({
    'Category': ['Alpha', 'Beta', 'Charlie'],
    'Value': [alpha, beta, charlie]
})

# save tables
df.to_csv("Table1.csv", index=False)  #t1
table_2.to_csv("Table2.csv", index=False)  #results

print("Tables processed and saved successfully.")
