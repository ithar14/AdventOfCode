import re

data = re.split(r'[a-z]*\n\n', open('/input/Day5.txt', 'r').read())
seeds=re.findall(r"\d+",data[0])


def loc(seed):

    for i in range(1,8):
      map=re.findall(r"\d+",data[i])
      val=[]
      for i in range(0,len(map),3):
        dest=int(map[i:i+3][0])
        src=int(map[i:i+3][1])
        reach=int(map[i:i+3][2])
        #print(dest,src,reach)
        if int(seed)<=src+reach-1 and int(seed)>=src:
          val.append([int(seed)+dest-src,True])
        else:
          val.append([int(seed)+dest-src,False])
      if all([not v[1] for v in val]):
        #print(int(seed))
        seed=seed
      else:
        for i in range(len(val)):
          if val[i][1]:
            seed=val[i][0]
            #print(seed)
     #print("\n")
    #print("\n")
    return seed

location1=[]
for seed in seeds:
  location1.append(loc(seed))
