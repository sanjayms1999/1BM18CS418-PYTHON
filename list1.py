numlist=[]
while True:
   num=int(input())
   if num!=-1:
      numlist.append(num)
   else:
      break
evenlist=[]
for even in numlist:
        if even%2==0:
           evenlist.append(even)
print("the number in first list is",end= " ")
for num in numlist:
    print(num,end=" ")
print("\nthe even number's list is",end=" ")
for y in evenlist:
            print(y)
            
