import csv
from datetime import datetime
from FileClass import Files
from SaleListClass import SaleList
import GetFileName
import AssignFilePath
import TableFooter
import TableHeader
def main():
    SalesView()
def SalesView():
    while True:
        FindFile=0
        MyDictinary={}
        x=0
        try:
          Name=GetFileName.Name_File()
        except Exception:
            print("A file name must a string")
            continue 
        FormattingName=Files(Name)
        CheckFormat=FormattingName.FileNameFormat()

        '''Formatting File Name'''
        if CheckFormat==False:
            break
        else:
            pass

        '''Checking if region code exist in the dictionary'''
        CheckCode=FormattingName.AssigningCode()
        if CheckCode==False:
            break
        else:
            pass
        print(" ")

        '''Calling a method that assigns the path of csv file being imported'''
        CSVFilePath=AssignFilePath.CSVFile_Path(Name)
        '''Calling a method that assigns the path of text file that track imported csv files'''
        TextFilePath=AssignFilePath.TextFile_Path3()

        '''Reading file names in a text file to a list'''
        FileList=[]
        try:
            with open (TextFilePath,"r") as File:
                for record in File:
                   record=record.replace("\n","")
                   FileList.append(record)
        except FileNotFoundError:
            print("The text file path is not correct please ensure you python files are in a single folder not inside a folder of folder")
            break
        except Exception:
            print("Please ensure that your text file contains atleast 1 line")
            (" ")
            break

        '''Checking if the file name being imported already exist or not in text file that track imported CSV files'''
        for FileRecord in FileList:
            if FileRecord==Name:
                FindFile=0
                print("The file with the specified name has already been imported.")
                print(" ")
                break
            if not FileRecord==Name:      
                FindFile=FindFile+1
            
        if FindFile>0:
            try:
                corruption=0
                NotFile=0
                '''Reading record in a csv file into a dictionary'''
                with open (CSVFilePath,"r") as CSVFile:              
                    SaleRecord=csv.reader(CSVFile,delimiter=';')
                    next(SaleRecord)
                    TableHeader.DisplayHeading()
                    for record in SaleRecord:
                        x=x+1
                        records=SaleList.CheckCorruption(record,record)
                        MyDictinary[x]=(records)
            except FileNotFoundError:
                NotFile=NotFile+1
                print("A file with the specified name is not found.")
                print(" ")
                break
            except Exception:
                print("Please ensure that the file being imported is not empty!")
                print(" ")
                break
            x=1
            TotalAmount=0
            '''Reading data from a dictionary into a table'''
            for code in MyDictinary:
                print(f"{code} ",end="  ")
                dataCount=0
                CodeList=MyDictinary[code]
                for listitem in CodeList:
                    dataCount=dataCount+1
                    if dataCount<=3:
                        if dataCount==1:
                            ConvDate=str(listitem)
                            try:
                                NormalDate=datetime.strptime(ConvDate,'%Y-%m-%d')
                                NormalDate=NormalDate.date()
                                if listitem==NormalDate:
                                    print(f"{listitem}  ",end="\t\t")
                            except Exception:
                                    print(f"*{listitem}  ",end="\t\t\t ")
                                    corruption=corruption+1
                        if dataCount==2:
                            if type(listitem)==int:
                                print(f"{listitem}  ",end="\t\t")
                            else:
                                print(f"{listitem}  ",end="\t\t")
                                corruption=corruption+1
                        if dataCount==3:
                            if type(listitem)==str:
                                if (listitem=="East") or (listitem=="West"):
                                    print(f"{listitem}  ",end="\t\t")
                                elif (listitem=="Mountain") or (listitem=="Central"):
                                    print(f"{listitem}  ",end="\t")
                                else:
                                    print(f"?",end="\t")
                                    corruption=corruption+1
                            else:
                                print(f"?",end="\t")
                                corruption=corruption+1
                    
                    elif dataCount==4:
                        Amount=listitem
                        if type(listitem)==float:
                            print(f"${listitem}  ",end="   ")
                            pass
                        else:
                            print(f"{listitem}  ",end="   ")
                            corruption=corruption+1
                print("\n")
                x=x+1
                try:
                    TotalAmount=TotalAmount+Amount
                except Exception:
                    pass
            TableFooter.DisplayFooter2(TotalAmount)
            if corruption==0:
                '''Writing the name of a successfully imported file with no error to a text file'''
                with open (TextFilePath,"a") as WriteFile:        
                    WriteFile.write(Name+"\n")
                print("Imported sales added to list.")
                print(" ")
                break
            elif corruption>0:
                print(f"File {Name} contains bad data. \nPlease correct the data in the file and try again!")
                print(" ")
                break
                
if __name__=="__main__":
    main()