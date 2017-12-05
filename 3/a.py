from pymining import itemmining
transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=2)
print(report)
print(len(report))


dataFile = open('dataFolder/data3.txt', 'r') 

dataF = dataFile.readlines()

dataFile.close()

dataSetToAct = []

dataSetToActAsSet = []

dataSetToActAsSetForDetection = []	

ka = 0

theta = 0
epsilon = 0
d = []

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

		tupleA = sorted(setJ) 
		tupleA = tuple(tupleA)
		d.append(tupleA)

minSupport = len(dataSetToAct)*theta

relim_input = itemmining.get_relim_input(d)
report = itemmining.relim(relim_input, min_support=minSupport)




print(report)
print(len(report))

