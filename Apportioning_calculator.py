from tkinter import *

def app():
    in1=float(e1.get())
    in2=float(e2.get())
    num_of_reads=float(e3.get())
    a=0
    x = in2 - in1
    y= x/num_of_reads
    start_num = in1

    list1.delete(0,END)
    if in2 < in1:
        list1.insert(END,"If meter has clocked please see example", "below:", "Read is 100 on a 4 dial, use 10100 instead")
    else:
        while a < num_of_reads:
            a=a+1
            in1=y+in1
            list1.insert(END,round(in1))

window=Tk()

window.wm_title("Apportioning Calc")

l1=Label(window, text="Start Read: ")
l1.grid(row=0, column=0)

l2=Label(window, text="End Read: ")
l2.grid(row=0, column=1)

l1=Label(window, text="Num of Reads: ")
l1.grid(row=0, column=2)

start_read_txt = IntVar()
e1=Entry(window, textvariable=start_read_txt)
e1.grid(row=1, column=0)

end_read_txt = IntVar()
e2=Entry(window, textvariable=end_read_txt)
e2.grid(row=1, column=1)

num_read_txt = IntVar()
e3=Entry(window, textvariable=num_read_txt)
e3.grid(row=1, column=2)

b1=Button(window, text="Apportion!", width=12, command=app)
b1.grid(row=3, column=2)

list1=Listbox(window, height=10, width=37)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)

window.mainloop()
