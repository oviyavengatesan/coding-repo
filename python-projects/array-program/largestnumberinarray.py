#write to the  largest number in array elements
a=[]
n=int(input("Enter the number of elements"))
for i in range(1,n+1):
    b=int(input("Enter the element:"))
    a.append(b)
print (a)
largest_number= max(a)
print(largest_number)
