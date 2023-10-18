import tkinter as tk
import json
import datetime
import requests 
from PIL import Image,ImageTk 
root=tk.Tk()

root.title("Weather Report")
root.geometry("1200x1200")


def weather(s):
    
    weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={s}&appid=512a50ef840fcdda964c53cab4d7a571")
    weatherdata=weather_data.json()
    

    def datefun(l):
            day,day2,day3,day4,day5=l[0],l[1],l[2],l[3],l[4]
            datelabel0['text']=datetime.datetime.fromtimestamp(day['dt']).strftime("%d/%m/%Y")
            value0['text']=str(round(day['main']['temp']-273.15,1))+'°C'
            pressure_value0['text']=day['main']['pressure']
            sealevel_value0['text']=day['main']['sea_level']
            groundlevel_value0['text']=day['main']['grnd_level']
            humidity_value0['text']=day['main']['humidity']
            moodlabel0['text']=day['weather'][0]['main']
            windspeed_value0['text']=day['wind']['speed']

            datelabel1['text']=datetime.datetime.fromtimestamp(day2['dt']).strftime("%d/%m/%Y")
            value1['text']=str(round(day2['main']['temp']-273.15,1))+'°C'
            pressure_value1['text']=day2['main']['pressure']
            sealevel_value1['text']=day2['main']['sea_level']
            groundlevel_value1['text']=day2['main']['grnd_level']
            humidity_value1['text']=day2['main']['humidity']
            moodlabel1['text']=day2['weather'][0]['main']
            windspeed_value1['text']=day2['wind']['speed']

            datelabel2['text']=datetime.datetime.fromtimestamp(day3['dt']).strftime("%d/%m/%Y")
            value2['text']=str(round(day3['main']['temp']-273.15,1))+'°C'
            pressure_value2['text']=day3['main']['pressure']
            sealevel_value2['text']=day3['main']['sea_level']
            groundlevel_value2['text']=day3['main']['grnd_level']
            humidity_value2['text']=day3['main']['humidity']
            moodlabel2['text']=day3['weather'][0]['main']
            windspeed_value2['text']=day3['wind']['speed']

            datelabel3['text']=datetime.datetime.fromtimestamp(day4['dt']).strftime("%d/%m/%Y")
            value3['text']=str(round(day4['main']['temp']-273.15,1))+'°C'
            pressure_value3['text']=day4['main']['pressure']
            sealevel_value3['text']=day4['main']['sea_level']
            groundlevel_value3['text']=day4['main']['grnd_level']
            humidity_value3['text']=day4['main']['humidity']
            moodlabel3['text']=day4['weather'][0]['main']
            windspeed_value3['text']=day4['wind']['speed']


            datelabel4['text']=datetime.datetime.fromtimestamp(day5['dt']).strftime("%d/%m/%Y")
            value4['text']=str(round(day5['main']['temp']-273.15,1))+'°C'
            pressure_value4['text']=day5['main']['pressure']
            sealevel_value4['text']=day5['main']['sea_level']
            groundlevel_value4['text']=day5['main']['grnd_level']
            humidity_value4['text']=day5['main']['humidity']
            moodlabel4['text']=day5['weather'][0]['main']
            windspeed_value4['text']=day5['wind']['speed']

       
    d=0
    l=[]
    if weatherdata['cod']=='200':

        for i in range(40):
            
            day=weatherdata['list'][i]['dt']
            date=datetime.datetime.fromtimestamp(day).strftime("%d/%m/%Y")
            if(d!=date):
                l.append(weatherdata['list'][i])
            d=date
        place_name['text']=weatherdata['city']['name']+","+weatherdata['city']['country']
        place_name['fg']='white'
        datefun(l)
        print(l)
    else:
        moodlabel0['text']='Error'
        moodlabel1['text']='Error'
        moodlabel2['text']='Error'
        moodlabel3['text']='Error'
        moodlabel4['text']='Error'
        place_name['text']='NO CITY FOUND'
        place_name['fg']='red'

