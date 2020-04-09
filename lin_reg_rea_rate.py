# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:20:01 2020

@author: MonOrdiPro
"""


import numpy as np
from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# données %evolution mort

y = np.array([29,29,12,15,24,20,17,14,12,12,8,10,8,8, 6])
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
plt.xlim(0,20)
plt.ylim(0,50)
plt.quiver(18.27,4,2,-5)
plt.annotate(
    "x_intercept = 18.27", xy=(16, 6))
plt.title('linear regression from rate reanimation evolution')
plt.plot(x, model(X,theta_final), c='r')
plt.savefig("lin_reg_rea_rate.png")

# a = -1.446 / -1.4461
# b = 26.41758 / 26.4176

# y = -1.446 * x + 26.418
# x = 26.418 / 1.446
# x = 18.27

# plateau dans 3 jours

y = np.array([29,29,12,15,24,20,17,14,12,12,8,10,8,8])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

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
print('Lerreur quadratique moyenne est {}'.format(rmse)) # 3.978908285698083 /*
print('le score R2 est {}'.format(r2)) # 0.6821983424195633 /
print('\n')
