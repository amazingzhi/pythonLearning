# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:03:15 2020

@author: amazi
"""

from datetime import datetime

#获取现在的时间
datetime.now()

datetime.now().year
datetime.now().month
datetime.now().day

#返回今天是周几，周一是0，周日是6
datetime.now().weekday()

#返回今天是一年中的第几周
datetime.now().isocalendar()#三个数，年，第多少周，星期几

#指定日期和时间的格式
datetime.now().date()#年月日

datetime.now().time()#时分秒毫秒

#显示自定义格式
#显示成xxxx-xx-xx xx:xx:xx 这样的格式
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#字符串和时间格式互相转换
now = datetime.now()
str(now)

#将字符串解析为时间
from dateutil.parser import parse
str_now = '2020-08-08'
time_now = parse(str_now)
time_now

#时间索引
import pandas as pd
df = pd.read_excel(r"C:/Users/amazi/python project 1/NBA data/2012-18_teamBoxScore_xlsx.xlsx")

type(df['gmDate'])
df['gmDate'] = pd.to_datetime(df['gmDate'])
df['gmDate']

# =============================================================================
# type(df['gmDate'])
# df[df['gmDate']==datetime(2012,10,30)]#注意不要写07要写7
# =============================================================================

#选择一段时间的数据
df[(df['gmDate']>=datetime(2012,10,30))&(df['gmDate']<=datetime(2013,4,17))]

#时间运算
# =============================================================================
# delta = datetime(2020,5,21,21,59,30) - datetime(2013,5,22,23,48,12)
# delta
# =============================================================================











