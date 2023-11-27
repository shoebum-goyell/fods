import numpy as np

def func_without_kernel(x,y):
    fx = []
    fy = []
    for i in range(n):
        for j in range(n):
            fx.append(x[i]*x[j])
            fy.append(y[i]*y[j])
    res = np.dot(fx, fy)
    print(res)



def func_with_kernel(x,y):
    res = np.dot(x,y)
    print(res**2)

n = int(input(""))
x = []
y = []
x = input("").split(" ")
y = input("").split(" ")
for i in range(n):
    x[i] = int(x[i])
    y[i] = int(y[i])
func_without_kernel(x, y)
func_with_kernel(x, y)


