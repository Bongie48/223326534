from dataclasses import dataclass
from datetime import datetime
My2DList=[]

@dataclass
class SaleList():
    row:int =0
    column:int =0
    corruption: int =0
    
    '''Checking if record in a list in an appropriate datatype'''
    def CheckCorruption(self,record):
        RecordList=[record]
        NewRecordList=[]
        Quarter:str
        RecordList=record
        try:
            Dates=RecordList[0]
            DateObj=datetime.strptime(Dates,'%Y-%m-%d')
            MyDateOnly=DateObj.date()
        except Exception:
            MyDateOnly=str("?")
        try:
            Quarter=int(RecordList[1])
        except Exception:
            Quarter=str("?")
        try:
            Regions=RecordList[2]
        except Exception:
            Regions="?"
        try:
            Amounts=float(RecordList[3])
        except Exception:
            Amounts=str("?")
            
        NewRecordList=[MyDateOnly,Quarter,Regions,Amounts]
        My2DList.append(NewRecordList)
        return NewRecordList
    