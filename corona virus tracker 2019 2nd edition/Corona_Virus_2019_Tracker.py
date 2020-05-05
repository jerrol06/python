from tkinter import *
from tkinter import Tk
from covid import Covid
from tkinter.ttk import Combobox
from time import strftime
from tkinter import messagebox

windows_form = Tk()
windows_form.title('Corona Virus 2019 Tracker')
windows_form.geometry('1200x620')  # set size windows form
windows_form.configure(bg='skyblue4')  # set background color windows form
windows_form.iconbitmap('corona.ico')  # set icon and get the pic from the given path
windows_form.resizable(False, False)  # set to non resizeable windows form


list_country = []  # assgin a list for a container country
corona_virus = Covid(source="worldometers")  # call the covid module or api
get_data = corona_virus.get_status_by_country_name('World')
get_new_cases = get_data['new_cases']
get_critical = get_data['critical']
get_new_deaths = get_data['new_deaths']
all_list_country = corona_virus.list_countries()  # get all list country from covid module
confirmed = corona_virus.get_total_confirmed_cases()  # get all total confirmed from covid module
deaths = corona_virus.get_total_deaths()  # get all total deaths from covid module
recovered = corona_virus.get_total_recovered()  # get all total recovered from covid module
active = corona_virus.get_total_active_cases()  # get all total active from covid module



# create a for loop to get all country from covid module
for country in all_list_country:
    list_country.append(country.capitalize())
list_country.sort()  # arrange all country in order

# photo image,size and location of corona picture
corona_pic = PhotoImage(file="newcoronapic.png")  # set a other photo image
img = corona_pic.subsample(3)  # mechanically, here it is adjusted
photo_icon = Label(windows_form, image=img, bg='skyblue4')
photo_icon.configure(textvariable=img)
photo_icon.place(x=990, y=65)


# create definition for getting confirmed,deaths,recovered,active from selected country in combobox
def data_for_selected_country(event):
    try:
        country = country_combo.get()

        if country == '':
            messagebox.showinfo('Message', 'Please Select a Country.')
            local_confirmed_counter.configure(text='')
            local_deaths_counter.configure(text='')
            local_recovered_counter.configure(text='')
            local_active_counter.configure(text='')
            local_new_cases_counter.configure(text='')
            local_critical_counter.configure(text='')
            local_new_deaths_counter.configure(text='')
            local_total_tests_counter.configure(text='')
        else:
            get_country = corona_virus.get_status_by_country_name(country)
            local_confirmed_counter.configure(text=get_country['confirmed'])
            local_deaths_counter.configure(text=get_country['deaths'])
            local_recovered_counter.configure(text=get_country['recovered'])
            local_active_counter.configure(text=get_country['active'])
            local_new_cases_counter.configure(text=get_country['new_cases'])
            local_critical_counter.configure(text=get_country['critical'])
            local_new_deaths_counter.configure(text=get_country['new_deaths'])
            local_total_tests_counter.configure(text=get_country['total_tests'])
            selected_country.configure(text=f'{country.capitalize()}')

    except:
        print('hello')


