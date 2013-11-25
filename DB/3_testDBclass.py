#!/usr/bin/python3

#todo
# after user created, pop up window!, test pop up!
# after validation pop up response!
#line all columns! why not working?

# 1, if button pressed, clear textFields
# 2. create user
#3. test user 
# 4. refactor

from tkinter import *
from tkinter import ttk
import dbClassTest

#from dbClassTest import database

root = Tk()
usernameVal = StringVar()
passwordVal = StringVar()
 


def submitForm(*args):
    try:
        print("submitForm pressed")
        #root.title("sasa")
        #value = float(feet.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        #wow, set the variable! not the widget! and the widget changes!

        print('name is %s' % usernameVal.get()) #mira como hace el print!
        print('pass is %s' % passwordVal.get()) #mira como hace el print!

        #resultsContents.set(name.get()) #set la variable y cambia widget!

    except ValueError:
        pass


def testLogin(*args):
    try:
        print("testLogin")
        #root.title("sasa")
        #value = float(feet.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        #wow, set the variable! not the widget! and the widget changes!

        #print('current butoneado is %s' % name.get()) #mira como hace el print!
        #resultsContents.set(name.get()) #set la variable y cambia widget!

    except ValueError:
        pass

def main():
    print('el main')

    #instance
    db = dbClassTest.database(filename = 'timeSheetsTeta.db', table = 'Employee')

    #how to set _db attribute

    print('Create table Employee')

    db.sql_do('drop table if exists Employee')

    db.sql_do('create table Employee ( name text, surname int )')

    print('Create rows')
    db.insert(dict(name = 'one', surname = 1))
    db.insert(dict(name = 'two', surname = 2))
    db.insert(dict(name = 'three', surname = 3))
    db.insert(dict(name = 'four', surname = 4))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two'))

    print('Update rows')
    db.update(dict(name = 'one', surname = 101))
    db.update(dict(name = 'three', surname = 103))
    for row in db: print(row)

    print('Delete rows')
    db.delete('one')
    db.delete('three')
    for row in db: print(row)
 
    #root = Tk()
    root.title("SLWA DESKTOP APP")

#container view
    mainframe = ttk.Frame(root, padding="3 3 12 12") #  mainframe contained by root!, init

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #  add subview mainframe
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

#UI widgets
    createLbl = ttk.Label(mainframe, text='Create login & Password')
    createLbl.grid(column=2 , row=1, sticky=(W,E))

# user name
    nameLbl = ttk.Label(mainframe, text='User Name')
    nameLbl.grid(column=1 , row=2, sticky=(W,E))

    #usernameVal = StringVar()
    usernameTf = ttk.Entry(mainframe, textvariable = usernameVal)
    usernameTf.grid(column=2 , row=2, sticky=(W,E))

# password
    passLbl = ttk.Label(mainframe, text='Password')
    passLbl.grid(column=3 , row=2, sticky=(W,E))

#pass = StringVar()
    #passVal = StringVar()
    passTf = ttk.Entry(mainframe, textvariable = passwordVal)
    passTf.grid(column=4 , row=2, sticky=(W,E))


    button = ttk.Button(mainframe, text='Create User', command=submitForm)
    button.grid(column=3 , row=3, sticky=(W,E))    


#create user

    separatour = ttk.Separator(mainframe)
    separatour.grid(column=1 , row=4, sticky=(W,E))


#test login
    testLbl = ttk.Label(mainframe, text='Test your login')
    testLbl.grid(column=2 , row=5, columnspan = 4, sticky=(W,E))

# user name
    logNameLbl = ttk.Label(mainframe, text='Test User Name')
    logNameLbl.grid(column=1 , row=6, sticky=(W,E))

#username = StringVar()
    logVal = StringVar()
    logUsernameTf = ttk.Entry(mainframe, textvariable = logVal)
    logUsernameTf.grid(column=2 , row=6, sticky=(W,E))

# password
    logPassLbl = ttk.Label(mainframe, text='Password')
    logPassLbl.grid(column=3 , row=6, sticky=(W,E))

#pass = StringVar()
    logPassVal = StringVar()
    logPassTf = ttk.Entry(mainframe, textvariable = logPassVal)
    logPassTf.grid(column=4 , row=6, sticky=(W,E))

#create user
    logButton = ttk.Button(mainframe, text='Test User', command=testLogin)
    logButton.grid(column=3 , row=7, sticky=(W,E))    

#my loop
    root.mainloop()

 
 
 #show window!,
 



if __name__ == "__main__": main()




