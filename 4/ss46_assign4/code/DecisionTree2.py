import sys
import random

import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def parseFiles(fileName):
	
	f = open(fileName,"r")
	allLines = f.readlines()
	#print(allLines)
	labelExamples = dict()
	for i in allLines:
		example = i.split(" ", 1)
		#print(example)
		if int(example[0]) in labelExamples:
			labelExamples[int(example[0])].append(example[1])
		else:
			labelExamples[int(example[0])] = [example[1]]


	X_example = []
	Y_example = []

	for i in labelExamples.keys():
		listOfExamples = labelExamples[i]
		#print(listOfExamples)
		
		for j in listOfExamples:
			Y_example.append(i)
			stripAtEnd = j.rstrip()

			featVal = stripAtEnd.split(" ")
			exampleToAdd = []

			for k in featVal:
				r = k.split(":")
				exampleToAdd.append(int(r[1]))

			#print(exampleToAdd)	
			X_example.append(exampleToAdd)

	print(len(X_example))	
	print(len(Y_example))	
	return X_example, Y_example



def main():

	trainFile = sys.argv[1]
	testFile = sys.argv[2]

	X_train, Y_train = parseFiles(trainFile)
	X_test, Y_test = parseFiles(testFile)

	#Tree = trainDecisionTree(X_train, Y_train, max_depth)
	
	if "balance.scale" in trainFile:
		max_depth = 3
	elif "led" in trainFile:
		max_depth = 7
	elif "nursery" in trainFile:
		max_depth = 7
	elif "synthetic.social" in trainFile:
		max_depth = 7	


	clf = DecisionTreeClassifier(max_depth=max_depth)

    # Classifier for each fold

    

	clf.fit(X_train, Y_train)

	predicted = clf.predict(X_test)

	correct = 0
	total = 0
	print(type(predicted))
	Y_test = np.array(Y_test)
	for i,j in zip(predicted,Y_test):
		total += 1
		if int(i) == int(j):
			correct += 1

	print(float(correct)/total)








if __name__ == '__main__':
	
	main()