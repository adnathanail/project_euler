from datetime import datetime
tally = 0
for i in range(1901,2001):
	for j in range(1,12+1):
		if datetime(i,j,1).weekday() == 6:
			tally += 1

print(tally)
