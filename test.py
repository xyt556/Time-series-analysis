# -*- codeing =utf-8 -*-
# @Time : 2022/4/1$ 18:20
# Author : YantaoXI
# @File : test.py
# @Software: PyCharm
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_trendline(x, y, n):
    mpl.pylab.plot(x, y, 'ko')
    parameter = np.polyfit(x, y, n)  # n=1为一次函数，返回函数参数
    f = np.poly1d(parameter)  # 拼接方程
    # mpl.pylab.plot(x, f(x), "r--")
    mpl.pyplot((x, f(x), "r--"))
    plt.show()
df = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result.xlsx", sheet_name= 'Average')
print(df)
# print(np.array(df['Year']))
x = np.array(df['Year'])
print(x)
y1 = np.array(df['RSEI'])
print(y1)
y2 = np.array(df['NDVI'])
y3 = np.array(df['WET'])
y4 = np.array(df['NDBSI'])
y5 = np.array(df['LST'])
plt.scatter(x,y1)
plt.plot(x,y1, label = 'RSEI')
plt.scatter(x,y2)
plt.plot(x,y2, label = 'NDVI')
plt.scatter(x,y3)
plt.plot(x,y3, label = 'WET')
plt.scatter(x,y4)
plt.plot(x,y4, label = 'NDBSI')
plt.scatter(x,y5)
plt.plot(x,y5, label = 'LST')
plt.legend()
plt.show()
n = 1
# plot_trendline(x1,y1,n)
# x1=[20,33,51,79,101,121,132,145,162,182,203,219,232,243,256,270,287,310,325]
#
# y1=[49,48,48,48,48,87,106,123,155,191,233,261,278,284,297,307,341,319,341]
#
# x2=[31,52,73,92,101,112,126,140,153,175,186,196,215,230,240,270,288,300]
#
# y2=[48,48,48,48,49,89,162,237,302,378,443,472,522,597,628,661,690,702]
#
# x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
#
# y3=[48,48,48,48,66,173,351,472,586,712,804,899,994,1094,1198,1360,1458,1578,1734,1797,1892]

# p1=np.poly1d(np.polyfit(x1[:],y1[:],1))

# p2=np.poly1d(np.polyfit(x2[5:],y2[5:],1))

# p3=np.poly1d(np.polyfit(x3[5:],y3[5:],1))

# x=np.arange(1985,2020)

# l1=plt.plot(x1,p1(x),'r--',label='532nm')

# l2=plt.plot(x,p2(x),'g--',label='offKDP')
#
# l3=plt.plot(x,p3(x),'b--',label='offNd:VYO4')

# plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')

# plt.title('The Lasers in Three Conditions')
#
# plt.xlabel('I/mA')
#
# plt.ylabel('Power/uW')
#
# plt.legend()
#
# plt.show()