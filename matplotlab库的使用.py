# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:40:38 2020

@author: amazi
"""

import matplotlib.pyplot as plt

plt.plot([3,1,4,2,5])#如果plot函数后面加的是一维数组，则它自动变成y值，而x的值就是这些数的索引。
plt.ylabel('grade')
plt.savefig('test',dpi=600)#savefig函数前面的参数是文件名，后面的参数dpi是图片质量，意思是一英寸内有多少个点，保存图片形式为png
plt.show()

plt.plot([0,2,4,6,8],[3,1,4,5,2])#当输入两个列表是，默认第一列为x的值，第二列是y的值
plt.ylabel('grade')
plt.axis([-1,10,0,6])#axis函数的作用是确定坐标系的大小。-1和10是x轴最小值和最大值；0和6是y轴最小最大值。
plt.show()


#在一个区域中绘制多个坐标系
import numpy as np

def f(t):#f(t)为能量衰减函数
    return np.exp(-t)*np.cos(2*np.pi*t)

a = np.arange(0.0,5.0,0.02)

plt.subplot(211)#这里的意思是建立一个2行1列的图像，选择第一行第一列的图像区域呈现下面的函数。
plt.plot(a,f(a))

plt.subplot(212)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()