x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False

name = 'john'
age = 21

if name == 'john' and age == 21:
    print('Hi %s, you are %d' % (name, age))

# in operator
if name in 'hoanjoanjohn':
    print('%s, you exist' % name)
else:
    print('%s, you do not exist' % name)

# is operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# not operator
print(not True) # Prints out False