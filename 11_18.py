# Raad Barnett 1231583
list1 = input().split()
list1 = [int(x) for x in list1]
list1.sort()
for num in list1:
    if(num>=0):
        print(num,end=' ')
