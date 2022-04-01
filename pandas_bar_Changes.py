# -*- codeing =utf-8 -*-
# @Time : 2022/3/24$ 8:47
# Author : YantaoXI
# @File : pie.py
# @Software: PyCharm
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# workpath = r'D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\fig'
df1985_2001 = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result.xlsx",
                   sheet_name= '1985_2001')
print(df1985_2001)
# labels = np.array(df1985_2001['Class_name'])#.tolist() # 也可以不tolist
labels = ['1985-2001','2001-2020','1985-2020']
print(labels)
data1985_2001 = np.array(df1985_2001['Area'])#.tolist()
print(data1985_2001)
df2001_2020 = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result.xlsx",
                   sheet_name= '2001_2020')
data2001_2020 = np.array(df2001_2020['Area'])#.tolist()
df1985_2020 = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result.xlsx",
                   sheet_name= '1985_2020')
data1985_2020 = np.array(df1985_2020['Area'])#.tolist()
x = np.arange(len(labels))
print(x)
df1985_2020.plot.bar(x='Class_name',y='Area')
plt.title('1985_2020')
jpgfile = 'bar' + '.jpg'
print(jpgfile)
plt.savefig(jpgfile, dpi=600)
plt.show()