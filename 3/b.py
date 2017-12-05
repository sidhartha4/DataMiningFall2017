from collections import Counter
from itertools import groupby
import itertools
from pymining import itemmining


def mineFrePat(dataSetToActAsSet, minSupport):

	a = dict()
	b = set()
	c = set()

	totfreqSet = set()
	freqSet = set()

	for setRow in dataSetToActAsSet:	
		for col in setRow:

			tupleA = col 

			if tupleA in a.keys():
				a[tupleA] += 1
			else: 
				a[tupleA] = 1
			
			if a[tupleA] >= minSupport:
				totfreqSet.add(tupleA)
				freqSet.add(tupleA)


	lengthPrevFreqSet = 0			

	sizeFreqSet = 2

	while lengthPrevFreqSet != len(totfreqSet):

		lengthPrevFreqSet = len(totfreqSet)

		candidatesGenerated = set()
		candidatesGenerated.clear()

		candidatesGeneratedDict = dict()
		candidatesGeneratedDict.clear()

		freqSetList = list(freqSet)

		for iNum in range(0, len(freqSetList)):
			for jNum in range(iNum+1, len(freqSetList)):

					lengthMatch1 = set(freqSetList[iNum]).union(set(freqSetList[jNum]))

					if len(lengthMatch1) == sizeFreqSet:

						tupleA = sorted(lengthMatch1) 
						tupleA = tuple(tupleA)

						if tupleA in candidatesGeneratedDict.keys():
							candidatesGeneratedDict[tupleA] += 1
						else: 
							candidatesGeneratedDict[tupleA] = 1
						
						if candidatesGeneratedDict[tupleA] >= float(sizeFreqSet)*(sizeFreqSet-1)/2:
							candidatesGenerated.add(tupleA)
		
		#print(candidatesGeneratedDict)
		#print(candidatesGenerated)	


		freqSetAdd = set()
		freqSetAdd.clear()

		for setRow in dataSetToActAsSet:
			for j in candidatesGenerated:
				lengthMatch = len(set(j).intersection(setRow))
				if lengthMatch == len(j):

					tupleA = sorted(j) 
					tupleA = tuple(tupleA)

					if tupleA in a.keys():
						a[tupleA] += 1
					else: 
						a[tupleA] = 1
					
					if a[tupleA] >= minSupport:
						freqSetAdd.add(tupleA)



		for i in freqSetAdd:
			totfreqSet.add(i)

		freqSet = freqSetAdd

		sizeFreqSet = sizeFreqSet + 1

	return totfreqSet

def mineFrePat2(spam, minSupport):

	a = dict()
	b = set()
	c = set()
	freqSet = set()
	threeLength = set()

	for row in spam:	
		for col in row:

			setA = set()
			setA.add(col)
			tupleA = sorted(setA) 
			tupleA = tuple(tupleA)
			b.add(col)
			if tupleA in a:
			#print(tupleA)
				a[tupleA] += 1
			else: 
				a[tupleA] = 1
			
			if a[tupleA] >= minSupport:
				freqSet.add(tupleA)

	
	flag = len(set(b))

		
	for i in range(1,flag):
		c = set(itertools.combinations(b, i+1))

		for row in spam:
			d = set(row)
			if len(row) >= i+1:
				e = set(itertools.combinations(d, i+1))
				f = c.intersection(e)
				for fa in f:
					setA = set()
					for iA in fa:
						setA.add(iA)

					tupleA = sorted(setA) 
					tupleA = tuple(tupleA)
					#print(tupleA)
					if tupleA in a:
						#print(tupleA)
						a[tupleA] += 1
					else: 
						a[tupleA] = 1

					if a[tupleA] >= minSupport:

						freqSet.add(tupleA)



	print(len(freqSet))
	return freqSet

def data():

	dataFile = open('dataFolder/data3.txt', 'r') 
	
	dataF = dataFile.readlines()

	dataFile.close()

	dataSetToAct = []

	dataSetToActAsSet = []

	dataSetToActAsSetForDetection = []	

	ka = 0

	theta = 0
	epsilon = 0

	for i in dataF:

		ja = "".join(i.split())
		
		ja = ja.split(',')
		#j =i.split()
		#print(j)

		if ka == 0:
			ka = 1
			theta = float(ja[0])
			epsilon = float(ja[1])

		else:

			j = []
			for jaa in ja:
				j.append(int(jaa))
			print(j)

			dataSetToAct.append(j)
			setJ = set(j)

			dataSetToActAsSetForDetection.append(setJ)
			dataSetToActAsSet.append(setJ)
			
	#print("theta:" + str(theta))
	#print("epsilon:" + str(epsilon))

	minSupport = len(dataSetToAct)*theta
	#minSupport = 20
	print(minSupport)
	#freqSet =  mineFrePat(dataSetToActAsSet, minSupport)
	freqSet = mineFrePat2(dataSetToAct, minSupport)


	relim_input = itemmining.get_relim_input(dataSetToAct)
	report = itemmining.relim(relim_input, min_support=minSupport)




	#print("--------------------------------------------------------------")
	#print(freqSet)
	#print(len(freqSet))

	freqSetVersion = []

	for i in freqSet:
		#print(i)
		freqSetVersion.append(set(i))

		

	for i in report:
		j = set(i)
		#print(type(j))
		flag = 0
		for k in freqSetVersion:
			if k == j:
				flag = 1
				break
				
		if flag == 0:
			print(j)

	print(report)
	print(len(report))



	aHere = dict()
	outlierResilient = set()

	for i in range(0,len(dataSetToAct)):
		for j in range(0,len(freqSetVersion)):

			lengthMatch = len(freqSetVersion[j].intersection(dataSetToActAsSetForDetection[i]))

			if lengthMatch == len(freqSetVersion[j]):

				epsilonLength = len(dataSetToAct[i])+1
				
				maxNumOutlier = float(lengthMatch)*epsilon

				sequenceIn = dataSetToAct[i]

				for startk in range(0,len(sequenceIn)):

					setToCheck = set()
					setToCheck.clear()
					outlierNum = 0

					for endk in range(startk,len(sequenceIn)):

						if sequenceIn[endk] in freqSetVersion[j]:
							setToCheck.add(sequenceIn[endk])
							if lengthMatch == len(setToCheck):
								if outlierNum <= epsilonLength:
									epsilonLength = outlierNum
								break							
						else:
							outlierNum = outlierNum + 1

					if float(epsilonLength) <= maxNumOutlier:
						break


				if float(epsilonLength) <= maxNumOutlier:
					
					tupleA = sorted(freqSetVersion[j]) 
					tupleA = tuple(tupleA)


					if tupleA in aHere.keys():
						aHere[tupleA] += 1
					else: 
						aHere[tupleA] = 1
					
					if aHere[tupleA] >= minSupport:
						outlierResilient.add(tupleA)

	print(outlierResilient)
	print(len(outlierResilient))

	f = open('output.txt', 'w')

	for i in outlierResilient:
		#print(i)
		for j in range(0,len(i)):
			f.write(str(i[j]))
			if j < len(i) - 1:
				f.write(', ')	
		f.write('\n')	
	f.close()	

if __name__ == "__main__":
	
	data()



