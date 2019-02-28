# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:26:16 2018

@author: Administrator
"""

import jieba as jb
from scipy.misc import imread
import wordcloud as wc
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]
f = open("F:/数据分析/111.txt")
bg_img = imread("F:/数据分析/12345.jpg")
A=f.read()
B=WordCloud(font_path="simhei.ttf",background_color="WHITE",width=2000,height=2000,
            max_font_size=300,mask=bg_img).generate(A)
image_colors = ImageColorGenerator(bg_img)
B.recolor(color_func=image_colors)
print(B)
fig=plt.subplots(figsize=(20,12))
plt.imshow(B)
plt.title("证监会主席")
plt.axis("off")
plt.show()
