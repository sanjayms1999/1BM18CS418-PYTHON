list=[]
numbers=int(input("enter the list length :"))
print("enter the numbers")
for i in range(numbers):
    data=int(input())
    list.append(data)
print(list)
search=int(input("enter the number to search \n"))
if search in list:
     print(search,"\n true, element is present at position",list.index(search)+1)
else:
    print(search,"\n false ,element not found")