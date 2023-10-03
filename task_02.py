import pandas as pd
import numpy as np

df=pd.read_excel('report.xlsx',keep_default_na=False,header=None)
df.drop(df.head(3).index, inplace= True)
df.replace("",np.nan,inplace=True)

df.dropna(axis='columns', thresh=12,inplace=True)

df.dropna(how='all',axis=0,inplace=True)
df.dropna(how='all',axis=1,inplace=True)


df.drop_duplicates(keep='first', inplace=True)
#since unnecessary data was there removing it like
df.drop([42,46,47], inplace=True)


df.columns=np.arange(0,len(df.columns))
df.reset_index(drop=True,inplace=True) 

print(df.head())


df.to_csv('output1.csv',header=False)
