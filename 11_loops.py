print(range(5))

for i in range(5):
    print(i)
print()

for i in range(1, 6):
    print(i)
print()

print('With Step of 2:')
for i in range(1, 6, 2):
    print(i)
print()

print('With Step of -2:')
for i in range(10, 1, -2):
    print(i)
print()


print('######### PRINT INDEX & VALUE #########')

fruits = ['apple', 'banana', 'mango', 'cherry']
print(fruits)
print()

##################################
print('### Using enumerate() ###')
##################################
for index, value in enumerate(fruits):
    print(f'Index={index}, value={value}')
print()

##################################
print('### Using range(len()) ###')
##################################
for index in range(len(fruits)):
    print(f'Index={index}, value={fruits[index]}')
print()

##################################
print('### Using zip() ###')
##################################
indices = [0, 1, 2, 3]
for index, value in zip(indices, fruits):
    print(f'Index={index}, value={value}')
print()



