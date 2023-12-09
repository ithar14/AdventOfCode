import re
import numpy as np

data = open('/input/Day6.txt', 'r').read().split('\n')

#================== part 1 ==================#

def wins():
  winnings=[]
  for j in range(len(time)):
      win=0
      for i in range(int(time[j])+1):
        dis=(int(time[j])-i)*i
        if dis>int(distance[j]):
          win+=1
      winnings.append(win)
  return winnings

print("Part 1 : ",np.product(wins()))

#================== part 2 ==================#

time=[int("".join(time))]
distance=[int("".join(distance))]

print("Part 2 : ",np.product(wins()))
