from dataclasses import dataclass
from datetime import datetime
AppendingList=[]
My2DList=[]

@dataclass
class Region:
    code:str ="w"
    
    def code(self):
        return self.code
    '''Check if the entered region code is correct'''
    def Assigningcode(self,command):
        self.code=command
        if self.code=="w" or self.code=="m" or self.code=="e" or self.code=="c":
            pass
        else:
            return False
    '''Assigns region code to region values'''      
    def AssigningRegion(self):
        RegionValues=["Mountain","West","East","Central"]
        name:str =RegionValues[0] 
        if self.code=="w":
            name=RegionValues[1]
        elif self.code=="m":
            name=RegionValues[0]
        elif self.code=="e":
            name=RegionValues[2]
        elif self.code=="c":
            name=RegionValues[3]
        return name
    '''Return an error message if an inappropriated region code is entered by the user'''
    def __str__():
        ErrorMessage="Please enter 'w' or 'm' or 'e' or 'c' "
        return ErrorMessage
    
