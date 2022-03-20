# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:12:22 2020

@author: amazi
"""

import pandas as pd

filePath = r'C:\Users\amazi\OneDrive\Desktop\15. excel and csv导出.xlsx'
df1 = pd.read_excel(filePath,sheet_name='Sheet1')
df2 = pd.read_excel(filePath,sheet_name='Sheet2')

df3 = pd.concat([df1,df2],ignore_index = True)
df3

#section1 导出为xlsx文件
#pip install xlsxwriter
resultPath = r'C:\Users\amazi\OneDrive\Desktop\result.xlsx'

#最简单的
#na_rep,设置缺失值; inf_rep, 设置无穷值;index = False, 不加结果提供的index
df3.to_excel(resultPath,sheet_name = '汇总', index = False,na_rep=0,inf_rep=0)

#导入多张excelsheet
writer = pd.ExcelWriter(resultPath,engine='xlsxwriter')
df3.to_excel(writer,sheet_name = '班级汇总有索引')
df3.to_excel(writer,sheet_name = '班级汇总无索引', index = False)
df3.to_excel(writer,sheet_name = '只导出姓名和成绩', index = False,columns = ['姓名','成绩'])
writer.save()

#section 2 导出为csv文件
#没有sheet_name和inf_rep
resultCSVPath = r'C:\Users\amazi\OneDrive\Desktop\result.csv'
df3.to_csv(resultCSVPath,index = False,na_rep = 0)