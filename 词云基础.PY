filename = "yes-minister.txt"
with open(filename,'r', encoding='UTF-8') as f:
    mytext = f.read()

# print(mytext)

# 呼唤(import)词云包，利用 mytext 中存储的文本内容来制造词云
from wordcloud import WordCloud
wordcloud = WordCloud().generate(mytext)

# %pylab inline
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
