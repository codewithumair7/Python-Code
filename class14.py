# If Else Conditional Statements in Python

# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.


a = int(input("Enter your age :"))

# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

#if else 
print("Your age is ",a)

if(a>18):
    print("You can drive. ")
else:
    print("You cannot drive")

# if elif    
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")


# Nested if statements
# We can use if, if-else, elif statements inside other if statements as well.
# Example:

num = 18
if (num < 0):
    print("Number is negative.") # indentation  / scope or block of if
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")