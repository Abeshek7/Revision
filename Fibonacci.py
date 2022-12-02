#Fibonacci

Number =int(input("Enter the NUmber :"))

first=0
second=1

if(Number <=0 | Number == " "):
    print("Please enter a valid number ")

for i in range (Number):
    print(first)
    temp=first
    first=second
    second=temp+second
