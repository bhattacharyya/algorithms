#!/usr/bin/python

f1 = open("knapsackfile.txt","r")
lines = f1.readlines()
A = []
for i in lines:
	A.append(i.strip())
total_weight = int(A[0])
parameters = A[1:]

table = [[0 for k in range(total_weight+1)] for n in range(len(parameters) + 1)]
for i in range(1,len(parameters)+1):
	item_name, item_wt, item_val = parameters[i-1].strip().split()
	for w in range(1,total_weight+1):
		if int(item_wt) > w:
			table[i][w] = table[i-1][w]
		else:
			table[i][w] = max(table[i-1][w], table[i-1][w-int(item_wt)] + int(item_val))

sack = []
tot_wt = total_weight
for m in range(len(parameters), 0, -1):
	if table[m][tot_wt] != table[m-1][tot_wt]:
		sack.append(parameters[m-1])
		tot_wt -= int(parameters[m-1].split()[1])


best_weight = best_value = 0
print "\nSelected objects : \n"
for i in sack:
	print i
	best_weight += int(i.split()[1])
	best_value += int(i.strip().split()[2])
		
print "\nTotal weight of selected objects : ", best_weight
print "Total value of selected objects : ", best_value