img=Image.open('img.webp')
print("jiojio")
img=img.resize((1200,1800),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg=tk.Label(root,image=img_photo)
bg.place(x=0,y=0,width=1200,height=1200)
heading_title=tk.Label(bg,text='Weather Report',fg='white',bg='#36454F',height=2,font=('Helvetica 18',50,'bold'),width=36,padx=0,pady=0)
heading_title.place(x=10,y=10)

place_name=tk.Label(heading_title,text='Banglore,IN',font=('Helvetica 18',30,'bold'),bg='#36454F',fg='white')
place_name.place(relheight=1,relwidth=0.2)
#search box
frame_one=tk.Frame(bg,bg='#36454F',bd=6,relief='sunken')
frame_one.place(x=700,y=150,width=450,height=50)

first_day=tk.Frame(bg,bg='white',bd=10,relief='sunken')
first_day.place(y=220,x=30,width=300,height=300)
datelabel0=tk.Label(first_day,font=('Helvetica 18',30,),fg='#36454F')
datelabel0.place(relheight=0.2,relwidth=1,rely=0)
moodlabel0=tk.Label(first_day,font=('Helvetica 18',30,),fg='#36454F',text='CLEAR')
moodlabel0.place(relheight=0.2,relwidth=1,rely=0.2)
value0=tk.Label(first_day,text='26°C',bg='#36454F',fg='white',font=('Helvetica 18',40,'bold'))
value0.place(relheight=0.6,rely=0.4,relwidth=0.5)
pressure_value0=tk.Label(first_day,text='0')
pressure_value0.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.2)
pressure_font=tk.Label(pressure_value0,text='Pressure',font=('Helvetica 18',9,'bold'))
pressure_font.place(relwidth=1,relheight=0.4,rely=0)
humidity_value0=tk.Label(first_day,text='0')
humidity_value0.place(relx=0.75,rely=0.4,relwidth=0.25,relheight=0.2)
humidity_font=tk.Label(humidity_value0,text='Humidity',font=('Helvetica 18',9,'bold'))
humidity_font.place(relwidth=1,relheight=0.4,rely=0)
groundlevel_value0=tk.Label(first_day,text='0')
groundlevel_value0.place(relx=0.5,rely=0.6,relwidth=0.25,relheight=0.2)
groundlevel_font=tk.Label(groundlevel_value0,text='Ground Level',font=('Helvetica 18',9,'bold'))
groundlevel_font.place(relwidth=1,relheight=0.4,rely=0)
sealevel_value0=tk.Label(first_day,text='0')
sealevel_value0.place(relx=0.75,rely=0.6,relwidth=0.25,relheight=0.2)
sealevel_font=tk.Label(sealevel_value0,text='Sea Level',font=('Helvetica 18',9,'bold'))
sealevel_font.place(relwidth=1,relheight=0.4,rely=0)
windspeed_value0=tk.Label(first_day,text='0')
windspeed_value0.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.2)
windspeed_font=tk.Label(windspeed_value0,text='Wind Speed',font=('Helvetica 18',9,'bold'))
windspeed_font.place(relwidth=1,relheight=0.4,rely=0)


second_day=tk.Frame(bg,bg='white',relief='sunken',bd=10)
second_day.place(y=220,x=455,width=300,height=300)
datelabel1=tk.Label(second_day,font=('Helvetica 18',30,),fg='#36454F')
datelabel1.place(relheight=0.2,relwidth=1,rely=0)
moodlabel1=tk.Label(second_day,font=('Helvetica 18',30,),fg='#36454F',text='CLEAR')
moodlabel1.place(relheight=0.2,relwidth=1,rely=0.2)
value1=tk.Label(second_day,text='26°C',bg='#36454F',fg='white',font=('Helvetica 18',40,'bold'))
value1.place(relheight=0.6,rely=0.4,relwidth=0.5)
pressure_value1=tk.Label(second_day,text='0')
pressure_value1.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.2)
pressure_font=tk.Label(pressure_value1,text='Pressure',font=('Helvetica 18',9,'bold'))
pressure_font.place(relwidth=1,relheight=0.4,rely=0)
humidity_value1=tk.Label(second_day,text='0')
humidity_value1.place(relx=0.75,rely=0.4,relwidth=0.25,relheight=0.2)
humidity_font=tk.Label(humidity_value1,text='Humidity',font=('Helvetica 18',9,'bold'))
humidity_font.place(relwidth=1,relheight=0.4,rely=0)
groundlevel_value1=tk.Label(second_day,text='0')
groundlevel_value1.place(relx=0.5,rely=0.6,relwidth=0.25,relheight=0.2)
groundlevel_font=tk.Label(groundlevel_value1,text='Ground Level',font=('Helvetica 18',9,'bold'))
groundlevel_font.place(relwidth=1,relheight=0.4,rely=0)
sealevel_value1=tk.Label(second_day,text='0')
sealevel_value1.place(relx=0.75,rely=0.6,relwidth=0.25,relheight=0.2)
sealevel_font=tk.Label(sealevel_value1,text='Sea Level',font=('Helvetica 18',9,'bold'))
sealevel_font.place(relwidth=1,relheight=0.4,rely=0)
windspeed_value1=tk.Label(second_day,text='0')
windspeed_value1.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.2)
windspeed_font=tk.Label(windspeed_value1,text='Wind Speed',font=('Helvetica 18',9,'bold'))
windspeed_font.place(relwidth=1,relheight=0.4,rely=0)


