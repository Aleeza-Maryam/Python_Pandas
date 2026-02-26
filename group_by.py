import pandas as pd
var=pd.DataFrame(
    {
        "name":["Ali","Khan","zara","Zoya","Ali","Khan","zara","Zoya","Salar"],
        "age":[12,13,14,15,12,13,14,15,16],
        "s1":[90,80,70,60,90,80,70,60,100],
        "s1":[40,50,30,20,40,50,30,20,5]

    }
)
# random data group k andr arrange ho jae
var_new=var.groupby("name")
print(var_new)     #isse show nhi ho ga

for x,y in var_new:
    print(x)   #name show ho ga
    print(y)   #name k hisab se data show ho ga
    print()
