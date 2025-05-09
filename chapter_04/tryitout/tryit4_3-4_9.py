# Print a range of numbers
# numbers = list(range(1,21))
# print(numbers)

# Print numbers from 1 to 1million
# million = []
# for value in range(0,1000000):
#     million.append(value + 1)

# # print(million)
# print(min(million))
# print(max(million))
# print(sum(million))

# Print the odd numbers from 1 - 20
# odd_numbers = []
# for value in range(1,20,2):
#     odd_numbers.append(value)
    
# print(odd_numbers)

# Make a list multiples of 3
# multiples_of_three = []
# for value in range(3,31,3):
#     multiples_of_three.append(value)
    
# print(multiples_of_three)

# Cubes
# thirdpower = []
# for value in range(1,11):
#     thirdpower.append(value**3)

# print(thirdpower)

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)