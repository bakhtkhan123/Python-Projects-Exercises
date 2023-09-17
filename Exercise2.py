# adding up the numbers of string
first_digit = input("Enter first two digit number = ")
a=first_digit[0]
print(a)
b=first_digit[1]
print(b)
Sum=int(a)+int(b)
print("the sum is = ",Sum)

digit=input('enter any arbirary integers = ')
sum=0
for i in range(len(digit)):
    x=int(digit[i])
    sum += x
    x=[]
print("the sum is = ",sum)