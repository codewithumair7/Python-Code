# tuples in python
# =============================
# A kind of constant list
# unchangeable

tup = (1,3,7,87,5,45,44,34,98,233,76,45)
# tup[0]=7 #error
print(type(tup))

if 45 in tup:
    print("yes")

tup1 = tup  #copy

print(tup1)