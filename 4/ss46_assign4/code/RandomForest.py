import sys
import random
#Decision Tree Portion Started

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
			exampleToAdd = dict()

			for k in featVal:
				r = k.split(":")
				exampleToAdd[int(r[0])] = int(r[1])

			#print(exampleToAdd)	
			X_example.append(exampleToAdd)

	print(len(X_example))	
	print(len(Y_example))	
	return X_example, Y_example


def GiniIndex(Y_example):

	p = 1.
	keyVal = dict()
	for i in Y_example:
		#print(i)
		if i in keyVal:
			keyVal[i] += 1
		else: 
			keyVal[i] = 1

	total = len(Y_example)
	for i in keyVal.keys():		
		p = p - (float(keyVal[i])/total)**2

	return p

def GiniIndexWrapper(X_train, Y_train):

	Partition = {}

	totalY = len(Y_train)

	for i,j in zip(X_train, Y_train):
	
		randBet = random.randint(1,len(i))
		randVal = random.sample(i.keys(), randBet)

		for k in randVal:
			if k in Partition:
		
				if i[k] in Partition[k]:			
					Partition[k][i[k]]["X_train"].append(i)
					Partition[k][i[k]]["Y_train"].append(j)
		
				else:
					Partition[k][i[k]] = {"X_train":[i], "Y_train":[j]}
					

			else:
				Partition[k] = {i[k]: {"X_train":[i], "Y_train":[j]}}

	figureOutFeature = None
	GiniMin = 1.1

	for i in Partition.keys():
		
		GiniVal = 0.0
		for j in Partition[i].keys():
			GiniVal += len(Partition[i][j]["Y_train"])*GiniIndex(Partition[i][j]["Y_train"])/totalY
						
		
		if GiniMin > GiniVal:
			GiniMin =  GiniVal
			figureOutFeature = i

	return figureOutFeature, Partition[figureOutFeature], GiniMin

def removekey(d, key):

    r = dict(d)
    del r[key]
    return r



def trainDecisionTree(X_train, Y_train, max_depth=5):


	GiniOld = GiniIndex(Y_train)
	figureOutFeature, Partition, GiniMin = GiniIndexWrapper(X_train, Y_train)

	if GiniOld == GiniMin or max_depth == 0 or len(X_train) == 1 or len(X_train[0]) == 1 :

		keyVal = dict()
		for i in Y_train:
			if i in keyVal:
				keyVal[i] += 1
			else:
				keyVal[i] = 1

		answer = None
		maxVal = -1
		#print(keyVal)
		for i in keyVal.keys():		
			if keyVal[i] > maxVal:
				maxVal = keyVal[i]
				answer = i

		return {"feature": "Final", "answer":answer}

	Tree = {"feature": figureOutFeature, "child":{}}
	

	#print("-------------------------a--------------------------")
	#print(figureOutFeature)

	#print("-------------------------b---------------------------")
	#print(Partition.keys())
	for i in Partition.keys():
		
		X = []
		Y = []
		
		for p,q in zip(Partition[i]["X_train"],Partition[i]["Y_train"]):
			Y.append(q)
			#print(p)
			p1 = removekey(p, figureOutFeature)
			#print(p1)
			X.append(p1)



		ChildTree = trainDecisionTree(X, Y, max_depth-1)	
		Tree["child"][i] = ChildTree


	#print("-------------------------c--------------------------")

	return Tree



def findClass(Tree,X):
	if  Tree["feature"] == 'Final':
		#print("--------------------------------Final------------------------")
		return Tree["answer"]

	#print(Tree["feature"])
	#print("yo")

	if X[Tree["feature"]] in Tree["child"]: 
		return findClass(Tree["child"][X[Tree["feature"]]], X) 
	else:

		randVal = random.sample(Tree["child"].keys(), 1)
		return findClass(Tree["child"][randVal[0]], X)

#Decision Tree Portion Ended


def findClassRandomForest(Tree,X):

	val = dict()

	for i in range(0,len(Tree)):
		
		j = findClass(Tree[i],X)
		if j in val:
			val[j] += 1
		else:
			val[j] = 1

	answer = None
	maxVal = -1
	#print(keyVal)
	for i in val.keys():		
		if val[i] > maxVal:
			maxVal = val[i]
			answer = i

	return answer

def trainRandomForest(X_train, Y_train, max_depth=5, num_of_trees =10):

	Tree = []
	
	for i in range(0,max_depth):
		Tree.append(trainDecisionTree(X_train, Y_train, max_depth))

	return Tree
	

def testRandomForest(Tree, X_test, Y_test):

	correct = 0
	total = 0
	
	for i,j in zip(X_test, Y_test):
		retVal = findClassRandomForest(Tree, i)
		total += 1
		if int(retVal) == int(j):
			correct += 1

	acc = float(correct)/total

	return acc


def main():

	trainFile = sys.argv[1]
	testFile = sys.argv[2]

	if "balance.scale" in trainFile:
		max_depth = 3
		num_of_trees = 100

	elif "led" in trainFile:
		max_depth = 7
		num_of_trees = 100
	
	elif "nursery" in trainFile:
		max_depth = 7
		num_of_trees = 100
	
	elif "synthetic.social" in trainFile:
		max_depth = 7	
		num_of_trees = 100
	
	X_train, Y_train = parseFiles(trainFile)
	X_test, Y_test = parseFiles(testFile)

	Tree = trainRandomForest(X_train, Y_train, max_depth, num_of_trees)
	
	acc = testRandomForest(Tree, X_train, Y_train)
	print("-----------Training Accuracy-----------------")
	print(acc)


	acc = testRandomForest(Tree, X_test, Y_test)
	print("-----------Testing Accuracy----------------")
	print(acc)

	#print(GiniIndex(Y_train))




if __name__ == '__main__':
	
	main()