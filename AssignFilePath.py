import os
import GetFileName
def main():
    FileName=GetFileName.Name_File()
    CSVFile_Path(FileName)
    TextFile_Path3()

def CSVFile_Path(FileName):
    '''Ássigning the file path for the csv file that are being imported for all parts'''
    path=os.getcwd()
    FilePath=path+"/"+FileName
    FilePath=FilePath.replace("\\","/")
    return FilePath
def TextFile_Path3():
    '''Assigning the file path for the text file that track imported csv files for part3'''
    path=os.getcwd()
    MyTextFileName="Track_Imported_CSVfiles3.txt"
    TextFilePath=path+"/"+MyTextFileName
    TextFilePath=TextFilePath.replace("\\","/")
    return TextFilePath
if __name__=="__main__":
    main()