third_day=tk.Frame(bg,bg='white',relief='sunken',bd=10)
third_day.place(y=220,x=860,width=300,height=300)
datelabel2=tk.Label(third_day,font=('Helvetica 18',30,),fg='#36454F')
datelabel2.place(relheight=0.2,relwidth=1,rely=0)
moodlabel2=tk.Label(third_day,font=('Helvetica 18',30,),fg='#36454F',text='CLEAR')
moodlabel2.place(relheight=0.2,relwidth=1,rely=0.2)
value2=tk.Label(third_day,text='26°C',bg='#36454F',fg='white',font=('Helvetica 18',40,'bold'))
value2.place(relheight=0.6,rely=0.4,relwidth=0.5)
pressure_value2=tk.Label(third_day,text='0')
pressure_value2.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.2)
pressure_font=tk.Label(pressure_value2,text='Pressure',font=('Helvetica 18',9,'bold'))
pressure_font.place(relwidth=1,relheight=0.4,rely=0)
humidity_value2=tk.Label(third_day,text='0')
humidity_value2.place(relx=0.75,rely=0.4,relwidth=0.25,relheight=0.2)
humidity_font=tk.Label(humidity_value2,text='Humidity',font=('Helvetica 18',9,'bold'))
humidity_font.place(relwidth=1,relheight=0.4,rely=0)
groundlevel_value2=tk.Label(third_day,text='0')
groundlevel_value2.place(relx=0.5,rely=0.6,relwidth=0.25,relheight=0.2)
groundlevel_font=tk.Label(groundlevel_value2,text='Ground Level',font=('Helvetica 18',9,'bold'))
groundlevel_font.place(relwidth=1,relheight=0.4,rely=0)
sealevel_value2=tk.Label(third_day,text='0')
sealevel_value2.place(relx=0.75,rely=0.6,relwidth=0.25,relheight=0.2)
sealevel_font=tk.Label(sealevel_value2,text='Sea Level',font=('Helvetica 18',9,'bold'))
sealevel_font.place(relwidth=1,relheight=0.4,rely=0)
windspeed_value2=tk.Label(third_day,text='0')
windspeed_value2.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.2)
windspeed_font=tk.Label(windspeed_value2,text='Wind Speed',font=('Helvetica 18',9,'bold'))
windspeed_font.place(relwidth=1,relheight=0.4,rely=0)


