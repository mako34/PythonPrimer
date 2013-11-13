#0


from tkinter import *
from tkinter import ttk

#function called by command , event handler de boton!
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        #wow, set the variable! not the widget! and the widget changes!
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

#container view
mainframe = ttk.Frame(root, padding="3 3 12 12") #	mainframe contained by root!, init

#grid is the geometry manager! one of many!
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #  add subview mainframe
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#watch changes on this variable, get and set!
feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) #init object!
feet_entry.grid(column=2, row=1, sticky=(W, E))  #  add subview feet_entry

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) 
#la monia! mira como lo inita y adenda en misma linea!

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
#comand ... envent handling!

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#mira variable text!

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate) #q hace!

root.mainloop()