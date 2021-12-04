# https://adventofcode.com/2021/day/3
"""
The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.
"""

inst = open("input_d3.txt").read().splitlines() 

"""
Part1 : What is the power consumption of the submarine?
"""
print("====PART1====")
gamma = ''
epsilon = ''
for j in range(len(inst[0])):
    num0 = 0
    num1 = 0
    for i in range(len(inst)):
        if int(inst[i][j]) == 1 :
            num1+=1
        else :
            num0+=1 
    if num0>num1 :
        gamma+='0'
        epsilon+='1'
    else:
        gamma+='1'
        epsilon+='0'
print('the power consumption of the submarine :',int(gamma,2)*int(epsilon,2))


"""
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Part2 : What is the life support rating of the submarine?
"""
print("====PART2====")
o2=inst
for j in range(len(o2[0])):
    num0 = 0
    num1 = 0
    for i in range(len(o2)):
        if int(o2[i][j]) == 1 :
            num1+=1
        else :
            num0+=1  
    if num0>0 and num1>0:
        if num1>=num0:
            o2 =list(filter(lambda a: int(a[j])==1, o2))
        
        if num0>num1:
            o2 =list(filter(lambda a: int(a[j])==0, o2)) 

co2=inst
for j in range(len(co2[0])):
    num0 = 0
    num1 = 0
    for i in range(len(co2)):
        if int(co2[i][j]) == 1 :
            num1+=1
        else :
            num0+=1 
    if num0>0 and num1>0:
        if num1>=num0:
            co2 =list(filter(lambda a: int(a[j])==0, co2))
        if num0>num1:
            co2 =list(filter(lambda a: int(a[j])==1, co2))
print('the life support rating of the submarine :',int(o2[0],2)*int(co2[0],2))