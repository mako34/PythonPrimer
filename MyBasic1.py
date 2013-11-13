#myBasic
from tkinter import *
from tkinter import ttk

def submitForm(*args):
    try:
        root.title("sasa")
        #value = float(feet.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        #wow, set the variable! not the widget! and the widget changes!

        print('current butoneado is %s' % name.get()) #mira como hace el print!
        resultsContents.set(name.get()) #set la variable y cambia widget!

    except ValueError:
        pass

def metricChanged(*args):
    try:
        root.title("metricChanged")
        #value = float(feet.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        #wow, set the variable! not the widget! and the widget changes!
    except ValueError:
        pass


def functionComboBox(*args):
    try:
        print("a combo boxa cho")  
        #value = float(feet.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        #wow, set the variable! not the widget! and the widget changes!
    except ValueError:
        pass


root = Tk()
root.title("My Basic")

#container view
mainframe = ttk.Frame(root, padding="3 3 12 12") #	mainframe contained by root!, init

#grid is the geometry manager! one of many!
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #  add subview mainframe
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#A LABEL
label = ttk.Label(mainframe, text='Full name:')
label.grid(column=1 , row=1, sticky=(W,E))

resultsContents = StringVar() #var to handle get set on widget!
label['textvariable'] = resultsContents #las asocia!
resultsContents.set('New value to display') #set la variable y cambia widget!

#image, on a label!!
image = PhotoImage(file='globe.gif')
#label['image'] = image
#size! is as on file, can this be edited?

#button
button = ttk.Button(mainframe, text='Okay', command=submitForm)
button.grid(column=3 , row=2, sticky=(W,E))
#button can have image!
#state : selected, disabled


#checkButton
measureSystem = StringVar()
check = ttk.Checkbutton(mainframe, text='Use Metric', 
	    command=metricChanged, variable=measureSystem,
	    onvalue='metric', offvalue='imperial')
check.grid(column=2 , row=3, sticky=(W,E))

check.instate(['alternate']) #togle val of checkbox!

#radioButton
phone = StringVar()
home = ttk.Radiobutton(mainframe, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(mainframe, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(mainframe, text='Mobile', variable=phone, value='cell')

home.grid(column=1 , row=4, sticky=(W,E))
office.grid(column=2 , row=5, sticky=(W,E))
cell.grid(column=3 , row=6, sticky=(W,E))

#textField
username = StringVar()
name = ttk.Entry(mainframe, textvariable=username)
name.grid(column=1 , row=7, sticky=(W,E))

print('current value is %s' % name.get())
name.delete(0,'end')         ; # delete between two indices, 0-based
name.insert(0, 'your name')  ; # insert new text at a given index



#comboBox
countryvar = StringVar()
country = ttk.Combobox(mainframe, textvariable=countryvar)
country.grid(column=2 , row=8, sticky=(W,E))

country['values'] = ('USA', 'Canada', 'Australia')

#selector ver los otros binds!
country.bind('<<ComboboxSelected>>', functionComboBox)

root.mainloop()