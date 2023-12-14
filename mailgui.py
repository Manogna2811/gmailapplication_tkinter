youremail="manognasai178@gmail.com"
yourpass="vvggfwfhyuevbsms"
import tkinter as t
import tkinter.messagebox
import datetime
from time import *
import smtplib

root=t.Tk()
count=0
def k():
	global count
	st=strftime("%S")
	st=str(count)
	st="second "+str(count)
	count+=1
	a.config(text=st)
	a.after(1000,k)

def showmsg():

    ems = b.get()
    msg = texte.get(1.0,"end-1c")
    
    def sendmail(to,content):
        try:
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.ehlo()
            server.starttls()
            server.login(youremail,yourpass)
            try:
                server.sendmail(youremail,to,content)
                tkinter.messagebox.showinfo("Information","message send successfully!")
                server.close()
            except:
                tkinter.messagebox.showwarning("alert","check your internet connection")
        except:
         tkinter.messagebox.showwarning("alert","check your internet connection")
    	
    if ems == "" or msg=="":
            tkinter.messagebox.showwarning("warning","please enter email")
    else:sendmail(ems,msg)
    
a=t.Label(root,fg="yellow",font=("times",30,"bold"),bg="red")
a.pack(side="top",fill="x")
k()
count=0
t.Label(root,text="\u2689",font=("times",72,"bold"),fg="white",bg="lightblue").pack(fill="x")
ef=t.Frame(root)
ef.pack(side="top")
t.Label(ef,text="Enter Email:").pack(side="left")
b=t.Entry(ef)
b.pack(side="left")
mf=t.Frame(root)
mf.pack(side="top")
t.Label(mf,text="message:").pack(side="left")
texte=t.Text(mf,width=21,height=10)
texte.pack(side="left")

t.Button(root,text="send",command=showmsg).pack(side="top",fill="x")
t.Button(root,text="close",bg="red",command=exit).pack(side="top",fill="x")
root.mainloop()