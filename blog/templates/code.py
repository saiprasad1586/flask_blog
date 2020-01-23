import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('M:\MACHINE__LEARNING\winequality-red.csv')
x = data.iloc[:, :-1].values
y = data.iloc[:, 11].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

ply_reg = PolynomialFeatures(degree=2)
x_poly = ply_reg.fit_transform(x)
x_testing = ply_reg.fit_transform(x_test)

lin = LinearRegression()
lin.fit(x_poly, y)
