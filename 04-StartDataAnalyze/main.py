#Library
import seaborn as sns
import pandas as pd
import numpy as np
#DataSet
dataSet = sns.load_dataset("diamonds")
db = dataSet.copy()

#Dataset Analyze
print(db.head())
print(db.tail())

print(db["carat"].count())

print(db.dtypes)
db.cut = pd.Categorical(db.cut)
print(db.dtypes)

print(db.shape)
print(db.columns)

print(db.describe().T)
print(db.describe(include="all").T)


