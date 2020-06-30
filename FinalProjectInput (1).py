import csv

class ReadWrite:
    
    def getCSVFileData(self,filename): 
        #get data from csv file and return data as dictionary
        f = open(filename+".csv",'r')
        f_read = csv.reader(f, delimiter=',')

        dict1 = {}
        #key is itemID
        for row in f_read:
            dict1.update({row[0]:row[1:]})
        f.close()
        return dict1
    
    def putDataToCSVFile(self,filename,data): #Writes data in rows to CSV from a dictionary
        f = open(filename+".csv",'w',newline='')
        f_read = csv.writer(f)
        #data is a dictionary
        for key,value in data.items():
            row = [key]
            row = row + value
            f_read.writerow(row)

        f.close()
    
    def printCSVFile(self,filename): #prints all rows of CSV file
        f = open(filename+".csv",'r')
        f_read = csv.reader(f, delimiter=',')
        
        for row in f_read:
            print(row)
        f.close()
