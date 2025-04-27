# While Loops in Python

# for i in range(10):
#     print(i)


# while Loop
a=0
while(a<6):
    print(a)
    a=a+1

# Else with While Loop
# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the
#  while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.
count=6
while(count>0):
    print(count)
    count=count-1
else:
    print("I am outside the loop")


# while loop with True

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break



# interpreter run the programm
