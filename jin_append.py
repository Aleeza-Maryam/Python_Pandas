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