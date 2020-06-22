# Raad Barnett 1231583
list1 = input().split()
dict1 = dict()
for word in list1:
    if(word in dict1.keys()):
        dict1[word]+=1
    else:
        dict1[word]=1
for word in list1:
    print(word,dict1[word])
