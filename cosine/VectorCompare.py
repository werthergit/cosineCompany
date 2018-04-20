import math


class VectorCompare(object):
    def __init__(self, str):
        print("-----")

    # 计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量之间的 cos 值
    def relation(self, concord1, concord2):
        # relevance = 0
        topvalue = 0
        for word, count in concord1.items():
            if concord2.get(word):
                topvalue += count * concord2[word]
        return topvalue / (self.magnitude(concord1) * self.magnitude(concord2))