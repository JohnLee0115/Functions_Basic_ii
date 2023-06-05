# 1.
def countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList

call = countDown(10)
print(call)

# 2.
def print_and_return(list):
    print(list[0])
    return list[1]

call = print_and_return([1, 2])
print(call)

# 3.
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum
example = [1, 2, 3, 4, 5,]
call = first_plus_length(example)
print(call)

# 4. 
def value_greater_than_second(list):
    newList = []
    if len(list) >= 2:
        for i in list:
            if i > list[1]:
                newList.append(i)
        print(len(newList))
        return newList
    else:
        return False

example1 = [5, 2, 3, 1, 4]
example2 = [3]

call1 = value_greater_than_second(example1)
call2 = value_greater_than_second(example2)

print(call1)
print(call2)

# 5. 
def length_and_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

call1 = length_and_value(4,7)
call2 = length_and_value(6,2)

print(call1)
print(call2)
