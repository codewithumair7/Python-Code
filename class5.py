#  Comments, Escape Sequences & Print Statement 
print("I am a good boy \nand my partners are also good")
print("I am a \"good boy\" \nand my partners are also good") # \"  \' character
print(3,4,5, sep="-", end=" done")

# Other Parameters of Print Statement
# object(s): Any object, and as many as you like. Will be converted to string before printed
# sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
# end='end': Specify what to print at the end. Default is '\n' (line feed)
# file: An object with a write method. Default is sys.stdout
# Parameters 2 to 4 are optional

p = 7
if (p > 5):
    print("\np is greater than 5.")
else:
    print("p is not greater than 5.")