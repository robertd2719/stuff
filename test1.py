print('some testing stuff for git')


def factorial(value):
    if value <= 1:
        return 1
    else:
        return factorial(value-1) * value


list1 = [factorial(x) for x in range(10)]

print(list1)
print('hello darkness my old friend')
