numbers_lst = [1, 2, 3, 2, 4, 5]
print(numbers_lst)
print(type(numbers_lst))

numbers = tuple(numbers_lst)
print(numbers)
print(type(numbers))

nums = (1, 2, 3)
print(nums)
print(type(nums))

nums_lst = list(nums)
print(nums_lst)
print(type(nums_lst))

mixed_tuple = (1, "Hello world!", 3.14, True)
print(mixed_tuple)

print(numbers[2])
print(numbers[-1])

print(numbers[0:4])
print(numbers[1:4])

print('All numbers:')
print(numbers[::])

print('Reverse of all numbers:')
print(numbers[::-1])

concat_tuple = numbers + mixed_tuple
print(concat_tuple)

print(mixed_tuple * 3)

##################################################
########### Immutable Nature of Tuples ###########
##################################################
lst = [1, 2, 3, 4, 5]
lst[0] = 'Krish'
print(lst)

tpl = (1, 2, 3, 4, 5, 6)
# tpl[0] = 'Krish'  ## TypeError: 'tuple' object does not support item assignment
print(tpl)

lst = list(tpl)
lst[-1] = 'Krish'
print(lst)

tpl = tuple(lst)
print(tpl)

### Tuple Methods ###
print("### TUPLE METHODS ###")

print(numbers)

print('### Count the number ###')
print(f"Number of 2's: {numbers.count(2)}")
print(f"Number of 3's: {numbers.count(3)}")
print(f"Number of 6's: {numbers.count(6)}")

print('### Index of the number ###')
print(f"Index of 2: {numbers.index(2)}")
print(f"Index of next 2: {numbers.index(2, numbers.index(2) + 1)}")
print(f"index of 3: {numbers.index(3)}")
# print(f"index of 6: {numbers.index(6)}") ## ValueError: tuple.index(x): x not in tuple

### Tuple - Packing & Unpacking ###
print("### TUPLE Packing ###")
a = 1
b = 'Hello'
c = 3.14

packed_tpl = a, b, c
print(packed_tpl)

print("### TUPLE unpacking ###")
d, e, f = packed_tpl

print(d)
print(e)
print(f)

## Unpacking with *
first, *middle, last = numbers
print(first)
print(middle)
print(last)

####################################
print('####### Nested List #######')
####################################
lst = [[1,2,3,4], [6,7,8,9], [1, 'Hello', 3.14, True]]
print(lst[2][1])
print(lst[1][1:3])

lst = [[1,2,3,4], [6,7,8,9], (1, 'Hello', 3.14, True)]
print(lst[2][1])
print(lst[2][0:3])

#####################################
print('####### Nested Tuple #######')
#####################################
nested_tpl = ((1, 2, 3), ('a', 'b', 'c'), (True, False))
print(nested_tpl[1])
print(nested_tpl[1][1:])

###################################################
print('####### Interate over Nested Tuple #######')
###################################################
for sub_tpl in nested_tpl:
    print('|', end = ' ')
    for item in sub_tpl:
        print(item, end = ' | ')
    print()
