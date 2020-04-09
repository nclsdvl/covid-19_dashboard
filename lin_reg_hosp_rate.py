# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:24:07 2020

@author: MonOrdiPro
"""


import numpy as np
from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# données %evolution mort

y = np.array([37,28,12,17,24,17,18,14,13,11,9,8,8,8])
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


theta_final = gradient_descent(X, y, theta, learning_rate=.01, n_iterations=10000) 

plt.scatter(x,y)
plt.xlim(0,20)
plt.ylim(0,50)
plt.quiver(16.5,4,2,-5)
plt.annotate(
    "x_intercept = 17", xy=(16, 6))
plt.title('linear regression from rate hospitalisation evolution')
plt.plot(x, model(X,theta_final), c='r')
plt.savefig("lin_reg_hosp_rate.png")

# a = -1.6923
# b = 28.6923

# y = -1.692 * x + 28.692
# x = 28.692 / 1.692
# x = 17

# plateau dans 2 jours


y = np.array([37,28,12,17,24,17,18,14,13,11,9,8,8,8,6])
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
print('Lerreur quadratique moyenne est {}'.format(rmse)) # 4.617215753967029 / 4.501542945356502
print('le score R2 est {}'.format(r2)) #0.6858299595141699 / 0.7086661341853036
print('\n')