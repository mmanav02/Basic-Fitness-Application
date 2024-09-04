import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from datetime import date
import time

# Create table
try:
    conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('pscpythonia.db')
    # cursor created
    c = conn.cursor()
    '''c.execute("""CREATE TABLE customerdata (
        userid TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phonenum TEXT,
        gender TEXT,
        PRIMARY KEY(userid)
    )
    """)
    c.execute("""CREATE TABLE hwdata(
        userid TEXT,
        height INTEGER,
        weight INTEGER,
        dob TEXT,
        age INTEGER,
        CONSTRAINT fk_column
        FOREIGN KEY (userid)
        REFERENCES customerdata(userid)
    )""")
    c.execute("INSERT INTO customerdata VALUES ('U10000','Meet','Shingala','meet1762002@gmail.com','8758549035','M')")
    c.execute("INSERT or IGNORE INTO hwdata VALUES ('U10000','176','98','2002-06-17','20')")'''
    conn.commit()
except sqlite3.Error as error:
    print("Error while connecting to sqlite ", error)

window = tk.Tk()
bgimg = Image.open("Images/Background.jpg")
bgimg = ImageTk.PhotoImage(bgimg)
window.geometry('%dx%d' % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.state("zoomed")
window.title("Fitness Application")
bg = tk.Label(window, image=bgimg, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
bg.place(relx=0, rely=0)


# function for different buttons
def exit_app():
    window.destroy()


def newU_button_hover(e):
    Des.config(text="New User Menu")


def newU_button_hover_leave(e):
    Des.config(text="")


def AccD_button_hover(e):
    Des.config(text="Access Your Data")


def AccD_button_hover_leave(e):
    Des.config(text="")


def Exit_button_hover(e):
    Des.config(text="Exit The Application")


def Exit_button_hover_leave(e):
    Des.config(text="")


# logo
logo = Image.open("Images/Fitnesslogo.png")
logo = logo.resize((380, 380), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(window, image=logo)
logo_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Descriptive line
Des = tk.Label(window, text="", fg="#FFFFFF", font=("Helvetica", 30, "bold"), bg="#64023A")
Des.place(relx=0.5, rely=0.62, anchor=tk.CENTER)

# Exit Button
Exit = Image.open("Images/Exit.jpeg")
Exit = Exit.resize((270, 200), Image.LANCZOS)
Exit = ImageTk.PhotoImage(Exit)
Exitbutton = tk.Button(image=Exit, command=exit_app)
Exitbutton.place(relx=0.9, rely=0.8, anchor=tk.E)

# binding descriptive line to all the buttons
Exitbutton.bind("<Enter>", Exit_button_hover)
Exitbutton.bind("<Leave>", Exit_button_hover_leave)


def display_db():
    Update_Button.place_forget()
    Back_Button_toMain.place_forget()
    Display_Button.place_forget()
    label_uid.place(relx=0.1, rely=0.2)
    display_uid.place(relx=0.3, rely=0.2)
    fetch_data.place(relx=0.6, rely=0.2, height=40, width=100)

    label_bmi.place(relx=0.1, rely=0.3)
    display_bmi.place(relx=0.3, rely=0.3)

    label_bf.place(relx=0.1, rely=0.4)
    display_bf.place(relx=0.3, rely=0.4)

    label_lbm.place(relx=0.1, rely=0.5)
    display_lbm.place(relx=0.3, rely=0.5)

    label_tbw.place(relx=0.1, rely=0.6)
    display_tbw.place(relx=0.3, rely=0.6)

    Display_section_img_display.place(relx=0.5, rely=0.3)
    Back_Button_toMain.place(relx=0.02, rely=0.02, height=50, width=50)


# display function
def display():
    try:
        uid = display_uid.get()
        dv = (uid,)
        c.execute("SELECT height FROM hwdata NATURAL JOIN customerdata where customerdata.userid=?", dv)
        height = c.fetchone()
        c.execute("SELECT weight FROM hwdata NATURAL JOIN customerdata where userid=?", dv)
        weight = c.fetchone()
        BMI = weight[0] / (height[0] / 100) ** 2
        c.execute("SELECT gender FROM hwdata NATURAL JOIN customerdata where userid=?", dv)
        gender = c.fetchone()
        c.execute("SELECT age FROM hwdata NATURAL JOIN customerdata where userid=?", dv)
        age = c.fetchone()
        if gender == 'M':
            gender = 0
        else:
            gender = 1
        Body_fat = (0.503 * age[0]) + 10.689 * gender + 3.172 * BMI - (0.026 * BMI * 2) + (0.181 * BMI * gender) - (
                0.02 * BMI * age[0]) - (0.005 * BMI ** 2 * gender) + (0.00021 * BMI * 2 * age[0]) - 44.988
        LBM = 0.407 * weight[0] + 0.267 * height[0] - 19.2
        if gender == 'M':
            TBW = 2.447 - 0.09156 * age[0] + 0.1074 * height[0] + 0.3362 * weight[0]
        else:
            TBW = -2.097 + 0.1069 * height[0] + 0.2466 * weight[0]
        display_error_msg.place_forget()
        display_bmi.place_forget()
        display_bmi.config(text=BMI)
        display_bmi.place(relx=0.3, rely=0.3)
        display_bf.place_forget()
        display_bf.config(text=Body_fat)
        display_bf.place(relx=0.3, rely=0.4)
        display_lbm.place_forget()
        display_lbm.config(text=LBM)
        display_lbm.place(relx=0.3, rely=0.5)
        display_tbw.place_forget()
        display_tbw.config(text=TBW)
        display_tbw.place(relx=0.3, rely=0.6)
    except TypeError:
        display_error_msg.place(relx=0.7, rely=0.2)


def accDatabase():
    NewUserbutton.place_forget()
    AccDatabutton.place_forget()
    Exitbutton.place_forget()
    logo_label.place_forget()
    Update_Button.place(relx=0.35, rely=0.12)
    Back_Button_toMain.place(relx=0.02, rely=0.02, height=50, width=50)
    Display_Button.place(relx=0.35, rely=0.52)


def to_MainMenu():
    U_Id_input.place_forget()
    U_Id_input.delete(0, 'end')
    U_Id.place_forget()
    f_Name_input.place_forget()
    f_Name_input.delete(0, 'end')
    f_Name.place_forget()
    l_Name_input.place_forget()
    l_Name_input.place_forget()
    l_Name.place_forget()
    email_label.place_forget()
    email_input.place_forget()
    email_input.delete(0, 'end')
    PhNo.place_forget()
    PhNo_input.place_forget()
    PhNo_input.delete(0, 'end')
    Gender.place_forget()
    Gender_input.place_forget()
    Gender_input.delete(0, 'end')
    Info.place_forget()
    Next_Button.place_forget()
    Back_Button_toMain.place_forget()
    Update_Button.place_forget()
    label_uid.place_forget()
    label_bf.place_forget()
    label_bmi.place_forget()
    label_lbm.place_forget()
    label_tbw.place_forget()
    display_uid.place_forget()
    display_uid.config(text='UID')
    display_bmi.place_forget()
    display_bmi.config(text='BMI')
    display_bf.place_forget()
    display_bf.config(text='BF')
    display_lbm.place_forget()
    display_lbm.config(text='LBM')
    display_tbw.place_forget()
    display_tbw.config(text='TBW')
    Display_Button.place_forget()
    New_PhNo.place_forget()
    New_PhNo_input.place_forget()
    New_PhNo_input.delete(0, 'end')
    New_Weight.place_forget()
    New_Weight_input.place_forget()
    New_Weight_input.delete(0, 'end')
    New_Height.place_forget()
    New_Height_input.place_forget()
    New_Height_input.delete(0, 'end')
    Update_Button.place_forget()
    Display_Button.place_forget()
    Submit_Update.place_forget()
    New_User_form_img_display.place_forget()
    Update_section_img_display.place_forget()
    fetch_data.place_forget()
    UID_update.place_forget()
    UID_update_input.place_forget()
    display_error_msg.place_forget()
    UID_update_input.delete(0, 'end')
    User_Date_input.delete(0, 'end')
    User_Year_input.delete(0, 'end')
    User_Month_input.delete(0, 'end')
    User_Height_input.delete(0, 'end')
    User_Weight_input.delete(0, 'end')
    display_uid.delete(0, 'end')
    Display_section_img_display.place_forget()
    logo_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    Des.place(relx=0.5, rely=0.62, anchor=tk.CENTER)
    NewUserbutton.place(relx=0.1, rely=0.8, anchor=tk.W)
    AccDatabutton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    Exitbutton.place(relx=0.9, rely=0.8, anchor=tk.E)


def update_db_page():
    Update_Button.place_forget()
    Display_Button.place_forget()
    UID_update.place(relx=0.1, rely=0.25)
    UID_update_input.place(relx=0.35, rely=0.25, height=30, width=200)
    New_PhNo.place(relx=0.1, rely=0.35)
    New_PhNo_input.place(relx=0.35, rely=0.35, height=30, width=200)
    New_Height.place(relx=0.1, rely=0.45)
    New_Height_input.place(relx=0.35, rely=0.45, height=30, width=200)
    New_Weight.place(relx=0.1, rely=0.55)
    New_Weight_input.place(relx=0.35, rely=0.55, height=30, width=200)
    Submit_Update.place(relx=0.35, rely=0.65, height=40, width=200)
    Update_section_img_display.place(relx=0.55, rely=0.25)


# checks for numbers
def check_number(num):
    try:
        val = int(num)
    except ValueError:
        try:
            val = float(num)
        except ValueError:
            return False
    return True


def update_db():
    uid = UID_update_input.get()
    phonenum = New_PhNo_input.get()
    if check_number(phonenum):
        if len(phonenum) == 10:
            pvals = (phonenum, uid,)
            c.execute("UPDATE customerdata SET phonenum=? WHERE userid=?", pvals)
    weight = New_Weight_input.get()
    if check_number(weight):
        uvals = (weight, uid,)
        c.execute("Update hwdata SET weight=? where userid=?", uvals)
    height = New_Height_input.get()
    if check_number(height):
        hvals = (height, uid,)
        c.execute("Update hwdata SET height =? where userid=?", hvals)
    conn.commit()
    to_MainMenu()


def More_Info():
    Info.place_forget()
    U_Id.place_forget()
    U_Id_input.place_forget()
    f_Name.place_forget()
    f_Name_input.place_forget()
    l_Name.place_forget()
    l_Name_input.place_forget()
    email_label.place_forget()
    email_input.place_forget()
    PhNo.place_forget()
    PhNo_input.place_forget()
    Gender.place_forget()
    Gender_input.place_forget()
    Next_Button.place_forget()
    Back_Button_toMain.place_forget()
    info_submenu.place(relx=0.1, rely=0.1)
    User_Height.place(relx=0.1, rely=0.17)
    User_Height_input.place(relx=0.27, rely=0.17, height=30, width=200)
    User_Weight.place(relx=0.1, rely=0.24)
    User_Weight_input.place(relx=0.27, rely=0.24, height=30, width=200)
    User_Date.place(relx=0.1, rely=0.31)
    User_Date_input.place(relx=0.27, rely=0.31, height=30, width=200)
    User_Month.place(relx=0.1, rely=0.38)
    User_Month_input.place(relx=0.27, rely=0.38, height=30, width=200)
    User_Year.place(relx=0.1, rely=0.45)
    User_Year_input.place(relx=0.27, rely=0.45, height=30, width=200)
    Submit_Button.place(relx=0.27, rely=0.52, height=40, width=200)


def Submit_New_Data():
    User_Height.place_forget()
    User_Weight.place_forget()
    User_Date.place_forget()
    User_Month.place_forget()
    User_Year.place_forget()
    User_Height_input.place_forget()
    User_Weight_input.place_forget()
    User_Date_input.place_forget()
    User_Month_input.place_forget()
    User_Year_input.place_forget()
    Submit_Button.place_forget()
    info_submenu.place_forget()
    Back_Button_toMain.place_forget()
    New_User_form_img_display.place_forget()
    logo_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    Des.place(relx=0.5, rely=0.62, anchor=tk.CENTER)
    AccDatabutton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    Exitbutton.place(relx=0.9, rely=0.8, anchor=tk.E)
    NewUserbutton.place(relx=0.1, rely=0.8, anchor=tk.W)
    userid = U_Id_input.get()
    first_name = f_Name_input.get()
    last_name = l_Name_input.get()
    email = email_input.get()
    phone = PhNo_input.get()
    gender = Gender_input.get()
    newcustomer(userid, first_name, last_name, email, phone, gender)


# new customer
def dateselect(date):
    if date > 0 and date <= 9:
        str1 = "%02d" % date
        return str1
    else:
        return str(date)


def leapyear(Year):
    if (Year % 400 == 0 or Year % 100 != 0) and (Year % 4 == 0):
        return True
    else:
        return False


def datevalidate(date, month, year):
    if date == 29 and month == 2 and leapyear(year):
        return True
    elif date <= 28 and month == 2:
        return True
    elif date <= 30 and (month in [4, 6, 9, 11]):
        return True
    elif date <= 31 and (month in [1, 3, 5, 7, 8, 10, 12]):
        return True
    else:
        return False


def monthvalidate(month):
    if (month > 12 and month <= 0):
        return False
    else:
        return True


def monthselect(month):
    if 12 < month <= 0:
        return
    elif month == 12:
        return "12"
    elif month == 11:
        return "11"
    elif month == 10:
        return "10"
    elif month == 9:
        str = "%2d" % month
        return str
    elif month == 8:
        str = "%2d" % month
        return str
    elif month == 7:
        str = "%2d" % month
        return str
    elif month == 6:
        str = "%2d" % month
        return str
    elif month == 5:
        str = "%2d" % month
        return str
    elif month == 4:
        str = "%2d" % month
        return str
    elif month == 3:
        str = "%2d" % month
        return str
    elif month == 2:
        str = "%2d" % month
        return str
    else:
        str = "%2d" % month
        return str


# This function creates a new row/entry in our table of a new customer
def newcustomer(uid, first_name, last_name, email, phone, gender):
    weight = int(User_Weight_input.get())
    height = int(User_Height_input.get())
    date1 = int(User_Date_input.get())
    month = int(User_Month_input.get())
    year = int(User_Year_input.get())
    age = calculateAge(int(year), int(month), int(date1))
    date = int(dateselect(date1))
    month = int(monthselect(month))
    final_date = str(year) + "-" + str(month) + "-" + str(date)
    if ((len(email) - 10)) != "@gmail.com" and (len(first_name) >= 2 and len(first_name) <= 40) and (
            len(last_name) >= 2 and len(last_name) <= 40 and len(phone) == 10 and (
            gender == 'M' or gender == 'F' or gender == 'O')) and uid[0]=="U":
        try:
            values = (uid, first_name, last_name, email, phone, gender)
            c.execute("INSERT INTO customerdata VALUES (?,?,?,?,?,?)", values)
            conn.commit()
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
    else:
        to_MainMenu()
    if 2012 > year > 1900 and datevalidate(date, month, year) == True and monthvalidate(month) == True:
        try:
            Values = (uid, str(height), str(weight), final_date, str(age))
            c.execute("INSERT INTO 'hwdata' VALUES (?,?,?,?,?)", Values)
            conn.commit()
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        else:
            print("New Customer Data Administered!")


def calculateAge(year, month, date1):
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, date1))
    return age


# all the buttons
Update_section_img = Image.open("Images/Update_form.jpg")
Update_section_img = Update_section_img.resize((520, 280))
Update_section_img = ImageTk.PhotoImage(Update_section_img)
Update_section_img_display = tk.Label(image=Update_section_img)
Display_section_img = Image.open("Images/Display_form.jpg")
Display_section_img = Display_section_img.resize((520, 280))
Display_section_img = ImageTk.PhotoImage(Display_section_img)
Display_section_img_display = tk.Label(image=Display_section_img)
New_User_form_img = Image.open("Images/New_User_Form.jpg")
New_User_form_img = New_User_form_img.resize((500, 350))
New_User_form_img = ImageTk.PhotoImage(New_User_form_img)
New_User_form_img_display = tk.Label(image=New_User_form_img)
Update = Image.open("Images/update.webp")
Update = Update.resize((450, 250))
Update = ImageTk.PhotoImage(Update)
Update_Button = tk.Button(image=Update, command=update_db_page, anchor=tk.CENTER)
Display = Image.open("Images/display.jpg")
Display = Display.resize((450, 250))
Display = ImageTk.PhotoImage(Display)
Display_Button = tk.Button(image=Display, command=display_db, anchor=tk.CENTER)
Info = tk.Label(window, text="New User Form", fg="#FFFFFF", font=("Helvetica", 30, "bold"), bg="#251B3E")
U_Id = tk.Label(window, text="User ID:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#251B3E")
U_Id_input = tk.Entry(window, fg="#6ED3FF", bg="#A8FF85", font=("Helvetica", 16, "bold"))
f_Name = tk.Label(window, text="First Name:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#251B3E")
f_Name_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
l_Name = tk.Label(window, text="Last Name:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#251B3E")
l_Name_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
email_label = tk.Label(window, text="Email:", fg="#6ED3FF", bg="#251B3E", font=("Helvetica", 20, "bold"))
email_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
email_input.insert(0, "G-Mail Only")
PhNo = tk.Label(window, text="Phone Number:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#251B3E")
PhNo_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
Gender = tk.Label(window, text="Gender:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#251B3E")
Gender_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
Next_Button = tk.Button(window, text="Next", fg="#FFFFFF", bg="#A8FF85", font=("Helvetica", 25, "bold"),
                        command=More_Info)
Back_Button_toMain = tk.Button(window, text="<--", fg="#FFFFFF", bg="#191234", font=("Helvetica", 20, "bold"),
                               command=to_MainMenu)
info_submenu = tk.Label(window, text="Enter:", fg="#5DFF00", font=("Helvetica", 25, "bold"), bg="#201639")
User_Weight = tk.Label(window, text="Weight (in kg):", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#201639")
User_Height_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
User_Height = tk.Label(window, text="Height (in cm):", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#201639")
User_Weight_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
User_Date = tk.Label(window, text="Date of Birth:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#201639")
User_Date_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
User_Month = tk.Label(window, text="Month of Birth:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#201639")
User_Month_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
User_Year = tk.Label(window, text="Year of Birth:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#201639")
User_Year_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
Submit_Button = tk.Button(window, text="Submit", fg="#6ED3FF", bg="#A8FF85", font=("Helvetica", 25, "bold"),
                          command=Submit_New_Data)

# in display function
label_uid = tk.Label(window, text="User Id ", font=("helvetica", 20, "bold"), fg="#6ED3FF", bg="#251B3E")
display_uid = tk.Entry(window, font=("helvetica", 20), fg="#6ED3FF", bg="#A8FF85")
fetch_data = tk.Button(window, text="Fetch", font=("helvetica", 20, 'bold'), fg="#FFFFFF", bg="#A8FF85",
                       command=display)
label_bmi = tk.Label(window, text="BMI:", font=("helvetica", 20, "bold"), fg="#6ED3FF", bg="#352E4F")
display_bmi = tk.Label(window, text="BMI", font=("helvetica", 20), fg="#6ED3FF", bg="#352E4F")
label_bf = tk.Label(window, text="Body Fat %:", font=("helvetica", 20, "bold"), fg="#6ED3FF", bg="#352E4F")
display_bf = tk.Label(window, text="Body_fat", font=("helvetica", 20), fg="#6ED3FF", bg="#352E4F")
label_lbm = tk.Label(window, text="Lean Body Mass:", font=("helvetica", 20, "bold"), fg="#6ED3FF", bg="#352E4F")
display_lbm = tk.Label(window, text="LBM", font=("helvetica", 20), fg="#6ED3FF", bg="#352E4F")
label_tbw = tk.Label(window, text="Body Water:", font=("helvetica", 20, "bold"), fg="#6ED3FF", bg="#352E4F")
display_tbw = tk.Label(window, text="TBW", font=("helvetica", 20), fg="#6ED3FF", bg="#352E4F")
display_error_msg = tk.Label(window, text="No such entry found", font=("helvetica", 20, 'bold'), fg="#6ED3FF", bg="#352E4F")
# in update database
UID_update = tk.Label(window, text="User Id ", font=("helvetica", 20, "bold"), fg="#6ED3FF", bg="#271D40")
UID_update_input = tk.Entry(window, font=("Helvetica", 16, "bold"), fg="#6ED3FF", bg="#A8FF85")
New_PhNo = tk.Label(window, text="New Phone Number:", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#271D40")
New_PhNo_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
New_Height = tk.Label(window, text="Height (in cm):", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#271D40")
New_Height_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
New_Weight = tk.Label(window, text="Weight (in kg):", fg="#6ED3FF", font=("Helvetica", 20, "bold"), bg="#271D40")
New_Weight_input = tk.Entry(window, fg="#6ED3FF", font=("Helvetica", 16, "bold"))
Submit_Update = tk.Button(window, text="Update", fg="#FFFFFF", bg="#A8FF85", font=("Helvetica", 22, "bold"),
                          command=update_db)


def NewUserMenu():
    NewUserbutton.place_forget()
    AccDatabutton.place_forget()
    Exitbutton.place_forget()
    logo_label.place_forget()
    Info.place(relx=0.1, rely=0.1)
    U_Id.place(relx=0.1, rely=0.2)
    U_Id_input.place(relx=0.27, rely=0.2, height=30, width=200)

    New_User_form_img_display.place(relx=0.5, rely=0.2)

    f_Name.place(relx=0.1, rely=0.27)
    f_Name_input.place(relx=0.27, rely=0.27, height=30, width=200)

    l_Name.place(relx=0.1, rely=0.35)
    l_Name_input.place(relx=0.27, rely=0.35, height=35, width=200)

    email_label.place(relx=0.1, rely=0.42)
    email_input.place(relx=0.27, rely=0.42, height=30, width=200)

    PhNo.place(relx=0.1, rely=0.49)
    PhNo_input.place(relx=0.27, rely=0.49, height=30, width=200)

    Gender.place(relx=0.1, rely=0.56)
    Gender_input.place(relx=0.27, rely=0.56, height=30, width=200)

    Next_Button.place(relx=0.27, rely=0.63, height=40, width=200)
    Back_Button_toMain.place(relx=0.02, rely=0.02, height=50, width=50)


# New user button
NewUser = Image.open("Images/NewUser.png")
NewUser = NewUser.resize((250, 200), Image.LANCZOS)
NewUser = ImageTk.PhotoImage(NewUser)
NewUserbutton = tk.Button(window, image=NewUser, command=NewUserMenu)
NewUserbutton.place(relx=0.1, rely=0.8, anchor=tk.W)
# binding descriptive line to all the buttons
NewUserbutton.bind("<Enter>", newU_button_hover)
NewUserbutton.bind("<Leave>", newU_button_hover_leave)

# Access database button
AccData = Image.open("Images/Accessdata.jpeg")
AccData = AccData.resize((315, 200), Image.LANCZOS)
AccData = ImageTk.PhotoImage(AccData)
AccDatabutton = tk.Button(image=AccData, borderwidth=0, command=accDatabase)
AccDatabutton.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
# binding descriptive line to all the buttons
AccDatabutton.bind("<Enter>", AccD_button_hover)
AccDatabutton.bind("<Leave>", AccD_button_hover_leave)

window.mainloop()