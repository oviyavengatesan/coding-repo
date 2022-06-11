#write to the  smallest number in array elements
a=[]
n=int(input("Enter the number of elements"))
for i in range(1,n+1):
    b=int(input("Enter the element:"))
    a.append(b)
print (a)
smallest_number= min(a)
print(smallest_number)
