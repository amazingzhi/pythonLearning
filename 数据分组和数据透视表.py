# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:54:12 2020

@author: amazi
"""

import pandas as pd
df = pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\python practice datasets\用户销量.xlsx')
df

#section 1 数据分组
#groupby（列名）

df.groupby('客户分类')

df.groupby('客户分类').count()
df.groupby('客户分类').sum()#对于不能加的列就不会显示

#对多列进行分组
df.groupby(['客户分类','区域']).count()#相当于对于第一列做了第二列的细分
df.groupby(['客户分类','区域']).sum()

#统计ABC客户分别有多少
df.groupby('客户分类')['用户ID'].count()

#aggregate函数
#一次性输出多个函数的结果
df.groupby('客户分类').aggregate(['count','sum'])
#对于不同列施加不同命令
df.groupby('客户分类').aggregate({'用户ID':'count','7月销量':'sum','8月销量':'sum'})

#对分组之后的数据重置索引，转换成标准的DataFrame类型
df.groupby('客户分类').sum().reset_index()

#section 2 数据透视表
#pivot_table(data,values=None,index=None,columns=None,aggfunc='mean',
#fill_value = None, margins = False, dropna = True,margin_name='All')
# data:整张表
# value：透视表数据
# index：行索引
# columns：列索引
# aggfunc： 聚合函数
# fill_value:对空值进行填充
# margins： 是否显示合计列
# dropna: 是否删除缺值，如果为True，删除
#margins_name:合计列的列名

#统计各个区域的各种客户类型7月销量
pd.pivot_table(df,values='7月销量',index='客户分类',columns='区域',aggfunc='count')
#增加合计列
pd.pivot_table(df,values='7月销量',index='客户分类',columns='区域',aggfunc='count',margins= True)
#重命名合计列为总和
pd.pivot_table(df,values='7月销量',index='客户分类',columns='区域',aggfunc='count',margins= True, margins_name='总和')
#将缺失值设置为0
pd.pivot_table(df,values='7月销量',index='客户分类',columns='区域',aggfunc='count',margins= True, margins_name='总和',fill_value=0)
#有多种value
pd.pivot_table(df,values=['7月销量','8月销量','9月销量'],index='客户分类',columns='区域',aggfunc='count',margins= True, margins_name='总和',fill_value=0)



















