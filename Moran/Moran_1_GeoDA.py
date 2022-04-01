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
df = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result.xlsx",
                   sheet_name= 'Moran1')
# print(df)
labels = df.columns.tolist()[1:]
print(labels)
nAttr = len(labels)
print(nAttr)

# 设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
print(angles)

# 按行读取
index = 1
data = []
#绘图
fig = plt.figure()
#设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
#添加每个特质的标签
ax.set_thetagrids(angles*180/np.pi,labels)
#设置极轴范围
ax.set_ylim(0.1,0.8)
angles = np.concatenate((angles, [angles[0]]))
print(angles)
print(len(angles))
data1 = []

# 按行获取数据
for index, row in df.iterrows():
    # print(np.array(row[1:6]))
    data = np.array(row[1:6])
    # data.append(np.array(row[1:6]))

    # 使雷达图封闭起来
    values = np.concatenate((data, [data[0]]))
    print(len(values))
    data1.append(values)
    print(data1)
    # ax.plot(angles, values, 'bo-', color='r', linewidth=1, label = '1985')
    # ax.fill(angles, values, facecolor='g', alpha=0.25)
    # plt.thetagrids(angles * 180 / np.pi, labels)
    # print(type(row))
#绘制折线图
# ax.plot(angles, data1[0], 'bo-', color='#2AAB7B', linewidth=1, label = '1985')
# ax.plot(angles, data1[1], 'bo-', color='#3B329F', linewidth=1, label = '1990')
# ax.plot(angles, data1[2], 'bo-', color='#BD3B30', linewidth=1, label = '1995')
# ax.plot(angles, data1[3], 'bo-', color='#c24f44', linewidth=1, label = '2001')
# ax.plot(angles, data1[4], 'bo-', color='#BBB62D', linewidth=1, label = '2005')
# ax.plot(angles, data1[5], 'bo-', color='#CA4A93', linewidth=1, label = '2010')
# ax.plot(angles, data1[6], 'bo-', color='#2C7EA9', linewidth=1, label = '2015')
# ax.plot(angles, data1[7], 'bo-', color='#36BEC6', linewidth=1, label = '2020')
# 用循环画图
# colour = ['#2AAB7B','#3B329F','#BD3B30','#c24f44','#BBB62D','#CA4A93','#2C7EA9','#36BEC6']
colour = ['#05450a', '#78d203', '#dcd159', '#fbff13', '#b6ff05', '#a5a5a5', '#ff6d4c', '#1c0dff']
for i in range(1,8,2):

    ax.plot(angles, data1[i], 'bo-', color=colour[i], linewidth=1, label=df['Year'][i])

plt.tight_layout()  #自动调整子图参数,使之填充整个图像区域。
plt.legend(loc="lower right", title="Moran\'I", fancybox=False, ncol=1, shadow=True, bbox_to_anchor=(1.25, -0.05))
# plt.text(1,-1,'1985_2020')
# plt.title('1985_2020')
jpgfile = 'Moran_GeoDA2' + '.jpg'
print(jpgfile)
plt.savefig(jpgfile, dpi=600)
plt.show()