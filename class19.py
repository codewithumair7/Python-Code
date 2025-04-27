# break and continue in Python

# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

for  i in range(12):
    print("5 x ",i," = ",i*5)
    if(i==10):
        break

# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in range(12):
  print("5 X", i, "=", 5 * i)
  if(i == 10):
    print("Skip the iteration")
    continue
  
i=0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break
