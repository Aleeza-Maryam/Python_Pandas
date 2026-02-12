# List se dataframe
import pandas as pd
l =[1,2,3,4,5]
var=pd.DataFrame(l)
print(var)

# dictionary se dataframe
dict={
    "name ": ["Ali","Khan","Zoya"],
    "roll no":[1,2,3]
}
var1=pd.DataFrame(dict)
print(var1)


# particular_column chahiye to
particular_col=pd.DataFrame(dict,columns=["roll no"])
print(particular_col)


# Multiple columns

dict2={
    "name": ["Ali","Khan","Zoya"],
    "roll no":[1,2,3],
     2:[4,5,6],
     "address":["Pakistan","Canada","Italy"]


}
var3=pd.DataFrame(dict2,columns=["name",2,"address"])
print(var3)

# agr index ko chnage krna mtlb  0 , 1 ... se a, b .... krna
var4=pd.DataFrame(dict2,columns=["name",2,"address"] , index=["A","B","C"])
print(var4)


# agr particular index ki clue access krni hai to
var5=pd.DataFrame(dict2,columns=["name",2,"address"] , index=["A","B","C"])
print(var5["name"]["C"])


# list within list

list_1=[
    [1,2,3,4,5],
    [6,7,8,9,10]
]
var6=pd.DataFrame(list_1)
print(var6)

var7=pd.DataFrame(list_1)
print(var7[1])
print(var7.loc[1].values)


# series se dataframe
sr={
    "a":pd.Series([1,2,3,4]),
    "b":pd.Series([7,8,9,5])
}

var8=pd.DataFrame(sr)
print(var8)