from sklearn.linear_model import LogisticRegression

# Minimal training data
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
model = LogisticRegression().fit(X, y)
print(model.predict([[1]]))