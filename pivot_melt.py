import pandas as pd
var=pd.DataFrame({
    "days":[1,2,3,4,5,6],
    "eng":[10,12,14,15,16,12],
    "math":[17,18,19,23,14,16]
})
print(var)    # ye table horizontal mai aae ga

# horizontal se vertical 
print(pd.melt(var))
# id bnana
print(pd.melt(var,id_vars=["days"]))

# variable aur value ka name change krna
print(pd.melt(var,id_vars=["days"],var_name="subject",value_name="marks"))

# pivot function
# for data arangement /reshaping
var1=pd.DataFrame({
    "days":[1,2,3,4,5,6],
    "st_name":["a","b","c","a","b","c"],
    "eng":[10,12,14,15,16,12],
    "math":[17,18,19,23,14,16]
})
# st_name k according data change
print(var1.pivot(index="days",columns="st_name"))   #atleast 2 arguments

# agr sirf eng ka data chahiye

print(var1.pivot(index="days",columns="st_name",values="eng"))

# aggfunc
var2=pd.DataFrame({
    "days":[1,1,1,2,2,6],
    "st_name":["a","b","a","a","b","c"],
    "eng":[10,12,14,15,16,12],
    "math":[17,18,19,23,14,16]
})
var3=var2.pivot_table(index="days",columns="st_name",aggfunc="mean",margins=True)   # margins se total aae ga
print(var3)
var4=var2.pivot_table(index="days",columns="st_name",aggfunc="sum",margins=True) 
print(var4)
var5=var2.pivot_table(index="days",columns="st_name",aggfunc="max",margins=True) 
print(var5)