from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Wing Zero Gandamu")
window.minsize(width=600, height=600)

#Labels
label = Label(text="Gundam Pilot")
label.config(text="Zero System Offline")
label.pack()

#Buttons
def action():
    print(label.config(text="Zero System Activated", font=("Arial", 24)))

#calls action() when pressed
button = Button(text="Activate Zero System", command=action)
button.pack()

#Entries
entry = Entry(width=30, justify="center")
#Add some text to begin with
entry.insert(END, string="Wu-Fei Cannot Pilot me")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=2, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.tag_configure("center", justify="center")
text.insert(END, "Ryokai")
text.tag_add("center", "1.0", "end")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
fruits = ["Wing Zero", "Nataku", "Deathscythe", "Heavyarms", "Sandrock"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

