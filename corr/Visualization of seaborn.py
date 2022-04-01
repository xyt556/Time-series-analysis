# -*- codeing =utf-8 -*-
# @Time : 2022/3/28$ 13:46
# Author : YantaoXI
# @File : Visualization of seaborn.py
# @Software: PyCharm
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('./sample_2020.csv')
print(tips.head())
print(tips.corr())
# print(tips.corr().type())
# sns.pairplot(tips, kind='reg')
# sns.pairplot(tips ,hue ='RESI', markers=["o", "s"])
corr = np.array(tips.corr())
# corr[0:1,1:] = numpy.nan
# mask掉右上角
for i in range(5):
    corr[i,i+1:] = numpy.nan
print(corr)
sns.heatmap(corr, annot = True, xticklabels=['NDVI','WET','NDBSI','LST','RSEI'], yticklabels=['NDVI','WET','NDBSI','LST','RSEI'],)
# 全部
# sns.heatmap(tips.corr(), annot = True)
# sns.clustermap(tips.corr())
# sns.distplot(tips['RESI'])
# sns.jointplot(x = 'NDVI', y = 'RESI', data = tips)
plt.savefig('heatmap.jpg', dpi=600)
plt.show()

sns.pairplot(tips, kind='reg')
plt.savefig('pairplot.jpg', dpi=600)
plt.show()

# sns.jointplot(x = 'NDVI', y = 'RESI', data = tips)
# plt.show()