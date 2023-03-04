from tkinter import *


def convert():
    num = input_entry.get()
    base_from = int(from_entry.get())
    base_to = int(to_entry.get())

    try:

        base10_num = int(num, base_from)

        target_num = ""
        while base10_num > 0:
            remainder = base10_num % base_to
            target_num = str(remainder) + target_num
            base10_num //= base_to

        result_label.config(text=f"{num} ({base_from}) = {target_num} ({base_to})")
    except ValueError:
        result_label.config(text="Invalid input!")


root = Tk()
root.title("Number Base Converter")
root.config(bg="#222222")

fg_color = "#ffffff"
bg_color = "#222222"
button_color = "#444444"
button_active_color = "#555555"

root.option_add("*Font", "Helvetica")
root.option_add("*Background", bg_color)
root.option_add("*Foreground", fg_color)
root.option_add("*Button.Background", button_color)
root.option_add("*Button.Foreground", fg_color)
root.option_add("*Button.ActiveBackground", button_active_color)
root.option_add("*Button.ActiveForeground", fg_color)
root.option_add("*Entry.Background", button_color)
root.option_add("*Entry.Foreground", fg_color)

input_label = Label(root, text="Enter Number:")
input_label.pack()

input_entry = Entry(root)
input_entry.pack()

from_label = Label(root, text="From Base:")
from_label.pack()

from_entry = Entry(root)
from_entry.pack()

to_label = Label(root, text="To Base:")
to_label.pack()

to_entry = Entry(root)
to_entry.pack()

convert_button = Button(root, text="Convert", command=convert, bg="#00A36C", fg=fg_color,
                        activebackground=button_active_color, activeforeground=fg_color)
convert_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()

# Number Base Converter by FunnyCocker


