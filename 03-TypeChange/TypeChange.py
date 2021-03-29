# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:49:33 2021

@author: Ignorant
"""
#Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
#Import

#Code

#Data Import
unprocessedData=pd.read_csv("UnprocessedData.csv")
#Data Import

#Var
data=unprocessedData
imputeData=data.iloc[:,0:4].values
classes=data.iloc[:,4:5].values
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
labelEncoder=preprocessing.LabelEncoder()
oneHotEncoder=preprocessing.OneHotEncoder()
#Var

#Data Pre Proccess
imputer=imputer.fit(imputeData)
imputeData=imputer.transform(imputeData)
data.iloc[:,0:4]=imputeData

classes=labelEncoder.fit_transform(classes)

oneHotEncoder.fit_transform(classes)
#Data Pre Proccess

#Code