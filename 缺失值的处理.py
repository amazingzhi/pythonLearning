# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import datetime
#导入数据
df = pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\lesson5.xlsx')
#查找缺失值
df.info()

df.isnull()
#缺失值删除
df1 = df
df.dropna()#删除存在空值的行

df = df1
df.dropna(how = 'all')#只删除全部为空值的行

#缺失值填充
df = df1
df.fillna(0)#将空值填充为0

#也可以根据不同的列填充不同的值
df = df1
dateTime_p = datetime.datetime.strptime('2020/7/20 00:00:00',r'%Y/%m/%d %H:%M:%S')
df.fillna({'顶踩比例':0,'发布时间':dateTime_p})#用字典方式填充

#重复值处理
#对重复值做删除处理
df = pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\lesson5.xlsx', sheet_name = 'Sheet2')
df1 = df

#用drop_duplicates(), 用keep设置保留第几个，默认第一个，first，last，false（表明都删除）
df.drop_duplicates(subset = '名称', keep = 'last')

#也可以传入多个列名，只要有一个不一样就不删除。
df.drop_duplicates(subset = ['名称', '观看次数'])


















