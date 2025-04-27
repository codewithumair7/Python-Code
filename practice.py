# datan=[]
# dataage=[]
# datag=[]
# i=0
# print("To print data you can press 0 ")
# while(True):
#     datan.append(input("Enter Name: "))
#     dataage.append(input("Enter Age: "))
#     datag.append(input("Enter Gender: "))
#     if(dataage[i] or dataage[i] or datag[i] == -1):
#      break
#     i+=1

# print(datan,dataage,datag)

datan=[]
dataage=[]
datag=[]
i=0
while(True):
    i=input("Enter Name: ")
    datan.append(i)
    i=input("Enter age: ")
    dataage.append(i)
    i=input("Enter Gender: ")
    datag.append(i)
    a=input("To print data press -1 or To enter data press any key ")
    if(a == -1 or '-1'):
     break

for x in range(len(datag)):
 print("Name ",datan[x],"Age ", dataage[x],"Gender ", datag[x])