import csv
from datetime import datetime
from RegionClass import Region
from DailySalesClass import DailySales
import GetCSVPath
def main():
    AddingRecord()
def AddingRecord():
        while True:
            TwoDSalesList2=[]
            '''Getting user input '''
            try:
              SalesAmount=float(input("Amount: "))
              if SalesAmount<=0:
                raise Exception
              
            except FloatingPointError:
                print("Please don't enter an integer")
                print(" ")
                continue
            except ValueError:
                print("Enter float variable") 
                print(" ")
                continue
            except Exception:
                print("Please enter an float variable that is greater than 0!")
                print(" ")
                continue
            try:
                SaleDate=input("Date (yyyy-mm-dd): ")
                DateObj=datetime.strptime(SaleDate,'%Y-%m-%d')
            except Exception:
                print("Date must be valid and in 'yyyy-mm-dd' format.")
                print(" ")
                continue
            try:
                region=input("Region: ")
                AddReg=Region(region)
                InvalidCode=AddReg.Assigningcode(region)    
                if InvalidCode==False:
                    Message=Region.__str__()
                    print(Message)
                    continue
                if type(region)==str:
                    pass
                else:
                    raise Exception
            except Exception:
                print("Please enter only a char/string!")
                continue
            print(" ")
            '''Appending record added by the user to a 2D list '''
            AddList=DailySales(SalesAmount,DateObj,AddReg.AssigningRegion())
            TwoDSalesList2.append(AddList.DataTypesAssignment())
            print(" ")
            print(f"Sales for {SaleDate} added.")

            '''Calling a method that assigns the path of csv file being imported'''
            CSVFilePath=GetCSVPath.CSVPath3()
            '''Calling a method that assigns the path of csv file being imported'''
            Myfile=open(CSVFilePath,"a",newline='')
            write=csv.writer(Myfile,delimiter=';')
            write.writerows(TwoDSalesList2)
            Myfile.close()

def GetDate(dateObj):
    return dateObj
if __name__=="__main__":
    main()