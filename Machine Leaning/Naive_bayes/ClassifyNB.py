def classify(features_train, labels_train):
	from sklearn.naive_bayes import GaussianNB
	clf = GaussianNB()
	classifier = clf.fit(features_train, labels_train)
	return classifier
### import the sklearn module for GaussianNB
### create classifier
### fit the classifier on the training features and labels
### return the fit classifier
### your code goes here!
