# 政府工作报告词云绘制

import jieba
import wordcloud
f = open("scripts_3_附件.txt", "r", encoding = "utf-8")
t = f.read()        #将文本内容一次性读入变量t
f.close()
ls = jieba.cut(t)       #分词，结果保存在列表
txt = " ".join(ls)
#用空格将每一个元素连接起来，形成一个长字符串
#即为：即将要进行词云展示的字符串文本
w = wordcloud.WordCloud(  font_path = "msyh.ttc", \
                        width = 1000, height = 700, background_color = "white")
w.generate(txt)     #加载文本
w.to_file("grwordcloud.png")        #生成词云文件
