import random
import statistics
from collections import OrderedDict


# 乱数の生成
def generate(N):
    result = []
    for _ in range(N):
        i = random.random()
        if random.random() > 0.5:
            i = -i
        result.append(i)
    return result


# 正規化的な何か
def normalize(N):
    return abs(N)


# サマリー情報的な何かを作成する何か
def get_summary(name, nums):
    d = OrderedDict()
    d["src"] = name
    d["sum"] = sum(nums)
    d["mean"] = statistics.mean(nums)
    d["median"] = statistics.median(nums)
    d["sd"] = statistics.stdev(nums)
    return d
