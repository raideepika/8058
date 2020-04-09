

from tkinter import *
import smtplib

f=Tk()
f.title("Gmail ")
send_email=StringVar()
send_pass=StringVar()
recv_email=StringVar()
msg_body=None



def layout():
    global msg_body
    menuBar=Menu(f)
    send=Button(f,text='Send',width=10,command=mail,bd=3)
    cancel=Button(f,text='Cancel',width=10,command=destroy,bd=3)
    lbl1=Label(f,text="Compose Email ")
    sender_email=Label(f,text="Sender’s Email ID: ")
    sender_entry=Entry(f,textvariable=send_email,bd=3 , width= 70)
    sender_pass=Label(f,text="Sender’s Email Pass: ")
    sender_passentry=Entry(f,show='*',textvariable=send_pass,bd=3 , width= 70)

    receiver_email=Label(f,text="To: ")
    receiver_entry=Entry(f,textvariable=recv_email,bd=3, width= 70)

    msg_label=Label(f,text='Message')

    msg_body=Text(f,height=5,bd=3,width= 50)

    
    lbl1.grid(row=0 , column=0, padx=5, pady =3)
    sender_email.grid(row=1,column=0,padx=5,pady=3)
    sender_entry.grid(row=1,column=1,padx=5,pady=3)
    sender_pass.grid(row=2,column=0,padx=5,pady=3)
    sender_passentry.grid(row=2,column=1,padx=5,pady=3)
    receiver_email.grid(row=3,column=0,padx=5,pady=3)
    receiver_entry.grid(row=3,column=1,padx=5,pady=3)
    msg_label.grid(row=4,column=0,padx=5,pady=3)
    msg_body.grid(row=4,column=1,padx=5,pady=3)
    send.grid(row=0,column=2,padx=5,pady=3)
    cancel.grid(row=0,column=3,padx=5,pady=3)
    f.mainloop()

def destroy():
    f.destroy()

def msg_box():
    messagebox.showinfo("Email Info","Mail Sent")

def mail():
    try:
        if send_email.get()=="" or send_pass.get()=="" or recv_email.get()=="":
            messagebox.showerror("Error","Please enter the complete details.")
        else:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            a=send_email.get()
            b=send_pass.get()
            c=msg_body.get('1.0',END)
            d=recv_email.get()
            server.login(a,b)
            server.sendmail(a,d,c)
            server.close()
            msg_box()
    except Exception as e:
        print(e)


layout()
