# 三国演义中文文本人物出场次数统计

import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","主公","军士",\
            "左右","军马","引兵","次日","大喜","天下","东吴","于是","今日","不敢","魏兵","陛下",\
            "一人","都督","人马","不知","汉中","只见","众将","后主","蜀兵","上马","大叫","太守",\
            "此人","夫人","先主","后人","背后","城中","天子","一面","何不","大军","忽报","先生",\
            "百姓","何故","然后","先锋","不如","赶来"}
txt = open("scripts_2.2_附件.txt", "r", encoding = "utf8").read()
words = jieba.cut(txt)     #分词处理，形成所有中文单词的列表
counts = {}                     #构造字典
for word in words:          #逐一遍历中文单词
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
    #在字典内进行计数
for word in excludes:
    del counts[word]
items = list(counts.items())    #字典转换为列表类型
items.sort(key = lambda x:x[1], reverse = True)
#按需求在列表内排序
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
