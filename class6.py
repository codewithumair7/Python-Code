# variables and datatypes
a=4
b=a
c="umair"
d=True

# In python we can print the type of any operator using type function
print("type of a is", type(a))
print("type of c is", type(c))
print("type of b is", type(b))
print("type of d is", type(d))

# By default, python provides the following built-in data types:

# 1. Numeric data: int, float, complex
# 2. Text data: str
# 3. Boolean data:
# 4. Sequenced data: list, tuple          list--as array  
# 5. Mapped data: dict


# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.
#  Lists are mutable and can be modified after creation.

#  Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
#   Tuples are immutable and can not be modified after creation.

# dict: A dictionary is an unordered collection of data containing a key:value pair. 
# The key:value pairs are enclosed within curly brackets.

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
