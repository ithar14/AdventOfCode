import re
import numpy as np

data = open('/input/Day2.txt', 'r').read().split('\n')

sum_1=0 
sum_2=0

for game in data:
  RGB=[] # colors in each set

  num_red=0
  num_green=0
  num_blue=0

  sets=re.split(r'Game \s*|: \s*|\s*;\s*', game)[1:] # split based on sets ";"
  game_ind=int(sets[0]) # game index
  sets=sets[1:] 

  for clr_set in sets:
    # find the number of each color
    num_red=re.search(r'[\s\S]\d(?= red)|\d(?= red)',clr_set)
    num_green=re.search(r'[\s\S]\d(?= green)|\d(?= green)',clr_set)
    num_blue=re.search(r'[\s\S]\d(?= blue)|\d(?= blue)',clr_set)
    if num_red :
      num_red=int(num_red.group())
    else:
      num_red=0
    if num_green :
      num_green=int(num_green.group())
    else:
      num_green=0
    if num_blue :
      num_blue=int(num_blue.group())
    else:
      num_blue=0

    RGB.append([num_red,num_green,num_blue])
    
#================== part 1 ==================#
  if ((np.array(RGB)/np.array([12,13,14]))<=1).all():
    sum_1+=game_ind
    
#================== part 2 ==================#
  sum_2+=np.prod(np.array([max(s) for s in np.array(RGB).T]))

print("the sum of the IDs of games if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes is :", sum_1)
print("the sum of the power of the minimum set of cubes is :",sum_2)
