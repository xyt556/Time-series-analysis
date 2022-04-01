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
df = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result.xlsx", sheet_name= 'RSEI')
print(df)

print('---------')
print(list(df))


year = list(df)[1]
print(year)
print('----------')
labels = np.array(df['type'])#.tolist() # 也可以不tolist
print(labels)
data = np.array(df[year])#.tolist()
print(data)
explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# x = [1, 2, 3, 4]
# colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
# 定义颜色
colors = ['#A50026', '#F88E52', '#FFFFBF', '#86CB66', '#006837']
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, colors =colors, labels=labels, autopct='%1.2f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

fig1.tight_layout()  #自动调整子图参数,使之填充整个图像区域。
# plt.legend(loc="lower right", title="Answer", fancybox=False, ncol=1, shadow=True)
plt.text(1,-1,year[:4])
jpgfile = 'pie' + str(year) + '.jpg'
print(jpgfile)
plt.savefig(jpgfile, dpi=600)
plt.show()