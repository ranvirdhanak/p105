import math 
import csv 


data = [60,61,65,63,98,99,90,95,91,96]

def calculate_mean(data):
    
    n = len(data)

    total = 0

    for x in data:
        total = total + x

    mean = total / n

    return mean

square_list = []
for num in data:
    a = int(num)-calculate_mean(data)
    a = a**2
    square_list.append(a)

sum = 0
for i in square_list:
    sum = sum + i

result = sum/(len(data)-1)

std = math.sqrt(result)
print(std)

