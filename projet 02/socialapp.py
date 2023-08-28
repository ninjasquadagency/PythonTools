from tkinter import *
import webview # please install librery ==> Go to cmd type pip install webview or pywebview

app =Tk() #Object Tk() هي واجهة صغيرة موجودة في تكنتر

app.geometry('1000x600+200+50') # width x height + left + top (تمركز الواجهة)
app.title('MySocialApp')
app.iconbitmap('img/icon.ico')
app.configure(background='whitesmoke')

#======== programming ======

def Whatsapp():
    url = 'https://wa.me.com/0718113533'
    webview.create_window(
        'Mr.Marouan [ Whatsapp ]',
        url,
        width=815,
        height=560,
        resizable=False,
        background_color='#D8D8D8',
        x=390 , y=120,
        zoomable=True,
    )
    webview.start()
def Instagram():
    url = 'https://instagram.com/marouan_anouar'
    webview.create_window(
        'Mr.Marouan [ Instagram ]',
        url,
        width=815,
        height=560,
        resizable=False,
        background_color='#D8D8D8',
        x=390 , y=120,
        zoomable=True,
    )
    webview.start()
def Github():
    url = 'https://github.com/marouananouar'
    webview.create_window(
        'Mr.Marouan [ Github ]',
        url,
        width=815,
        height=560,
        resizable=False,
        background_color='#D8D8D8',
        x=390 , y=120,
        zoomable=True,
    )
    webview.start()
def Blogger():
    url = 'https://www.cyberblog.cf/'
    webview.create_window(
        'Mr.Marouan [ Blogger ]',
        url,
        width=815,
        height=560,
        resizable=False,
        background_color='#D8D8D8',
        x=390 , y=120,
        zoomable=True,
        
    )
    webview.start()
def Portfolio():
    url = 'https://marouananouar.github.io/MYSpace/'
    webview.create_window(
        'Mr.Marouan [ Portfolio ]',
        url,
        width=815,
        height=560,
        resizable=False,
        background_color='#D8D8D8',
        x=390 , y=120,
        zoomable=True,
    )
    webview.start()
def Shop():
    url = 'https://linktr.ee/ninjasquad.agency'
    webview.create_window(
        'Mr.Marouan [ Shop ]',
        url,
        width=815,
        height=560,
        resizable=False,
        background_color='#D8D8D8',
        x=390 , y=120,
        zoomable=True,
    )
    webview.start()




#======= Top Title ====

title1 = Label(app, text='Social Media System', fg='black',bg='white',font=('courier',16))
title1.pack(fill=X)

logo   = PhotoImage(file='img/logo.png')
logoo  = Label(app, image=logo,bg='whitesmoke') 
logoo.place(x=240,y=85,width=700,height=400)

title2 = Label(app, text='Application Social Media System', fg='black',bg='whitesmoke',font=('courier',26,'bold'))
title2.place(x=290,y=520)

#====== sidebare ======

side = Frame(app,width=180,height=590,bg='white',bd=0,relief=GROOVE)
side.place(x=0,y=24)

side_title1 = Label(side, text='  Ninja Squad', fg='black',bg='white',font=('courier',13))
side_title1.place(x=5,y=10)

#======== images ======

user      = PhotoImage(file='img/user.png')
whatsapp  = PhotoImage(file='img/whatsapp.png')
instagram = PhotoImage(file='img/instagram.png')
github    = PhotoImage(file='img/github.png')
blogger   = PhotoImage(file='img/blogger.png')
portfolio = PhotoImage(file='img/portfolio.png')
shop      = PhotoImage(file='img/shop.png')

button = Button(side, text='Marouan Anouar', cursor='hand2',image=user,compound=TOP ,width=120,bd=0,relief=RIDGE,bg='white')
button.place(x=25,y=42)

side_title2 = Label(side, text='Social Media', fg='black',bg='white',font=('courier',12))
side_title2.place(x=25,y=190)

button1 = Button(side, text='Whatsapp',cursor='hand2',image=whatsapp,width=130,compound=TOP,bd=0,relief=RIDGE,command=Whatsapp)

button1.place(x=20,y=220)

button2 = Button(side, text='instagram',cursor='hand2',image=instagram,width=130,compound=TOP,bd=0,relief=RIDGE,command=Instagram)

button2.place(x=20,y=280)

button3 = Button(side, text='github',cursor='hand2',image=github,width=130,compound=TOP,bd=0,relief=RIDGE,command=Github)

button3.place(x=20,y=340)

button4 = Button(side, text='blogger',cursor='hand2',image=blogger,width=130,compound=TOP,bd=0,relief=RIDGE,command=Blogger)

button4.place(x=20,y=400)

button5 = Button(side, text='portfolio',cursor='hand2',image=portfolio,width=130,compound=TOP,bd=0,relief=RIDGE,command=Portfolio)

button5.place(x=20,y=460)

button6 = Button(side, text='shop',cursor='hand2',image=shop,width=130,compound=TOP,bd=0,relief=RIDGE,command=Shop)

button6.place(x=20,y=520)


app.mainloop()  #Run