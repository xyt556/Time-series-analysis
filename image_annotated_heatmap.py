import numpy as np
import matplotlib
import matplotlib.pyplot as plt

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]     
#蔬菜类
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
#农民类

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
#定义热力图数据

fig, ax = plt.subplots()  
#将元组分解为fig和ax两个变量 
im = ax.imshow(harvest)   
#显示图片


ax.set_xticks(np.arange(len(farmers)))    
#设置x轴刻度间隔
ax.set_yticks(np.arange(len(vegetables)))    
#设置y轴刻度间隔
ax.set_xticklabels(farmers)        
#设置x轴标签'''
ax.set_yticklabels(vegetables)     
#设置y轴标签'''

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
#设置标签 旋转45度 ha有三个选择：right,center,left（对齐方式）


for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")
'''
画图
j,i:表示坐标值上的值
harvest[i, j]表示内容
ha有三个选择：right,center,left（对齐方式）
va有四个选择：'top', 'bottom', 'center', 'baseline'（对齐方式）
color:设置颜色
'''

ax.set_title("Harvest of local farmers (in tons/year)")      
#设置题目
fig.tight_layout()  #自动调整子图参数,使之填充整个图像区域。
plt.show()      #图像展示