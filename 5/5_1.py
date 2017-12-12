import numpy as np
import pickle
import time
import json

def getKNNOutput(x, trainX, trainY, k):

    dist = []
    for i in trainX:
        dist.append((np.sum(((x-i)**2)))**0.5)
        #dist.append(np.sum(abs(x-i)))

    dist = np.array(dist)
    idx = dist.argsort()[:k]
    val = {}
    val[-1] = 0
    val[1] = 0

    for i in idx:
        val[int(trainY[i])] += 1

    if val[-1] > val[1]:
    	return -1

    return 1


def test(k, trainX, trainY, testX, testY):

    print(trainX.shape)
    print(trainY.shape)
    
    total = 0
    correct = 0

    for x,y in zip(testX,testY):
        total += 1
        classified = getKNNOutput(x, trainX, trainY, k)
        if int(classified) == int(y):
            correct += 1

    acc = float(correct)/total
    print("test accuracy:" + str(acc))

    return acc


if __name__ == "__main__":
    
	X_train = [[1,0.5], [2,1.2], [2.5,2], [3,2], [1.5,2], [2.3,3], [1.2,1.9], [0.8,1]]
	Y_train = [1,1,1,1,-1,-1,-1,-1]

	X_test = [[2.7,2.7], [2.5,1], [1.5,2.5], [1.2,1]]
	Y_test = [1,1,-1,-1]

	X_train = np.array(X_train)
	Y_train = np.array(Y_train)
	X_test = np.array(X_test)
	Y_test = np.array(Y_test)
	acc = test(3, X_train, Y_train, X_test, Y_test)
    

