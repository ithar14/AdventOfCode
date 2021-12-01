"""
As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.
"""

depth = open("input_d1.txt").read().splitlines() 

"""
Part1 : count the number of times a depth measurement increases from the previous measurement. 
"""
print("====PART1====")
count =0
for i in range(len(depth)-1):
    if int(depth[i+1])>int(depth[i]):
        count+=1
print("the number of times a depth measurement increases",count)


"""
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.
Instead, consider sums of a three-measurement sliding window. 

Part2 : count the number of times the sum of measurements in this sliding window increases from the previous sum.
"""
print("====PART2====")
count = 0
Sum = []
for i in range(len(depth)-2):
    num = int(depth[i+2])+int(depth[i+1])+int(depth[i])
    Sum.append(num)
for i in range(len(Sum)-1):
    if Sum[i+1]>Sum[i] :
        count+=1
print("the number of times the sum is larger than the previous sum",count)