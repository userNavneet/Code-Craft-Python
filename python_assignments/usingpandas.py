import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Emma', 'David', 'Sophia', 'James'],
    'Age': [28, 35, 40, 29, 42],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Boston']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

# Accessing columns
print("Accessing columns:")
print(df['Name'])  # Accessing a single column
print(df[['Name', 'Age']])  # Accessing multiple columns
print()

# Accessing rows
print("Accessing rows:")
print(df.loc[0])  # Accessing a single row by label
print(df.iloc[0])  # Accessing a single row by integer index
print(df.loc[[1, 3]])  # Accessing multiple rows by label
print(df.iloc[[1, 3]])  # Accessing multiple rows by integer index
print()

# Adding a new column
df['Gender'] = ['Male', 'Female', 'Male', 'Female', 'Male']
print("DataFrame with new column:")
print(df)
print()

# Filtering rows based on condition
print("Filtered DataFrame:")
print(df[df['Age'] > 30])
print()

# Grouping and aggregating data
print("Grouped DataFrame:")
grouped_df = df.groupby('Gender').agg({'Age': 'mean'})
print(grouped_df)
print()

# Merging DataFrames
data2 = {
    'Name': ['John', 'Emma', 'David'],
    'Salary': [60000, 70000, 80000]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='Name', how='left')
print("Merged DataFrame:")
print(merged_df)
print()

# Exporting DataFrame to CSV
df.to_csv('example.csv', index=False)
print("DataFrame exported to CSV.")