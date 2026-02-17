import pandas as pd
csv=pd.read_csv("E:\\Pandas\\info.csv")
print(csv)

# jaise ab first 3 rows chahiye bas ya first 2
csv1=pd.read_csv("E:\\Pandas\\info.csv",nrows=2);
print(csv1)

# sepcific column chahiye
csv2=pd.read_csv("E:\\Pandas\\info.csv",usecols=["name ","Grade"])
print(csv2)

# colums ko index k through bhi fetch kr skte
csv3=pd.read_csv("E:\\Pandas\\info.csv",usecols=[0,1])