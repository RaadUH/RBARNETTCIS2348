import csv
str1 = input()
with open(str1, 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')
    
    for row in grades_reader:
        list1 = list(row)
        break
dict1 = dict()
for word in list1:
    if(word not in dict1):
        dict1[word] = 1
    else:
        dict1[word] +=1

for keys,values in dict1.items():
    print(keys,values)
    
