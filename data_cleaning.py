import pandas as pd

df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

# Filter pink morsel
df0 = df0[df0['product'] == 'pink morsel']
df1 = df1[df1['product'] == 'pink morsel']
df2 = df2[df2['product'] == 'pink morsel']

# Clean price column - remove $ and convert to float
df0['price'] = df0['price'].str.replace('$', '', regex=False).astype(float)
df1['price'] = df1['price'].str.replace('$', '', regex=False).astype(float)
df2['price'] = df2['price'].str.replace('$', '', regex=False).astype(float)

# Create sales column
df0['sales'] = df0['price'] * df0['quantity']
df1['sales'] = df1['price'] * df1['quantity']
df2['sales'] = df2['price'] * df2['quantity']

# Combine
df_combined = pd.concat([df0, df1, df2], ignore_index=True)

# Select columns and save
df_combined = df_combined[['sales', 'date', 'region']]
df_combined.to_csv('data/output.csv', index=False)