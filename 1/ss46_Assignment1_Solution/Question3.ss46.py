

import math

def question3():
	
	dataFile = open("data/data.libraries.inventories.txt","r")	

	dataList = dataFile.readlines()
	CML = []
	CBL = []
	for i in dataList[1:]:
		j = i.split()
		if j[0] == "CML":
			CML = j[1:]
		else:
			CBL = j[1:]

	print("Q3. Part 1")
	q = float(58)/(122+58);
	q = round(q,3)
	print("jaccard coefficient:" + str(q))

	print("Q3. Part 2")
	manhattan = 0.0
	euclid = 0.0 
	supremum = 0.0

	#print(CML)

	modCML = 0.0
	modCBL = 0.0
	cos = 0.0
	totCML = 0.0
	totCBL = 0.0
	for i in range(0,len(CML)):
		if (supremum < math.fabs(float(CML[i])-float(CBL[i]))):
			supremum = math.fabs(float(CML[i])-float(CBL[i]))

		manhattan += math.fabs(float(CML[i])-float(CBL[i]))
		euclid += (float(CML[i])-float(CBL[i]))**(2)
		cos += (float(CML[i])*float(CBL[i]))

		modCML += (float(CML[i]))**(2)
		modCBL += (float(CBL[i]))**(2)


		totCML += float(CML[i])
		totCBL += float(CBL[i])


	modCML = modCML**(0.5)
	modCBL = modCBL**(0.5)	
	euclid = euclid**(0.5)
	manhattan = round(manhattan,3)
	euclid = round(euclid,3)
	supremum = round(supremum,3)
	print("h=1:"+str(manhattan))
	print("h=2:"+str(euclid))
	print("h=infinity:"+str(supremum))

	print("Q3. Part 3")

	cos = cos/(modCML*modCBL)
	cos = round(cos,3)
	print("cosine similarity:"+ str(cos))

	print("Q3. Part 4")
	p = 0.0

	for i in range(0,len(CML)):
		pCML = float(CML[i])/totCML
		#print(pCML)
		pCBL = float(CBL[i])/totCBL
		#print(pCBL)
		p += (pCML*(math.log(pCML) - math.log(pCBL)))

	p = round(p,3)	
	print("KL Divergence:"+str(p))

if __name__ == "__main__":
	question3()