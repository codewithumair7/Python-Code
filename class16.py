# Match Case Statements in Python 
# A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. 
# The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

# The match case consists of three main entities :

# The match keyword
# One or more case clauses
# Expression for each case

# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, 
# and a set of statements to be executed if the pattern matches.

x = int(input("Enter the value of x "))

match x:
    case 0:
        print("Select zero")
    case 1:
        print("Select one")
    case 2:
        print("Select two")

        # default case w
    case _:
        print("Select default") # default case



a = int(input("Enter the value of x: "))
# x is the variable to match
match a:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if a!=90:
        print(a, "is not 90")
    case _ if a!=80:
        print(a, "is not 80")
    case _:
        print(x)