# -*- coding: utf-8 -*-
# ----------------------------------
# @Time   : 2019/8/13$ 14:22$
# @Author : 何荣荣
# @Email  ：2667871980@qq.com
# @File   : 基于Pyecharts的词云图$.PY
# Description  :25000条评论的源文件下载链接:
# https://pan.baidu.com/s/1MqN1qNgZKbVEE2lWumt_dg 密码: f57b
# ----------------------------------

# 1.读取文件中的内容，引入pandas库，用pandas库中的read_csv方法读取文件
# ，sep这个参数根据csv文件实际情况进行设置。
# 读取文件成功后，打印选出的前10个
import pandas as pd
df = pd.read_csv("labeledTrainData.csv", sep='\t', escapechar='\\')
# print(df.head(10))

# 2.获得评论列表
# 从上一幅图中可以看出评论在数据类型为DataFrame的df变量的review字段中，
# 通过df['review']取出。df['review']是Series对象，Series对象有tolist方法，
# 返回值的数据类型为列表list。df['review'].tolist()的返回值是每一条评论组成的列表list。
# 导入BeautifulSoup库，去除评论当中的标签。利用了列表推导式，还可以写成for循环形式。
review_list = df['review'].tolist()
from bs4 import BeautifulSoup as bs
comment_list = [bs(k, 'lxml').text for k in review_list]

# 3.去除标点并让所有字母小写
# 首先通过字符串的join方法，让一个列表转化为字符串，
# join方法前面的字符串表示列表中每个元素拼接成为一个字符串时的间隔符
# 第1行代码all_comment = ' '.join(comment_list)就表示以空格为间隔符拼接评论列表。
# 第2-5行是通过正则表达式去除标点符号。
# 第6行是让所有的字母小写。
all_comment = ' '.join(comment_list)
import re
pattern = r'[^\w\s]'
replace = ''
all_comment = re.sub(pattern, replace, all_comment)
all_comment = all_comment.lower()

# 4.词频统计
# 首先引入collection中的Counter方法，Counter方法需要填入1个参数，参数的数据类型为列表。
# Counter方法的返回值数据类型是一个collections.Counter对象，集成了字典dict的一些特性。
from collections import Counter
word_list = all_comment.split(' ')
wordCount_dict = Counter(word_list)
# print(wordCount_dict)

# 5.删除词频统计中的停顿词
# 停顿词文本文件stopwords.txt下载链接:
#  https://pan.baidu.com/s/1ThD7Ay9glzX8Wml9nSmTbA 密码: bfbu
with open("stopwords.txt") as file:
    stopword_list = [k.strip() for k in file.readlines()]
for stopword in stopword_list:
    if stopword in wordCount_dict:
        wordCount_dict.pop(stopword)
wordCount_dict.pop('')

# 6.取出出现次数排名前200的单词
# 用到了sorted方法和lambda匿名函数
choices_number = 200
count_list = sorted(wordCount_dict.items(), key=lambda x:x[1],reverse=True)
count_list = count_list[:choices_number]
keyword_list = [k[0] for k in count_list]
value_list = [k[1] for k in count_list]

# 7.利用pyecharts库绘图
# wordcloud.add需要填入4个参数，第1个参数是标签，可以为空，
# 第2个参数是出现的单词，第3个参数是单词对应的词频，第4个参数是词云上字体大小。
from pyecharts import WordCloud
wordcloud = WordCloud(width=800,height=500)
wordcloud.add('',keyword_list,value_list,word_size_range=[20,100])
wordcloud







