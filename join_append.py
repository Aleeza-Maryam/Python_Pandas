import pandas as pd
var1=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
})
var2=pd.DataFrame({
    "C":[16,17,18,19],
    "D":[20,21,22,23]
})
print(var1.join(var2))

# agr data aik maisekam ho jae to usko join krna
var3=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
})
var4=pd.DataFrame({
    "C":[16,17],
    "D":[20,21]
})
print(var3.join(var4))
# agr aik k sath index diya to C , D ki saari NaN ho jaen gi
var5=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
},index=["A","B","C","D"])
var6=pd.DataFrame({
    "C":[16,17],
    "D":[20,21]
})
print(var5.join(var6))
# index ko set krna

var7=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
},index=["A","B","C","D"])
var8=pd.DataFrame({
    "C":[16,17],
    "D":[20,21]
},index=["A","B"])
print(var7.join(var8))
print(var7.join(var8,how="inner"))
print(var7.join(var8,how="outer"))
print(var7.join(var8,how="left"))
print(var7.join(var8,how="right"))

# # agr column name same ho to value error aae ga 
# var9=pd.DataFrame({
#     "A":[1,2,3,4],
#     "B":[11,12,13,14]
# },index=["A","B","C","D"])
# var10=pd.DataFrame({
#     "A":[16,17],
#     "D":[20,21]
# },index=["A","B"])

# print(var9.join(var10))

# isliye suffix use krein ge
var9=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
},index=["A","B","C","D"])
var10=pd.DataFrame({
    "A":[16,17],
    "D":[20,21]
},index=["A","B"])

print(var9.join(var10,how="outer",lsuffix="_left",rsuffix="_right"))


# Append functon
# Pandas ke latest versions (2.0+) me append() remove ho chuka hai.Agar aap new version use kar rahi hain to error aayega:
var11=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
},index=["A","B","C","D"])
var12=pd.DataFrame({
    "A":[16,17],
    "D":[20,21]
},index=["A","B"])
# print(var11.append(var12))
print(pd.concat([var11, var12]))
print(pd.concat([var11, var12],ignore_index=True))

