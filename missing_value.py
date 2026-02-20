import pandas as pd
var=pd.read_csv("E:\\pandas\\missing.csv")
print(var)

# missing data ko drop krna
var1=var.dropna()
print(var1)

# axis parameter se column ya row drop krna    axis=1 column    axis=0 row
var2=var.dropna(axis=1)
print(var2)

# agr poori row ki value missing hai
varr=pd.read_csv("E:\\pandas\\miss.csv")
print(varr)
var3=var.dropna(how="any")
print(var3)

# particular clumn k along NaN htana
var4=var.dropna(subset=["name "])
print(var4)

# inplace parameter se Nan kisi bhi random value se replace ho jati
var5=var.dropna(inplace=True)
print(var5)


# thresh jbaaik row k andr multple values NAn Ki aa jae

var6=var.dropna(thresh=1)
print(var6)

# FILLna us value ko fill krne k liye
var.fillna("python")
print(var)

# particular column k andr fillna
var.fillna({
    "name ":"python"
})
print(var)
print("HY")

# forwardfill method se missing value ko previous value se fill krna aur backward fill method se next value se fill krna
var.fillna(method="ffill")
print(var)
var.fillna(method="bfill")
print(var)

# kisi column k along
var.fillna(method="ffill",axis=1)
print(var)

# inplace jhn pe NaN hai whn fill
var.fillna(12,inplace=True)
print(var)


# limit parameter se kitni values fill krni hai
var.fillna("python",limit=2)
print(var)