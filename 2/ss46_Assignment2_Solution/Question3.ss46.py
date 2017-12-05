from collections import Counter
from itertools import groupby
import itertools

import csv

def data():
	a = dict()
	b = set()
	c = set()
	freqSet = set()
	threeLength = set()
	maxPat = set()

	with open('data/Q3data', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

		spam = []
		for row in spamreader:
			spam.append(row)

		for row in spam:	
			for col in row:
				tupleA = col 
				if tupleA in a.keys():
				#print(tupleA)
					a[tupleA] += 1
				else: 
					a[tupleA] = 1
				
				if a[tupleA] == 20:
					freqSet.add(tupleA)
					maxPat.add(tupleA)

		b = set(a)
		
		flag = len(set(a))

		
		for i in range(1,flag):
			c = set(itertools.combinations(b, i+1))
			#print(i)

			for row in spam:
				d = set(row)
				#print(d)
				if len(row) >= i+1:
					e = set(itertools.combinations(d, i+1))
					#print(e)

					f = c.intersection(e)
					#print(f)
					for fa in f:						
						tupleA = fa 
						#print(tupleA)
						if tupleA in a.keys():
							#print(tupleA)
							a[tupleA] += 1
						else: 
							a[tupleA] = 1

						if a[tupleA] == 20:
							if i+1 == 3:
								threeLength.add(tupleA)
							freqSet.add(tupleA)

							checkTupleSet = set(tupleA)
							
							while 1:
								flag = 1
								for mi in maxPat:
									iSet = set(mi)
									if iSet.issubset(checkTupleSet) == True:
										maxPat.remove(mi)
										flag = 0
										break

								if flag == 1:
									break

							maxPat.add(tupleA)

	print("Question 3 Part a. 1 :" + str(len(freqSet)))	
	print("Question 3 Part a. 2 :" + str(len(threeLength)))
	print("Question 3 Part a. 3 :" + str(len(maxPat)))


def data10():
	a = dict()
	b = set()
	c = set()
	freqSet = set()
	threeLength = set()
	maxPat = set()

	with open('data/Q3data', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		#print(spamreader)
		spam = []
		for row in spamreader:
			spam.append(row)

		for row in spam:	
			for col in row:
				tupleA = col 
				if tupleA in a.keys():
				#print(tupleA)
					a[tupleA] += 1
				else: 
					a[tupleA] = 1
				
				if a[tupleA] == 10:
					freqSet.add(tupleA)
					maxPat.add(tupleA)

		b = set(a)
		
		flag = len(set(a))

		
		for i in range(1,flag):
	
			for row in spam:
				d = set(row)

				if len(row) >= i+1:
					e = set(itertools.combinations(d, i+1))

					for fa in e:

						tupleA = sorted(fa) 
						tupleA = tuple(tupleA)
						#print(tupleA)
						if tupleA in a.keys():
							#print(tupleA)
							a[tupleA] += 1
						else: 
							a[tupleA] = 1

						if a[tupleA] == 10:
							if i+1 == 3:
								threeLength.add(tupleA)
							freqSet.add(tupleA)

							checkTupleSet = set(tupleA)
							
							while 1:
								flag = 1
								for mi in maxPat:
									iSet = set(mi)
									if iSet.issubset(checkTupleSet) == True:
										maxPat.remove(mi)
										flag = 0
										break

								if flag == 1:
									break

							maxPat.add(tupleA)
							
	tuple1 = ('A','C','E')
	tuple2 = ('C','E')
	
	val1 = float(a[tuple1])/a[tuple2]

	tuple1 = ('A','B','C','E')
	tuple2 = ('A','B','C')


	val2 = float(a[tuple1])/a[tuple2]

	print("Question 3 Part b. 1 :" + str(len(freqSet)))
	print("Question 3 Part b. 2 :" + str(len(threeLength)))
	print("Question 3 Part b. 3 :" + str(len(maxPat)))
	print("Question 3 Part b. 4 :" + str(round(val1,3)))

	print("Question 3 Part b. 5 :" + str(round(val2,3)))
			

if __name__ == "__main__":
	data()
	data10()