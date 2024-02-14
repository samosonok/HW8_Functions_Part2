# Your task is to write a function called add_one that takes a list of digits,
# which represent a single number. You need to add 1 to it.
#
# That is, you need to obtain a number from the set of digits in the list, add 1 to it,
# then split the resulting sum into a list of digits again.
#
# As a result, the function returns a list of digits representing the sum.
#
# So, from the list of digits [1, 2, 3, 4], the number 1234 should be obtained. Adding 1 to it gives 1235.
# After that, you need to split the obtained number into its component digits.
# The result should be the list [1, 2, 3, 5], which the function returns.

def add_one(some_list):
    converted_list = map(str, some_list)
    concatenated_string = ''.join(converted_list)
    number = int(concatenated_string)
    number += 1
    result = [int(digit) for digit in str(number)]
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
