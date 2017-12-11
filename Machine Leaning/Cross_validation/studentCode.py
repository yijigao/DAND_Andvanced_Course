from sklearn.model_selection import cross_validate,train_test_split
from sklearn.svm import SVC
from sklearn import datasets


iris = datasets.load_iris()
features = iris.data
labels = iris.target

# set the random_state to 0 and the test_size to 0.4 so
# we can exactly check your result

features_train, features_test, labels_train, labels_test = train_test_split(features, labels,
                                                                            test_size=0.4, random_state=0)
# classifier
clf = SVC(kernel="linear", C=1)
clf.fit(features_train, labels_train)

print(clf.score(features_test, labels_test))
