import math
def  Getsumofthesquares(N):

    sum=0
    for i in range(1,N+1):
        sum=sum+math.pow(i, 2)
    return sum
n=int(input("enter N number : "))
print("sum of squres of first",n,"natural number is",Getsumofthesquares(n))
