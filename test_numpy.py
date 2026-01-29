import numpy as np

# 创建两个 2x2 的矩阵
a = np.array([[1, 2], 
              [3, 4]])

b = np.array([[5, 6], 
              [7, 8]])

# 矩阵相乘
result = np.dot(a, b)

print("我的第一个矩阵运算结果：")
print(result)