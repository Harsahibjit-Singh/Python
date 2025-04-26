# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 19:08:49 2025

@author: harsahibjit singh
"""

import pandas as pd
import numpy as np
s1=pd.Series([1, 2, 3, 4])
print(s1)
s1=pd.Series(['A', 2, 'C', 'D'],index=[1,2,3,4]) #using labels
print(s1[1])
a1=np.array([1,2,3,4])
s1=pd.Series(a1)
print(s1)
dict1={"India":"New Delhi","England":"london"}
s1=pd.Series(dict1)
print(s1[0])
print(s1[[0,1]]) #multiple index
print(s1[0:1]) #slicing


#Attributes of Series
s1.name='Capitals'
s1.index.name='Countries'
print(s1.values)
print(s1.size)
print(s1.empty)



#methods on series
s1=pd.Series(np.arange(0,11))
print(s1.head(5))
print("count : ",s1.count())
print(s1.tail(3))


#Mathematical Operations
S2=pd.Series([1,2,4,5,6])
print(s1+S2)# add
print(s1.add(S2,fill_value=0))
print(s1-S2)# sub
print(s1.sub(S2,fill_value=0))
print(s1*S2)# mul
print(s1.mul(S2,fill_value=0))
print(s1/S2)# div
print(s1.div(S2,fill_value=0))