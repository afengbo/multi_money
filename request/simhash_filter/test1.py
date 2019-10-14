import re
from simhash import Simhash


def get_features(s):
    width = 3
    s = s.lower()   # 转换成小写
    s = re.sub(r'[^\w]+', '', s)   # 删除空格和非字符(标点符号)
    participle = [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]   # 分词
    # print(participle)
    return participle


# 计算hash值
# print('%x' % Simhash(get_features('How are you? I am fine. Thanks.')).value)
# print('%x' % Simhash(get_features('How are u? I am fine.     Thanks.')).value)
# print('%x' % Simhash(get_features('How r you?I    am fine. Thanks.')).value)

# 计算海明距离
print(Simhash('aa').distance(Simhash('bb')))
print(Simhash('aa').distance(Simhash('aa')))
