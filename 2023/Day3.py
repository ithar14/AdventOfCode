def extract(data,regx):
  parts=[]
  gears=[]
  symbols=[]
  for i in range(len(data)):
    symbols=[[sym.group(),sym.start(0),sym.end(0)] for sym in re.finditer(regx,data[i])]
    digits_line=[[int(dig.group()),dig.start(0),dig.end(0)] for dig in re.finditer(r'\d+',data[i]) ]
    if i-1>=0:
      digits_up=[[int(dig.group()),dig.start(0),dig.end(0)] for dig in re.finditer(r'\d+',data[i-1]) ]
    else:
      digits_up=[]
    if i<len(data)-1 and i+1!=len(data):
      digits_down=[[int(dig.group()),dig.start(0),dig.end(0)] for dig in re.finditer(r'\d+',data[i+1]) ]
    else:
      digits_down=[]
    
    part=([dig[0] for sym in symbols for dig in digits_up for n in range(len(str(dig[0]))+2)  if (dig[2]-n)==sym[1]]
       +[dig[0] for sym in symbols for dig in digits_down for n in range(len(str(dig[0]))+2)  if (dig[2]-n)==sym[1]]
       +[dig[0] for sym in symbols for dig in digits_line if dig[2]==sym[1] or (dig[1]-1)==sym[1]])

    gear = ([[digup[0]*digdn[0]] for sym in symbols for digup in digits_up for digdn in digits_down for nup in range(len(str(digup[0]))+2) for ndn in range(len(str(digup[0]))+2) if (digup[2]-nup)==sym[1] and (digdn[2]-ndn)==sym[1]]
    +[[digleft[0]*digright[0]] for sym in symbols for digleft in digits_line for digright in digits_line if digleft[2]==sym[1] and (digright[1]-1)==sym[1]])

                
    print(i-1,digits_up)
    print(i,symbols,"   ",digits_line) 
    print(i+1,digits_down)
    print(parts)
    print("\n")

    parts.append(part)
    gears.append(gear)
  if regx=='[^\d.]':
    return parts
  elif regx=="\*":
    return gears
#parts=[num for p in extract(data,'[^\d.]') if p != [] for num in p]
#print(sum(parts))

gears=[list(np.array(x).flatten()) for p in extract(data,"\*") if p != [] for x in p]
print(sum(np.array(gears).flatten()))
