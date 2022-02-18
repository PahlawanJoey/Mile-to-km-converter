from tkinter import *

window = Tk()
window.title("PahlawanJoey's Mile to KM converter")
window.minsize(width=200, height=150)
window.config(padx=100, pady=40)

miles = Label(text="Miles", font=("Arial", 10))
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

KM_text = Label(text="KM")
KM_text.grid(column=2, row=1)

km_empty = Label(text=0)
km_empty.grid(column=1, row=1)


def listbox_used(event):
    global KM_text
    miles.config(text=listbox.get(listbox.curselection()))
    if listbox.get(listbox.curselection()) == "Miles":
        KM_text.config(text="KM")
    else:
        KM_text.config(text="Miles")


listbox = Listbox(height=2, width=8)
fruits = ["KM", "Miles"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.config(justify="center")
listbox.grid(column=1, row=3)
listbox.selection_set(1)


def button_clicked():
    if listbox.get(listbox.curselection()) == "KM":
        user_input = float(input.get())
        km = round(user_input / 1.609344)
        return km_empty.config(text=km)
    if listbox.get(listbox.curselection()) == "Miles":
        user_input = float(input.get())
        mile = round(user_input * 1.609344)
        return km_empty.config(text=mile)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=15)
input.config(justify="center")
input.grid(column=1, row=0)

window.mainloop()
