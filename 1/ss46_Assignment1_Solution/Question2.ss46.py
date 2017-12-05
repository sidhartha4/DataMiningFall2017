
def data():
	dataFile = open("data/data.online.scores.txt","r")	

	dataList = dataFile.readlines()

	midsemScoreArray = []
	totalSum = 0
	totalSumEndsem = 0
	endsemScoreArray = []
	for i in dataList:
		words = i.split()
		midsemScore = int(words[1])
		endsemScore = int(words[2])

		midsemScoreArray.append(midsemScore)
		endsemScoreArray.append(endsemScore)
		totalSum = totalSum + midsemScore 
		totalSumEndsem = totalSumEndsem + endsemScore


	print("Q2. Part 1")

	mean = float(totalSum)/len(midsemScoreArray)
	totalElements = len(midsemScoreArray)

	varSum = 0
	varSumAfter = 0

	for i in midsemScoreArray:
		varSum = varSum + ((i-mean)**(2))
		

	eVarianceBefore = float(varSum)/float(totalElements-1)
	
	stDeviation = eVarianceBefore**(0.5)

	for i in midsemScoreArray:
		varSumAfter = varSumAfter + (((i-mean)/stDeviation)**(2))


	eVarianceAfter = float(varSumAfter)/float(totalElements-1)

	eVarianceBefore = round(eVarianceBefore, 3)
	eVarianceAfter = round(eVarianceAfter, 3)
	print("Emperical Variance Before:" + str(eVarianceBefore))
	print("Emperical Variance After:" + str(eVarianceAfter))
	#print("Emperical Variance:" + str(varSum2))

	print("Q2. Part 2")
	
	zScore = float(90-mean)/float(stDeviation)

	zScore = round(zScore, 3)
	print("Original score:90 then z-score:" + str(zScore))

	print("Q2. Part 3")

	meanEndsem = float(totalSumEndsem)/len(endsemScoreArray)
	totalElementsEndsem = len(endsemScoreArray)

	varSumEndsem = 0

	for i in endsemScoreArray:
		varSumEndsem = varSumEndsem + ((i- meanEndsem)**(2))


	eVarianceEndsem = float(varSumEndsem)/float(totalElementsEndsem-1)

	stDeviationEndsem = eVarianceEndsem**(0.5)

	pearsonValTotal = 0
	pearsonValTotal2 = 0

#	print(totalElements)
#	print(totalElementsEndsem)
	
	for i,j in zip(midsemScoreArray, endsemScoreArray):
		pearsonValTotal = pearsonValTotal + ((i- mean)*(j- meanEndsem))		
		pearsonValTotal2 = pearsonValTotal2 + i*j

	pearsonValTotal2 = pearsonValTotal2 - (totalElements*mean*meanEndsem)	
	
	pearsonVal = float(pearsonValTotal)/float((totalElements-1)*stDeviation* stDeviationEndsem)	

	pearsonVal2 = float(pearsonValTotal2)/ float((totalElements-1)*stDeviation* stDeviationEndsem)

	pearsonVal = round(pearsonVal, 3)
	print("Pearson's coefficient between midterm scores and final scores is:" + str(pearsonVal))

	print("Q2. Part 4")

	coVarianceVal = float(pearsonValTotal)/float(totalElements-1)

	coVarianceVal = round(coVarianceVal, 3)
	print("Covariance between midterm scores and final scores is:" + str(coVarianceVal))


	dataFile.close()

if __name__ == "__main__":
	data()