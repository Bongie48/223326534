from dataclasses import dataclass

@dataclass
class Files:
    FileName:str
    '''Formatting file name'''
    def FileNameFormat(self):
        try:   
          "sales_q{0}_{1}{2}{3}{4}_{5}.csv".format(int(self.FileName[7]),int(self.FileName[9]),int(self.FileName[10]),int(self.FileName[11]),int(self.FileName[12]),self.FileName[14])
          return True
        except Exception:
          print("The filename isn't in the expected format, use this format for file name sales_qn_yyyy_r.csv")
          return False
    '''Checking the region code if it exist in a dictinary'''  
    def AssigningCode(self):
        MyRegions={"c":"Central","w":"West","m":"Mountain","e":"East"}

        GetCode=0 
        for RegionCode in MyRegions:
           if RegionCode==self.FileName[14]:
              GetCode=GetCode+1
              return True
           else:
              GetCode=0
        if GetCode==0:
           print(" ")
           print(f"File Name {self.FileName} doesn't include one of following region code ['w','m','c','e']")
           return False
