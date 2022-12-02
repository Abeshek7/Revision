number=int(input("Enter the number:"))

#print("The Reversed Number is :",str(number)[::-1])

rev_num =0

while number!=0:
    digit=number%10
    rev_num=rev_num*10+digit
    number//=10

print("The Reversed number is :",rev_num)

#Count the number of digits in a number:

# count=0
#
# while(number>0):
#     count=count+1
#     number//=10
#
# print("The Count of the number is :",count)


