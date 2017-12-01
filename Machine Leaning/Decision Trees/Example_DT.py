from sklearn import tree
import math

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)

print(clf.predict([[2., 2.]]))
print(-(2/3) * math.log((2/3), 2) - (1/3) * math.log((1/3), 2))

a = 0.9081223000003
def round_this():
	return {"acc": round(a,4)}
print(round_this())