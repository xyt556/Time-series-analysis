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
df1985_2001 = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result1.xlsx",
                   sheet_name= '1985_2001')
print(df1985_2001)
labels = np.array(df1985_2001['Class_name']).tolist() # 也可以不tolist
# labels = ['1985-2001','2001-2020','1985-2020']
print(labels)
data1985_2001 = np.array(df1985_2001['Area2'])#.tolist()
print(data1985_2001)
df2001_2020 = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result1.xlsx",
                   sheet_name= '2001_2020')
data2001_2020 = np.array(df2001_2020['Area2'])#.tolist()
df1985_2020 = pd.read_excel(r"D:\Pan_CUMT\CloudSpace\personal_space\study\RESI\PCA_result1.xlsx",
                   sheet_name= '1985_2020')
data1985_2020 = np.array(df1985_2020['Area2'])#.tolist()
x = np.arange(len(labels))
print(x)
width = 0.3  # the width of the bars

# fig, ax = plt.subplots()
plt.bar(x - width, data1985_2001, width, label='1985-2001')
plt.bar(x , data2001_2020, width, label='2001-2020',tick_label = labels)
plt.bar(x + width, data1985_2020, width, label='1985-2020')

# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Area(square km)', )
plt.xlabel('Transition')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x, labels)
plt.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
# plt.figure(figsize=(40, 6.5))
plt.tight_layout()  #自动调整子图参数,使之填充整个图像区域。
# plt.legend(loc="lower right", title="Answer", fancybox=False, ncol=1, shadow=True)
# plt.text(1,-1,'1985_2020')
# plt.title('1985_2020')
jpgfile = 'bar1' + '.jpg'
print(jpgfile)
plt.savefig(jpgfile, dpi=600)
plt.show()