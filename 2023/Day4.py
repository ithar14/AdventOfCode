import re

data = open('/input/Day4.txt', 'r').read().split('\n')

cards=[]
points=0
for card in data: 
  sets=re.split(r':|\|', card)
  ind=int(re.search(r'\d+', sets[0]).group())
  winning_num=re.findall(r"\d+",sets[1])
  numbers=re.findall(r"\d+",sets[2])

  
  point=0
  pts=0
  matches=0
  for i in numbers:
    for j in winning_num:  
      x=point
      if i==j:
        x+=1
        point=2*x-1
        pts=x

        matches+=1
  
  points+=pts
  
  cards.append([tuple([ind,matches, pts])])

c=cards.copy()
for i in range(len(cards)-1):
  
  for j in range(len(cards[i+1])):
    print(j)
    for matchs in range(cards[i][j][1]) :
      print(cards[i][j],cards[matchs+cards[i][j][0]][j])
      c[i+1].append(cards[matchs+cards[i][j][0]][j])
  cards=c.copy()
  print("\n")
cards
