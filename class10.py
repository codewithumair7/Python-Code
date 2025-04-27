# Taking User Input in Python 
# ==============================
# In python, we can take user input directly by using input() function.
# This input function gives a return value as string/character
# hence we have to pass that into a variable


a = input("enter your name ")
print("my name is ",a)


x = input("Enter your first Numb: ") # this returns value as a string
y = input("Enter your second Numb: ")
print(x+y)

# one way
x = input("Enter your first Numb: ") # this returns value as a string
y = input("Enter your second Numb: ")
print(int(x) + int(y))


# hence using typecasting
x = int(input("Enter your first Numb: ")) # this returns value as a string
y = int(input("Enter your second Numb: "))
print(x+y)