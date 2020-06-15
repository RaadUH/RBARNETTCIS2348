input1 = input()
password=""
for p in input1:
    if(p=='i'):
        password+='!'
    elif(p=='a'):
        password+='@'
    elif(p=='m'):
        password+='M'
    elif(p=='B'):
        password+='8'
    elif(p=='o'):
        password+='.'
    else:
        password+=p
password+='q*s'
print(password)
