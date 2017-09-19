

def question4():
	Q11 = 150
	Q12 = 40
	Q21 = 15
	Q22 = 3300
	total = Q11 + Q12 + Q21 + Q22  
	E11 = float(Q11+Q12)*(Q11+Q21)/total
	E12 = float(Q11+Q12)*(Q12+Q22)/total
	E21 = float(Q11+Q21)*(Q21+Q22)/total
	E22 = float(Q22+Q21)*(Q12+Q22)/total

	chi = (Q11 - E11)**(2)/E11
	chi += (Q12 - E12)**(2)/E12
	chi += (Q21 - E21)**(2)/E21
	chi += (Q22 - E22)**(2)/E22


	chi = round(chi, 3)
	print("chi-value:"+ str(chi))

if __name__ == "__main__":
	question4()