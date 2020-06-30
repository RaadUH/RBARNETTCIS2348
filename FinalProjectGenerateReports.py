# Raad Barnett 1231583
from FinalProject.FinalProjectInput import ReadWrite
from datetime import date,datetime
class Generate:

    def generateFullInventoryListCSV(self): #generated FullInevntory file as CSV
        test = ReadWrite()
        dict1 = test.getCSVFileData("ManufacturerList")
        dict2 = test.getCSVFileData("PriceList")
        dict3 = test.getCSVFileData("ServiceDatesList")
        
        for k in dict2.keys():
            dict1[k].insert(2,dict2[k][0])
        for k in dict3.keys():
            dict1[k].insert(3,dict3[k][0])

        def func(obj):
            return obj[1][0]
        d = {}
        for k,v in sorted(dict1.items(),key=func): #sorted by Manufacturer name
            d[k]=v
            print(k,v)
        test.putDataToCSVFile("FullInventory", d)
        
    def generateItemTypeInventoryListCSV(self): #generates Item Type Inventory multiple file as CSVs
        test = ReadWrite()
        dict1 = test.getCSVFileData("FullInventory")
        
        list1 = []
        for v in dict1.values():
            list1.append(v[1])
            
        types = set(list1)
        
        for type in types:
            items = {}
            for k in sorted(dict1):
                if(dict1[k][1]==type):
                    dict1[k].remove(type)
                    items[k]=dict1[k]
            test.putDataToCSVFile(type.title()+"Inventory", items)
    
    def generatePastServiceDateInventoryCSV(self): #generates Past Service Date file as CSV 
        test = ReadWrite()
        dict1 = test.getCSVFileData("FullInventory")
        for k,v in dict1.items():
            date = datetime.strptime(v[3],'%m/%d/%Y')
            dict1[k][3]=date
        def func(x):
            return x[1][3]
        today_date = date.today()
        dict2 = {}
        for k,v in sorted(dict1.items(),key=func): #sorted by Manufacturer name
            print(v[3],today_date)
            print(k,v)
            if(v[3]<today_date):
                v[3] = v[3].strftime('%m/%d/%Y')
                dict2[k]=v
        obj = ReadWrite()
        obj.putDataToCSVFile("PastServiceDateInventory", dict2)

    def generateDamagedInventory(self): #generates DamagesInventory CSV file
        test = ReadWrite()
        dict1 = test.getCSVFileData("FullInventory")
        def func(x):
            return x[1][2]
        dict2 = {}
        for k,v in sorted(dict1.items(),key=func):
            if(v[-1]=='damaged'):
                dict2[k]=v[:-1]
        obj = ReadWrite()
        obj.putDataToCSVFile("DamagedInventory", dict2)

            
            
test = Generate()
test.generateItemTypeInventoryListCSV()
test.generateFullInventoryListCSV()
test.generatePastServiceDateInventoryCSV()
test.generateDamagedInventory()
obj = ReadWrite()
# obj.printCSVFile("FullInventory")
# obj.printCSVFile("TowerInventory")
# obj.printCSVFile("PhoneInventory")
#obj.printCSVFile("PastServiceDateInventory")
# obj.printCSVFile("DamagedInventory")
