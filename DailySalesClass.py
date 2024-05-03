from dataclasses import dataclass

@dataclass
class DailySales:
    Amount:str
    Date:str
    Region:str
    
    '''Retrieving data from a csv file and converting to appropriate datatype'''
    def DataTypesAssignment(self):
      AppendingList=[]
      try:
          self.Amount=float(self.Amount)
      except Exception:
          print("Please enter a float variable")
          print(" ")
      try:
          self.Date
          MyDateOnly=self.Date.date()
      except ValueError:
          print("Date must be valid and in 'yyyy-mm-dd' format.")
          print(" ")
      try:
        self.Region=str(self.Region)
      except Exception:
          print("Please enter a region code")
          print(" ")
      Quartes=self.AppendList(MyDateOnly)
      AppendingList=[MyDateOnly,Quartes,self.Region,self.Amount]
      return AppendingList
   
    '''Append inputed data to a list'''
    def AppendList(self,dateObject):
        Quarter=int
        
        if dateObject.month==1 or dateObject.month==2 or dateObject.month==3:
            Quarter= 1
        elif dateObject.month==4 or dateObject.month==5 or dateObject.month==6:
            Quarter=2
        elif dateObject.month==7 or dateObject.month==8 or dateObject.month==9:
            Quarter=3
        elif dateObject.month==10 or dateObject.month==11 or dateObject.month==12:
            Quarter=4
       
        return Quarter
    