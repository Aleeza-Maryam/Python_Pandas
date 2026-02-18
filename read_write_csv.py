import pandas as pd
csv_1=pd.read_csv("E:\\Downloads\\machine-readable-business-employment-data-sep-2025-quarter.csv")
print(csv_1)

# index dekhna k khn se start ho rha khn stop
print(csv_1.index)
# columns dekhna (names)
print(csv_1.columns)
# min max dekhna ya mean std...
print(csv_1.describe())
 
# fixed data chahye jaise start k 2 3 rows
print(csv_1.head(3))
# jaise ab last k dekne to 
print(csv_1.tail(2))
# fixed rows ko dekhna
print(csv_1[:3])
# index ko array k andr
print(csv_1.index.array)
# numpy k andr
print(csv_1.to_numpy)


# OR

import numpy as np
v=np.asarray(csv_1)
print(v)
# ascending to descending
csv_1.sort_index(axis=0,ascending=False)
print(csv_1)
# data change krna hai
csv_1["Period"][1]=1234
# print(csv_1)   warning aae gi

# another safe method
csv_1.loc[0,"Period"]="1"
print(csv_1)

# specific ondex ka data show krna
csv_1.loc[[3,4],["Period","STATUS"]]
print(csv_1)
# saara data chahhiye specific columns ka
csv_2=pd.read_csv("E:\\Downloads\\machine-readable-business-employment-data-sep-2025-quarter.csv")
csv_2.loc[[2,3],:]
print(csv_2)

# iloc
csv_2.iloc[0,1]
print(csv_2)

# delete column
csv_2.drop("STATUS",axis=1)
print(csv_2)

#delete row
csv_2.drop(3,axis=0)
print(csv_2)