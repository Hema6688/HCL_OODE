import pandas as pd
data = {'Country': ['Belglum', 'India', 'Brazil'], 'Capital': ['Brussels', 'New Delhi', 'Brasilia'], 'Population': [52117214, 12345678, 76609853]}
df = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])
print(df)