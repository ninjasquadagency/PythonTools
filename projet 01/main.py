from tkinter import *
from tkintermapview import TkinterMapView  # تعامل معا الخرائط : ===> Go CMD Type "pip install tkintermapview" To fix problem.

root = Tk()
root.geometry('880x450')  # حجم النافدة
root.title('TopG - الصيدليات المناوبة') # عنوان النافدة
root.iconbitmap('icon.ico') # ايكون النافدة
root.configure(background='white') # تغير لون النافدة

# ======== Star Pharmacy Buttons ====
def markazi01():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.0444926845303, -6.77486282889221)
    map.set_zoom(15)
    marker = map.set_marker(34.0444926845303, -6.77486282889221)
    marker.set_text('TopG - الصيدلية لباز سلا')
def markazi02():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.04516384589653, -6.77468916034578)
    map.set_zoom(15)
    marker = map.set_marker(34.04516384589653, -6.77468916034578)
    marker.set_text('TopG - الصيدلية القاعدة الجوية سلا')
def markazi03():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.055198329804504, -6.77967869561248)
    map.set_zoom(15)
    marker = map.set_marker(34.055198329804504, -6.77967869561248)
    marker.set_text('TopG -  الصيدلية الشعبية سلا')
def markazi04():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.07709719455205, -6.7602949390356795)
    map.set_zoom(15)
    marker = map.set_marker(34.07709719455205, -6.7602949390356795)
    marker.set_text('TopG - الصيدلية أم سلمى سلا')
def markazi05():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.06725154303525, -6.778413567209415)
    map.set_zoom(15)
    marker = map.set_marker(34.06725154303525, -6.778413567209415)
    marker.set_text('TopG - الصيدلية إبن الهيثم سلا')
def markazi06():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.070185945219926, -6.77243226620342)
    map.set_zoom(15)
    marker = map.set_marker(34.070185945219926, -6.77243226620342)
    marker.set_text('TopG - الصيدلية دار االشباب سلا')
def markazi07():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.078948161969215, -6.775959910166012)
    map.set_zoom(15)
    marker = map.set_marker(34.078948161969215, -6.775959910166012)
    marker.set_text('TopG - الصيدلية سقراط سلا')
def markazi08():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.082390435256926, -6.786020344177844)
    marker = map.set_marker(34.082390435256926, -6.786020344177844)
    marker.set_text('TopG - الصيدلية بوشوك سلا')
def markazi09():
    map = TkinterMapView(root, width=460,height=417,corner_radius=0)
    map.place(x=420,y=33)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_position(34.073361806768126, -6.788938587542297)
    map.set_zoom(15)
    marker = map.set_marker(34.073361806768126, -6.788938587542297)
    marker.set_text('TopG - الصيدلية سعيد حجي سلا')                                
# ======== End Pharmacy Buttons ====

# ======== Star Proggraming enter ====

def cu():
    country = enter.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=40)
    map.set_address(country, marker=True)

# ======== End Proggraming enter ====






#===== TiTle =======
title1 = Label(root, text='مشروع صيدليات المناوبة', fg='white',bg='black',font=('Tajawal',18),)
title1.pack(fill=X)

#===== Logo =======
logo    = PhotoImage(file='logo.png')
lab_log = Label (root, image=logo, bd=0,bg='white',width='390',height='200')
lab_log.place(x=30,y=40)

#===== Lable + Enter + Button =======
lable = Label(root,text='Country:',font=('Tajawal 13'),fg='black',bg='white')
lable.place(x=35,y=260) 

enter = Entry(root, font=("Tajawal 14"),width=15, bd=2, relief=GROOVE, )
enter.place(x=140,y=260)

button = Button(root, text='Get Country', bg='black',fg='white',bd=1,relief=SOLID,width=10,cursor='hand2', command=cu)
button.place(x=335,y=260)

#===== Pharmacy Buttons =======

button01 = Button(root, text='لباز',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi01)
button01.place(x=60,y=300)

button02 = Button(root, text=' القاعدة الجوية',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi02)
button02.place(x=180,y=300)

button03 = Button(root, text=' الشعبية ',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi03)
button03.place(x=300,y=300)

button04 = Button(root, text='  أم سلمى',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi04)
button04.place(x=60,y=350)

button05 = Button(root, text=' إبن الهيثم ',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi05)
button05.place(x=180,y=350)

button06 = Button(root, text='  دار االشباب',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi06)
button06.place(x=300,y=350)

button07 = Button(root, text=' سقراط',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi07)
button07.place(x=60,y=400)

button08 = Button(root, text=' بوشوك',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi08)
button08.place(x=180,y=400)

button09 = Button(root, text=' سعيد حجي',cursor='hand2',bg='white',fg='black',bd=1,relief=SOLID,width=10,font=('Tajawal 12'),command=markazi09)
button09.place(x=300,y=400)

# =============== MAP =====

map = TkinterMapView(root, width=460,height=417,corner_radius=0)
map.place(x=420,y=33)




root.mainloop()