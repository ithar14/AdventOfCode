import re
import numpy as np

data = open('/input/Day8.txt', 'r').read().split('\n')

directions=re.findall("R|L",data[0])
networks=np.array([re.findall(r"[A-Z]+\w",data[i]) for i in range(2,len(data))]).T
start= networks[0][list(np.array(networks)[0]).index("AAA")]

i=0
while start!="ZZZ" :
  for direc in directions:
    if direc=="R" and start in networks[0]:
      start=networks[2][list(np.array(networks)[0]).index(start)]
      #print(start)
      i+=1
    if direc=="L" and start in networks[0]:
      start=networks[1][list(np.array(networks)[0]).index(start)]
      #print(start)
      i+=1
  
print(i)
