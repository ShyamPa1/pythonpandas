import tkinter as tk
from datetime import *
from tkinter import *
from tkinter import ttk, messagebox

import pytz
import requests
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

root = Tk()
root.title("weather App")
root.geometry("890x470+300+200")
root.configure(bg="orange")
root.resizable(False, False)


def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode((city))
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # weather
    key="89331c66dfceda76e1d61f158459b3db"
    API =f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={ key}"
    json_data = requests.get(API).json()

    temp = json_data["main"]['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']

    t.config(text=(temp,"°c"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hpa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))
    #first cell
    firstdayimage=json_data['weather'][0]['icon']

    photo1=ImageTk.PhotoImage(file=f"C:\\Users\\DELL\\Downloads\\weather\\icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1
    #second cell
    # seconddayimage = json_data['weather'][0]['icon']
    # img=(Image.open(f"C:\\Users\\DELL\\Downloads\\weather\\icon/{seconddayimage}@2x.png"))
    # # resized_image=img.resize(50,50)
    # photo2=ImageTk.PhotoImage(img)
    # secondimage.config(image=photo2)
    # secondimage.image=photo2

    # #third cell
    # thirddayimage = json_data['weather'][0]['icon']
    # img = (Image.open(f"C:\\Users\\DELL\\Downloads\\weather\\icon/{thirddayimage}@2x.png"))
    # # resized_image=img.resize(50,50)
    # photo3 = ImageTk.PhotoImage(img)
    # thirdimage.config(image=photo3)
    # thirdimage.image = photo3
    # #fourth cell
    # fourthdayimage = json_data['weather'][0]['icon']
    # img = (Image.open(f"C:\\Users\\DELL\\Downloads\\weather\\icon/{fourthdayimage}@2x.png"))
    # # resized_image=img.resize(50,50)
    # photo4 = ImageTk.PhotoImage(img)
    # fourthimage.config(image=photo4)
    # fourthimage.image = photo4
    # #fifthcell
    # fifthdayimage = json_data['weather'][0]['icon']
    # img = (Image.open(f"C:\\Users\\DELL\\Downloads\\weather\\icon/{fifthdayimage}@2x.png"))
    # # resized_image=img.resize(50,50)
    # photo5 = ImageTk.PhotoImage(img)
    # fifthimage.config(image=photo5)
    # fifthimage.image = photo5
    # #sixthcell
    # sixthdayimage = json_data['weather'][0]['icon']
    # img = (Image.open(f"C:\\Users\\DELL\\Downloads\\weather\\icon/{sixthdayimage}@2x.png"))
    # # resized_image=img.resize(50,50)
    # photo6 = ImageTk.PhotoImage(img)
    # sixthimage.config(image=photo6)
    # sixthimage.image = photo6
    # #seventh cell
    # seventhdayimage = json_data['weather'][0]['icon']
    # img = (Image.open(f"C:\\Users\\DELL\\Downloads\\weather\\icon/{seventhdayimage}@2x.png"))
    # # resized_image=img.resize(50,50)
    # photo7= ImageTk.PhotoImage(img)
    # seventhimage.config(image=photo7)
    # seventhimage.image = photo7





    #days
    first=datetime.now()
    day1.config(text=first.strftime(("%A")))

    # second=first+timedelta(days=1)
    # day2.config(text=second.strftime(("%A")))
    #
    # third = first + timedelta(days=2)
    # day3.config(text=third.strftime(("%A")))
    #
    # fourth = first + timedelta(days=3)
    # day4.config(text=fourth.strftime(("%A")))
    #
    # fifth = first + timedelta(days=4)
    # day5.config(text=fifth.strftime(("%A")))

    # sixth = first + timedelta(days=5)
    # day6.config(text=sixth.strftime(("%A")))
    #
    # seventh = first + timedelta(days=6)
    # day7.config(text=seventh.strftime(("%A")))


##icon
image_icon = PhotoImage(file="C:\\Users\DELL\\Downloads\\weather\\season.png", )
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="C:\\Users\\DELL\\Downloads\\weather\\vecteezy_square_1209957.png")
Label(root, image=Round_box, bg="#57adff", height=110, width=180).place(x=30, y=110)

