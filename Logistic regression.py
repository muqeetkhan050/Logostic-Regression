# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:02:24 2022

@author: Muqeet
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Social_Network_Ads.csv")

data

X=data.iloc[:,[2,3]].values
y=data.iloc[:,4].values


#splitting datasset

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

#feature Scalling

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

#Fitting linear regression 

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

#predicitng test set result

y_pred=classifier.predict(X_test)

#Making confusion Matrix

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#visualising the training set result











