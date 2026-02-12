import pandas as pd
result={
    "name": ["Ali","Jihan","Alam","Sarah"],
    "Science":[60,80,85,70],
    "C++":[80,70,95,60],
    "Python":[90,80,75,90]
}

calculation=pd.DataFrame(result)
calculation['Total_marks']=calculation["C++"]+calculation["Python"]+calculation["Science"]
calculation['Pass']=calculation['Total_marks']>=150
print(calculation)