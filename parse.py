#git shortlog --no-merges -s -a >> out.txt
from __future__ import division
import matplotlib.pyplot as plt
import datetime
inp = open("out.txt")
loopcount = 0
data = 0
numbers = []
userdata = []
while True:
	loopcount += 1
	line = inp.readline()
	if not line:
		break
	if loopcount%2 == 0:
		for a in line.split(":"):
			for b in a.split(" "):
				if "\n" in b or b.isdigit():
					if "\n" in b:
						data = int(b[0:len(b)-1])
					else:
						data = int(b)
					numbers.append(data)
a = 0
precent = []
users = []
while True:
	a += 3
	if a != len(numbers)+3:
		userdata.append(numbers[(a-3):a])
	else:
		break
sum = 0
for a in userdata:
	a[1] = a[1]-a[2]
	sum += a[1]
	del a[2]
for a in userdata:
	precent.append(float(a[1]/sum)*100)

x = open("user.txt")
out = open("log.txt" ,"a")
outstr = str(datetime.datetime.now())
loopcount = -1
while True:
	loopcount += 1
	line = x.readline()
	if not line:
		break
	else:
		print line+"	"+str(precent[loopcount])
		users.append(line[0:len(line)-1])
		outstr += "--"+line[0:len(line)-1]+"--"+str(precent[loopcount])
		print users
print out.write(outstr)


