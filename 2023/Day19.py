import re

data = open('/input/Day19.txt', 'r').read()

workflows=data.split("\n\n")[0].split("\n")
workflows=[re.findall("[^{|}|,]+",i) for i in workflows]

ratings=data.split("\n\n")[1].split("\n")
ratings=[re.findall("\d+",i) for i in ratings]

def sent(send,rating):
  while send!="A" and send!="R":
    for w in range(len(workflows)):
      workflow=workflows[w]
      if workflow[0]==send:

        for r in range(len(workflow[1:len(workflow)-1])):
          rule=workflow[1:len(workflow)-1][r]
          cat, digit, send =re.findall(">|<|\w+",rule)[0] , int(re.findall(">|<|\w+",rule)[2]) , re.findall(">|<|\w+",rule)[3]
          symbol=True
          if cat=="x":
            symbol=int(rating[0])<digit if rule[1]=="<" else int(rating[0])>digit
          elif cat=="m":
            symbol=int(rating[1])<digit if rule[1]=="<" else int(rating[1])>digit

          elif cat=="a":
            symbol=int(rating[2])<digit if rule[1]=="<" else int(rating[2])>digit
      
          elif cat=="s":
            symbol=int(rating[3])<digit if rule[1]=="<" else int(rating[3])>digit
        
          if symbol:
            break
            send=send
          else:
            send=workflow[len(workflow)-1]
    send=send
  return send
  
#================== part 1 ==================#
accepted=[]
for rt in range(len(ratings)):
  rating=ratings[rt] # [x=0, m=1, a=2, s=3]
  send="in" 
  send=sent(send,rating)
  if send=="A":
    accepted.append(sum([int(i)for i in rating]))
print("Part 1 : ratings'sum of accepted parts",sum(accepted))
