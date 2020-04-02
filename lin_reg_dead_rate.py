# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:13:10 2020

@author: MonOrdiPro
"""

import numpy as np
from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# données %evolution mort

y = np.array([50,37,16,20,36,27,26,22,17,15,12,16,16,14])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

x = x.reshape(-1,1)
y = y.reshape(-1,1)

plt.scatter(x,y)

print(x.shape)
print(y.shape)


# Creation de la matrice X
X = np.hstack((x,np.ones(x.shape)))
print(X.shape)

theta = np.random.randn(2,1)


def model (X, theta):
    return X.dot(theta)


def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

def grad(X, y, theta) :
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) -y)

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    for i in range (0, n_iterations) :
        theta = theta - learning_rate * grad(X, y, theta)
    return theta


theta_final = gradient_descent(X, y, theta, learning_rate=.02, n_iterations=10000) 

plt.scatter(x,y)
plt.xlim(0,23)
plt.ylim(0,55)
plt.quiver(19,4,2,-5)
plt.annotate(
    "x_intercept = 19.33", xy=(16, 6))
plt.title('linear regression from rate dead evolution')
plt.plot(x, model(X,theta_final), c='r')
plt.savefig("lin_reg_dead_rate.png")
# y = -1.96 * x + 37.88
# x = 37.88 / 1.96
# x = 19.33

# plateau dans 4 jours