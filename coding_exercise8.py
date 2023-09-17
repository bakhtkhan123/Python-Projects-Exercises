#love calculator
my_name=input('my name is:')
lover_name=input('enter your lover name:')
concate=(my_name+lover_name)
str=concate.lower()
t=str.count('t')
r=str.count('r')
u=str.count('u')
e=str.count('e')
l=str.count('l')
o=str.count('o')
v=str.count('v')
e=str.count('e')
true_count=t+r+u+e
love_count=l+o+v+e
love_score=(f'{true_count}{love_count}')
love_score=int(love_score)
print(f'my love score is {love_score}%')
if love_score<10 or love_score>90: 
    print('you live together')
elif love_score>40 and love_score<50:
    print("you are already together")
else: 
    print(love_score)
    
 
    
    