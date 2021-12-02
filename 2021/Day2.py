"""
It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

- forward X increases the horizontal position by X units.
- down X increases the depth by X units.
- up X decreases the depth by X units.
"""

inst = open("input_d2.txt").read().splitlines() 

"""
Part1 : What do you get if you multiply your final horizontal position by your final depth?
"""
print("====PART1====")
horiz = 0
depth = 0
for i in range(len(inst)):
    x = inst[i].split(" ")[0]
    if x =="forward" :
        horiz += int(inst[i].split(" ")[1])
    if x =="up" :
        depth -= int(inst[i].split(" ")[1])
    if x =="down" :
        depth += int(inst[i].split(" ")[1])
print("horizontal position * depth :",depth*horiz)


"""
In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
* It increases your horizontal position by X units.
* It increases your depth by your aim multiplied by X. 

Part2 : What do you get if you multiply your final horizontal position by your final depth?
"""
print("====PART2====")
aim = 0 
horiz = 0
depth = 0
for i in range(len(inst)):
    x = inst[i].split(" ")[0]
    if x =="forward" :
        horiz += int(inst[i].split(" ")[1])
        depth += int(inst[i].split(" ")[1])*aim
    if x =="up" :
        aim -= int(inst[i].split(" ")[1])
    if x =="down" :
        aim += int(inst[i].split(" ")[1])
print("horizontal position * depth :",depth*horiz)
