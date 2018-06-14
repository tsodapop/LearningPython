import numpy as np

def p(x):
	print(x)

list_1 = np.array([1,2,3])
list_2 = np.array([2,3,4])
# print(list_1,list_2)
# print(type(list_1 * list_2))

a = np.arange(15).reshape(3,5)
# print(a)
# print(type(a))

p(np.zeros([3,4]))