#pizza order program
size=input("Which size of pizza do you want (S/M/L)")
bill=0
if size=='S'or size== 's':
    bill +=100
elif size=='M'or size=='m':
    bill+=200
else:
    bill+=300
add_pepproni=input("do you want to take pepproni (y/N)")
if add_pepproni== 'Y'or add_pepproni== 'y':
    if size=='S'or size== 's':
        bill+=30
    else: 
        bill+=50
Extra_cheese=input("Do you want extra cheese (Y/N)")
if Extra_cheese == 'y'or Extra_cheese=='Y':
    print("Extra cheese for any size of pizza = 20 Rs")
    bill=bill+20
print(f"Your total bill is {bill}")

    
    
