# Use a dictionary to count the frequency of elments in list

numbers = [1, 2, 2, 3, 2, 4, 1, 3, 4, 5, 3, 5, 4, 1]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
