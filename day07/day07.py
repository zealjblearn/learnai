def sqr(num):
    return num*num

sqr(7)
sqr(1024)

# Over 1 score 6; Over 2 score 12; Over 3 score 18

def get_score(over):
    return over * 6

# Over 1 score 8; Over 2 score 14; Over 3 score 20

def get_score(over):
    return over * 6 + 2

score = [6, 12, 18]
score_2d = [[6], [12], [18]]

import numpy as np
print(np)
# over = np.array([[1],[2],[3],[5]])
# # scores = np.array([6, 12, 18, 30])
# # scores = np.array([8, 14, 20, 32])
# scores = np.array([1, 4, 9, 25])

# over = np.array([[1],[2],[3],[4],[5],[10],[50]])
# scores = np.array([1, 4, 9, 16, 25, 100, 2500])

over = np.array([[1],[2],[3],[4],[5]])
scores = np.array([8, 14, 20, 26, 32])

print(over.shape)
print(scores.shape)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
print(LinearRegression)


something = LinearRegression().fit(over, scores)
guess = int(something.predict([[6]])[0])
print(guess)

X_temp = np.array([[200], [250], [300], [350]])
y_time = np.array([20, 15, 10, 7])
pizza_tree = DecisionTreeRegressor().fit(X_temp, y_time)
print(int(pizza_tree.predict([[275]])[0]))