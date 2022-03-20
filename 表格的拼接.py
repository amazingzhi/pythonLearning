# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:28:50 2020

@author: amazi
"""
#表的横向拼接
#链接表的类型
import pandas as pd
filePath = r"C:\Users\amazi\OneDrive\Desktop\python practice datasets\表格拼接例子.xlsx"
df1 = pd.read_excel(filePath,sheet_name='Sheet1')
df2 = pd.read_excel(filePath,sheet_name='Sheet2')
print(df1)
print(df2)

#一对一拼接，表示两个表中公共列没有重复值
pd.merge(df1,df2)

#多对一，表示两个表的公共列一个有重复值，一个没有
df3 = pd.read_excel(filePath,sheet_name='Sheet3')
df3

pd.merge(df1,df3)

#多对多，表示两个表的公共列都有重复值
df4 = pd.read_excel(filePath,sheet_name='Sheet4')
df4

pd.merge(df3,df4)

#链接键类型
#默认以公共列为键
#用on指定键
df5 = pd.read_excel(filePath,sheet_name='Sheet5')
df5

#多个列为键拼接
pd.merge(df1,df5,on=['姓名','学号'])

#可以分别指定左右链接键
df6 = pd.read_excel(filePath,sheet_name='Sheet6')
df6

pd.merge(df1,df6,left_on='姓名',right_on='名字')#left_on和right_on的意思是以左表和右表作为键

#把索引列作为键
pd.merge(df1,df6,left_index=True,right_index=True)#按照行索引对应合并表格

#连接方式
#当公共列中左表的值无法在右表中完全找到或右表的值无法在左表完全找到
df7 = pd.read_excel(filePath,sheet_name='Sheet7')
df7

#内连接，取交集
pd.merge(df1,df7,how='inner')

#左连接，以左表为主
pd.merge(df1,df7,how='left')

#右链接，以右表为主
pd.merge(df1,df7,how='right')

#外链接，取并集
pd.merge(df1,df7,how='outer')

#section2 表格纵向拼接
df8 = pd.read_excel(filePath,sheet_name='Sheet8')
df9 = pd.read_excel(filePath,sheet_name='Sheet9')
print(df8)
print(df9)

#普通拼接
pd.concat([df8,df9])

#索引设置
pd.concat([df8,df9],ignore_index = True)

#有重复值
df10 = pd.read_excel(filePath,sheet_name='Sheet10')
df10

#存在重复值
pd.concat([df9,df10],ignore_index = True)

#删除重复值
pd.concat([df9,df10],ignore_index = True).drop_duplicates()
























