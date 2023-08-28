from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import tkinter as TK

root = TK.Tk()
root.title('Translator')
root.geometry("740x400")
root.configure(bg="light blue")

def show():
    v1 = combo_first.get()
    v2 = combo_second.get()
    first_lan.config(text=v1)
    second_lang.config(text=v2)
    root.after(1000, show)

def translate():
    trans = Translator()
    input_text_content = input_text.get(1.0, END).strip()  # Get the text content without leading/trailing whitespace
    trans_lang = trans.translate(input_text_content, src=combo_first.get(), dest=combo_second.get())
    output_text.delete(1.0, END)
    output_text.insert(END, trans_lang.text)

def clear():
    output_text.delete(1.0, END)
    input_text.delete(1.0, END)

def exit_app():
    root.destroy()

corr_img =PhotoImage(file=r'C:\Users\HP\Downloads\Convert.png').subsample(7)
clear_img = PhotoImage(file=r'C:\Users\HP\Downloads\Clear.png').subsample(13)
exit_img = PhotoImage(file=r'C:\Users\HP\Downloads\Exit.png').subsample(8)

first_lan = Label(root, text='English', font=('Engraves', '30', 'bold'), fg='#5582f9', bg='white',bd=5)
first_lan.place(x=90, y=20)

second_lang = Label(root, text='Hindi', font=('Engraves', '30', 'bold'), fg='#5582f9', bg='white',bd=5)
second_lang.place(x=500, y=20)

language = list(LANGUAGES.values())

combo_first = ttk.Combobox(root, values=language)
combo_first.place(x=90, y=80)
combo_first.set('English')

combo_second = ttk.Combobox(root, values=language)
combo_second.place(x=500, y=80)
combo_second.set('Hindi')

input_text = Text(root, height=10, width=35,bd=5,font=('Arial', '10', 'bold') ,fg='black', bg='white')
input_text.place(x=30, y=100)

output_text = Text(root, height=10, width=35,bd=5,font=('Arial', '10', 'bold') ,fg='black', bg='white')
output_text.place(x=430, y=100)

convert = Button(root, text='convert', image=corr_img, bg='white', bd=10, command=translate)
convert.place(x=100, y=300)

clear_btn = Button(root, text='clear', image=clear_img, bg='#5582f9', bd=10, command=clear)
clear_btn.place(x=300, y=300)

exit_btn = Button(root, text='exit', image=exit_img, bg='#5582f9', bd=10, command=exit_app)
exit_btn.place(x=530, y=300)

show()

root.mainloop()
