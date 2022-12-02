# Factorial

Number=int(input("Enter the Number:"))

factorial =1

if (Number==0):
    print("The Factorial is ",factorial)
elif(Number <0):
    print("Enter a positive Number")
else:
    for i in range(1,Number+1):
        factorial =factorial*i
    print("The Factorial of",Number,"is",factorial)