import pandas as pd
from pandas import Series,DataFrame
import numpy as np

#
# s1 = pd.Series(range(10, 21), index = range(11))
# s2 = pd.Series(range(20, 25), index = range(2,7))
# print(s1)
# print(s2)
#
# print(s1 + s2)


df1 = pd.DataFrame(np.ones((2,2)), columns = ['a', 'b'])
df2 = pd.DataFrame(np.ones((3,3)), columns = ['a', 'b', 'c'])
print(df1)
print("*"*50)
print(df2)
print("="*50)
print(df1 + df2)

# 遇到NaN 需要处理 1. 删除掉  10000条   30条
# 2. 补值-》列的平均值 。 最大 ，最小。次数最多的，策略