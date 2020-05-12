from tkinter import *  # import tkinter all
from tkinter import messagebox  # from tkinter import messagebox
import re  # import regex module
from tkinter import filedialog  # import filedialog to open and save

lista = []


def email_scrapper():  # define a email_scrapper function
    new_text_info = text_info.get(1.0, END)  # get the text from text_info

    if len(new_text_info) == 1:  # check the len of get text from new_text_info if is equal to 1
        messagebox.showinfo("Message",
                            "Please Enter Text First.")  # it show the message_box once the if statement become true

    elif len(new_text_info) > 1:  # check the len of get text from new_text_info if is greater than 1 and once true
        # bring down to code
        list_box.delete(0, END)  # delete all in listbox
        text_info_get = text_info.get(1.0, END)  # get the text from text_info
        emails_crapper = re.compile(r'[\w\.]+@[\w\.-]+')  # create regex form the find a email
        email_caller = emails_crapper.findall(str(text_info_get))  # find all same at emails_crapper
        email_caller.sort()  # sort the list in email_caller
        for get_email in (email_caller):  # create a for loop from email_caller list
            convert = ','.join(list_box.get(0, END))  # convert in to string plus a comma sign from listbox get
            if get_email in convert:  # check if get_email in to convert
                pass  # pass
            else:  # once if false it bring dow the code
                list_box.insert(0, get_email)  # insert the get_email not in convert to listbox

        count_num = (str(len(list_box.get(0, END))))  # create variable name count and get the all count in listbox
        results_label.configure(
            text=f'Results: {count_num}')  # configure a label and set to show 'Results : Count of the get list in listbox


def number_scrapper():  # create a definition for number scrapper
    new_text_info = text_info.get(1.0, END)  # get the text from text widget

    if len(new_text_info) == 1:  # check if the text info len is equal to 1 once true bring down the codes
        messagebox.showinfo("Message",
                            "Please Enter Text First.")  # create a messagebox for pop up a please enter text first
    elif len(new_text_info) > 1:  # once if statement first go here and check if len of text is greater than 1
        list_box.delete(0, END)  # list all text or data in listbox
        text_info_get = text_info.get(1.0, END)  # get all text or data in text widget
        numbers_scrapper = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # create a formula to find a phone numbers
        number_caller = numbers_scrapper.findall(str(text_info_get))  # find all same at numbers_scrapper
        number_caller.sort()  # sort the list

        for (get_num) in number_caller:  # create a for loop to get one by ine the list in list of number_caller
            convert = ','.join(list_box.get(0, END))  # join a comma sign to text or data in listbox
            if get_num not in convert:  # check the number in list number_caller if  not exist  and once true bring down

                list_box.insert(END, get_num)  # insert the get_num in listbox
            else:  # once if is false else proceed
                pass  # pass

        count_num = (str(len(list_box.get(0, END))))  # create variable name count and get the all count in listbox
        results_label.configure(
            text=f'Results: {count_num}')  # configure a label and set to show 'Results : Count of the get list in listbox


def clear_data():
    new_text_info = text_info.get(1.0, END)
    if len(new_text_info) == 1:
        messagebox.showinfo("Message", "No Text Found.")
    elif len(new_text_info) > 1:
        text_info.delete(1.0, END)
        list_box.delete(0, END)
        count_listbox = len(list_box.get(0, END))
        results_label.configure(text=f'Results:', textvariable=count_listbox)


def open_data():
    files = [('Text Document', '*.txt'),
             ('Python Files', '*.py'),
             ('All Files', '*.*'),

             ]
    try:
        open = filedialog.askopenfile(initialdir='Desktop', title='Open a File',
                                      filetypes=files)
        for open_text in open:
            text_info.insert(END, open_text)
    except (TypeError):
        pass
    except UnicodeDecodeError:
        messagebox.showinfo('Message', "Error Files")


def exit():
    root.destroy()


def save_data():
    if len(list_box.get(0, END)) == 0:
        messagebox.showinfo('Message', 'No Data Found !!')

    else:
        x = list(list_box.get(0, END))

        files = [('All Files', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]

        try:
            f = filedialog.asksaveasfile(mode='w', filetypes=files, defaultextension=".txt")
            for j in x:
                f.write(str(j))
                f.write('\n')
            f.close()

            messagebox.showinfo('Message', 'SuccessFully Saved..')
        except (AttributeError, UnicodeDecodeError):
            pass


root = Tk()
root.title("Email And Phone Numbers Extractor")
root.config(bg='skyblue4')
root.geometry("685x690")
root.iconbitmap('C:\\Users\\jerro\\Desktop\\PYCHARM FILES\\Email and Phone Number Scrapper\\scrapper.ico')
root.resizable(False, False)
var = StringVar()

menu = Menu(root)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_data)
file_menu.add_command(label="Save", command=save_data)
file_menu.add_command(label="Exit", command=exit)
root.config(menu=menu)

text_frame = LabelFrame(root, text='', bg='skyblue4', font=('arial', 12, 'bold'))
text_frame.place(x=10, y=40)

results_frame = LabelFrame(root, text='', bg='skyblue4', font=('arial', 12, 'bold'))
results_frame.place(x=10, y=350)

text_scroll = Scrollbar(text_frame, orient=VERTICAL)
text_info = Text(text_frame, font=('arial', 11, 'bold'), bg='lightgray', height=15, yscrollcommand=text_scroll.set)

text_info.pack(expand=True, side="left", fill="y")
text_scroll.config(command=text_info.yview)
text_scroll.pack(side="left", fill="y")

results_scroll = Scrollbar(results_frame, orient=VERTICAL)
list_box = Listbox(results_frame, width=91, height=14, font=('arial', 10, 'bold'), bg='lightgray',
                   yscrollcommand=results_scroll.set)
list_box.pack(expand=True, side="left", fill="y")
results_scroll.pack(expand=True, side="left", fill="y")
results_scroll.config(command=list_box.yview)
results_scroll.pack(side="left", fill="y")

email_button = Button(text='Email', bd=7, font=('arial', 10, 'bold'), width=7, bg='lightblue', command=email_scrapper)
email_button.place(x=10, y=610)

number_button = Button(text='Number', bd=7, font=('arial', 10, 'bold'), width=7, bg='lightblue',
                       command=number_scrapper)
number_button.place(x=300, y=610)

clear_button = Button(text='Clear', bd=7, font=('arial', 10, 'bold'), width=7, bg='lightblue', command=clear_data)
clear_button.place(x=600, y=610)

results_label = Label(text='Results: ', bg='skyblue4', font=('arial', 12, 'bold'))
results_label.place(x=10, y=320)

enter_text_label = Label(text='Enter Text Here: ', bg='skyblue4', font=('arial', 12, 'bold'))
enter_text_label.place(x=10, y=10)

root.mainloop()
