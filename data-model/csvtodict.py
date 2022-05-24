import csv

file = "income.csv"
final = dict()

head = ["Jan-2021", "Feb-2021", "Mar-2021", "Apr-2021", "May-2021", "Jun-2021", "Jul-2021", "Aug-2021", "Sep-2021", "Total", "Notes to Developers"]

for i in range(len(head)):
	with open(file, 'r') as data:
		next(data)
		a = dict()
		for row in csv.reader(data):
			a[row[0].strip()]=row[i+1].strip()
	final[head[i]]=a

print(final)
