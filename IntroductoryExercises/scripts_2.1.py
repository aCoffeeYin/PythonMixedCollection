# 哈姆雷特英文文本词频统计

def getText():
    txt = open("scripts_2.1_附件.txt", "r").read()        #打开文件
    txt = txt.lower()                                   #全文改为小写
    for ch in '!"#!@$%^&*()_+{}:"|<>?~`-=[]\;,./':
        txt = txt.replace(ch, " ")                      #将特殊符号替换为空格
    return txt          #替换后保存在TXT文本中

hamletTxt = getText()
words = hamletTxt.split()   #用空格分割形成单词列表
counts = {}     #形成空字典，单词及其出现次数形成键值对
for word in words:
    counts[word] = counts.get(word, 0) + 1
    #逐个判断单词是否已在字典中，并相应加1
items = list(counts.items())        #将字典类型转换为列表类型
items.sort(key=lambda x:x[1], reverse=True)
#对一个列表按照键值对的2个元素的第二个元素进行排序
#sort方法：确定哪一个多元选项的列作为排序列
#reverse=True：返回的排序从大到小
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
    #将出现次数最多的前十个单词及其次数打印











