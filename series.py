#git commit -m "first commit"
# git add .
# git commit -m "update message"
# git push

import pandas as pd
x=[1,2,3,4,5]
var=pd.Series(x)
print(var)
print(type(var))

# index chnage krna jaise 0 , 1 , 2 ki jgh a , b , c


x=[1,2,3,4,5]
var=pd.Series(x,index=['a','b','c','d','e'])
print(var)
print(type(var))
var1=pd.Series(x,index=['a','b','c','d','e'],name="python")


# datatype k chnage krna aur name dena 
var=pd.Series(x,index=['a','b','c','d','e'],datatype="float" ,name="python")
print(var)



# dictionary

dict={
    "name": ["bmw","porshe"],
    "por":[1,2]
}
var1=pd.Series(dict)
print(var)

#single data

s=pd.Series(12)
print(s)

# sigle data k multiple blocks

s1=pd.Series(12,index=[1,2,3,4,5])
print(s1)



# missing data handling

s2=pd.Series(12,index=[1,2,3,4,5])

s4=pd.Series(12,index=[1,2,3])
print(s2+s4)
