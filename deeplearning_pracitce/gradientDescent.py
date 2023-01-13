#%%
import numpy as np
import matplotlib as plt
def function(x1, x2):
    return 0.5*x1**2 + (5/2)*x2**2 - x1*x2 - 2*(x1 + x2)

def gradient(x1, x2):
    return np.array([-2 + x1 - x2, -2 - x1 + 5*x2])
    
x1 = 2
x2= 1
lr = 0.01 # step size
precision = 0.001 #epsilon
original = function(x1,x2)
i = 1

record = [[x1,x2]]

grad = gradient(x1,x2)

while abs(x2-x1) > precision:
    x1 = x1 - lr*grad[0]
    x2 = x2 - lr*grad[1]
    diff = function(x1,x2) - original
    record = np.vstack((record,[x1,x2]))
    original = function(x1,x2)
    grad = gradient(x1,x2)
    i += 1
    
record_x1 = record[:,0]
record_x2 = record[:,0]

x1 = np.linspace(2, 3.5, 150)
x2 = np.linspace(0.25, 1.75, 150)
X1, X2 = np.meshgrid(x1, x2)
Z = function(X1, X2)


fig = plt.figure(figsize = (10,7))
contours = plt.contour(X1, X2, Z, 20)
plt.clabel(contours, inline = True, fontsize = 10)
plt.title("Evolution of the cost function during gradient descent with level circles", fontsize=15)

plt.plot(record_x1, record_x2)
plt.plot(record_x1, record_x2, '*', label = "Cost function")

plt.xlabel('x1', fontsize=11)
plt.ylabel('x2', fontsize=11)
plt.colorbar()
plt.legend(loc = "upper right")
plt.show()
# %%
