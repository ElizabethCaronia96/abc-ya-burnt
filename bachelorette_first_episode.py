from sklearn.linear_model import LogisticRegression
import numpy as np
import csv
#create logistic regression object
model = LogisticRegression(solver='sag')
#1 true 0 false
#hannah b ep 1
chums = np.genfromtxt("becca_ep1.csv", delimiter = ',', skip_header=1, usecols = (1, 2, 3))
# chums = chums.reshape(-1, 1)
winner = np.genfromtxt("becca_winner.csv", delimiter = ',', skip_header=1, usecols = (1))

#train
model.fit(chums, winner)
#score
model.score(chums, winner)

#equation coefficient and intercept
print('Coeff: %d', model.coef_)
print('Intercept: %d', model.intercept_)

#predicted output
new_chums = np.genfromtxt("hannahb_ep1.csv", delimiter = ',', skip_header=1, usecols = (1, 2, 3))
# new_chums = new_chums.reshape(-1, 1)
predicted = model.predict(new_chums)
print (predicted)