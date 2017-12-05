
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
			for jNum in range(0, len(freqSetList)):

					lengthMatch1 = set(freqSetList[iNum]).union(set(freqSetList[jNum]))

					if len(lengthMatch1) == sizeFreqSet:

						tupleA = sorted(lengthMatch1) 
						tupleA = tuple(tupleA)

						if tupleA in candidatesGeneratedDict:
							candidatesGeneratedDict[tupleA] += 1
						else: 
							candidatesGeneratedDict[tupleA] = 1
						
						if candidatesGeneratedDict[tupleA] >= ((sizeFreqSet)*(sizeFreqSet-1)):
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
	prevFreqSetGen = set()

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
				prevFreqSetGen.add(tupleA)
	
	flag = len(set(b))
	prevfreqSetD = 0
	i = 1	
	while prevfreqSetD != len(freqSet):

		prevfreqSetD = len(freqSet)

		c = set()
		c.clear()

		dictFor = dict() 

		for iterGen in prevFreqSetGen:

			setA = set()
			for iA in iterGen:
				setA.add(iA)
			
			for iterGen2 in prevFreqSetGen:

				setB = set()
				for jA in iterGen2:
					setB.add(jA)

				setC = setA.union(setB)
				if len(setC) == i+1:


					tupleA = sorted(setC) 
					tupleA = tuple(tupleA)
					

					if tupleA in dictFor:
						dictFor[tupleA] = dictFor[tupleA] + 1
					else: 
						dictFor[tupleA] = 1
							
					if dictFor[tupleA] >= ((i+1)*(i)):

						c.add(tupleA)



		#c = set(itertools.combinations(b, i+1))

		newFreqSetGen = set()
		newFreqSetGen.clear()

		for row in spam:
			d = set(row)
			if len(d) >= i+1:

				for setPossible in c:
					#setA = setPossible
					setA = set()
					for iA in setPossible:
						setA.add(iA)

					lenSet = len(setA.intersection(d))
					if lenSet == len(setA):

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
							newFreqSetGen.add(tupleA)

		prevFreqSetGen = newFreqSetGen
		i = i+1
						
	#print(len(freqSet))
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


	valL = 0

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
			#print(j)

			dataSetToAct.append(j)
			setJ = set(j)

			dataSetToActAsSetForDetection.append(setJ)
			dataSetToActAsSet.append(setJ)
			

	minSupport = len(dataSetToAct)*theta

	freqSet = mineFrePat2(dataSetToAct, minSupport)

	#freqSet = mineFrePat(dataSetToAct, minSupport)
	print("Total number of frequent Itemsets: "+ str(len(freqSet)))

	freqSetVersion = []

	for i in freqSet:
		#print(i)
		freqSetVersion.append(set(i))


	aHere = dict()
	outlierResilient = set()

	for i in range(0,len(dataSetToAct)):
		for j in range(0,len(freqSetVersion)):

			lengthMatch = len(freqSetVersion[j].intersection(dataSetToActAsSetForDetection[i]))

			if lengthMatch == len(freqSetVersion[j]):

				epsilonLength = len(dataSetToAct[i])+1
				
				maxNumOutlier = float(lengthMatch)*epsilon

				sequenceIn = dataSetToAct[i]

				setToCheck = dict()

				outlierNum = 0

				startk = 0

				for endk in range(0,len(sequenceIn)):

					if sequenceIn[endk] in freqSetVersion[j]:
						
						if sequenceIn[endk] in setToCheck:
							setToCheck[sequenceIn[endk]] = setToCheck[sequenceIn[endk]] + 1
						else:
							setToCheck[sequenceIn[endk]] = 1

						if lengthMatch == len(setToCheck):
							if outlierNum <= epsilonLength:
								epsilonLength = outlierNum
							
							while startk < len(sequenceIn):
								#print(startk)
								if sequenceIn[startk] in setToCheck:
									setToCheck[sequenceIn[startk]] = setToCheck[sequenceIn[startk]] - 1
									if setToCheck[sequenceIn[startk]] == 0:
										del setToCheck[sequenceIn[startk]]
								elif sequenceIn[startk] not in freqSetVersion[j]:
									outlierNum = outlierNum - 1
								else:
									startk = startk + 1
									break

								startk = startk + 1

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

	#print(outlierResilient)
	print("Total number of outlier resilient frequent Itemsets: "+ str(len(outlierResilient)))

	f = open('output.txt', 'w')

	for i in outlierResilient:
		#print(i)
		strToPrint = ""
		for j in range(0,len(i)):
			f.write(str(i[j]))
			strToPrint = strToPrint + str(i[j])
			if j < len(i) - 1:
				f.write(', ')
				strToPrint = strToPrint + ", "

		print(strToPrint)
			
		f.write('\n')	
	f.close()	

if __name__ == "__main__":
	
	data()



