import pandas as pd
var1=pd.DataFrame(
    {
        "A":[1,2,3,4],
        "B":[2,3,4,5]
    }
)
var2=pd.DataFrame(
    {
        "A":[1,2,3,4],
        "C":[6,7,8,9]
    }
)
print(pd.merge(var1,var2,on="A"))

# Ab hum chahte C peeche aa jae B aage chla jae
print(pd.merge(var1,var2,on="A")[["C","A","B"]])

# Agr A ki value diff ho jae to
var3=pd.DataFrame(
    {
        "A":[1,2,3,4],
        "B":[2,3,4,5]
    }
)
var4=pd.DataFrame(
    {
        "A":[1,2,3,5],
        "C":[6,7,8,9]
    }
)
print(pd.merge(var3,var4,on="A"))
var5=pd.DataFrame(
    {
        "A":[1,2,3,4],
        "B":[2,3,4,5]
    }
)
var6=pd.DataFrame(
    {
        "A":[1,2,3,5],
        "C":[6,7,8,9]
    }
)
print(pd.merge(var5,var6,how="inner"))
print(pd.merge(var5,var6,how="outer"))

# Join Type	Kya karta hai
# inner	Sirf matching rows
# outer	Sab rows + NaN jahan data missing

# konsa data merge huwa konsa nhi
print(pd.merge(var5,var6,how="outer",indicator=True))
print(pd.merge(var5,var6,left_index=True,right_index=True))
print(pd.merge(var1,var2,left_index=True,right_index=True))
# agr name cange krna ho t uske liye suffix
print(pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("name","python")))



# concate

# 2 seriees ko jin krna
sr1=pd.Series([1,2,3,4])
sr2=pd.Series([5,6,7,8])
print(pd.concat([sr1,sr2]))

# for dataframes

var7=pd.DataFrame(
    {
        "A":[1,2,3,4],
        "B":[2,3,4,5]
    }
)
var8=pd.DataFrame(
    {
        "A":[1,2,3,5],
        "C":[6,7,8,9]
    }
)
print(pd.concat([var7,var8]))
print(pd.concat([var7,var8],axis=1))

# NaN ko htana 
d1=pd.DataFrame(
    {
        "A":[1,2,3,4],
        "B":[2,3,4,5]
    }
)
d2=pd.DataFrame(
    {
        "A":[1,2],
        "C":[6,7]
    }
)
print(pd.concat([d1,d2],axis=1,join="outer"))   #Nan show hoga
print(pd.concat([d1,d2],axis=1,join="inner"))   #Nan show nhi hoga 