import pandas as pd
dataset=pd.read_csv("E:\\Pandas\\heart.csv")
print(dataset)
# top 5 rows
rows_5=dataset.head()
print(rows_5)
# last 5 rows 
last_5=dataset.tail()
print(last_5)
# Find Shape of Our Dataset (Number of Rows And Number of Columns)
shape=dataset.shape
print(shape)
#  Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
info=dataset.info()
print(info)
# Check Null Values In The Dataset
null=dataset.isnull()
print(null)

# Check For Duplicate Data and Drop Them
duplicate=dataset.duplicated().sum()
print(duplicate)
drop_duplicates=dataset.drop_duplicates(inplace=True)
print(drop_duplicates)

# Get Overall Statistics About The Dataset
stats=dataset.describe()
print(stats)
#  Correlation 
cor=dataset.corr()
print(cor)

# How Many People Have Heart Disease, And How Many Don't Have Heart Disease In This Dataset?
target=dataset.target.count()
print(f"{target} people have heart disease")

# Find Count of  Male & Female in this Dataset
gender=dataset.sex.value_counts()
print(gender)

# Find Gender Distribution According to The Target Variable
gender_target=dataset.groupby("target")["sex"].value_counts()
print(gender_target)

# Check Age Distribution In The Dataset
age_dist=dataset.age.value_counts()
print(age_dist)

# Check Chest Pain Type
chest_pain=dataset.cp.value_counts()
print(chest_pain)
# Show The Chest Pain Distribution As Per Target Variable
chest_target=dataset.groupby("target")["cp"].value_counts()

#  Show Fasting Blood Sugar Distribution According To Target Variable
fbs_target=dataset.groupby("target")["fbs"].value_counts()

# Check Resting Blood Pressure Distribution
rest_blood=dataset.value_counts()
print(rest_blood)

# Compare Resting Blood Pressure As Per Sex Column
rest_bp=dataset.groupby("sex")["trestbps"].value_counts()
print(rest_bp)

# Show Distribution of Serum cholesterol
serum_cholestrol=dataset.chol.value_counts()
print(serum_cholestrol)

# Plot Continuous Variables
import matplotlib.pyplot as plt
dataset.hist(figsize=(10,10))
plt.show()