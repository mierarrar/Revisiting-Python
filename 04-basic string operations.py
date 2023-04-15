astring = "Hello world!"
print("single quotes are ' '")
# single quotes are ' '

print(len(astring))
# 12

print(astring.index('o'))
# 4

print(astring.count('l'))
# 3

print(astring[3:7])
# lo w

print(astring[::-1])
# !dlrow olleH

print(astring.upper())
# HELLO WORLD!

print(astring.startswith("Hello"))
# True

print(astring.endswith("asdfasdfasdf"))
# False

afewwords = astring.split(" ")
print(afewwords)
# ['Hello', 'world!']


# Try to fix the code to print out the correct information by changing the string.
# s = "Hey there! what should this string be?"
# # Length should be 20
# print("Length of s = %d" % len(s))

# # First occurrence of "a" should be at index 8
# print("The first occurrence of the letter a = %d" % s.index("a"))

# # Number of a's should be 2
# print("a occurs %d times" % s.count("a"))

# # Slicing the string into bits
# print("The first five characters are '%s'" % s[:5]) # Start to 5
# print("The next five characters are '%s'" % s[5:10]) # 5 to 10
# print("The thirteenth character is '%s'" % s[12]) # Just number 12
# print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
# print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# # Convert everything to uppercase
# print("String in uppercase: %s" % s.upper())

# # Convert everything to lowercase
# print("String in lowercase: %s" % s.lower())

# # Check how a string starts
# if s.startswith("Str"):
#     print("String starts with 'Str'. Good!")

# # Check how a string ends
# if s.endswith("ome!"):
#     print("String ends with 'ome!'. Good!")

# # Split the string into three separate strings,
# # each containing only a word
# print("Split the words of the string: %s" % s.split(" "))


s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))