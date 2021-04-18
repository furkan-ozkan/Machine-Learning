# Machine Learining
In this documantery for datasets will be used "df" variable name, and all varibales will be used like "VAR","VAR2","VAR3" etc...
### Installs

------------


!pip install pandas_datareader
### Libs

------------

- import numpy as np
- import pandas as pd
- import seaborn as sns
- import matplotlib as plt
- import pandas_datareader as pr
- from pandas.api.types import CategoricalDtype
### Data Analyze
------------
- df.head()
- df.tail()
- df.info()
- df.dtypes
- df.shape
- df.columns
- df.describe().T-> optionel -> df.describe(include = “all”).T
- df[“VAR”].describe()
- df.column.unique()
##### Missing Values

------------
- df.isnull().sum()
- df.["VAR"].fillna(0,inplace = True) -> 0 can be change, this code right now means “all nan values must be zero”
##### Categorical

------------
- df.select_dtypes(include = [“float64”, “int64”])
- df.pivot(“VAR”,”VAR2”,”VAR3”)
- df. select_dtypes(include = ["someType"]
- df[“VAR”] .value_counts()
- df[“VAR”] .value_counts().count()
- df.VAR.astype(CategoricalDtype( categories = [1,2,3,4…], ordered = True))
- df.index=pd.DatetimeIndex(df.index)
#####  Graphics

------------
###### List
- barplot
- catplot
- - could be used as default.
- - kind = "point"
- - kind = "violin"
- histplot
- kdeplot
- scatterplot
- lmplot
- pairplot
- heatmap (pivot df must be)
- lineplot
- facetgrid
- groupby

####### Sample Usage
- df[“VAR”] .value_counts().plot.barh().set_title(“test”);
- sns.barplot(x = “VAR”, y = df.VAR.index, hue = “color” , data = df);
- sns.catplot(x = “VAR” , y = “VAR2”,hue = “VAR3”,kind= “point”,data = df);
- sns.catplot(x = “VAR” , kind= “violin”,data = df);
- sns.histplot(x.VAR, kde = False);
- sns.kdeplot(x.Var,shade=True);
- sns.scatterplot(x="total_bill",y="tip",hue="size",style="sedf",size="size",data=df);
- sns.lmplot(x="VAR",y="VAR2",hue="VAR3",col=”VAR4”,row=”VAR5”,data=df)
- sns.pairplot(hue="VAR",kind="reg",data=df)
- sns.heatmap(df) -> df must be pivot – for this look at Categorical header
- sns.heatmap(df,annot =True,fmt="d",linewidths =.5)
- sns.lineplot(x="VAR",y="VAR2",hue="VAR3",style ="VAR4",markers=True, dashes = False,data=df)
- (sns.FaceTGrid(df,hue= “CAT_VAR”,height=5,dflim=(0,10000)).map(sns.kdeplot,“price”,shade=True ).add_legend());
- df.groupby([“VAR”, “VAR2”])[“VAR3”].mean()

