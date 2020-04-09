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

y = np.array([50,37,16,20,36,27,26,22,17,15,12,16,16,14,11])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

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

# a =  -1.964 / -1.9
# b =  37.879 / 37.533
# x0 = 19.33 / 19.75

# y = -1.964 * x + 37.879
# x = 37.88 / 1.96
# x = 19.33

# plateau dans 4 jours



y = np.array([50,37,16,20,36,27,26,22,17,15,12,16,16,14,11])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

x = x.reshape(-1,1)
y = y.reshape(-1,1)
lmodellineaire = LinearRegression()
lmodellineaire.fit(x, y)

# Evaluation du training set
y_predict = lmodellineaire.predict(x)
rmse = (np.sqrt(mean_squared_error(y, y_predict)))
r2 = r2_score(y, y_predict)
 
print('La performance du modèle sur la base dapprentissage')
print('--------------------------------------')
print('Lerreur quadratique moyenne est {}'.format(rmse)) # 6.85338521 / 6.853385
print('le score R2 est {}'.format(r2)) # 0.5892732219199377 / 0.5892732219199377
print('\n')