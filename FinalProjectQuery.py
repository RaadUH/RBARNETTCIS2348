# Raad Barnett 1231583
from FinalProject.FinalProjectInput import ReadWrite
from datetime import date,datetime

def combination():
    test = ReadWrite()
    dict1 = test.getCSVFileData("FullInventory")
    combination = []
    for k,v in dict1.items():
        row = []
        row.append(v[0].lower().strip())
        row.append(v[1].lower().strip())
        combination.append(row)
    return combination

def show_item(query):
    test = ReadWrite()
    dict1 = test.getCSVFileData("FullInventory")
    output = []
    for k,v in dict1.items():
        date = datetime.strptime(v[3],'%m/%d/%Y')
        today_date = date.today()
        if(v[0].lower().strip()==query[0] and v[1].lower().strip()==query[1] and date>=today_date and v[4]!='damaged'):
            row = []
            row.append(k.strip())
            row.append(v[0].strip())
            row.append(v[1].strip())
            row.append(v[2].strip())
            output.append(row)
    sorted_list = sorted(output, key=lambda x:x[2], reverse=True)
    return sorted_list[0]

def consider_item_result(query,price):
    test = ReadWrite()
    dict1 = test.getCSVFileData("FullInventory")
    output = []
    for k,v in dict1.items():
        date = datetime.strptime(v[3],'%m/%d/%Y')
        today_date = date.today()
        if(v[1].lower().strip()==query[1] and date>=today_date and v[4]!='damaged' and v[3]==price):
            row = []
            row.append(k.strip())
            row.append(v[0].strip())
            row.append(v[1].strip())
            row.append(v[2].strip())
            output.append(row)
    return output

message = 'Enter manufacturer and item type: '
print(message)
inp = input()
while(inp!='q'):
    query = inp.split()[-2:]
    query = [x.lower() for x in query]
    
    if(len(query)<2 or query[0]==query[1] or query not in combination()):
        print("No such item in inventory")
    else:
        result_item = show_item(query)
        
        if(len(result_item)==0):
            print("No such item in inventory")
        elif(len(result_item)>0):
            print("Your item is:",result_item[0],result_item[1],result_item[2],result_item[3])
            consider_item = consider_item_result(query,result_item[3])
            if(len(consider_item)>0):
                print("You may, also, consider:",consider_item[0],consider_item[1],consider_item[2],consider_item[3])

    print()
    print(message)
    inp = input() 
