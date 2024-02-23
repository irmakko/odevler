from tkinter import*
from PIL import ImageTk,Image
import requests
url='https://api.openweathermap.org/data/2.5/weather?'
api_key='0cc65b3dbd946b69a697251463dc14a9'
iconUrl='https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params={'q':city,'apikey':api_key,'lang':'tr'}
    data=requests.get(url,params=params).json()
    if data:
        city=data['name'].capitalize()
        country=data['sys']['country']
        temp=int(data['main']['temp']-273.15)
        condition=data['weather'][0]['icon']
        icon=data['weather'][0]['description']
        return(city,country,temp,condition,icon)
def main(): 
    city=cityEntry.get()
    weather=getWeather(city)
    if weather:
        lotationLabel['text']='{},{}'.format(weather[0],weather[1])
        tempLabel['text']='{}°C'.format(weather[2])
        conditionLabel['text']=weather[4]
        icon=ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image=icon
pencere=Tk()
pencere.geometry("300x450")
pencere.title("Hava Durumu")
#ŞEHİR İSMİNİN YAZILACAĞI TEXTBOX
cityEntry=Entry(pencere,justify='center')
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()
#ARAMA BUTTONU
searchButton=Button(pencere,text='Arama',font=('Arial',15),command=main)
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
#HAVANIN AÇIKMI KAPALIMI OLDUĞUNU SÖYLEYEN PIROGRAM
conditionLabel=Label(pencere,font=('Arial',20))
conditionLabel.pack()

pencere.mainloop()

