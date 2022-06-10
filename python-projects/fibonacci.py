
# To write the fibbonacci program
num=int(input("Enter the number of Terms"))
f1,f2=0,1
f3=f1+f2

print("Fibonacci series of first ",num,"Terms")
print(f1)
print(f2)

for i in range(3,num+1):
    print(f3)
    f1=f2
    f2=f3
    f3=f1+f2
