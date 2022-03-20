# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 08:14:39 2020

@author: amazi
"""

import pandas as pd
df = pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\lesson5.xlsx')
df.index = ['0a','1b','2c','3d','4e']
df1 = df
df

#section 1 数值删除
#传入列名删除列
df.drop(['名称','顶踩比例'], axis = 1)#这里axis等于1是列，axis等于0是行

#传入列号删除列
df.drop(df.columns[[0,3]],axis = 1)

#删除行
#传入列名删除行
df.drop(['0a','2c'],axis = 0)

#传入行号删除行
df.drop(df.index[[0,2]],axis = 0)

#section 2 数值计数
#查看某个值出现的次数
df['顶踩比例'].value_counts()

#查看数值出现的百分比
df['顶踩比例'].value_counts(normalize = True)

#section 3 获取唯一值
df['顶踩比例'].unique()

#section 4 数值查找
#针对某列
df['观看次数'].isin([480,235])#有480或235都是true

#针对全表
df.isin([480,235])





