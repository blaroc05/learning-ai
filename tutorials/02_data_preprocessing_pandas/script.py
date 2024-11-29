import pandas as pd

# Load the data
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    'Price': [1200, 800, None, 1200, 800],
    'Quantity': [2, None, 5, 3, 2],
    'OrderDate': ['2023-01-05', '2023-02-10', '02/15/2023', None, '2023-03-20'],
    'Region': ['West', 'East', 'North', 'West', 'East'],
    'Discount': [0.1, 0.05, None, 0.1, 0.05]
}
df = pd.DataFrame(data)

# Display the first few rows
print(df.head())

# Get a summary of the dataset
print(df.info())

# View basic statistics for numeric columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Fill missing Price with median
df['Price'] = df['Price'].fillna(df['Price'].median())

# Fill missing Quantity with mode
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mode()[0])

# Fill missing Discount with 0.0
df['Discount'] = df['Discount'].fillna(0.0)

# Fill missing OrderDate with a placeholder and convert to datetime
df['OrderDate'] = df['OrderDate'].fillna('1900-01-01')
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='mixed')

# Check for duplicates
print(df.duplicated().sum())

# Drop duplicates if any
df = df.drop_duplicates()

# Standardize text columns (e.g., Product, Region)
df['Product'] = df['Product'].str.lower()
df['Region'] = df['Region'].str.capitalize()

# Ensure OrderDate is in datetime format
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create Total Sales column
df['TotalSales'] = df['Price'] * df['Quantity']

# Encode Region as dummy variables
df = pd.get_dummies(df, columns=['Region'], drop_first=True)


# Display the first few rows
print(df.head())