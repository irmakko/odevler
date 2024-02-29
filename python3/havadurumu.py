from tkinter import*
from PIL import ImageTk,Image
import requests
import tkinter as tk
from tkinter import messagebox
url='https://api.openweathermap.org/data/2.5/weather?'
api_key='0cc65b3dbd946b69a697251463dc14a9'
iconUrl='https://openweathermap.org/img/wn/{}@2x.png'
def getWeather(city):
    params={'q':city,'apikey':api_key,'lang':'tr'}
    data=requests.get(url,params=params).json()
    if data['cod'] !='404':
        city=data['name'].capitalize()
        country=data['sys']['country']
        temp=int(data['main']['temp']-273.15)
        condition=data['weather'][0]['icon']
        icon=data['weather'][0]['description']
        return(city,country,temp,condition,icon)
    else:
        data=cityEntry.get()
        messagebox.showinfo("Şehir","Hatalı şehir ismi girdiniz!!!") 
def main_(): 
    city=cityEntry.get()
    weather=getWeather(city)
    if weather:
        lotationLabel['text']='{},{}'.format(weather[0],weather[1])
        tempLabel['text']='{}°C'.format(weather[2])
        conditionLabel['text']=weather[4]
        icon=ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image=icon    
def buton_aktif(event):
    if len(cityEntry.get())>=3:
        searchButton.config(state=tk.NORMAL)
    else:
        searchButton.config(state=tk.DISABLED)
pencere=tk.Tk()
pencere.geometry("300x450")
pencere.title("Hava Durumu")
#ŞEHİR İSMİNİN YAZILACAĞI TEXTBOX
cityEntry=Entry(pencere,justify='center')#,command=textbox_aktif
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.bind("<KeyRelease>",buton_aktif)
cityEntry.focus()
#ARAMA BUTTONU
searchButton=Button(pencere,text='Arama',font=('Arial',15),state=tk.DISABLED,command=main_)
searchButton.pack(fill=BOTH,ipady=10,padx=20)
#İCON LABELİ
iconLabel=Label(pencere)
iconLabel.pack()
#ŞEHİR VE ÜLKEYİ SÖYLEYEN LABEL
lotationLabel=Label(pencere,font=('Arial',40))
lotationLabel.pack()
#DERECE VERE LABEL
tempLabel=Label(pencere,font=('Arial',50,'bold'))
tempLabel.pack()
#HAVANIN AÇIKMI KAPALIMI OLDUĞUNU SÖYLEYEN PROGRAM
conditionLabel=Label(pencere,font=('Arial',20))
conditionLabel.pack()
pencere.mainloop()