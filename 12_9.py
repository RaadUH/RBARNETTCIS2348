# Raad Barnett 1231583
s = input()
list2 = []
while(s!='-1'):
    try:
        list2.append(s.split()[0])
        list2.append(int(s.split()[1])+1)
    except ValueError:
        list2.append('0')
    s = input()
for i in range(0,len(list2),2):
    print(list2[i],list2[i+1])
