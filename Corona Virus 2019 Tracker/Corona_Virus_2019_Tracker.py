from tkinter import *
from tkinter import Tk
from covid import Covid
from tkinter.ttk import Combobox
from time import strftime

windows_form = Tk()
windows_form.title('Corona Virus 2019 Tracker')
windows_form.geometry('1200x500')  # set size windows form
windows_form.configure(bg='skyblue4')  # set background color windows form
windows_form.iconbitmap('C:\Python\corona virus icon.ico')  # set icon and get the pic from the given path
windows_form.resizable(False, False)  # set to non resizeable windows form

list_country = []  # assgin a list for a container country
corona_virus = Covid()  # call the covid module or api

all_list_country = corona_virus.list_countries()  # get all list country from covid module
confirmed = corona_virus.get_total_confirmed_cases()  # get all total confirmed from covid module
deaths = corona_virus.get_total_deaths()  # get all total deaths from covid module
recovered = corona_virus.get_total_recovered()  # get all total recovered from covid module
active = corona_virus.get_total_active_cases()  # get all total active from covid module

# create a for loop to get all country from covid module
for country in all_list_country:
    list_country.append(country['name'])
list_country.sort()  # arrange all country in order

# photo image,size and location of corona picture
corona_pic = PhotoImage(file="newcoronapic.png")  # set a other photo image
img = corona_pic.zoom(10)  # with 250, I ended up running out of memory
img = corona_pic.subsample(4)  # mechanically, here it is adjusted
photo_icon = Label(windows_form, image=img, bg='skyblue4')
photo_icon.configure(textvariable=img)
photo_icon.place(x=1000, y=50)


# create definition for getting confirmed,deaths,recovered,active from selected country in combobox
def data_for_selected_country(event):
    country = country_combo.get()
    get_country = corona_virus.get_status_by_country_name(country)
    local_confirmed_counter.configure(text=get_country['confirmed'])
    local_deaths_counter.configure(text=get_country['deaths'])
    local_recovered_counter.configure(text=get_country['recovered'])
    local_active_counter.configure(text=get_country['active'])
    selected_country.configure(text=country)


# create combobox and bind with  def data_for_selected_country
country_combo = Combobox(windows_form, values=list_country)
country_combo.place(x=10, y=370)
country_combo.bind("<<ComboboxSelected>>", data_for_selected_country)


# defin function to create date and time
def orasan():
    oras = strftime("%x - %I:%M:%S %p")
    orasan_label.configure(text=oras)
    orasan_label.after(200, orasan)


# funtion for label
def all_label():
    # global and local design
    global_Design_line = Label(bg='azure3', width=1150, height=2)
    global_Design_line.grid()

    # global text design
    global_text_label = Label(text='World Wide Case', font=('arial', 16, 'bold'), bg='azure3', fg='Black')
    global_text_label.place(x=510, y=4)

    # global confirmed text
    global_confirmed = Label(text='Confirmed', bg='skyblue4', font=('arial', 18, 'bold'))
    global_confirmed.place(x=10, y=55)

    # global confirmed counter
    global_confirmed_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_confirmed_counter.configure(text=f'{confirmed}', font=('arial', 18, 'bold'), fg='cyan2')
    global_confirmed_counter.place(x=10, y=130)

    # global deaths text
    global_deaths = Label(text='Deaths', bg='skyblue4', font=('arial', 18, 'bold'))
    global_deaths.place(x=330, y=55)

    # global deaths counter
    global_deaths_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_deaths_counter.configure(text=f'{deaths}', font=('arial', 18, 'bold'), fg='red4')
    global_deaths_counter.place(x=330, y=135)

    # global recovered text
    global_recovered = Label(text='Recovered', bg='skyblue4', font=('arial', 18, 'bold'))
    global_recovered.place(x=560, y=55)

    # global recovered counter
    global_recovered_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_recovered_counter.configure(text=f'{recovered}', font=('arial', 18, 'bold'), fg='lime green')
    global_recovered_counter.place(x=560, y=135)

    # global active text
    global_active = Label(text='Active', bg='skyblue4', font=('arial', 18, 'bold'))
    global_active.place(x=810, y=55)

    # global active counter
    global_active_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_active_counter.configure(text=f'{active}', font=('arial', 18, 'bold'), fg='mediumspringgreen')
    global_active_counter.place(x=810, y=135)

    # local confirm text
    local_confirmed_case = Label(text='Confirmed', bg='skyblue4', font=('arial', 16, 'bold'))
    local_confirmed_case.place(x=330, y=300)

    # local deaths text
    local_deaths_case = Label(text='Deaths', bg='skyblue4', font=('arial', 16, 'bold'))
    local_deaths_case.place(x=550, y=300)

    # local recovered text
    local_recovered = Label(text='Recovered', bg='skyblue4', font=('arial', 16, 'bold'))
    local_recovered.place(x=780, y=300)

    # local active text
    local_active = Label(text='Active', bg='skyblue4', font=('arial', 16, 'bold'))
    local_active.place(x=1040, y=300)

    # country text
    country_label = Label(text='Select Country', bg='skyblue4', font=('arial', 15, 'bold'))
    country_label.place(x=10, y=300)

    # creator label
    creator_label = Label(text='Created By: Jerrol M. Montemayor', bg='skyblue4', font=('arial', 8, 'bold'), fg='cyan')
    creator_label.place(x=10, y=470)

    # corona words
    corona_words_label = Label(text='Stay at Home, Stop Covid19', bg='skyblue4', font=('arial', 8, 'bold'), fg='cyan')
    corona_words_label.place(x=500, y=470)

    end_label = Label(width=1200, height=1, bg='royal blue1')
    end_label.place(x=0, y=490)

# design line label with selected country label
local_Design_line = Label(bg='azure3', width=1150, height=2)
local_Design_line.place(x=0, y=240)

# local counter label for confirmed
local_confirmed_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='gray70')
local_confirmed_counter.place(x=330, y=370)

# local counter label for deaths
local_deaths_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='red4')
local_deaths_counter.place(x=550, y=372)

# local counter label fro recovered
local_recovered_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='lime green')
local_recovered_counter.place(x=780, y=370)

# local counter label for active
local_active_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='mediumspringgreen')
local_active_counter.place(x=1040, y=370)

# display selected country
selected_country = Label(text='', font=('arial', 16, 'bold'), bg='azure3')
selected_country.place(x=525, y=243)

# label to display date and time
orasan_label = Label(text='', bg='skyblue4', font=('arial', 8, 'bold'), fg='cyan')
orasan_label.place(x=1060, y=470)

all_label()  # call def all_label
orasan()  # call the orasan function

windows_form.mainloop()
