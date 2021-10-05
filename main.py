import csv
import math

with open ("data.csv", newline="") as f :
  read = csv.reader(f)
  filelist = list(read)

total = 0
totalnum = len(filelist)

for individual in filelist :
  total += float(individual[0])

mean = total/totalnum
print("The mean is", str(mean))

squarenumber = []
for i in filelist :
  a = int(i)-mean
  a = a**2
  squarenumber.append(a)

sum = 0
for i in squarenumber :
  sum += i

squareroot = sum/totalnum
result = math.sqrt(squareroot)
print("The standard deviation is", str(result))