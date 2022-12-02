number=int(input("Enter the number:"))

count=len(str(number))

a=list(map(int,str(number)))
print(a)
b=list(map(lambda x:x**count,a))
print(b)

if(sum(b)==number):
    print("The Number is Armstrong")
else:
    print("Not an Armstrong")