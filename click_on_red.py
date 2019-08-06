from tkinter import*
from tkinter import ttk
from random import*
import time

def main():
    major()
def halp():
    hlp = Tk()
    hlp.title('Help')
    hlp.geometry('500x150')
    tc1=Label(hlp,text='Igra se sastoji od 3x3 gumba koji nakon nekog vremena mjenjaju boju',font=("Helvetica", 9))
    tc1.place(x=10,y=10)
    tc2=Label(hlp,text='Igrač mora mišem stiskati crvena polja(#FF0000)',font=("Helvetica", 9))
    tc2.place(x=10,y=30)
    tc3=Label(hlp,text='Program zavšava nakon 20 pogodaka ili 2min',font=("Helvetica", 9))
    tc3.place(x=10,y=50)
    tc4=Label(hlp,text='Dozvoljeno je 10 pogrešaka',font=("Helvetica", 9))
    tc4.place(x=10,y=70)
    def closeh():
        hlp.destroy()
    bc= ttk.Button(hlp, text = 'OK', command=closeh)
    bc.pack(side='bottom')
    hlp.mainloop()

def about():
    abo = Tk()
    abo.title('O meni')
    abo.geometry('300x150')
    td1=Label(abo,text='Ime i prezime: Danijel Slavulj',font=("Helvetica", 9))
    td1.place(x=10,y=10)
    td2=Label(abo,text='Kontakt telefon: 0956379498',font=("Helvetica", 9))
    td2.place(x=10,y=30)
    td3=Label(abo,text='Kontakt email: danijel_slavulj@hotmail.com',font=("Helvetica", 9))
    td3.place(x=10,y=50)
    td4=Label(abo,text='Adresa: A. Mihanovica 82 Kutina',font=("Helvetica", 9))
    td4.place(x=10,y=70)
    def closea():
        abo.destroy()
    bd= ttk.Button(abo, text = 'OK', command=closea)
    bd.pack(side='bottom')
    abo.mainloop()

def major():
    glavni = Tk()
    glavni.title('Click on red')
    glavni.geometry('340x380')
    glavni.protocol('WM_DELETE_WINDOW', exit)
    global timeout,correct,failed
    timeout= time.time()+120
    correct=0
    failed=0
    
    def promjena():
        
        def provjera(x,b):
            b.config(state='disabled')
            global correct,failed
            if x=='#FF0000':
                correct=correct+1
            else:
                failed=failed+1
            t1= Label(glavni,text='Pogođeno: {}'.format(correct),font =('Helvetica bold',15))
            t1.place(x=20,y=10)
            t2= Label(glavni,text='Promašeno: {}'.format(failed),font =('Helvetica bold',15))
            t2.place(x=180,y=10)
        l=["#FFFFFF","#808080",'#C0C0C0','#000000','#800000','#FF0000','#800080','#FF00FF','#008000','#00FF00','#808000','#FFFF00','#000080','#0000FF','#008080','#00FFFF','#FFA500']
        a1=randint(0,16)
        a2=randint(0,16)
        a3=randint(0,16)
        a4=randint(0,16)
        a5=randint(0,16)
        a6=randint(0,16)
        a7=randint(0,16)
        a8=randint(0,16)
        a9=randint(0,16)
        
        b1= Button(glavni,bg=l[a1],command=lambda: provjera(l[a1],b1))
        b2= Button(glavni,bg=l[a2],command=lambda: provjera(l[a2],b2))
        b3= Button(glavni,bg=l[a3],command=lambda: provjera(l[a3],b3))
        b4= Button(glavni,bg=l[a4],command=lambda: provjera(l[a4],b4))
        b5= Button(glavni,bg=l[a5],command=lambda: provjera(l[a5],b5))
        b6= Button(glavni,bg=l[a6],command=lambda: provjera(l[a6],b6))
        b7= Button(glavni,bg=l[a7],command=lambda: provjera(l[a7],b7))
        b8= Button(glavni,bg=l[a8],command=lambda: provjera(l[a8],b8))
        b9= Button(glavni,bg=l[a9],command=lambda: provjera(l[a9],b9))
        b1.place(x=10,y=50,height=100,width=100)
        b2.place(x=120,y=50,height=100,width=100)
        b3.place(x=230,y=50,height=100,width=100)
        b4.place(x=10,y=160,height=100,width=100)
        b5.place(x=120,y=160,height=100,width=100)
        b6.place(x=230,y=160,height=100,width=100)
        b7.place(x=10,y=270,height=100,width=100)
        b8.place(x=120,y=270,height=100,width=100)
        b9.place(x=230,y=270,height=100,width=100)
        
        global timeout,failed,correct
        if int(timeout)==int(time.time()) or failed==10 or failed==11 or failed==12 or correct==20 or correct==21 or correct==22:
            b1.config(state='disabled')
            b2.config(state='disabled')
            b3.config(state='disabled')
            b4.config(state='disabled')
            b5.config(state='disabled')
            b6.config(state='disabled')
            b7.config(state='disabled')
            b8.config(state='disabled')
            b9.config(state='disabled')
            noti = Tk()
            noti.title('Igra završena')
            noti.geometry('150x100')
            def da():
                noti.destroy()
                glavni.destroy()
                main()
            def ne():
                exit()
            tc=Label(noti,text='Ponoviti igru?',font=("Helvetica", 14))
            tc.pack(fill=X)
            bc1= ttk.Button(noti, text = 'Da', command=da , width=5)
            bc1.place(x = 30, y = 50)
            bc2= ttk.Button(noti, text = 'Ne', command=ne , width=5)
            bc2.place(x = 80, y = 50)
            return
            noti.protocol('WM_DELETE_WINDOW', exit)
            noti.mainloop()
        else:
            glavni.after(1000,promjena)
    promjena()
    
    def restart():
        glavni.destroy()
        main()
    menubar = Menu(glavni)
    menubar.add_command(label="Help", command=halp)
    menubar.add_command(label="About", command=about)
    menubar.add_command(label="Restart", command=restart)
    menubar.add_command(label="Quit", command=exit)
    glavni.config(menu=menubar)
    
    glavni.mainloop()
    
if __name__ == '__main__':
    main()
