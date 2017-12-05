from collections import Counter
from itertools import groupby

def data():
	a = dict()
	b = dict()
	c = dict()
	d = 0
	e = 0
	import csv
	with open('data/Q2data.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		#print(spamreader)
		for row in spamreader:
			tupleA = (row[2],row[3],row[4],row[5]) 
			tupleB = (row[1],row[3],row[4],row[5])
			tupleC = (row[3],row[4],row[5])
			if tupleA in a.keys():
				#print(tupleA)
				a[tupleA] += 1
			else: 
				a[tupleA] = 1
			if tupleB in b.keys():
				#print(tupleA)
				b[tupleB] += 1
			else: 
				b[tupleB] = 1

			if tupleC in c.keys():
				#print(tupleA)
				c[tupleC] += 1
			else: 
				c[tupleC] = 1

			if row[1] == "Illinois" and row[5] == "3" and row[4] == "moderate":
				d = d + 1

			if row[2] == "Chicago" and row[3] == "food":
				e = e + 1
			#print(row)

	print("Question 2 Part 2 :" + str(len(a)))
	#print(a)
	

	print("Question 2 Part 3 :" + str(len(b)))


	print("Question 2 Part 4 :" + str(len(c)))


	print("Question 2 Part 5 :" + str(d))
				

	print("Question 2 Part 6 :" + str(e))
							

if __name__ == "__main__":
	data()