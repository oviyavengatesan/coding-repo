num = int(input("Enter the armstrong number"))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum= sum+digit**3
    temp= temp//10

 if num==sum:
    print(num,"arm strongnumber")
 else:
    print(num,"is not armstrong number")
    
