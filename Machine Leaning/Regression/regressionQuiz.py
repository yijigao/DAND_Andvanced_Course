import numpy
import matplotlib.pyplot as plt

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(ages_train, net_worths_train)

# get My net worth (I'm 25)
# sklearn predictions are returned in an array, so you'll want to index into
# the output to get what you want, e.g. net_worth = predict([[25]])[0][0]
My_net_worth = reg.predict(25)[0][0]
print("My_net_worth: ", My_net_worth)

# get the slope
slope = reg.coef_[0][0]
print("Slope: ", slope)

# get the intercept
intercept = reg.intercept_[0]
print("Intercept:", intercept)

# get the score on test data
test_score = reg.score(ages_test, net_worths_test)
print("Test score: ", test_score)

# get the training score
training_score = reg.score(ages_train, net_worths_train)
print("Training score: ", training_score)