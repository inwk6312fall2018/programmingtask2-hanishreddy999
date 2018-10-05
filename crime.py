
from tabulate import tabulate   #to print the output in table format
def crime_list(a):               #function definition
	file=open(a,"r")   #open csv file in read mode
	c1=dict()
	c2=dict()
	lst1=[]
	lst2=[]
	for line in file:
		line.strip()
		for lines in line.split(','):
			lst1.append(lines[-1])
			lst2.append(lines[-2])
	for b in lst1:
		if b not in c1:
			c1[b]=1
		else:
			c1[b]=c1[b]+1
	for c in lst2:
		if c not in c2:
			c2[c]=1
		else:
			c2[c]=c2[c]+1
	print(tabulate(headers=['CrimeType', 'CrimeId', 'CrimeCount']))
	for k1,v in c1.items():
		for k2,v in c2.items():
		 x=[k1,k2,v]	#tabular format
		print(tabulate(x))
file_name="Crime.csv"
crime_list(file_name)



