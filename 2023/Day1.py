data = open('../input/Day1.txt', 'r').read().split('\n')

#================== part 1 ==================#
calnums=[]
for line in data:
  calnum=""
  for i in range(len(line)):
    for num in range(10):
      if line[i]==str(num):
        calnum+=line[i]
  calnums.append(calnum)
print("Part 1 : the sum of all of the calibration values is",sum([int(calnums[i][0]+calnums[i][len(calnums[i])-1]) for i in range(len(calnums))]))

#================== part 2 ==================#
import re

numbers = {
  "one"   : 1,
  "two"   : 2, 
  "three" : 3,
  "four"  : 4,
  "five"  : 5,
  "six"   : 6, 
  "seven" : 7,
  "eight" : 8,
  "nine"  : 9
}
calnums=[]
for line in data:
  calnum=[]
  ind_lett=[] # the index of numbers in letter form
  ind_num=[] # the index of numbers
  cal_lett=[] # the numbers of the letter form 
  cal_num=[]  #the numbers
  for i in range(len(numbers)):
    for j in re.finditer(list(numbers.keys())[i], line):
      ind_lett.append(j.start())
      cal_lett.append(list(numbers.values())[i])
    for j in re.finditer(str(list(numbers.values())[i]), line):
      ind_num.append(j.start())
      cal_num.append(list(numbers.values())[i])
  ind=ind_lett+ind_num
  calnum=cal_lett+cal_num
  calnums.append([str(x) for y, x in sorted(zip(ind,calnum))])
print("Part 2 : the sum of all of the calibration values is",sum([int(calnums[i][0]+calnums[i][len(calnums[i])-1]) for i in range(len(calnums))]))
