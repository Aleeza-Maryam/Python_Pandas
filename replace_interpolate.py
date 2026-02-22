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

# limit parameter se kitni values replace krni hai
var.replace(23,method="bfill",limit=1)

# inplace parameter se original data change ho jata hai
var.replace(23,method="bfill",inplace=True)

# interpolate method se missing value ko fill krna
# blank value k automatically fll krta hai previos value se uske accrding

print(var)
var8=var.interpolate()
print(var8)

# axis aur method parameter k sath interpolate
var9=var.interpolate(method="linear",axis=0)
print(var9)
# limiy directed interpolation
var10=var.interpolate(method="linear",limit_direction="forward",limit=1)
var11=var.interpolate(method="linear",limit_direction="backward",limit=1)
var12=var.interpolate(method="linear",limit_direction="both",limit=1)
print(var10)
print(var11)
print(var12)
var.interpolate(limit_area="outside")  #  NaN ko fill ni kre ga
var.interpolate(limit_area="inside")  #  NaN ko fill kre ga