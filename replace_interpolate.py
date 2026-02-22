import pandas as pd
var=pd.read_csv("E:\\pandas\\info.csv")
var1=var.replace(to_replace=23,value=25)
print(var1)


# serial no. ko replace krna
var2=var.replace([12,23,25],1)
print(var2)

# reqex(regular expression)
var3=var.replace("[A-Za-z]","python",regex=True)
print(var3)


# using dictionary
var4=var.replace({
    "name ":'[A-Za-z]'
},22,regex=True)
print(var4)



# backward replace
print(var)
var5=var.replace(23,method="bfill")
print(var5)


# ffill
var6=var.replace("Zoya",method="ffill")
print(var6)
