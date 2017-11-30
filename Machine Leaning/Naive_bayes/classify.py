def NBAccuracy(features_tran, labels_train, features_test, labels_test):
	from sklearn.naive_bayes import GaussianNB
	from sklearn.svm import SVC

	# Create classifier
	clf = GaussianNB()
	#clf = SVC(C=2.0, kernel="linear")
	# fit the classifier on training features and labels
	clf.fit(features_tran, labels_train)
	# use the trained classifier to predict labels for test features
	pred = clf.predict(features_test)

	# calculate and return the accuracy on the test data
	# this is slightly different than example
	# where we just print the accuracy
	# you might need to import an sklearn module
	accuracy = clf.score(features_test,labels_test)
	return accuracy
