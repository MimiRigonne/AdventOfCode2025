# -*- coding: utf-8 -*-
#####################################
# Creator : Mimi Rigonne            #
# Project : AOC_DAY1                #
# Last Update : December 1st 2025   # 
# Add : Testing                     #
#####################################

#Testing data
#file = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

with open("day1_data.txt","r") as file : 

    data = [(x[0], int(x[1:])) for x in file.read().splitlines() if x.strip()]

# print(data)
pos = 50
out = 0
for d, v in data:
    if d == "L" : 
        pos = pos - v
        while pos < 0 : 
            pos = pos - 99
        
    else : 
        pos = pos + v
        while pos > 99 : 
            pos = pos - 99
    
    if pos == 0 : 
        out = out + 1
        

print(out)
