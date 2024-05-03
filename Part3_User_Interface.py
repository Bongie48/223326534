def main():
    import Import3
    import viewSales3
    import sales3
    import AllMenu
    '''This is the user inteface that allows the user to interact with system'''
    '''Calling the method for printing the menu'''
    AllMenu.Menu()
    while True:
     
     try:
        command=input("Please enter a command: ")
     except Exception:
        print("Please enter a string variable")
        print(" ")
     if command.lower()=="import":
        '''Importing sales as a table'''
        Import3.SalesView()
     elif command.lower()=="view":
        '''Viewing imported csv file as a table'''
        viewSales3.SalesView()
     elif command.lower()=="add":
        '''add new data to the imported csv file'''
        sales3.AddingRecord()
     elif command.lower()=="menu":
        '''print the menu'''
        AllMenu.Menu()
     elif command.lower()=="exit":
        print(" ")
        print("Bye!")
        break
     else:
        print("Please choose from the menu provided")
        print(" ")
        continue
if __name__=="__main__":
   main()
       