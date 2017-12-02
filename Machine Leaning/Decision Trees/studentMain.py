import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify
from sklearn import tree
from sklearn.metrics import accuracy_score


features_train, labels_train, features_test, labels_test = makeTerrainData()

# the classify() function in classifyDT is where the magic happens!
# clf_min_sample_split_2 = tree.DecisionTreeClassifier(min_samples_split=2)
#clf_min_sample_split_50 = tree.DecisionTreeClassifier(min_samples_split=50)

#clf_min_sample_split_2.fit(features_train, labels_train)
#clf_min_sample_split_50.fit(features_train, labels_train)


#acc_min_samples_split_2 = accuracy_score(clf_min_sample_split_2.predict(features_test), labels_test)
#acc_min_samples_split_50 = accuracy_score(clf_min_sample_split_50.predict(features_test), labels_test)
clf = classify(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print("acc 1: ", round(acc, 3))
def submitAccuracies():
	return "acc" , acc
print(submitAccuracies())
print("acc 2: ", round(acc, 3))
# grader code, do not modify below this line
# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())

#print("acc_min_samples_split_2:", round(acc_min_samples_split_2, 3))
#print("acc_min_samples_split_50:", round(acc_min_samples_split_50, 3))


