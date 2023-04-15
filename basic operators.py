number = 1 + 2 * 3 / 4.0
print(number) #2.5

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers) #[1, 3, 5, 7, 2, 4, 6, 8]

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = [x, y]*10

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# <script.py> output:
#     x_list contains 10 objects
#     y_list contains 10 objects
#     big_list contains 20 objects
#     Almost there...
#     Great!