from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import messagebox

a=CurrencyConverter()

window = tk.Tk()
window.title('Currency Converter')
window.geometry("500x400")
window.configure(bg="light blue")

def clicked():
    global e2,e3,e1,a
    amount = float(e1.get())
    cur1 = e2.get()
    if(amount<=0 or amount==" " or amount=="" ):
        tk.messagebox.showerror("Error","Please Enter Valid Amount !")
    
    else:    
        cur2 = e3.get()
        data = a.convert(amount,cur1, cur2)
        l5 = tk.Label(window,text = data,font="Times 25 bold").place(x=120,y=310)

l1= tk.Label(window,text="Currency converter",font="Times 25 bold").place(x = 100,y= 30)

l2= tk.Label(window,text="Enter Amount Here:",font="Times 18 bold").place(x = 50,y= 80)
e1 = tk.Entry(window)

l3= tk.Label(window,text="Enter Currency",font="Times 18 bold").place(x = 50,y= 130)
e2 = tk.Entry(window)
l6= tk.Label(window,text="( In Capital Letters )",font="Times 8 bold").place(x = 50,y= 165)


l4= tk.Label(window,text="Enter Req Currency : ",font="Times 18 bold").place(x = 50,y= 200)
e3 = tk.Entry(window)
l6= tk.Label(window,text="( In Capital Letters )",font="Times 8 bold").place(x = 50,y= 235)

b1=tk.Button(window,text="click", width=10,command=clicked).place(x=200,y=270)
b2=tk.Button(window,text="EXIT", width=10,command=window.destroy).place(x=300,y=270)
e1.place(x=300,y=90)
e2.place(x=300,y=140)
e3.place(x=300,y=205)

window.mainloop()