from tkinter import*
from PIL import ImageTK,Image

window=Tk()
window.title("simple interest calculator!")
window.geometry(400*400)
window.configure(bg="lightcyan")
bg= ImageTk.PhotoImage(file='./assets/back.jpg')


heading_label=Label(window,text="SIMPLE INTEREST CALCULATOR",fg="lightcyan",font=("helvetica",20),bd=5)
heading_label.place(x=50,y=20)

principal=Label(window,text="PRINCIPAL",fg="lightcyan",font=("calibri",10),bd=2)
principal.place(x=20,y=90)
principal_entry=Entry(window,text="",bd=2,width=22)
principal_entry.place(x=150,y=92)

rate=Label(window,text="RATE OF INTEREST",fg="lightcyan",font=("calibri",10),bd=2)
rate.place(x=20,y=140)
rate_entry=Entry(window,text="",bd=2,width=22)
rate_entry.place(x=150,y=142)

time=Label(window,text="TIME",fg="lightcyan",font=("calibri",10),bd=2)
time.place(x=20,y=180)
time_entry=Entry(window,text="",bd=2,width=22)
time_entry.place(x=150,y=187)

button=Button(window,text="CALCULATE",fg="black",by="cyan",
                bd=4,command=claculate_interes)
button.place(x=20,y=250)

result= LabelFrame(window,text="RESULT",bg="lightcyan",font=("calibri",12))
result.pack(padx=20,pady=20)
result.place(x=20,y=300)

res_label=Label(result,text="",bg="lightcyan",font=("calibri",12),width=33)
res_label.place(x=20,y=20)
res_label.pack()

def claculate_interest():
    p=float(principal.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest = round(i,2)

    res_label.destroy()

    message=Label(result,text="interest on is."+str(p)+"at rate of interest"+str(r)+"for"+str(t)+"years is RS."+str(interest),bg="gray",font=("calibri",12),width=85)
    message.place(x=20,y=40)
    message.pack()