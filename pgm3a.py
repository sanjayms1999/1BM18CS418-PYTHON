num=int(input("enter the number to find divisor:\n"))
div=[]
for i in range(1,num):
    if(num%i==0):
        div.append(i)
print(f"the factor of {num} are: {div}")
