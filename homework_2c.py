def find(date):
    output = ''
    list1 = date.split(' ')
    if(list1[0]=='January'):
         output+='1'
    elif(list1[0]=='Feburary'):
       output+='2'
    elif(list1[0]=='March'):
       output+='3'
    elif(list1[0]=='April'):
       output+='4'
    elif(list1[0]=='May'):
       output+='5'
    elif(list1[0]=='June'):
       output+='6'
    elif(list1[0]=='July'):
        output+='7'
    elif(list1[0]=='August'):
        output+='8'
    elif(list1[0]=='September'):
        output+='9'
    elif(list1[0]=='October'):
        output+='10'
    elif(list1[0]=='November'):
        output+='11'
    elif(list1[0]=='December'):
        output+='12'
    output+='/'
    output+=list1[1][:-1]
    output+='/'
    output+=list1[2]
    return output
flag = 0
list3 = []
f = open('inputDates.txt')
f1 = open('parsedDates.txt', 'w')
for line in f:
    if(line=='-1'):
        break
    else:
        list1 = ['January','February','March','April','May','June','July','August','September','October','November','December']
        list2 = line.split(' ')
        if(list2[0] not in list1):
            continue
        elif(list2[1][-1]!=',' or int(list2[1][:-1])>31 or int(list2[1][:-1])<1):
            continue
        else:
            
            str1 = find(line)
            f1.write(str1)
f1.close()
f.close()
