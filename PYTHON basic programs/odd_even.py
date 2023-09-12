a=int(input("enter the limit"))
list1=[]
oddlist=[]
evenlist=[]
for i in range(a):
    element=int(input("enter the data"))
    list1.append(element)
    if element % 2==0:
        evenlist.append(element)
    else:
        oddlist.append(element)
print("even list")
print(evenlist)
print("odd list")
print(oddlist)