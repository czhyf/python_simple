import pandas as pd

df = pd.read_csv('/Users/caozhan/a.csv',header=None)
print(df)
print("-----------")
df=pd.DataFrame(df)
print(df)