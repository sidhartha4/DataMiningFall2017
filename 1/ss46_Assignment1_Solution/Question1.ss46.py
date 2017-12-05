from collections import Counter
from itertools import groupby

def data():
	dataFile = open("data/data.online.scores.txt","r")	

	dataList = dataFile.readlines()

	maxMidsemScore = -1
	minMidsemScore = 100000000

	j = 0

	midsemScoreArray = []
	totalSum = 0

	for i in dataList:
		words = i.split()
		midsemScore = int(words[1])
		midsemScoreArray.append(midsemScore)
		totalSum = totalSum + midsemScore 
		if maxMidsemScore < midsemScore:
			maxMidsemScore = midsemScore

		if minMidsemScore > midsemScore:
			minMidsemScore = midsemScore

		#print(midsemScore)
		#print(i)

	midsemScoreArray.sort()

	#print(maxMidsemScore)
	#print(minMidsemScore)


	print()
	q1 = len(midsemScoreArray)/4
	q1 = int(q1)
	q1 = q1 - 1
	medianFirst =  len(midsemScoreArray)/2
	medianFirst = int(medianFirst)
	medianSecond = medianFirst + 1  
	q3 =  3*len(midsemScoreArray)/4
	q3 = int(q3)
	q3 = q3 - 1


	print("Q1. Part 1")
	print("Max Score:" + str(midsemScoreArray[len(midsemScoreArray)-1]))
	print("Min Score:" + str(midsemScoreArray[0]))

	print("Q1. Part 2")
	print("Q1 Score:" + str(midsemScoreArray[q1]))
	print("Median Score:" + str(float(midsemScoreArray[medianFirst] + midsemScoreArray[medianSecond])/2))
	print("Q3 Score:" + str(midsemScoreArray[q3]))
	
	print("Q1. Part 3")
	mean = float(totalSum)/len(midsemScoreArray)
	totalElements = len(midsemScoreArray)

	mean = round(mean, 3)
	print("Mean Score:" + str(mean))
	#dataList = Counter(midsemScoreArray)
	#print(dataList.most_common())   # Returns all unique items and their counts
	#print(dataList.most_common(1))  # Returns the highest occurring item
	print("Q1. Part 4")

	freqs = groupby(Counter(midsemScoreArray).most_common(), lambda x:x[1])
	# pick off the first group (highest frequency)
	print("Mode Score:" + str([val for val,count in freqs.next()[1]]))

	print("Q1. Part 5")
	varSum = 0
	#varSum2 = 0
	for i in midsemScoreArray:
		varSum = varSum + ((i-mean)*(i-mean))
	#	varSum2 = varSum2 + (i*i)
	#varSum2 = float(varSum2)/float(totalElements)
	#varSum2 = varSum2 - (mean*mean)

	eVariance = float(varSum)/float(totalElements-1)
	
	eVariance = round(eVariance, 3)
	print("Emperical Variance:" + str(eVariance))
	#print("Emperical Variance:" + str(varSum2))
	dataFile.close()

if __name__ == "__main__":
	data()