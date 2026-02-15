import pandas as pd
info={
    "name ":["Ali",  "Zoya", "Hassan"],
    "Age ":[12,23,25],
    "Grade":["A","B","A"]

}
df=pd.DataFrame(info)
print(df)
df.to_csv("Info.csv")
