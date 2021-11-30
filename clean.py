import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')

print(df)
del df['Star_name.1']
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']
del df['Luminosity']
del df['Unnamed: 5']
print(df)
df.reset_index(drop=True,inplace = True)
print(df)

df.to_csv('final_data.csv')

