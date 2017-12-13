import sys
from Naive_bayes.class_vis import prettyPicture, output_image
from Naive_bayes.prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

# import my training data
features_train, labels_train, features_test, labels_test = makeTerrainData()

names = ["Naive Bayes", "Linear SVM", "Decision Tree", "Nearest Neighbor", "Random Forest", "AdaBoost"]

classifiers = [GaussianNB(),
               SVC(kernel="linear"),
               DecisionTreeClassifier(min_samples_split=50),
               KNeighborsClassifier(n_neighbors=1),
               RandomForestClassifier(n_estimators=2),
               AdaBoostClassifier(n_estimators=25)]

for name, clf in zip(names, classifiers):
    clf.fit(features_train, labels_train)
    score = clf.score(features_test, labels_test)
    print(f"{name}", score)
    prettyPicture(name, clf, features_test, labels_test)
    output_image(f'{name}.png', "png", open(f"{name}.png", "rb").read())
