input1 = input()
input2 = input1.replace(" ","")
reverse = input2[::-1]

if(reverse==input2):
    print(input1,"is a palindrome")
else:
    print(input1,"is not a palindrome")
