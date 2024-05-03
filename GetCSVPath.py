import AssignFilePath
def main():
    CSVPath3()
def CSVPath3():
    Name=""
    FileList=[]
    
    '''Getting the path of the text file'''
    TextFilePath=AssignFilePath.TextFile_Path3()

    '''Reading record in the text file that keeps track of successfully imported files'''
    try:
        with open (TextFilePath,"r") as File:
            for record in File:
                record=record.replace("\n","")
                FileList.append(record)
    except FileNotFoundError:
        print("The text file path is not correct please ensure you python files are in a single folder not inside a folder of folder")

    '''Getting the name of the last imported file from a list called FileList'''
    for record in FileList:
        Name=record

    '''Calling a method that assigns the path of csv file being imported'''
    FilePath=AssignFilePath.CSVFile_Path(Name)
    return FilePath

if __name__=="__main__":
    main()