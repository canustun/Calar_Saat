from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pygame
pygame.init()
kurulan_vakit_baş=""
bip=pygame.mixer.Sound('bip_sesi.mp3')
renk=["orange","gray","yellow","gold","white","red"]
pencere=Tk()
pencere.title("                  Saat Uygulamasını Geliştiriyorum")
pencere.geometry("300x300")
x=60

saniye=0.0
calis=True
dakika,eklenecek_rakam=0,0.1
def kronometre():
    
    kronometre=Tk()
    kronometre.geometry("300x300")
    kronometre.title("Kronometre")
    gecen_sure=Label(kronometre,text="0",bg="Gray",fg="White")
    gecen_sure.place(x=100,y=70)
    
    def anamenu_gecis():
        global saniye,calis,dakika,eklenecek_rakam
        kronometre.destroy()
        saniye=0
        dakika=0
        eklenecek_rakam=0.1
        calis=True

    def zaman_art():
        global saniye,eklenecek_rakam,dakika
        if saniye>60:
            dakika+=1
            saniye=0.0
            
        saniye+=eklenecek_rakam
        gecen_sure['text']="Dakika : "+str(dakika)+"\nSaniye : "+str(saniye)[:4]

        kronometre.after(100,zaman_art)

    def basladur_durumu():
        global eklenecek_rakam,calis
        
        if dur_basla['text']=="Başla":
            dur_basla['text']="Dur"
            eklenecek_rakam=0.1
        else:
            dur_basla['text']="Başla"
            eklenecek_rakam=0.0
        if calis:
            zaman_art()
            calis=False
        

    dur_basla=Button(kronometre,text="Başla",bg="Cyan")
    dur_basla.config(command = basladur_durumu)
    dur_basla.place(x=120,y=105)
    
    ana_menu=Button(kronometre,text="Ana Menü",bg="Orange")
    ana_menu.config(command = anamenu_gecis)
    ana_menu.place(x=105,y=175)
    
    kronometre.mainloop()
    
def saat_göster():
    global renk
    saat=Label(text="Anlık Saat : "+str(datetime.now())[:19],bg="Gray",fg="Yellow",height=2)
    saat.place(x=55,y=10)
    pencere.after(500,saat_göster)

def alarm_kur_ve_calis():
    global kurulan_vakit_baş,kurulan_vakit
    kurulan_vakit=str(datetime.now())[:8]+kurulan_vakit_baş
    if kurulan_vakit==str(datetime.now())[:16]:
        kurulan_vakit_baş=""
        bip.play()
    pencere.after(1,alarm_kur_ve_calis)

def alarm_kurma():
    global kurulan_vakit_baş
    alarm_sayfası=Tk()
    alarm_sayfası.geometry("400x300")
    Label(alarm_sayfası,text="").pack()
    def alarm_islem_tamam():
        global kurulan_vakit_baş
        onay["bg"]="Red"
        if len(gun.get())>2 or len(saat.get())>2 or len(dakika.get())>2:
         messagebox.showerror("Hatalı Girdi","Gün,saat veya dakikayı uzun girdin!")
        else:
         kurulan_vakit_baş=str(gun.get()+" "+saat.get()+":"+dakika.get())
         alarm_kur_ve_calis()
         alarm_sayfası.destroy()
        
    Label(alarm_sayfası,text="Alarm Kurma Ekranına Hoşgeldin :)",bg="cyan",font="Arial").pack()
    gun=Entry(alarm_sayfası,text="Gün Bilgisi")
    saat=Entry(alarm_sayfası)
    dakika=Entry(alarm_sayfası,text="Dakika Bilgisi")
    
    gun.place(x=130,y=80,width=25)
    saat.place(x=130,y=120,width=25)
    dakika.place(x=130,y=160,width=25)
    #################
    
    bilgigun=Label(alarm_sayfası,text="Gün :")
    bilgisaat=Label(alarm_sayfası,text="Saat :")
    bilgidakika=Label(alarm_sayfası,text="Dakika :")

    bilgigun.place(x=50,y=80)
    bilgisaat.place(x=50,y=120)
    bilgidakika.place(x=50,y=160)

    ##################

    onay=Button(alarm_sayfası,text="Alarmı Kur !",bg="Orange")
    onay.config(command = alarm_islem_tamam)
    onay.place(x=160,y=220)
    alarm_sayfası.mainloop()
 
def kurulu_alarm():
    global kurulan_vakit_baş,kurulan_vakit,x
    if kurulan_vakit_baş=="":
        x=60
        alarm_goster["text"]="Kurulu Alarm Gözükmüyor :D"
        alarm_goster.place(x=x,y=130)
    else:
        x=30
        alarm_goster["text"]=f"\"{kurulan_vakit}\" Vaktine Alarm Kurulmuş !"
        alarm_goster.place(x=x,y=130)
        
    pencere.after(1000,kurulu_alarm)

alarm_goster=Label()
alarm_goster.place(x=x,y=130)

kurulu_alarm()

alarm=Button(text="Alarm Kur",bg="cyan",height=0,font="Italic")
alarm.config(command = alarm_kurma)
alarm.place(x=170,y=90)

krono=Button(text="Kronometre",bg="cyan",height=0,font="Italic")
krono.config(command = kronometre)
krono.place(x=30,y=90)

yapımcı=Label(text="Product by Can Üstün")
yapımcı.place(x=0,y=280)

versiyon=Label(text="Versiyon 0.1")
versiyon.place(x=220,y=280)

saat_göster()
pencere.mainloop()
