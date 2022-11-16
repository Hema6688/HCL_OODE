import pandas as pd
data = pd.read_csv(r'C:\PythonCode1\Giant.csv')
df = pd.DataFrame(data, columns=['CEO', 'Established'])
print(df)