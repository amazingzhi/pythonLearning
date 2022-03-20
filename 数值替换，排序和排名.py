# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:57:33 2020

@author: amazi
"""

import pandas as pd
df =pd.read_excel(r'C:\Users\amazi\OneDrive\Desktop\lesson5.xlsx')
df1 = df

#section1 数值替换
#一对一替换
#将顶踩比例替换
#一定要重新赋值
df['顶踩比例'] = df['顶踩比例'].replace(2.000,1.000)#这里不能写百分数，因为在结果中没有百分数.
df

df = df1
#也可以将整个excel2.000 替换成 1.000
df = df.replace(2.000,1.000)
df


#多对一替换
df = df1
#将 480 和 342 的替换成 1314
df = df.replace([480,342],1314)
df

# 多对多替换
df = df1
df = df.replace({480:400,342:300})
df
df = df1

#section 2 数值排序
# 按照观看次数升序排列
#升序排列
df.sort_values(by = ['观看次数'], ascending = True)
#降序排列
df.sort_values(by = ['观看次数'], ascending = False)

#将第二行的发布时间设为none
df.loc[[1],['发布时间']] = None
df

#按照发布时间从晚到早拍，空值拍到最开始。
df.sort_values(by = ['发布时间'], ascending = False, na_position = 'first')

#按照发布时间从早到晚拍，空值拍到最后。
df.sort_values(by = ['发布时间'], na_position = 'last')

#按照多列排序
#按照顶踩比例降序，按照观看次数升序排列（首先按照前面的排列，但是如果前面的一样，则按照后面的排列）
df.sort_values(by = ['顶踩比例','观看次数'], ascending = [False,True])

#section 3 数值排名
#用rank（ascending，method）函数进行排名（就是增加一列写出排名1，2，3...）
#ascending表明是升序还是降序， method有average，first，min，max这四种取值
#按照顶踩比例，降序排列
df['顶踩比例']
#average,这个average的意思是，排名相同时取平均值
df['顶踩比例'].rank(ascending = False,method = 'average')

#first，这个意思是相同以第一个为1
df['顶踩比例'].rank(ascending = False,method = 'first')

#min，这个意思是相同取最小值
df['顶踩比例'].rank(ascending = False,method = 'min')

#max,这个意思是相同取最大值
df['顶踩比例'].rank(ascending = False,method = 'max')





























