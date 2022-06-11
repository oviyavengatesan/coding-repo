#to write the compound interest

principle=float(input("Enter the principle amount"))
time=int(input("Enter the year"))
rate=float(input("Enter the rate"))

compound_interest=principle*pow(1+rate/100),time
    
print("The compound interest :",compound_interest)
