# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:44:34 2021

@author: Ignorant
"""
#lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
#lib
#codes

#data import
unprocessedData = pd.read_csv("unprocessed.csv")
#data import

#var
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
irisNanValues=unprocessedData.iloc[:,0:4].values
#var

#data pre process
imputer=imputer.fit(irisNanValues)
irisNanValues=imputer.transform(irisNanValues)
unprocessedData.iloc[:,0:4]=irisNanValues
#data pre process

#codes