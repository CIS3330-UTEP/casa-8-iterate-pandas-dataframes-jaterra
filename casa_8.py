import pandas as pd


df = pd.read_csv('big-mac-full-index.csv')

for i, r in df.iterrows():
    print(r['date'],
          r['iso_a3'])
    

print(df.apply(lambda row: row['date'], axis=1))
print(df.apply(lambda row: row['iso_a3'], axis=1))