# Introduction to Lists in Python
# ===================================

# like array in c++
# A list type allow different datatypes in one list

l = [1,2,3,4,5]
print("type of l is ",type(l))
print(l)

# Similar to positive indexing, negative indexing is also used to access items, 
# but from the end of the list. The last item has index [-1], 
# second last item has index [-2], third last item has index [-3] and so on.
#its actually print(color[len(color)-3])
# ==========================================

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])


# To find something in list  if/else statement
# ============================

if "Yellow" in colors:
  print("Yellow is present")
else:
  print("Yellow is not present")



# Range of Index:
# ====================
# You can print a range of list items by specifying where you want to start, 
# where do you want to end and if you want to skip elements in between the range.

# Syntax:

# listName[start : end : jumpIndex]
# =======================================
# Note: jump Index is optional. We will see this in later examples.

# Example:1 printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes

# Example:2 printing all element from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes

# Example:3 printing all element from stsar to given index 
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:5])	#using positive indexes

# Example:4 Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		# jump 2 like animals[1st index+2]=animals[0+2]



# List Comprehension
# ======================= 
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)