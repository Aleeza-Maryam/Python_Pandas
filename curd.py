import pandas as pd
var=pd.DataFrame({
    "a":[1,2,3,4],
    "b":[4,6,8,3],
    "c":[4,6,8,3]
})

var.insert(3,"new_col",var["a"])
print(var)
var.insert(4,"new_col2",[5,8,3,7])
print(var)

# limited data chahiye
var["limited_data"]=var["new_col"][:3]
print(var)


# new row
var.loc[4]=[1,2,3,4,5,6]
print(var)

# delete column     pop
var1=var.pop("limited_data")
print(var1)
print(var)


# del

del var["new_col2"]
print(var)



# row delete
var=var.drop(3)
print(var)

# multiple rows del
var=var.drop([0,4])
print(var)
