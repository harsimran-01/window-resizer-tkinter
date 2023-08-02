from tkinter import *

window = Tk()
window.title("Window Resizer")
window.geometry("400x200")
window.config(bg="#F4F2DE")


frame = Frame(window, width=200 , height=200)
frame.grid(row=0, column=1, pady=10, padx=4)
label = Label(frame ,text="Window Resizer", fg="#071952", font=("Arial", 19, "bold"))
label.pack()
##########################

frame_1 = Frame(window, width=200 , height=200)
frame_1.grid(row=1, column=0, pady=5, padx=5)
label_1 = Label(frame_1, text="Width", fg="#071952", font=("Arial", 19, "bold") )
label_1.pack(anchor="w",side=LEFT)

widthvalue = StringVar()

widthentry = Entry(window, textvariable=widthvalue)
widthentry.grid(row=1, column=1)

##########################33
frame_1 = Frame(window, width=200 , height=200)
frame_1.grid(row=2, column=0, pady=5, padx=5)
label_1 = Label(frame_1, text="Height", fg="#071952", font=("Comicsansms", 19, "bold") )
label_1.pack(anchor="w",side=LEFT)

heightvalue = StringVar()

heightentry = Entry(window, textvariable=heightvalue)
heightentry.grid(row=2, column=1)
########################

def resize():
    window.geometry(f"{widthvalue.get()}x{heightvalue.get()}")
    print(f"Your Window is Resized..")


button = Button(window, text="Resize", command=resize)
button.grid(column=2)


window.mainloop()

