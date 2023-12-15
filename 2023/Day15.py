import re

data = open('/input/Day15.txt', 'r').read()
data=data.split(",")

#================== part 1 ==================#
def hash(string):
  curr_val=0
  for chr in string:
    curr_val+=ord(chr)
    curr_val=(curr_val*17)%256
  return curr_val
  
alg=[]
for seq in data:
  alg.append(hash(seq))
  
print("Part 1 :",sum(alg))

#================== part 2 ==================#
boxes=[ [] for _ in range(256)]

for d in data:
  seq=re.findall("[^\=|\-]+",d)
  box_num=hash(seq[0])
  
  for lens in boxes[box_num]:
    if len(seq)>1:
      if seq[0] in lens[0]:
        boxes[box_num][boxes[box_num].index(lens)]=tuple(seq)  
    else:
      if seq[0] in lens[0]:
        boxes[box_num].remove(lens)
  if len(seq)>1 and tuple(seq) not in boxes[box_num]:
    boxes[box_num].append(tuple(seq))
    
focus_pwr=[]
for i in range(len(boxes)):
  for j in range(len(boxes[i])):
    if boxes[i] is not []:
      focus_pwr.append((i+1)*(j+1)*int(boxes[i][j][1]))
      
print("Part 2 : the focusing power of the resulting lens configuration",sum(focus_pwr))
