# ........Python Data Types..........
# Data types in Python define the type of value stored in a variable and determine the operations that can be performed on that data. Since Python treats everything as an object, each value is associated with a specific data type.

a = 5
b = 5.0
c = 2 + 4j  # j is a imaginary value which is

# print(type(a))
# print(type(b))
# print(type(c))


# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(d[1])
# print(d.get(2))

# ...................1. String..............
# s = 'Welcome to the Geeks World'
# print(s)
# print(type(s))

# access string with index
# print(s[1])
# print(s[-1])


# ..........2. List...............
# a = [1, 2, 3]
# print(a)

# b = ["Geeks", "For", "Geeks", 4, 5]
# print(b[3])
# print(b[-3])
# b[0] = "g"
# print(b[0])


# ............. 3. Tuple................
# t1 = (1,)
# print(type(t1));

# t2 = ("greek", "for", "greek", 1, 2)

# print(t2[3])
# print(t2[-3])
# # t2[0] = "g"
# print(t2[0])


# ........Truthy and Falsy Values....................
# if 1 :
#     print("1 is truthy value")

# if not 0 :
#     print("0 is falsy")


number_input = input("enter the number: ")
if number_input:
    number = int(number_input)

    if number:
     print("This will print because the number is truthy.");

    if not number:
     print("This will NOT print because 0 is falsy.");

else:
    print("you did not enter anything")

