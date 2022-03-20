# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:59:55 2020

@author: amazi
"""

import pandas as pd
df1 = pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\lesson5.xlsx', sheet_name = 'Sheet1')
df2 = pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\lesson5.xlsx', sheet_name = 'Sheet2')
df1
df2

#section 1 插入新的行和列
#插入行，相当于将两个文件合并
df = pd.concat([df1,df2])
df.index = [0,1,2,3,4,5,6,7,8,9]
df3 =df.copy()
df

#插入列
df.insert(3,'顶的人数',[11,12,13,14,15,16,17,18,19,20])
df

df = df3

#直接增加一列在最后面
df['顶的人数'] = [11,12,13,14,15,16,17,18,19,20]
df

#section 2 行列互换
df.T

df = df3
df4=df['观看次数'].apply(lambda x:x+1)
df4

#applymap()就是针对整张表apply，但是如果有其他类型数据，比如时间，python就不知道怎么处理了，会报错。