from collections import Counter
# You need to write a function called find_unique_value that takes a list of numbers,
# finds the unique number among them, and returns it. A unique number is a number
# that appears only once in the list. There is no need to check for cases
# where there are multiple unique numbers in one list.


def find_unique_value(some_list):
    counts = Counter(some_list)
    for item, count in counts.items():
        if count == 1:
            return item


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
