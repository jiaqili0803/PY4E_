import numpy as np

print ("Hello world")

a = np.arange(24)
print(a.ndim)             # a 现只有一个维度
# 现在调整其大小 
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
def new_func(b):
    print(b.ndim)

new_var = new_func(b)
new_var 

    """[summary]
    """     
