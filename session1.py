# Python Introduction
# Last Updated : 16 May, 2026
# Python is a high-level programming language known for its simple and readable syntax. It has the following features:

# Allows writing clean code with fewer lines.
# Supports multiple programming paradigms including object-oriented, functional and procedural programming.
# Widely used in web development, automation, data analysis, artificial intelligence and many other fields.
# Dynamically typed and has automatic garbage collection


# .........Hello world program..........
# print("hello world");


# ..........Input and output in python...........
name = input("Enter your name: ");
# print("Hello", name, "!welcome");

x, y = input("Enter two number: ").split();
# print(x, y);

i = int(input("How old are you ?: "));
f = float(input("Evaluate 7/2: "));
# print(i, f);

# print(5);


# ..........python variables..............
x = 5 
name = "Alex"
# print(x, name)

# a = b = c = 100
# print(a)

# x, y, z = 1, 3.4 , "Hello"
# print(x, y , z )

# x = 2 
# y = x 
# y = 5 
# x = 10 
# print(x, y )

# .......Deleting a Variable.........
# x = 10 
# del x
# print(x) # x is not defined 

#.......... Swapping Two Variables..........
# a = 10
# b = 15
# a , b = 10 , 15 
# a, b = b, a 
# print(a, b)

# .......... Counting Characters in a String:.......
# word = "Python"
# length = len(word)
# print(f"the length is : {length}")

# x = 10
# print(x);
# x = "Now a string"
# print(x);

# ...........Python Operators..........

#.................. Arithmetic Operators.............

# a = 15
# b = 4

# print("Addition:", a + b)  

# print("Subtraction:", a - b) 

# print("Multiplication:", a * b)  

# print("Division:", a / b) 

# print("Floor Division:", a // b)  

# print("Modulus:", a % b) 

# print("Exponentiation:", a ** b)  

# ...........Comparison Operators.........
# a = 13
# b = 33

# print(a > b) # false 
# print(a < b) # true
# print(a == b) # false 
# print(a != b) # true
# print(a >= b) # false 
# print(a <= b) # true

# .......Logical Operators..................
a = True
b = False
# print(a and b) # false 
# print(a or b) # true

# age = 14
# fivePass = False
# if age >= 12 and fivePass: 
#     print("you can play footbal")
# else : print("you are not eligible for playing football game")

# .............Bitwise Operators......................
a = 7 
b = 4

# print(a & b) # 4
# print(a | b) # 7 
# print(~a) # ~x = -(x + 1) # -8
# print(a ^ b) # 3 
# print(a >> 2) # for right shift formula  (a / 2^n)  -> 7 / 2^2 = 1
# print(a << 2) # for left shift, formula (a * 2^n ) -> 7 * 2^2 = 28


# ............. Identity operator - "is" and "is not" .............
a = 10
b = 20
c = a

# print(a is not b) # true
# print(a is c) # true


# .................Membership Operators -> "in" and "not in"......................
x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

# if x not in my_list : 
#     print("x is not present in given list")
# else :
#     print("x is present in given list")    

# if(y in my_list) : 
#     print("y is present in given list")
# else :
#     print("y is not present in given list")


# .....................Ternary Operator.......................
a, b = 10 , 20
# print(a if a < b else b )


# .....................Operator Precedence...............
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

# if name == "Alex" or name == "John" and age > 2 : # this is higher precedence - name == "John" and age > 2 _ false or true -> true
#     print("Hello Welcome")
# else : 
#     print("good bye!")



# ...................Getting List of all Python keywords..............
# Getting List of all Python keywords
# import keyword
# print("The list of keywords are : ")
# print(keyword.kwlist)


