import pandas as pd
df = pd.read_csv('online-retail.csv')
df.head()
print(df)
df['LinePrice'] = df['Quantity'] * df['Unitprice']
df.head()
print(df)