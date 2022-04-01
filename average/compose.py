# -*- codeing =utf-8 -*-
# @Time : 2022/3/23$ 20:17
# Author : YantaoXI
# @File : compose.py
# @Software: PyCharm
import PIL.Image as Image
import os

IMAGES_PATH = './'  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式

IMAGE_ROW = 1  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 2  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SIZE_w = 3840  # 每张小图片的大小,单个图像的横向像素数
IMAGE_SIZE_h = 2880  # 每张小图片的大小,单个图像的纵向像素数
IMAGE_SAVE_PATH = r'.\average1_2.jpg'  # 图片转换后的地址

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
print(image_names)
# 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")


# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE_w, IMAGE_ROW * IMAGE_SIZE_h))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE_w, IMAGE_SIZE_h), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE_w, (y - 1) * IMAGE_SIZE_h))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


image_compose()  # 调用函数