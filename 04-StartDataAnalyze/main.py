#Library
import seaborn as sns
import pandas as pd
import numpy as np
import scipy as spcs
import matplotlib.pyplot as plt

#DataSet
dataSet = sns.load_dataset("planets")
df = dataSet.copy()

#Dataset Analyze
print(df.head())
print(df.tail())

print(df["method"].count())

print(df.info())

print(df.dtypes)
df.method = pd.Categorical(df.method)
print(df.dtypes)

print(df.shape)
print(df.columns)

print(df.describe().T)
print(df.describe(include="all").T)

#Missing values
print("Eksik Veri Var mı ? : ", df.isnull().values.any())

print("Toplam Eksik Veri Sayıları : \n", df.isnull().sum())

df["orbital_period"].fillna(0, inplace = True)
df["mass"].fillna(df.mass.mean(), inplace = True)
df["distance"].fillna(df.distance.mean(), inplace = True)

print("Toplam Eksik Veri Sayıları : \n", df.isnull().sum())

print(df.method.unique())

print(df.method.value_counts())

#matplotlib graph
#df["method"].value_counts().plot.barh().set_title("Titles")
#plt.show()
#df["number"].value_counts().plot.barh()
#plt.show()


#Dia Dataset process
dataSet= sns.load_dataset("diamonds")
df=dataSet.copy()

print(df.cut.head())

cut_Category_Order = ["Fair" , "Good" , "Very Good" , "Premium" , "Ideal"]
df.cut = df.cut.astype(pd.CategoricalDtype(categories=cut_Category_Order , ordered = True))

print(df.cut.head(1))

sns.barplot(x = df.cut , y = df.cut.index , data = df)
plt.show()
