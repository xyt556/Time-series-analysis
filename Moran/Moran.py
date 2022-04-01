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
                   sheet_name= 'Moran')
print(df)
labels = np.array(df['Year']).tolist() # 也可以不tolist
# labels = ['1985-2001','2001-2020','1985-2020']
print(labels)
#
fig, ax = plt.subplots()
ax.plot(df['Year'], df['RSEI'],label= 'RSEI', color = '#009000')
ax.plot(df['Year'], df['NDVI'],label= 'RSEI', color = '#8BF359')
ax.plot(df['Year'], df['WET'],label= 'WET', color = '#0013E2')
ax.plot(df['Year'], df['NDBSI'],label= 'NDBSI', color = '#E2F369')
ax.plot(df['Year'], df['LST'],label= 'LST', color = '#E23636')

# rects1 = ax.bar(x - width, data1985_2001, width, label='1985-2001')
# rects2 = ax.bar(x , data2001_2020, width, label='2001-2020',tick_label = labels)
# rects3 = ax.bar(x + width, data1985_2020, width, label='1985-2020')
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Moran\'I')
ax.set_xlabel('Year')
# # ax.set_title('Scores by group and gender')
# # ax.set_xticks(x, labels)
plt.legend(loc = 'lower left')
# # 以下代码决定是否显示数值
# ax.bar_label(rects1, padding=1, fmt= '%1.1f', label_type= 'edge')
# ax.bar_label(rects2, padding=1, fmt= '%1.1f', label_type= 'edge')
# ax.bar_label(rects3, padding=1, fmt= '%1.1f', label_type= 'edge')
# # plt.figure(figsize=(40, 6.5))
fig.tight_layout()  #自动调整子图参数,使之填充整个图像区域。
# plt.legend(loc="lower right", title="Answer", fancybox=False, ncol=1, shadow=True)
# plt.text(1,-1,'1985_2020')
# plt.title('1985_2020')
jpgfile = 'Moran' + '.jpg'
print(jpgfile)
plt.savefig(jpgfile, dpi=600)
plt.show()