fourth_day=tk.Frame(bg,bg='white',relief='sunken',bd=10)
fourth_day.place(y=550,x=230,width=300,height=300)
datelabel3=tk.Label(fourth_day,font=('Helvetica 18',30,),fg='#36454F')
datelabel3.place(relheight=0.2,relwidth=1,rely=0)
moodlabel3=tk.Label(fourth_day,font=('Helvetica 18',30,),fg='#36454F',text='CLEAR')
moodlabel3.place(relheight=0.2,relwidth=1,rely=0.2)
value3=tk.Label(fourth_day,text='26°C',bg='#36454F',fg='white',font=('Helvetica 18',40,'bold'))
value3.place(relheight=0.6,rely=0.4,relwidth=0.5)
pressure_value3=tk.Label(fourth_day,text='0')
pressure_value3.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.2)
pressure_font=tk.Label(pressure_value3,text='Pressure',font=('Helvetica 18',9,'bold'))
pressure_font.place(relwidth=1,relheight=0.4,rely=0)
humidity_value3=tk.Label(fourth_day,text='0')
humidity_value3.place(relx=0.75,rely=0.4,relwidth=0.25,relheight=0.2)
humidity_font=tk.Label(humidity_value3,text='Humidity',font=('Helvetica 18',9,'bold'))
humidity_font.place(relwidth=1,relheight=0.4,rely=0)
groundlevel_value3=tk.Label(fourth_day,text='0')
groundlevel_value3.place(relx=0.5,rely=0.6,relwidth=0.25,relheight=0.2)
groundlevel_font=tk.Label(groundlevel_value3,text='Ground Level',font=('Helvetica 18',9,'bold'))
groundlevel_font.place(relwidth=1,relheight=0.4,rely=0)
sealevel_value3=tk.Label(fourth_day,text='0')
sealevel_value3.place(relx=0.75,rely=0.6,relwidth=0.25,relheight=0.2)
sealevel_font=tk.Label(sealevel_value3,text='Sea Level',font=('Helvetica 18',9,'bold'))
sealevel_font.place(relwidth=1,relheight=0.4,rely=0)
windspeed_value3=tk.Label(fourth_day,text='0')
windspeed_value3.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.2)
windspeed_font=tk.Label(windspeed_value3,text='Wind Speed',font=('Helvetica 18',9,'bold'))
windspeed_font.place(relwidth=1,relheight=0.4,rely=0)


fifth_day=tk.Frame(bg,bg='white',relief='sunken',bd=10)
fifth_day.place(y=550,x=660,width=300,height=300)
datelabel4=tk.Label(fifth_day,font=('Helvetica 18',30,),fg='#36454F')
datelabel4.place(relheight=0.2,relwidth=1,rely=0)
moodlabel4=tk.Label(fifth_day,font=('Helvetica 18',30,),fg='#36454F',text='CLEAR')
moodlabel4.place(relheight=0.2,relwidth=1,rely=0.2)
value4=tk.Label(fifth_day,text='26°C',bg='#36454F',fg='white',font=('Helvetica 18',40,'bold'))
value4.place(relheight=0.6,rely=0.4,relwidth=0.5)
pressure_value4=tk.Label(fifth_day,text='0')
pressure_value4.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.2)
pressure_font=tk.Label(pressure_value4,text='Pressure',font=('Helvetica 18',9,'bold'))
pressure_font.place(relwidth=1,relheight=0.4,rely=0)
humidity_value4=tk.Label(fifth_day,text='0')
humidity_value4.place(relx=0.75,rely=0.4,relwidth=0.25,relheight=0.2)
humidity_font=tk.Label(humidity_value4,text='Humidity',font=('Helvetica 18',9,'bold'))
humidity_font.place(relwidth=1,relheight=0.4,rely=0)
groundlevel_value4=tk.Label(fifth_day,text='0')
groundlevel_value4.place(relx=0.5,rely=0.6,relwidth=0.25,relheight=0.2)
groundlevel_font=tk.Label(groundlevel_value4,text='Ground Level',font=('Helvetica 18',9,'bold'))
groundlevel_font.place(relwidth=1,relheight=0.4,rely=0)
sealevel_value4=tk.Label(fifth_day,text='0')
sealevel_value4.place(relx=0.75,rely=0.6,relwidth=0.25,relheight=0.2)
sealevel_font=tk.Label(sealevel_value4,text='Sea Level',font=('Helvetica 18',9,'bold'))
sealevel_font.place(relwidth=1,relheight=0.4,rely=0)
windspeed_value4=tk.Label(fifth_day,text='0')
windspeed_value4.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.2)
windspeed_font=tk.Label(windspeed_value4,text='Wind Speed',font=('Helvetica 18',9,'bold'))
windspeed_font.place(relwidth=1,relheight=0.4,rely=0)

txt_box=tk.Entry(frame_one,font=('times new roman',24,'bold'),width=29,bg='#36454F',fg='white')
txt_box.grid(row=0,column=0)

btn=tk.Button(txt_box,text='search',font=('Helvetica 18',11,'bold'),bg='#36454F',fg='white',height=2,command=lambda:weather(txt_box.get()))
btn.place(relx=0.8,rely=0)

root.mainloop()











    



