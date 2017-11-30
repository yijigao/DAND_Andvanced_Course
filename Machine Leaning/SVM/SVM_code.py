import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## SVM ########################
from sklearn.svm import SVC
clf = SVC(kernel = "linear")

### fit the classifier using training features/labels
clf.fit(features_train, labels_train)

### predict
pred = clf.predict(features_test)

### Score your prediction
#print(clf.score(features_test,labels_test))
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print(acc)