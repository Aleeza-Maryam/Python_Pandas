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
print(csv3)
# header files skip(rows skip)

csv_4=pd.read_csv("E:\\Pandas\\info.csv",skiprows=1)
print(csv_4)

# index ko change krna
csv_5=pd.read_csv("E:\\Pandas\\info.csv",index_col="name ")
print(csv_5)

# heading ko change krna mtln kisi row ki values of heading bnana
csv_6=pd.read_csv("E:\\Pandas\\info.csv",header=2)
print(csv_6)
# headings ka name apni mrzi se likhna

csv_7=pd.read_csv("E:\\Pandas\\info.csv",names=["col1","col2","cl3","col4"])
print(csv_7)
# header ko remove krna
csv_8=pd.read_csv("E:\\Pandas\\info.csv",header=None)
print(csv_8)
# prefix add krna
# csv_9=pd.read_csv("E:\\Pandas\\info.csv",prefix="col")
# print(csv_9)

# datatype ko change krna
csv_10=pd.read_csv("E:\\Pandas\\info.csv",dtype={"name ":str,"Grade":str})
print(csv_10)