# create combobox and bind with  def data_for_selected_country
country_combo = Combobox(windows_form, values=list_country)
country_combo.place(x=10, y=380)
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
    global_confirmed = Label(text='Confirmed', bg='skyblue4', font=('arial', 16, 'bold'))
    global_confirmed.place(x=10, y=55)

    # global confirmed counter
    global_confirmed_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_confirmed_counter.configure(text=f'{confirmed}', font=('arial', 16, 'bold'), fg='white')
    global_confirmed_counter.place(x=10, y=120)

    # global deaths text
    global_deaths = Label(text='Deaths', bg='skyblue4', font=('arial', 16, 'bold'))
    global_deaths.place(x=330, y=55)

    # global deaths counter
    global_deaths_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_deaths_counter.configure(text=f'{deaths}', font=('arial', 16, 'bold'), fg='white')
    global_deaths_counter.place(x=330, y=120)

    # global recovered text
    global_recovered = Label(text='Recovered', bg='skyblue4', font=('arial', 16, 'bold'))
    global_recovered.place(x=560, y=55)

    # global recovered counter
    global_recovered_counter = Label(text=' ', bg='skyblue4')
    global_recovered_counter.configure(text=f'{recovered}', font=('arial', 16, 'bold'), fg='white')
    global_recovered_counter.place(x=560, y=120)

    # global active text
    global_active = Label(text='Active', bg='skyblue4', font=('arial', 16, 'bold'))
    global_active.place(x=810, y=55)

    # global active counter
    global_active_counter = Label(text=' ', bg='skyblue4', fg='sea green')
    global_active_counter.configure(text=f'{active}', font=('arial', 16, 'bold'), fg='white')
    global_active_counter.place(x=810, y=120)

    # global new cases
    global_new_cases = Label(text='New Cases', bg='skyblue4', font=('arial', 16, 'bold'))
    global_new_cases.place(x=10, y=180)

    # global new cases counter
    global_new_cases_counter = Label(text=f'{get_new_cases}', font=('arial', 16, 'bold'), bg='skyblue4', fg='white')
    global_new_cases_counter.place(x=10, y=240)

    # global critical cases
    global_critical = Label(text='Critical', bg='skyblue4', font=('arial', 16, 'bold'))
    global_critical.place(x=330, y=180)

    # global critical counter
    global_critical_counter = Label(text=f'{get_critical}', font=('arial', 16, 'bold'), bg='skyblue4', fg='white')
    global_critical_counter.place(x=330, y=240)

    # global new deaths text
    global_new_deaths = Label(text='New Deaths', bg='skyblue4', font=('arial', 16, 'bold'))
    global_new_deaths.place(x=560, y=180)

    # global new deaths counter
    global_new_deaths_counter = Label(text=f'{get_new_deaths}', font=('arial', 16, 'bold'), bg='skyblue4', fg='white')
    global_new_deaths_counter.place(x=560, y=240)

    # local confirm text
    local_confirmed_case = Label(text='Confirmed', bg='skyblue4', font=('arial', 16, 'bold'))
    local_confirmed_case.place(x=330, y=330)

    # local deaths text
    local_deaths_case = Label(text='Deaths', bg='skyblue4', font=('arial', 16, 'bold'))
    local_deaths_case.place(x=550, y=330)

    # local recovered text
    local_recovered = Label(text='Recovered', bg='skyblue4', font=('arial', 16, 'bold'))
    local_recovered.place(x=780, y=330)

    # local active text
    local_active = Label(text='Active', bg='skyblue4', font=('arial', 16, 'bold'))
    local_active.place(x=1040, y=330)

    # local new cases
    local_new_case = Label(text='New Cases', bg='skyblue4', font=('arial', 16, 'bold'))
    local_new_case.place(x=330, y=470)

    # local critical
    local_Critical = Label(text='Critical', bg='skyblue4', font=('arial', 16, 'bold'))
    local_Critical.place(x=550, y=470)

    # local new deaths text
    local_new_deaths = Label(text='New Deaths', bg='skyblue4', font=('arial', 16, 'bold'))
    local_new_deaths.place(x=780, y=470)

    # local total tests text
    local_total_tests = Label(text='Total Tests', bg='skyblue4', font=('arial', 16, 'bold'))
    local_total_tests.place(x=1040, y=470)



    # corona words
    corona_words_label = Label(text='Stay at Home, Stop Covid19', bg='skyblue4', font=('arial', 8, 'bold'))
    corona_words_label.place(x=10, y=590)

    # country text
    country_label = Label(text='Select Country', bg='skyblue4', font=('arial', 15, 'bold'))
    country_label.place(x=10, y=330)


# design line label with selected country label
local_Design_line = Label(bg='azure3', width=1150, height=1)
local_Design_line.place(x=0, y=290)

# local counter label for confirmed
local_confirmed_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_confirmed_counter.place(x=330, y=400)

# local counter label for deaths
local_deaths_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_deaths_counter.place(x=550, y=400)

# local counter label fro recovered
local_recovered_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_recovered_counter.place(x=780, y=400)

# local counter label for active
local_active_counter = Label(text=' ', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_active_counter.place(x=1040, y=400)

# local new case counter
local_new_cases_counter = Label(text='', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_new_cases_counter.place(x=330, y=530)

# local critical counter
local_critical_counter = Label(text='', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_critical_counter.place(x=550, y=530)

# local new deaths
local_new_deaths_counter = Label(text='', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_new_deaths_counter.place(x=780, y=530)

# local total tests counter
local_total_tests_counter = Label(text='', font=('arial', 16, 'bold'), bg='skyblue4', fg='cyan')
local_total_tests_counter.place(x=1040, y=530)

# display selected country
selected_country = Label(text='', font=('arial', 19, 'bold'), bg='skyblue4', fg='Limegreen')
selected_country.place(x=10, y=430)

# label to display date and time
orasan_label = Label(text='', bg='skyblue4', font=('arial', 8, 'bold'))
orasan_label.place(x=1060, y=590)

all_label()  # call def all_label
orasan()  # call the orasan function

windows_form.mainloop()
