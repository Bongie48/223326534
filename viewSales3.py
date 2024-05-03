import csv
from datetime import datetime
from SaleListClass import SaleList
import GetCSVPath
import TableFooter
import TableHeader
def main():
    SalesView()
def SalesView():
    TwoDSalesList=[]
    corruption=0
    FindFile=0
    '''Calling a method that assigns the path of csv file being imported'''
    CSVFilePath=GetCSVPath.CSVPath3()
    try:
        '''Reading record from the csv file and converting it to its appropriate datatype'''
        with open (CSVFilePath,"r") as CSVFile:            
            SaleRecord=csv.reader(CSVFile,delimiter=';')
            next(SaleRecord)
            TableHeader.DisplayHeading()
            for record in SaleRecord:
                records=SaleList.CheckCorruption(record,record)
                TwoDSalesList.append(records)
    except FileNotFoundError:
        FindFile=FindFile+1
        print("File not found please import the file first then view it")
    x=1
    TotalAmount=0
    '''Reading record from the 2D list into a table for viewing'''
    for listitems in TwoDSalesList:
        dataCount=0
        print(f"{x}.",end=" ")
        for listitem in listitems:
            dataCount=dataCount+1
            if dataCount<=3:
                
                if dataCount==1:
                   ConvDate=str(listitem)  
                   try:
                        NormalDate=datetime.strptime(ConvDate,'%Y-%m-%d')
                        NormalDate=NormalDate.date()
                        if listitem==NormalDate:
                            print(f"{listitem}  ",end="\t\t\t")
                   except Exception:
                    print(f"{listitem}  ",end="\t\t\t\t")
                    corruption=corruption+1
                if dataCount==2:
                    
                    if type(listitem)==int:
                        print(f"{listitem}  ",end="\t\t")
                    else:
                        print(f"{listitem}  ",end="\t\t\t\t")
                        corruption=corruption+1
                if dataCount==3:
                    
                    if type(listitem)==str:
                        if (listitem=="East") or (listitem=="West"):
                           print(f"{listitem}  ",end="\t\t")
                        elif (listitem=="Mountain") or (listitem=="Central"):
                           print(f"{listitem}  ",end="\t")
                        else:
                            print(f"?  ",end="\t\t")
                            corruption=corruption+1
            elif dataCount==4:               
                Amount=listitem
                if type(listitem)==float:
                    print(f"${listitem}  ",end="\t\t")
                    pass
                else:
                    print(f"{listitem}  ",end="\t\t")
                    corruption=corruption+1
        print("\n")
        x=x+1
        try:
            TotalAmount=TotalAmount+Amount
        except Exception:
            pass
    if FindFile==0:
        TableFooter.DisplayFooter2(TotalAmount)
    if corruption>0:
        print("The file contains bad data")
if __name__=="__main__":
    main()