# label
label1 = Label(root, text="Temperature", font=("Helvetice", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetice", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="pressure", font=("Helvetice", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="wind speed", font=("Helvetice", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetice", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

##search
search_image = PhotoImage(
    file="C:\\Users\\DELL\\Downloads\\weather\\vecteezy_black-grunge-square-brush-rectangular-frame_21971249_524.png")
myimage = Label(image=search_image, width=450, height=40, bg='orange')
myimage.place(x=270, y=120)

textfield = tk.Entry(root, justify='center', width=15, font=('popins', 25, 'bold'), bg='#203243', border=0, fg='white')
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file="C:\\Users\\DELL\\Downloads\\weather\\icons8-search-100.png")
myimage_icon = Button(image=search_icon, borderwidth=0, width=30, height=30, cursor='hand2', bg='orange',
                      command=getweather)
myimage_icon.place(x=608, y=132)

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="C:\\Users\\DELL\\Downloads\\weather\\vecteezy_square_1209957.png")

Label(frame, image=firstbox, bg="white", width=210, height=150,anchor="center").place(x=405, y=30)
# Label(frame, image=firstbox, bg="#212120", width=80, height=130).place(x=805, y=30)
# Label(frame, image=firstbox, bg="#212120", width=80, height=130).place(x=305, y=30)
# Label(frame, image=firstbox, bg="#212120", width=80, height=130).place(x=405, y=30)
# Label(frame, image=firstbox, bg="#212120", width=80, height=130).place(x=505, y=30)
# Label(frame, image=firstbox, bg="#212120", width=80, height=130).place(x=605, y=30)
# Label(frame, image=firstbox, bg="#212120", width=80, height=130).place(x=705, y=30)

# clock
clock = Label(root, text="2:30 pm", font=("Helvatica", 30, "bold"), fg="white", bg="orange")
clock.place(x=30, y=20)

# timezone
timezone = Label(root, text="2:30 pm", font=("Helvatica", 20), fg="white", bg="orange")
timezone.place(x=700, y=20)

long_lat = Label(root, text="2:30 pm", font=("Helvatica", 30), fg="white", bg="orange")
long_lat.place(x=700, y=20)

#thpwd
t=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
t.place(x=150,y=120)
h=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
h.place(x=150,y=140)
p=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
p.place(x=150,y=160)
w=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
w.place(x=150,y=180)
d=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
d.place(x=150,y=200)

#first cell
firstframe=Frame(root,width=500,height=150,bg="#282829")
firstframe.place(x=205,y=315)

day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)
# #second cell
# secondframe=Frame(root,width=80,height=132,bg="#282829")
# secondframe.place(x=305,y=325)
#
# day2=Label(secondframe,bg="#282829",fg="#fff")
# day2.place(x=10,y=5)
#
# secondimage=Label(secondframe,bg="#282829")
# secondimage.place(x=7,y=20)
# #third cell
# thirdframe=Frame(root,width=80,height=132,bg="#282829")
# thirdframe.place(x=405,y=325)
#
# day3=Label(thirdframe,bg="#282829",fg="#fff")
# day3.place(x=10,y=5)
#
# thirdimage=Label(thirdframe,bg="#282829")
# thirdimage.place(x=7,y=20)
# #fourth cell
# fourthframe=Frame(root,width=80,height=132,bg="#282829")
# fourthframe.place(x=505,y=325)
#
# day4=Label(fourthframe,bg="#282829",fg="#fff")
# day4.place(x=10,y=5)
#
# fourthimage=Label(fourthframe,bg="#282829")
# fourthimage.place(x=7,y=20)
# #fifth cell
# fifthframe=Frame(root,width=80,height=132,bg="#282829")
# fifthframe.place(x=605,y=325)
#
# day5=Label(fifthframe,bg="#282829",fg="#fff")
# day5.place(x=10,y=5)
#
# fifthimage=Label(firstframe,bg="#282829")
# fifthimage.place(x=7,y=20)
# #sixth cell
# sixthframe=Frame(root,width=80,height=132,bg="#282829")
# sixthframe.place(x=705,y=325)
#
# day6=Label(sixthframe,bg="#282829",fg="#fff")
# day6.place(x=10,y=5)
#
# sixthimage=Label(sixthframe,bg="#282829")
# sixthimage.place(x=7,y=20)
# #seventh cell
# seventhframe=Frame(root,width=80,height=132,bg="#282829")
# seventhframe.place(x=805,y=325)
#
# day7=Label(seventhframe,bg="#282829",fg="#fff")
# day7.place(x=10,y=5)
#
# seventhimage=Label(seventhframe,bg="#282829")
# seventhimage.place(x=7,y=20)

root.mainloop()
