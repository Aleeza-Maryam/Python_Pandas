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
