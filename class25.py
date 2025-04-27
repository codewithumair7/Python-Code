# Tuples Method
# =================

tup=(1,2,3,4,5,3,4,5,6,7,9)
tup.count(3) # count the number
tup.index(3) # return index of first accurance of 3 if present
# tup.index(3,2,5) # return index of 3 b/t index[2] & index[5]
r=tup.index(3,2,5) # return index of 3 if present
print(r)



# Convert tuple into list
# ==========================

tup1=(33,5,5,54,3,556,7,877,665,33,223,88,89,67)
temp = list(tup1)
temp[0]=44
temp.append(500)
tup1=tuple(temp)
print("\n Change the tuple into list, Make some changes in list and then convert it inti tupleb\n",tup1)
