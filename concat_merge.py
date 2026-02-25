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