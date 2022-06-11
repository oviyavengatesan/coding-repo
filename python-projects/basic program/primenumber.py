#to write the prime number

num=int(input("Enter the number"))
count=0
for i in range(1,num+1):
    if(num%i==0):
         count+=1
if count==2:
   print("there is a prime number :")

else:
   print("there is a not prime number")
