#-------------importing modules here-------------------------#
import email
from email.mime import text
from tkinter import *
from tkinter import messagebox
import os
from tkinter import font
import tkinter.messagebox as tmsg
from tkinter import PhotoImage
from types import TracebackType
import pywhatkit
from user_details import *
from back import *
from bicep import *
from chest import *
from legs import *
from shoulders import *
from triceps import *
from tkinter import ttk
from PIL import ImageTk,Image
from server import *
import pyttsx3
import speech_recognition as sr
import time
import playsound as pl
#--------------------------------------------------------------------------------------------------
#workout planner speech
listener=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',145)
def talk(text):
    engine.say(text)
    engine.runAndWait()
#defining all list here
muscle_groups_list=['Chest','Back','Biceps','Shoulders','Triceps','Legs']

food_and_nutrients_list=['Protien',
'Carbohydrates','Good Fats']

protien_foods=['Eggs','Greek Yogurt','Chicken Breast','Almonds','Oats','Milk','Whey Protien','Pumpkin Seeds','Fish (all types)','Peanuts','SoyaBean','Cottage Cheese','Meat','Shrimps']

carb_foods=['Sweet Potatoes','Brown Rice','White Bread','Potatoes','Pasta','Cereals']

good_fats=['Avocado','Nuts','Dryfruits','Fish Oil (supplement)','Dark Choclate','Chia Seeds','Tofu']
#-----------------------------------------------------------------------------------------  

def temp_windows():
#window starts here
    temp_window=Tk()
    temp_window.iconbitmap('icon.ico')
    screen_width=temp_window.winfo_screenwidth()
    screen_height=temp_window.winfo_screenheight()
    app_width=480
    app_height=190
    x=(screen_width/2)-(app_width/2)
    y=(screen_height/2)-(app_height/2)
    temp_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    temp_window.config(bg='#141414')
    temp_window.title('Information Processing')
#progress bar function here
    def start_progress_bar():
        for x in range(200):
            prb['value']+=0.5
            temp_window.update_idletasks()
            time.sleep(0.01)
#labels here
    label1=Label(temp_window,text='',bg='#141414',fg='white')
    label1.pack(pady=50)
    update_label=Label(temp_window,text='',bg='#141414',fg='white')
    update_label.pack()
#making progress bar here
    prb=ttk.Progressbar(temp_window,orient=HORIZONTAL,length=300,mode='determinate')
    prb.pack()
#defining updates here
    def update1():
        label1.config(text='Please wait while we process your information')
        temp_window.update_idletasks()
    def update2():
        label1.config(text='Creating Directories on your PC',font=4)
    def update3():
        update_label.config(text='Shortlisting perfect excersises for you',font=1)
    def update4():
        temp_window.destroy()
        chestdisplay_window()

    temp_window.after(10,update1)
    temp_window.after(100,send_email)
    temp_window.after(2600,update2)
    temp_window.after(4600,update3)
    temp_window.after(5000,start_progress_bar)
    temp_window.after(5500,update4)

    temp_window.mainloop()

def previous_plan_window():
#window starts here
    root=Tk()
    root.iconbitmap('icon.ico')
    root.title('Enter your current schedule')
    width=530
    height=400
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    root.maxsize(530,400)
    root.config(bg='black')
    font='ubuntulight 17 bold'
    padx=20
    pady=5
#defining lables here
    heading=Frame(root,bg='black').grid()
    hello_user=Label(heading,text=f'Hello {nameentry.get()}',font='helvetica 20 bold',bg='black',fg='white',padx=-10,pady=pady)
    hello_user.grid(column=2)
    monday_label=Label(root,text='Monday',font=font,bg='black',fg='white',padx=padx,pady=pady)
    monday_label.grid(row=4,column=1)
    tuesday_label=Label(root,text='Tuesday',font=font,bg='black',padx=padx,pady=pady,fg='white')
    tuesday_label.grid(row=5,column=1)
    wednesday_label=Label(root,text='Wednesday',font=font,bg='black',padx=padx,pady=pady,fg='white')
    wednesday_label.grid(row=6,column=1)
    thursday_label=Label(root,text='Thursday',font=font,bg='black',padx=padx,pady=pady,fg='white')
    thursday_label.grid(row=7,column=1)
    friday_label=Label(root,text='Friday',font=font,bg='black',padx=padx,pady=pady,fg='white')
    friday_label.grid(row=8,column=1)
    saturday_label=Label(root,text='Saturday',font=font,bg='black',padx=padx,pady=pady,fg='white')
    saturday_label.grid(row=9,column=1)
#defiing hoverovers for hello user label here
    if gender_info.get()==0:
        def hover10(e):
            hello_user.config(fg='#31c4ce')
        def over10(e):
            hello_user.config(fg='white')
    elif gender_info.get()==1:
        def hover10(e):
            hello_user.config(fg='Pink')
        def over10(e):
            hello_user.config(fg='white')
#binding hello user label here
    hello_user.bind('<Enter>',hover10)
    hello_user.bind('<Leave>',over10)
#making string variables here
    monday=StringVar()
    tuesday=StringVar()
    wednesday=StringVar()
    thursday=StringVar()
    friday=StringVar()
    saturday=StringVar() 
#defining hoverups for labels  here
    label_fg='#f29300'
    def hoverup(e):
        monday_label.config(fg=label_fg)
    def leave(e):
        monday_label.config(fg='white')
    def hoverup1(e):
        tuesday_label.config(fg=label_fg)
    def leave1(e):
        tuesday_label.config(fg='white')
    def hoverup2(e):
        wednesday_label.config(fg=label_fg)
    def leave2(e):
        wednesday_label.config(fg='white')
    def hoverup3(e):
        thursday_label.config(fg=label_fg)
    def leave3(e):
        thursday_label.config(fg='white')
    def hoverup4(e):
        friday_label.config(fg=label_fg)
    def leave4(e):
        friday_label.config(fg='white')
    def hoverup5(e):
        saturday_label.config(fg=label_fg)
    def leave5(e):
        saturday_label.config(fg='white')
#binding the labels here
    monday_label.bind('<Enter>',hoverup)
    monday_label.bind('<Leave>',leave)
    tuesday_label.bind('<Enter>',hoverup1)
    tuesday_label.bind('<Leave>',leave1)
    wednesday_label.bind('<Enter>',hoverup2)
    wednesday_label.bind('<Leave>',leave2)
    thursday_label.bind('<Enter>',hoverup3)
    thursday_label.bind('<Leave>',leave3)
    friday_label.bind('<Enter>',hoverup4)
    friday_label.bind('<Leave>',leave4)
    saturday_label.bind('<Enter>',hoverup5)
    saturday_label.bind('<Leave>',leave5)
#defining submit button here
    def submit1():
        if monday.get()=='' or tuesday.get=='' or wednesday.get()=='' or thursday.get()=='' or friday.get()=='' or saturday.get()=='':
            tmsg.showinfo('Information','Please enter all the details')
            
        elif monday.get()!='' and tuesday.get!='' and wednesday.get()!='' and thursday.get()!='' and friday.get()!='' and saturday.get()!='':
            workout_schedule={'monday':monday.get(),'tuesday':tuesday.get(),'wednesday':wednesday.get(),'thursday':thursday.get(),'friday':friday.get(),'saturday':saturday.get()}
            with open('user_plan.py','w') as f:
                f.write(f'workout_schedule={workout_schedule}')
            root.destroy()
            temp_windows()
#making entry widgets here
    monday_entry=Entry(root,textvariable=monday,font=font)
    monday_entry.grid(row=4,column=2)
    tuesday_entry=Entry(root,textvariable=tuesday,font=font)
    tuesday_entry.grid(row=5,column=2)
    wednesday_entry=Entry(root,textvariable=wednesday,font=font)
    wednesday_entry.grid(row=6,column=2)
    thursday_entry=Entry(root,textvariable=thursday,font=font)
    thursday_entry.grid(row=7,column=2)
    friday_entry=Entry(root,textvariable=friday,font=font)
    friday_entry.grid(row=8,column=2)
    saturday_entry=Entry(root,textvariable=saturday,font=font)
    saturday_entry.grid(row=9,column=2)
#defining hover overs for submit button here
    def submit_hover(e):
        submit_button.config(bg='black',fg='#f29300')
    def submit_over(e):
        submit_button.config(bg='black',fg='white')
#making submit button here
    submit_button=Button(text='Submit',font='comicsans 10 bold',borderwidth=5,bg='black',fg='white',relief=SUNKEN,bd=4,command=submit1,padx=15,pady=3)
    submit_button.grid(row=10,column=2)
#binding submit button here    
    submit_button.bind('<Enter>',submit_hover)
    submit_button.bind('<Leave>',submit_over)
#defining hoverups for entry widgets here
    entry_bg='#999997'
    def hover(e):
        monday_entry.config(bg=entry_bg)
    def over(e):
        monday_entry.config(bg='white')
    def hover1(e):
        tuesday_entry.config(bg=entry_bg)
    def over1(e):
        tuesday_entry.config(bg='white')
    def hover2(e):
        wednesday_entry.config(bg=entry_bg)
    def over2(e):
        wednesday_entry.config(bg='white')
    def hover3(e):
        thursday_entry.config(bg=entry_bg)
    def over3(e):
        thursday_entry.config(bg='white')
    def hover4(e):
        friday_entry.config(bg=entry_bg)
    def over4(e):
        friday_entry.config(bg='white')
    def hover5(e):
        saturday_entry.config(bg=entry_bg)
    def over5(e):
        saturday_entry.config(bg='white')
#binding the entry widgets here
    monday_entry.bind('<Enter>',hover)
    monday_entry.bind('<Leave>',over)
    tuesday_entry.bind('<Enter>',hover1)
    tuesday_entry.bind('<Leave>',over1)
    wednesday_entry.bind('<Enter>',hover2)
    wednesday_entry.bind('<Leave>',over2)
    thursday_entry.bind('<Enter>',hover3)
    thursday_entry.bind('<Leave>',over3)
    friday_entry.bind('<Enter>',hover4)
    friday_entry.bind('<Leave>',over4)
    saturday_entry.bind('<Enter>',hover5)
    saturday_entry.bind('<Leave>',over5)
    root.mainloop()

def newuser_window():
    global nameentry,gender_info
    start=Tk()
    width=600
    height=460
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    start.iconbitmap('icon.ico')
#making stringvars here
    nameentry=StringVar()
    ageentry=StringVar()
    contactentry=StringVar()
    weightentry=StringVar()
    heightentry=StringVar()
    emailentry=StringVar()
    gender_info=IntVar()
    gender_info.set(2)
    user_gender=StringVar()
#defining submit button here
    def userdetails_submit():
        if nameentry.get()=='':
            tmsg.showwarning('Warning','please enter all the details')
        elif ageentry.get()=='':
            tmsg.showwarning('Warning','please enter all the details')
        elif contactentry.get()=='':
            tmsg.showwarning('Warning','please enter all the details')
        elif weightentry.get()=='':
            tmsg.showwarning('Warning','please enter all the details')
        elif heightentry.get()=='':
            tmsg.showwarning('Warning','please enter all the details')
        elif emailentry.get()=='':
            tmsg.showwarning('Warning','please enter all the details')
        elif gender_info.get()==2:
            tmsg.showwarning('Warning','please enter all the details')

        elif nameentry.get()!='' and ageentry.get()!='' and contactentry.get()!='' and weightentry.get()!='' and heightentry.get()!=0 and emailentry.get()!=0 and gender_info.get()!=2:
            if gender_info.get()==0:
                user_gender.set('Male')
            elif gender_info.get()==1:
                user_gender.set('Female')

            user_details={'Username':nameentry.get(),'Age':ageentry.get(),'Contact':contactentry.get(),'Weight':weightentry.get(),'Height':heightentry.get(),'E-Mail':emailentry.get(),'Gender':user_gender.get()}
            
            with open('user_details.py','w') as f:    
                f.write(f'user_details={user_details}')
            with open('user_details.py','r') as s:
                detail=s.read()
            with open('user_details.txt','w') as g:
                g.write(detail)
            start.destroy()
            previous_plan_window() 
#window starts here
    start.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    start.title('Fill the form to continue')
    start.config(bg='black')
    pady=10
    padx=20
    font='ubuntulight 17 bold'
    name_label=Label(start,text='Name',font=font,fg='white',bg='black',pady=pady,padx=padx)
    name_label.grid(row=1,column=0)
    age_label=Label(start,text='Age',font=font,fg='white',bg='black',pady=pady,padx=padx)
    age_label.grid(row=2,column=0)
    contact_number=Label(start,text='Contact Number',font=font,fg='white',bg='black',pady=pady,padx=padx)
    contact_number.grid(row=3,column=0)
    weight_label=Label(start,text='Weight',font=font,fg='white',bg='black',pady=pady,padx=padx)
    weight_label.grid(row=4,column=0)
    height_label=Label(start,text='Height',font=font,fg='white',bg='black',pady=pady,padx=padx)
    height_label.grid(row=5,column=0)
    Email_label=Label(start,text='E-Mail',font=font,fg='white',bg='black',pady=pady,padx=padx)
    Email_label.grid(row=6,column=0)
    gender_label=Label(start,text='Gender',font=font,fg='white',bg='black',pady=pady,padx=padx)
    gender_label.grid(row=7,column=0)
    label_fg='#f29300' 
#hoverups for labels
    def hoverup(e):
        name_label.config(fg=label_fg)
    def leave(e):
        name_label.config(fg='white')
    def hoverup1(e):
        age_label.config(fg=label_fg)
    def leave1(e):
        age_label.config(fg='white')
    def hoverup2(e):
        contact_number.config(fg=label_fg)
    def leave2(e):
        contact_number.config(fg='white')
    def hoverup3(e):
        weight_label.config(fg=label_fg)
    def leave3(e):
        weight_label.config(fg='white')
    def hoverup4(e):
        height_label.config(fg=label_fg)
    def leave4(e):
        height_label.config(fg='white')
    def hoverup5(e):
        Email_label.config(fg=label_fg)
    def leave5(e):
        Email_label.config(fg='white')
    def hoverup6(e):
        gender_label.config(fg=label_fg)
    def leave6(e):
        gender_label.config(fg='white')
#binding labels here
    name_label.bind('<Enter>',hoverup)
    name_label.bind('<Leave>',leave)
    age_label.bind('<Enter>',hoverup1)
    age_label.bind('<Leave>',leave1)
    contact_number.bind('<Enter>',hoverup2)
    contact_number.bind('<Leave>',leave2)
    weight_label.bind('<Enter>',hoverup3)
    weight_label.bind('<Leave>',leave3)
    height_label.bind('<Enter>',hoverup4)
    height_label.bind('<Leave>',leave4)
    Email_label.bind('<Enter>',hoverup5)
    Email_label.bind('<Leave>',leave5)
    gender_label.bind('<Enter>',hoverup6)
    gender_label.bind('<Leave>',leave6)
#defining entry wwidgets here
    name_entry=Entry(start,textvariable=nameentry,font=font)
    name_entry.grid(row=1,column=1)
    age_entry=Entry(start,textvariable=ageentry,font=font,)
    age_entry.grid(row=2,column=1)
    contact_entry=Entry(start,textvariable=contactentry,font=font,)
    contact_entry.grid(row=3,column=1)
    weight_entry=Entry(start,textvariable=weightentry,font=font,)
    weight_entry.grid(row=4,column=1)
    height_entry=Entry(start,textvariable=heightentry,font=font,)
    height_entry.grid(row=5,column=1)
    email_entry=Entry(start,textvariable=emailentry,font=font,)
    email_entry.grid(row=6,column=1)
#defining hoverups for radio buttons here
    def male_hoverup(e):
        male.config(bg='#31c4ce',fg='white')
    def male_hoverup_leave(e):
        male.config(bg='black',fg='#31c4ce')
    def female_hoverup(e):
        female.config(bg='pink',fg='white')
    def female_hoverup_leave(e):
        female.config(bg='black',fg='pink')
#defining entry widgets hovers here:
    entry_bg='#999997'
    def hover(e):
        name_entry.config(bg=entry_bg)
    def over(e):
        name_entry.config(bg='white')
    def hover1(e):
        age_entry.config(bg=entry_bg)
    def over1(e):
        age_entry.config(bg='white')
    def hover2(e):
        contact_entry.config(bg=entry_bg)
    def over2(e):
        contact_entry.config(bg='white')
    def hover3(e):
        weight_entry.config(bg=entry_bg)
    def over3(e):
        weight_entry.config(bg='white')
    def hover4(e):
        height_entry.config(bg=entry_bg)
    def over4(e):
        height_entry.config(bg='white')
    def hover5(e):
        email_entry.config(bg=entry_bg)
    def over5(e):
        email_entry.config(bg='white')
#binding entry widgets here
    name_entry.bind('<Enter>',hover)
    name_entry.bind('<Leave>',over)
    age_entry.bind('<Enter>',hover1)
    age_entry.bind('<Leave>',over1)
    contact_entry.bind('<Enter>',hover2)
    contact_entry.bind('<Leave>',over2)
    weight_entry.bind('<Enter>',hover3)
    weight_entry.bind('<Leave>',over3)
    height_entry.bind('<Enter>',hover4)
    height_entry.bind('<Leave>',over4)
    email_entry.bind('<Enter>',hover5)
    email_entry.bind('<Leave>',over5)
#making radio buttons here
    male=Radiobutton(start,text='Male',variable=gender_info,value=0,padx=20,font=3,pady=-1,bg='black',fg='#31c4ce')
    male.grid(row=7,column=1)
    female=Radiobutton(start,text='Female',variable=gender_info,value=1,padx=10,font=3,pady=-1,bg='black',fg='pink')
    female.grid(row=8,column=1)
#binding radio buttons here
    male.bind('<Enter>',male_hoverup)
    female.bind('<Enter>',female_hoverup)
    male.bind('<Leave>',male_hoverup_leave)
    female.bind('<Leave>',female_hoverup_leave)  
#making submit button here
    submit_Button=Button(start,text='Submit',font='comicsans 10 bold',bg='black',fg='white',command=userdetails_submit,padx=15,pady=1,relief=SUNKEN,bd=4)
    submit_Button.grid(row=10,column=2)    
#defininig hoverup for submit button here
    def submit_hover(e):
        submit_Button.config(bg='black',fg='#f29300')
    def submit_over(e):
        submit_Button.config(bg='black',fg='white')
#binding submit button here 
    submit_Button.bind('<Enter>',submit_hover)
    submit_Button.bind('<Leave>',submit_over)
    start.mainloop()

def chestdisplay_window():
#chest submit button function
    def chest_submit():
        workout_chest_dict={'Barbell Bench Press':Barbell_bench_press.get(),'Barbell Incline Press':barbell_incline_press.get(),'Barbell decline press':barbell_decline_press.get(),'Dumbell Bench Press': dumbell_bench_press.get(),'Incline Dumbell Press':incline_dumbell_press.get(),'Decline Dumbell Press':decline_dumble_press.get(),'Cable Crossover':cable_crossover.get(),'Low cable crossover':low_cable_crossover.get(),'Dumbell Fly':dumbell_fly.get(),'Dumbell Pullover':dumbell_pull_over.get(),'Pushups':pushups.get(),'Narrow grip pushups':narrow_grip_pushups.get(),'Wide Grip Pushups':wide_grip_pushups.get(),'Dips':Dips.get()}
        
        with open('chest.py','w') as f:
            f.write(f'workout_chest_dict={workout_chest_dict}')
        chest.destroy()
        backdisplay_windows()
#chest windows here----------------------------------------------------
    chest=Tk()
    chest.iconbitmap('icon.ico')
    chest.title('Select the excersies')
    width=400
    height=650
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    chest.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    chest.maxsize(400,650)
    chest.config(bg='#141414')
#making chest label here   
    Label(chest,text='CHEST',font='comicsans 25 bold',pady=10,padx=130,bg='#141414',fg='white',relief=RIDGE,bd=2).pack(anchor=CENTER,pady=12)
#making second frame here
    second_framE=Frame(chest,bg='#141414')
    second_framE.pack(fill='x')
#chest submit button here
    submit_chest=Button(chest,text='Submit',command=chest_submit,font='Comicsans 12 bold',relief=SUNKEN,bd=4,bg='#141414',fg='white',padx=40,activebackground='#ffcc66',activeforeground='#141414')
    submit_chest.pack(anchor=CENTER,fill='x',pady=5)
#defining hoverups for submit button here
    def hover_submit(e):
        submit_chest.config(fg='#ffcc66')
    def over_submit(e):
        submit_chest.config(fg='white')
#binding submit button here
    submit_chest.bind('<Enter>',hover_submit)
    submit_chest.bind('<Leave>',over_submit)
#attributes of check buttons
    font_style='regular 16'
    bgcolor= '#141414'
    fgcolor=  '#ffcc66'          
#chest variables here    
    Barbell_bench_press=IntVar()
    barbell_incline_press=IntVar()
    barbell_decline_press=IntVar()
    dumbell_bench_press=IntVar()
    incline_dumbell_press=IntVar()
    decline_dumble_press=IntVar()
    cable_crossover=IntVar()
    low_cable_crossover=IntVar()
    dumbell_fly=IntVar()
    dumbell_pull_over=IntVar()
    pushups=IntVar()
    narrow_grip_pushups=IntVar()
    wide_grip_pushups=IntVar()
    Dips=IntVar()
#chest checkbuttons here:
    one=Checkbutton(second_framE,text='Barbell Bench Press',font=font_style,variable=Barbell_bench_press,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    one.pack(anchor=CENTER,fill='x')
    two=Checkbutton(second_framE,text='Barbell Incline Press',font=font_style,variable=barbell_incline_press,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    two.pack(anchor=CENTER,fill='x')
    three=Checkbutton(second_framE,text='Barbell Decline Press',variable=barbell_decline_press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    three.pack(anchor=CENTER,fill='x')
    four=Checkbutton(second_framE,text='Dumbell Bench Press',variable=dumbell_bench_press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    four.pack(anchor=CENTER,fill='x')
    five=Checkbutton(second_framE,text='Incline Dumbell Press',variable=incline_dumbell_press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    five.pack(anchor=CENTER,fill='x')
    six=Checkbutton(second_framE,text='Decline Dumbell Press',variable=decline_dumble_press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    six.pack(anchor=CENTER,fill='x')
    seven=Checkbutton(second_framE,text='Cable Crossover',variable=cable_crossover,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    seven.pack(anchor=CENTER,fill='x')
    eight=Checkbutton(second_framE,text='Low Cable Crossover',variable=low_cable_crossover,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eight.pack(anchor=CENTER,fill='x')
    nine=Checkbutton(second_framE,text='Dumbell Fly',variable=dumbell_fly,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    nine.pack(anchor=CENTER,fill='x')
    ten=Checkbutton(second_framE,text='Dumbell Pull Over',variable=dumbell_pull_over,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    ten.pack(anchor=CENTER,fill='x')
    eleven=Checkbutton(second_framE,text='Pushups',variable=pushups,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eleven.pack(anchor=CENTER,fill='x')
    twelve=Checkbutton(second_framE,text='Narrow Grip Pushups',variable=narrow_grip_pushups,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    twelve.pack(anchor=CENTER,fill='x')
    thirteen=Checkbutton(second_framE,text='Wide Grip Pushups',variable=wide_grip_pushups,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    thirteen.pack(anchor=CENTER,fill='x')
    fourteen=Checkbutton(second_framE,text='Dips',variable=Dips,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    fourteen.pack(anchor=CENTER,fill='x')
#defining hoverups here:
    fg='#ffcc66'
    bg='#141414'
    hover_font='regular 19 '
    over_font='regular 16 '
    def one_hover(e):
        one.config(fg=bg,font=hover_font,bg=fg)
    def one_over(e):
        one.config(fg=fg,bg=bg,font=over_font)
    def two_hover(e):
        two.config(fg=bg,font=hover_font,bg=fg)
    def two_over(e):
        two.config(fg=fg,bg=bg,font=over_font)
    def three_hover(e):
        three.config(fg=bg,font=hover_font,bg=fg)
    def three_over(e):
        three.config(fg=fg,bg=bg,font=over_font)   
    def four_hover(e):
        four.config(fg=bg,font=hover_font,bg=fg)
    def four_over(e):
        four.config(fg=fg,bg=bg,font=over_font)
    def five_hover(e):
        five.config(fg=bg,font=hover_font,bg=fg)
    def five_over(e):
        five.config(fg=fg,bg=bg,font=over_font)
    def six_hover(e):
        six.config(fg=bg,font=hover_font,bg=fg)
    def six_over(e):
        six.config(fg=fg,bg=bg,font=over_font)
    def seven_hover(e):
        seven.config(fg=bg,font=hover_font,bg=fg)
    def seven_over(e):
        seven.config(fg=fg,bg=bg,font=over_font)
    def eight_hover(e):
        eight.config(fg=bg,font=hover_font,bg=fg)
    def eight_over(e):
        eight.config(fg=fg,bg=bg,font=over_font)
    def nine_hover(e):
        nine.config(fg=bg,font=hover_font,bg=fg)
    def nine_over(e):
        nine.config(fg=fg,bg=bg,font=over_font)
    def ten_hover(e):
        ten.config(fg=bg,font=hover_font,bg=fg)
    def ten_over(e):
        ten.config(fg=fg,bg=bg,font=over_font)
    def eleven_hover(e):
        eleven.config(fg=bg,font=hover_font,bg=fg)
    def eleven_over(e):
        eleven.config(fg=fg,bg=bg,font=over_font)
    def twelve_hover(e):
        twelve.config(fg=bg,font=hover_font,bg=fg)
    def twelve_over(e):
        twelve.config(fg=fg,bg=bg,font=over_font)
    def thirteen_hover(e):
        thirteen.config(fg=bg,font=hover_font,bg=fg)
    def thirteen_over(e):
        thirteen.config(fg=fg,bg=bg,font=over_font)
    def fourteen_hover(e):
        fourteen.config(fg=bg,font=hover_font,bg=fg)
    def fourteen_over(e):
        fourteen.config(fg=fg,bg=bg,font=over_font)
#binding checkbuttons here
    one.bind('<Enter>',one_hover)
    one.bind('<Leave>',one_over)
    two.bind('<Enter>',two_hover)
    two.bind('<Leave>',two_over)
    three.bind('<Enter>',three_hover)
    three.bind('<Leave>',three_over)
    four.bind('<Enter>',four_hover)
    four.bind('<Leave>',four_over)
    five.bind('<Enter>',five_hover)
    five.bind('<Leave>',five_over)
    six.bind('<Enter>',six_hover)
    six.bind('<Leave>',six_over)
    seven.bind('<Enter>',seven_hover)
    seven.bind('<Leave>',seven_over)
    eight.bind('<Enter>',eight_hover)
    eight.bind('<Leave>',eight_over)
    nine.bind('<Enter>',nine_hover)
    nine.bind('<Leave>',nine_over)
    ten.bind('<Enter>',ten_hover)
    ten.bind('<Leave>',ten_over)
    eleven.bind('<Enter>',eleven_hover)
    eleven.bind('<Leave>',eleven_over)
    twelve.bind('<Enter>',twelve_hover)
    twelve.bind('<Leave>',twelve_over)
    thirteen.bind('<Enter>',thirteen_hover)
    thirteen.bind('<Leave>',thirteen_over)
    fourteen.bind('<Enter>',fourteen_hover)
    fourteen.bind('<Leave>',fourteen_over)

    chest.mainloop()

def backdisplay_windows():
#defining submit button here
    def back_submit():
        workout_back_dict={'Deadlift':deadlift.get(),'Pull_ups':pull_ups.get(),'Dumbell Rows':dumbell_rows.get(),'Lat Pulldown':Lat_Pulldown.get(),'Chinups':chinups.get(),'Seated Cable Rows':seated_cable_rows.get(),'Reverse Butterfly':reverse_butterfly.get(),'T_BAR':T_BAR.get(),'Incline Dumbell Rows':incline_dumbell_rows.get(),'Back Extensions':back_extensions.get(),'Kettlebell swing':kettlebell_swing.get(),'Lying_Lateral_Raise':lying_lateral_raise.get(),'Barbell Back Squat':barbell_back_squat.get(),'Med Ball Slam':med_ball_slam.get()}
        with open('back.py','w') as f:
            f.write(f'workout_back_dict={workout_back_dict}')         
        back.destroy()
        bicepsdisplay_windows()
#back windows here----------------------------------------------------
    back=Tk()
    back.iconbitmap('icon.ico')
    back.title('Select the excersies')
    width=400
    height=650
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    back.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    back.maxsize(400,650)
    back.config(bg='#141414')
#back label here
    Label(back,text='BACK',font='comicsans 25 bold',pady=10,padx=130,bg='#141414',fg='white',relief=RIDGE,bd=4).pack(anchor=CENTER,pady=12)
#making second frame here
    second_framE=Frame(back,bg='#141414')
    second_framE.pack(fill='x')
#back submit button here
    submit_back=Button(back,text='Submit',command=back_submit,font='Comicsans 12 bold',relief=SUNKEN,bd=4,bg='#141414',fg='white',padx=40,activebackground='#ffcc66',activeforeground='#141414')
    submit_back.pack(anchor=CENTER,fill='x',pady=5)
#attributes of check buttons
    font_style='regular 16'
    bgcolor= '#141414'
    fgcolor=  '#ffcc66'        
#back variables here:
    deadlift=IntVar()
    pull_ups=IntVar()
    dumbell_rows=IntVar()
    Lat_Pulldown=IntVar()
    chinups=IntVar()
    seated_cable_rows=IntVar()
    reverse_butterfly=IntVar()
    T_BAR=IntVar()
    incline_dumbell_rows=IntVar()
    back_extensions=IntVar()
    kettlebell_swing=IntVar()
    lying_lateral_raise=IntVar()
    barbell_back_squat=IntVar()
    med_ball_slam=IntVar()
#back checkbuttons here
    one=Checkbutton(second_framE,text='Deadlift',font=font_style,variable=deadlift,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    one.pack(anchor=CENTER,fill='x')
    two=Checkbutton(second_framE,text='Pull Ups',font=font_style,variable=pull_ups,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    two.pack(anchor=CENTER,fill='x'  )
    three=Checkbutton(second_framE,text='Dumbell rows',variable=dumbell_rows,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    three.pack(anchor=CENTER,fill='x'    )
    four=Checkbutton(second_framE,text='Lat Pulldown',variable=Lat_Pulldown,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    four.pack(anchor=CENTER,fill='x' )
    five=Checkbutton(second_framE,text='Chinups',variable=chinups,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    five.pack(anchor=CENTER,fill='x' )
    six=Checkbutton(second_framE,text='Seated Cable Rows',variable=seated_cable_rows,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    six.pack(anchor=CENTER,fill='x')
    seven=Checkbutton(second_framE,text='Reverse Butterfly',variable=reverse_butterfly,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    seven.pack(anchor=CENTER,fill='x'    )
    eight=Checkbutton(second_framE,text='T-BAR',variable=T_BAR,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eight.pack(anchor=CENTER,fill='x')
    nine=Checkbutton(second_framE,text='Incline Dumbell Rows',variable=incline_dumbell_rows,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    nine.pack(anchor=CENTER,fill='x' )
    ten=Checkbutton(second_framE,text='Back Extensions',variable=back_extensions,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    ten.pack(anchor=CENTER,fill='x'  )
    eleven=Checkbutton(second_framE,text='Kettlebell swing',variable=kettlebell_swing,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eleven.pack(anchor=CENTER,fill='x'   )
    twelve=Checkbutton(second_framE,text='Lying Lateral Raise',variable=lying_lateral_raise,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    twelve.pack(anchor=CENTER,fill='x'   )
    thirteen=Checkbutton(second_framE,text='Barbell Back Squat',variable=barbell_back_squat,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    thirteen.pack(anchor=CENTER,fill='x' )
    fourteen=Checkbutton(second_framE,text='Med Ball slam',variable=med_ball_slam,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    fourteen.pack(anchor=CENTER,fill='x' )
#defining hoverups for submit button here
    def hover_submit(e):
        submit_back.config(fg='#ffcc66')
    def over_submit(e):
        submit_back.config(fg='white')
#binding submit button here
    submit_back.bind('<Enter>',hover_submit)
    submit_back.bind('<Leave>',over_submit)
#defining hoverups here:
    fg='#ffcc66'
    bg='#141414'
    hover_font='regular 19 '
    over_font='regular 16 '
    def one_hover(e):
        one.config(fg=bg,font=hover_font,bg=fg)
    def one_over(e):
        one.config(fg=fg,bg=bg,font=over_font)
    def two_hover(e):
        two.config(fg=bg,font=hover_font,bg=fg)
    def two_over(e):
        two.config(fg=fg,bg=bg,font=over_font)
    def three_hover(e):
        three.config(fg=bg,font=hover_font,bg=fg)
    def three_over(e):
        three.config(fg=fg,bg=bg,font=over_font)   
    def four_hover(e):
        four.config(fg=bg,font=hover_font,bg=fg)
    def four_over(e):
        four.config(fg=fg,bg=bg,font=over_font)
    def five_hover(e):
        five.config(fg=bg,font=hover_font,bg=fg)
    def five_over(e):
        five.config(fg=fg,bg=bg,font=over_font)
    def six_hover(e):
        six.config(fg=bg,font=hover_font,bg=fg)
    def six_over(e):
        six.config(fg=fg,bg=bg,font=over_font)
    def seven_hover(e):
        seven.config(fg=bg,font=hover_font,bg=fg)
    def seven_over(e):
        seven.config(fg=fg,bg=bg,font=over_font)
    def eight_hover(e):
        eight.config(fg=bg,font=hover_font,bg=fg)
    def eight_over(e):
        eight.config(fg=fg,bg=bg,font=over_font)
    def nine_hover(e):
        nine.config(fg=bg,font=hover_font,bg=fg)
    def nine_over(e):
        nine.config(fg=fg,bg=bg,font=over_font)
    def ten_hover(e):
        ten.config(fg=bg,font=hover_font,bg=fg)
    def ten_over(e):
        ten.config(fg=fg,bg=bg,font=over_font)
    def eleven_hover(e):
        eleven.config(fg=bg,font=hover_font,bg=fg)
    def eleven_over(e):
        eleven.config(fg=fg,bg=bg,font=over_font)
    def twelve_hover(e):
        twelve.config(fg=bg,font=hover_font,bg=fg)
    def twelve_over(e):
        twelve.config(fg=fg,bg=bg,font=over_font)
    def thirteen_hover(e):
        thirteen.config(fg=bg,font=hover_font,bg=fg)
    def thirteen_over(e):
        thirteen.config(fg=fg,bg=bg,font=over_font)
    def fourteen_hover(e):
        fourteen.config(fg=bg,font=hover_font,bg=fg)
    def fourteen_over(e):
        fourteen.config(fg=fg,bg=bg,font=over_font)
#binding checkbuttons here
    one.bind('<Enter>',one_hover)
    one.bind('<Leave>',one_over)
    two.bind('<Enter>',two_hover)
    two.bind('<Leave>',two_over)
    three.bind('<Enter>',three_hover)
    three.bind('<Leave>',three_over)
    four.bind('<Enter>',four_hover)
    four.bind('<Leave>',four_over)
    five.bind('<Enter>',five_hover)
    five.bind('<Leave>',five_over)
    six.bind('<Enter>',six_hover)
    six.bind('<Leave>',six_over)
    seven.bind('<Enter>',seven_hover)
    seven.bind('<Leave>',seven_over)
    eight.bind('<Enter>',eight_hover)
    eight.bind('<Leave>',eight_over)
    nine.bind('<Enter>',nine_hover)
    nine.bind('<Leave>',nine_over)
    ten.bind('<Enter>',ten_hover)
    ten.bind('<Leave>',ten_over)
    eleven.bind('<Enter>',eleven_hover)
    eleven.bind('<Leave>',eleven_over)
    twelve.bind('<Enter>',twelve_hover)
    twelve.bind('<Leave>',twelve_over)
    thirteen.bind('<Enter>',thirteen_hover)
    thirteen.bind('<Leave>',thirteen_over)
    fourteen.bind('<Enter>',fourteen_hover)
    fourteen.bind('<Leave>',fourteen_over)

    back.mainloop()

def bicepsdisplay_windows():
#defining submit button here
    def bicep_submit():
        workout_bicep_dict={'EZ_Bar_Preacher_Curl':EZ_Bar_Preacher_Curl.get(),'hammer_curls':hammer_curls.get(),'behind_back_cable_curls':behind_back_cable_curls.get(),'reverse_curls':reverse_curls.get(),'Wide_grip_curls':Wide_grip_curls.get(),'close_grip_curls':close_grip_curls.get(),'Dumbell_curls':Dumbell_curls.get(),'side_cable_curls':side_cable_curls.get(),'band_curls':band_curls.get(),'drag_curls':drag_curls.get(),'cheat_curls':cheat_curls.get(),'Incline_biceps_curl':Incline_biceps_curl.get(),'one_arm_preacher_curls':one_arm_preacher_curls.get(),'weighted_chinups':weighted_chinups.get()}
        with open('bicep.py','w') as f:
            f.write(f'workout_bicep_dict={workout_bicep_dict}')
        bicep.destroy()
        shouldersdisplay_windows()
#bicep windows here-----
    bicep=Tk()
    bicep.iconbitmap('icon.ico')
    bicep.title('Select the excersies')
    width=400
    height=650
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    bicep.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    bicep.maxsize(400,650)
    bicep.config(bg='#141414')
#bicep label here
    Label(bicep,text='BICEPS',font='comicsans 25 bold',pady=10,padx=130,bg='#141414',fg='white',relief=RIDGE,bd=4).pack(anchor=CENTER,pady=12)
#second frame here
    second_framE=Frame(bicep,bg='#141414')
    second_framE.pack(fill='x')
#making submit button here
    submit_bicep=Button(bicep,text='Submit',command=bicep_submit,font='Comicsans 12 bold',relief=SUNKEN,bd=4,bg='#141414',fg='white',padx=40,activebackground='#ffcc66',activeforeground='#141414')
    submit_bicep.pack(anchor=CENTER,fill='x',pady=5)
#attributes of check buttons
    font_style='regular 16'
    bgcolor= '#141414'
    fgcolor=  '#ffcc66'        
#bicep varibales here:
    EZ_Bar_Preacher_Curl=IntVar()
    hammer_curls=IntVar()
    behind_back_cable_curls=IntVar()
    reverse_curls=IntVar()
    Wide_grip_curls=IntVar()
    close_grip_curls=IntVar()
    Dumbell_curls=IntVar()
    side_cable_curls=IntVar()
    band_curls=IntVar()
    drag_curls=IntVar()
    cheat_curls=IntVar()
    Incline_biceps_curl=IntVar()
    one_arm_preacher_curls=IntVar()
    weighted_chinups=IntVar()
#bicep checkbuttons here
    one=Checkbutton(second_framE,text='EZ-Bar Preacher Curl',font=font_style,variable=EZ_Bar_Preacher_Curl,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    one.pack(anchor=CENTER,fill='x')
    two=Checkbutton(second_framE,text='Hammer Curls',font=font_style,variable=hammer_curls,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    two.pack(anchor=CENTER,fill='x')
    three=Checkbutton(second_framE,text='Behind Back Cable Curls',variable=behind_back_cable_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    three.pack(anchor=CENTER,fill='x')
    four=Checkbutton(second_framE,text='Reverse Curl',variable=reverse_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    four.pack(anchor=CENTER,fill='x')
    five=Checkbutton(second_framE,text='Wide-Grip Curl',variable=Wide_grip_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    five.pack(anchor=CENTER,fill='x')
    six=Checkbutton(second_framE,text='Close-Grip Curl',variable=close_grip_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    six.pack(anchor=CENTER,fill='x')
    seven=Checkbutton(second_framE,text='Dumbbell Curl',variable=Dumbell_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    seven.pack(anchor=CENTER,fill='x')
    eight=Checkbutton(second_framE,text='Side Cable Curls',variable=side_cable_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    eight.pack(anchor=CENTER,fill='x')
    nine=Checkbutton(second_framE,text='Band Curls',variable=band_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    nine.pack(anchor=CENTER,fill='x')
    ten=Checkbutton(second_framE,text='Drag Curls',variable=drag_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    ten.pack(anchor=CENTER,fill='x')
    eleven=Checkbutton(second_framE,text='Cheat Curls',variable=cheat_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    eleven.pack(anchor=CENTER,fill='x')
    twelve=Checkbutton(second_framE,text='Incline Biceps Curl',variable=Incline_biceps_curl,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    twelve.pack(anchor=CENTER,fill='x')
    thirteen=Checkbutton(second_framE,text='One Arm Preacher Curl',variable=one_arm_preacher_curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    thirteen.pack(anchor=CENTER,fill='x')
    fourteen=Checkbutton(second_framE,text='Weighted Chinups',variable=weighted_chinups,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    fourteen.pack(anchor=CENTER,fill='x')
#defining hoverups here:
    fg='#ffcc66'
    bg='#141414'
    hover_font='regular 19 '
    over_font='regular 16 '
    def one_hover(e):
        one.config(fg=bg,font=hover_font,bg=fg)
    def one_over(e):
        one.config(fg=fg,bg=bg,font=over_font)
    def two_hover(e):
        two.config(fg=bg,font=hover_font,bg=fg)
    def two_over(e):
        two.config(fg=fg,bg=bg,font=over_font)
    def three_hover(e):
        three.config(fg=bg,font=hover_font,bg=fg)
    def three_over(e):
        three.config(fg=fg,bg=bg,font=over_font)   
    def four_hover(e):
        four.config(fg=bg,font=hover_font,bg=fg)
    def four_over(e):
        four.config(fg=fg,bg=bg,font=over_font)
    def five_hover(e):
        five.config(fg=bg,font=hover_font,bg=fg)
    def five_over(e):
        five.config(fg=fg,bg=bg,font=over_font)
    def six_hover(e):
        six.config(fg=bg,font=hover_font,bg=fg)
    def six_over(e):
        six.config(fg=fg,bg=bg,font=over_font)
    def seven_hover(e):
        seven.config(fg=bg,font=hover_font,bg=fg)
    def seven_over(e):
        seven.config(fg=fg,bg=bg,font=over_font)
    def eight_hover(e):
        eight.config(fg=bg,font=hover_font,bg=fg)
    def eight_over(e):
        eight.config(fg=fg,bg=bg,font=over_font)
    def nine_hover(e):
        nine.config(fg=bg,font=hover_font,bg=fg)
    def nine_over(e):
        nine.config(fg=fg,bg=bg,font=over_font)
    def ten_hover(e):
        ten.config(fg=bg,font=hover_font,bg=fg)
    def ten_over(e):
        ten.config(fg=fg,bg=bg,font=over_font)
    def eleven_hover(e):
        eleven.config(fg=bg,font=hover_font,bg=fg)
    def eleven_over(e):
        eleven.config(fg=fg,bg=bg,font=over_font)
    def twelve_hover(e):
        twelve.config(fg=bg,font=hover_font,bg=fg)
    def twelve_over(e):
        twelve.config(fg=fg,bg=bg,font=over_font)
    def thirteen_hover(e):
        thirteen.config(fg=bg,font=hover_font,bg=fg)
    def thirteen_over(e):
        thirteen.config(fg=fg,bg=bg,font=over_font)
    def fourteen_hover(e):
        fourteen.config(fg=bg,font=hover_font,bg=fg)
    def fourteen_over(e):
        fourteen.config(fg=fg,bg=bg,font=over_font)
#defining hoverups for submit button here
    def hover_submit(e):
        submit_bicep.config(fg='#ffcc66')
    def over_submit(e):
        submit_bicep.config(fg='white')
#binding submit button here
    submit_bicep.bind('<Enter>',hover_submit)
    submit_bicep.bind('<Leave>',over_submit)
#binding checkbuttons here
    one.bind('<Enter>',one_hover)
    one.bind('<Leave>',one_over)
    two.bind('<Enter>',two_hover)
    two.bind('<Leave>',two_over)
    three.bind('<Enter>',three_hover)
    three.bind('<Leave>',three_over)
    four.bind('<Enter>',four_hover)
    four.bind('<Leave>',four_over)
    five.bind('<Enter>',five_hover)
    five.bind('<Leave>',five_over)
    six.bind('<Enter>',six_hover)
    six.bind('<Leave>',six_over)
    seven.bind('<Enter>',seven_hover)
    seven.bind('<Leave>',seven_over)
    eight.bind('<Enter>',eight_hover)
    eight.bind('<Leave>',eight_over)
    nine.bind('<Enter>',nine_hover)
    nine.bind('<Leave>',nine_over)
    ten.bind('<Enter>',ten_hover)
    ten.bind('<Leave>',ten_over)
    eleven.bind('<Enter>',eleven_hover)
    eleven.bind('<Leave>',eleven_over)
    twelve.bind('<Enter>',twelve_hover)
    twelve.bind('<Leave>',twelve_over)
    thirteen.bind('<Enter>',thirteen_hover)
    thirteen.bind('<Leave>',thirteen_over)
    fourteen.bind('<Enter>',fourteen_hover)
    fourteen.bind('<Leave>',fourteen_over)   
    
    bicep.mainloop()

def shouldersdisplay_windows():
#defining submit button here
    def shoulder_submit():
        workout_shoulder_dict={'dumbell overhead press':Dumbbell_overhead_press.get(),'dumbell front raise':dumbbell_front_raise.get(),'barbell upright row':Barbell_upright_row.get(),'dumbell lateral raise':Dumbbell_lateral_raise.get(),'barbell overhead press':Barbell_Overhead_press.get(),'barbell shrug':Barbell_shrug.get(),'dumbell shrug':Dumbbell_Shrug.get(),'cable front raise':Cable_Front_Raise.get(),'seated single arm press':Seated_Single_Arm_Press.get(),'machine upright rows':Machine_upright_rows.get(),'face pull':Face_Pull.get(),'trap raise':Trap_Raise.get(),'band front raise':Band_Front_Raise.get(),'band lateral raise':Band_Lateral_Raise.get()}
        with open('shoulders.py','w') as f:
            f.write(f'workout_shoulder_dict={workout_shoulder_dict}')
        shoulder.destroy()
        tricepdisplay_windows()
#shoulder windows here
    shoulder=Tk()
    shoulder.iconbitmap('icon.ico')
    shoulder.title('Select the excersies')
    width=400
    height=650
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    shoulder.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    shoulder.maxsize(400,650)
    shoulder.config(bg='#141414')
#making shoulder label here
    Label(shoulder,text='Shoulders',font='comicsans 25 bold',pady=10,padx=130,bg='#141414',fg='white',relief=RAISED,bd=8).pack(anchor=CENTER,pady=12)
#making second frame here
    second_framE=Frame(shoulder,bg='#141414')
    second_framE.pack(fill='x')
#making submit button here
    submit_shoulder=Button(shoulder,text='Submit',command=shoulder_submit,font='Comicsans 12 bold',relief=SUNKEN,bd=4,bg='#141414',fg='white',padx=40,activebackground='#ffcc66',activeforeground='#141414')
    submit_shoulder.pack(anchor=CENTER,fill='x',pady=5)
#attributes of check buttons
    font_style='regular 16'
    bgcolor= '#141414'
    fgcolor=  '#ffcc66'        
#shoulder varibales here 
    Dumbbell_overhead_press=IntVar()
    dumbbell_front_raise=IntVar()
    Barbell_upright_row=IntVar()
    Dumbbell_lateral_raise=IntVar()
    Barbell_Overhead_press=IntVar()
    Barbell_shrug=IntVar()
    Dumbbell_Shrug=IntVar()
    Cable_Front_Raise=IntVar()
    Seated_Single_Arm_Press=IntVar()
    Machine_upright_rows=IntVar()
    Face_Pull=IntVar()
    Trap_Raise=IntVar()
    Band_Front_Raise=IntVar()
    Band_Lateral_Raise=IntVar()
#shoulder checkbuttons here
    one=Checkbutton(second_framE,text='Dumbbell Overhead Press',font=font_style,variable=Dumbbell_overhead_press,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    one.pack(anchor=CENTER,fill='x')
    two=Checkbutton(second_framE,text=' Dumbbell Front Raise',font=font_style,variable= dumbbell_front_raise,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    two.pack(anchor=CENTER,fill='x')
    three=Checkbutton(second_framE,text='Barbell Upright Row',variable=Barbell_upright_row,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    three.pack(anchor=CENTER,fill='x')
    four=Checkbutton(second_framE,text='Dumbbell Lateral Raise',variable=Dumbbell_lateral_raise,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    four.pack(anchor=CENTER,fill='x')
    five=Checkbutton(second_framE,text='Barbell Overhead Press',variable=Barbell_Overhead_press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    five.pack(anchor=CENTER,fill='x')
    six=Checkbutton(second_framE,text='Barbell Shrug',variable=Barbell_shrug,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    six.pack(anchor=CENTER,fill='x')
    seven=Checkbutton(second_framE,text='Dumbbell Shrug',variable=Dumbbell_Shrug,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    seven.pack(anchor=CENTER,fill='x')
    eight=Checkbutton(second_framE,text='Cable Front Raise',variable=Cable_Front_Raise,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eight.pack(anchor=CENTER,fill='x')
    nine=Checkbutton(second_framE,text='Seated Single-Arm Press',variable=Seated_Single_Arm_Press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    nine.pack(anchor=CENTER,fill='x')
    ten=Checkbutton(second_framE,text='Machine Upright Rows',variable=Machine_upright_rows,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    ten.pack(anchor=CENTER,fill='x')
    eleven=Checkbutton(second_framE,text='Face Pull',variable=Face_Pull,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eleven.pack(anchor=CENTER,fill='x')
    twelve=Checkbutton(second_framE,text='Trap Raise',variable=Trap_Raise,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    twelve.pack(anchor=CENTER,fill='x')
    thirteen=Checkbutton(second_framE,text='Band Front Raise',variable=Band_Front_Raise,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    thirteen.pack(anchor=CENTER,fill='x')
    fourteen=Checkbutton(second_framE,text='Band Lateral Raise',variable=Band_Lateral_Raise,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    fourteen.pack(anchor=CENTER,fill='x')
#defining hoverups here:
    fg='#ffcc66'
    bg='#141414'
    hover_font='regular 19 '
    over_font='regular 16 '
    def one_hover(e):
        one.config(fg=bg,font=hover_font,bg=fg)
    def one_over(e):
        one.config(fg=fg,bg=bg,font=over_font)
    def two_hover(e):
        two.config(fg=bg,font=hover_font,bg=fg)
    def two_over(e):
        two.config(fg=fg,bg=bg,font=over_font)
    def three_hover(e):
        three.config(fg=bg,font=hover_font,bg=fg)
    def three_over(e):
        three.config(fg=fg,bg=bg,font=over_font)   
    def four_hover(e):
        four.config(fg=bg,font=hover_font,bg=fg)
    def four_over(e):
        four.config(fg=fg,bg=bg,font=over_font)
    def five_hover(e):
        five.config(fg=bg,font=hover_font,bg=fg)
    def five_over(e):
        five.config(fg=fg,bg=bg,font=over_font)
    def six_hover(e):
        six.config(fg=bg,font=hover_font,bg=fg)
    def six_over(e):
        six.config(fg=fg,bg=bg,font=over_font)
    def seven_hover(e):
        seven.config(fg=bg,font=hover_font,bg=fg)
    def seven_over(e):
        seven.config(fg=fg,bg=bg,font=over_font)
    def eight_hover(e):
        eight.config(fg=bg,font=hover_font,bg=fg)
    def eight_over(e):
        eight.config(fg=fg,bg=bg,font=over_font)
    def nine_hover(e):
        nine.config(fg=bg,font=hover_font,bg=fg)
    def nine_over(e):
        nine.config(fg=fg,bg=bg,font=over_font)
    def ten_hover(e):
        ten.config(fg=bg,font=hover_font,bg=fg)
    def ten_over(e):
        ten.config(fg=fg,bg=bg,font=over_font)
    def eleven_hover(e):
        eleven.config(fg=bg,font=hover_font,bg=fg)
    def eleven_over(e):
        eleven.config(fg=fg,bg=bg,font=over_font)
    def twelve_hover(e):
        twelve.config(fg=bg,font=hover_font,bg=fg)
    def twelve_over(e):
        twelve.config(fg=fg,bg=bg,font=over_font)
    def thirteen_hover(e):
        thirteen.config(fg=bg,font=hover_font,bg=fg)
    def thirteen_over(e):
        thirteen.config(fg=fg,bg=bg,font=over_font)
    def fourteen_hover(e):
        fourteen.config(fg=bg,font=hover_font,bg=fg)
    def fourteen_over(e):
        fourteen.config(fg=fg,bg=bg,font=over_font)
#defining hoverups for submit button here
    def hover_submit(e):
        submit_shoulder.config(fg='#ffcc66')
    def over_submit(e):
        submit_shoulder.config(fg='white')
#binding submit button here
    submit_shoulder.bind('<Enter>',hover_submit)
    submit_shoulder.bind('<Leave>',over_submit)
#binding checkbuttons here
    one.bind('<Enter>',one_hover)
    one.bind('<Leave>',one_over)
    two.bind('<Enter>',two_hover)
    two.bind('<Leave>',two_over)
    three.bind('<Enter>',three_hover)
    three.bind('<Leave>',three_over)
    four.bind('<Enter>',four_hover)
    four.bind('<Leave>',four_over)
    five.bind('<Enter>',five_hover)
    five.bind('<Leave>',five_over)
    six.bind('<Enter>',six_hover)
    six.bind('<Leave>',six_over)
    seven.bind('<Enter>',seven_hover)
    seven.bind('<Leave>',seven_over)
    eight.bind('<Enter>',eight_hover)
    eight.bind('<Leave>',eight_over)
    nine.bind('<Enter>',nine_hover)
    nine.bind('<Leave>',nine_over)
    ten.bind('<Enter>',ten_hover)
    ten.bind('<Leave>',ten_over)
    eleven.bind('<Enter>',eleven_hover)
    eleven.bind('<Leave>',eleven_over)
    twelve.bind('<Enter>',twelve_hover)
    twelve.bind('<Leave>',twelve_over)
    thirteen.bind('<Enter>',thirteen_hover)
    thirteen.bind('<Leave>',thirteen_over)
    fourteen.bind('<Enter>',fourteen_hover)
    fourteen.bind('<Leave>',fourteen_over)   

    shoulder.mainloop()

def tricepdisplay_windows():
#defining submit button here
    def tricep_submit():
        workout_tricep_dict={'cable rope tricep pushdown':Cable_Rope_Tricep_Pushdown.get(),'tricep dips':Tricep_Dips.get(),'diamond push ups':Diamond_Push_Ups.get(),'one arm overhead extensions':One_Arm_Overhead_Extension.get(),'skull crushers':skull_crushers.get(),'bench dip':Bench_Dip.get(),'close grip bench press':Close_Grip_Bench_Press.get(),'underhand kickback':Underhand_Kickback.get(),'dumbell skull crushers':dumbell_skull_crushers.get(),'ez bar skull crushers':EZ_bar_skull_crushers.get(),'double underhand kickback':double_Underhand_Kickback.get(),'kettle floor press':Kettlebell_Floor_Press.get(),'landmine press':Landmine_press.get(),'L-sit':L_sit.get()}
        with open('triceps.py','w') as f:
            f.write(f'workout_tricep_dict={workout_tricep_dict}')
        tricep.destroy()
        legdisplay_windows()
#tricep windows here
    tricep=Tk()
    tricep.iconbitmap('icon.ico')
    tricep.title('Select the excersies')
    width=400
    height=650
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    tricep.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    tricep.maxsize(400,650)
    tricep.config(bg='#141414')
#making tricep label here
    Label(tricep,text='TRICEPS',font='comicsans 25 bold',pady=10,padx=130,bg='#141414',fg='white',relief=RAISED,bd=8).pack(anchor=CENTER,pady=12)
#making second frame here
    second_framE=Frame(tricep,bg='#141414')
    second_framE.pack(fill='x')
#making submit button here
    submit_triceps=Button(tricep,text='Submit',command=tricep_submit,font='Comicsans 12 bold',relief=SUNKEN,bd=4,bg='#141414',fg='white',padx=40,activebackground='#ffcc66',activeforeground='#141414')
    submit_triceps.pack(anchor=CENTER,fill='x',pady=5)
#attributes of check buttons
    font_style='regular 16'
    bgcolor= '#141414'
    fgcolor=  '#ffcc66'          
#tricep varibales here
    Cable_Rope_Tricep_Pushdown=IntVar()
    Tricep_Dips=IntVar()
    Diamond_Push_Ups=IntVar()
    One_Arm_Overhead_Extension=IntVar()
    skull_crushers=IntVar()
    Bench_Dip=IntVar()
    Close_Grip_Bench_Press=IntVar()
    Underhand_Kickback=IntVar()
    dumbell_skull_crushers=IntVar()
    EZ_bar_skull_crushers=IntVar()
    double_Underhand_Kickback=IntVar()
    Kettlebell_Floor_Press=IntVar()
    Landmine_press=IntVar()
    L_sit=IntVar()
#defining hoverups here:
    fg='#ffcc66'
    bg='#141414'
    hover_font='regular 19 '
    over_font='regular 16 '
    def one_hover(e):
        one.config(fg=bg,font=hover_font,bg=fg)
    def one_over(e):
        one.config(fg=fg,bg=bg,font=over_font)
    def two_hover(e):
        two.config(fg=bg,font=hover_font,bg=fg)
    def two_over(e):
        two.config(fg=fg,bg=bg,font=over_font)
    def three_hover(e):
        three.config(fg=bg,font=hover_font,bg=fg)
    def three_over(e):
        three.config(fg=fg,bg=bg,font=over_font)   
    def four_hover(e):
        four.config(fg=bg,font=hover_font,bg=fg)
    def four_over(e):
        four.config(fg=fg,bg=bg,font=over_font)
    def five_hover(e):
        five.config(fg=bg,font=hover_font,bg=fg)
    def five_over(e):
        five.config(fg=fg,bg=bg,font=over_font)
    def six_hover(e):
        six.config(fg=bg,font=hover_font,bg=fg)
    def six_over(e):
        six.config(fg=fg,bg=bg,font=over_font)
    def seven_hover(e):
        seven.config(fg=bg,font=hover_font,bg=fg)
    def seven_over(e):
        seven.config(fg=fg,bg=bg,font=over_font)
    def eight_hover(e):
        eight.config(fg=bg,font=hover_font,bg=fg)
    def eight_over(e):
        eight.config(fg=fg,bg=bg,font=over_font)
    def nine_hover(e):
        nine.config(fg=bg,font=hover_font,bg=fg)
    def nine_over(e):
        nine.config(fg=fg,bg=bg,font=over_font)
    def ten_hover(e):
        ten.config(fg=bg,font=hover_font,bg=fg)
    def ten_over(e):
        ten.config(fg=fg,bg=bg,font=over_font)
    def eleven_hover(e):
        eleven.config(fg=bg,font=hover_font,bg=fg)
    def eleven_over(e):
        eleven.config(fg=fg,bg=bg,font=over_font)
    def twelve_hover(e):
        twelve.config(fg=bg,font=hover_font,bg=fg)
    def twelve_over(e):
        twelve.config(fg=fg,bg=bg,font=over_font)
    def thirteen_hover(e):
        thirteen.config(fg=bg,font=hover_font,bg=fg)
    def thirteen_over(e):
        thirteen.config(fg=fg,bg=bg,font=over_font)
    def fourteen_hover(e):
        fourteen.config(fg=bg,font=hover_font,bg=fg)
    def fourteen_over(e):
        fourteen.config(fg=fg,bg=bg,font=over_font)
#defining hoverups for submit button here
    def hover_submit(e):
        submit_triceps.config(fg='#ffcc66')
    def over_submit(e):
        submit_triceps.config(fg='white')
#binding submit button here
    submit_triceps.bind('<Enter>',hover_submit)
    submit_triceps.bind('<Leave>',over_submit)
#tricep checkbuttons here
    one=Checkbutton(second_framE,text='Cable Rope Tricep Pushdown',font=font_style,variable=Cable_Rope_Tricep_Pushdown,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    one.pack(anchor=CENTER,fill='x')
    two=Checkbutton(second_framE,text='Tricep Dips',font=font_style,variable= Tricep_Dips,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    two.pack(anchor=CENTER,fill='x')
    three=Checkbutton(second_framE,text='Diamond Push-Ups',variable=Diamond_Push_Ups,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    three.pack(anchor=CENTER,fill='x')
    four=Checkbutton(second_framE,text='One-Arm Overhead Extension',variable=One_Arm_Overhead_Extension,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    four.pack(anchor=CENTER,fill='x')
    five=Checkbutton(second_framE,text='Skull Crushers',variable=skull_crushers,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    five.pack(anchor=CENTER,fill='x')
    six=Checkbutton(second_framE,text='Bench Dip',variable=Bench_Dip,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    six.pack(anchor=CENTER,fill='x')
    seven=Checkbutton(second_framE,text=' Close-Grip Bench Press',variable= Close_Grip_Bench_Press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    seven.pack(anchor=CENTER,fill='x')
    eight=Checkbutton(second_framE,text='Underhand Kickback',variable=Underhand_Kickback,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eight.pack(anchor=CENTER,fill='x')
    nine=Checkbutton(second_framE,text='Dumbell Skull Crushers',variable=dumbell_skull_crushers,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    nine.pack(anchor=CENTER,fill='x')
    ten=Checkbutton(second_framE,text='EZ Bar Skull Crushers',variable=EZ_bar_skull_crushers,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    ten.pack(anchor=CENTER,fill='x')
    eleven=Checkbutton(second_framE,text='Double Underhand Kickback',variable=double_Underhand_Kickback,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    eleven.pack(anchor=CENTER,fill='x')
    twelve=Checkbutton(second_framE,text='Kettlebell Floor Press',variable=Kettlebell_Floor_Press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    twelve.pack(anchor=CENTER,fill='x')
    thirteen=Checkbutton(second_framE,text='Landmine Press',variable=Landmine_press,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    thirteen.pack(anchor=CENTER,fill='x')
    fourteen=Checkbutton(second_framE,text='L-sit',variable=L_sit,font=font_style,bg=bgcolor,fg=fgcolor,activebackground=bgcolor,activeforeground=fgcolor)
    fourteen.pack(anchor=CENTER,fill='x')
#binding checkbuttons here
    one.bind('<Enter>',one_hover)
    one.bind('<Leave>',one_over)
    two.bind('<Enter>',two_hover)
    two.bind('<Leave>',two_over)
    three.bind('<Enter>',three_hover)
    three.bind('<Leave>',three_over)
    four.bind('<Enter>',four_hover)
    four.bind('<Leave>',four_over)
    five.bind('<Enter>',five_hover)
    five.bind('<Leave>',five_over)
    six.bind('<Enter>',six_hover)
    six.bind('<Leave>',six_over)
    seven.bind('<Enter>',seven_hover)
    seven.bind('<Leave>',seven_over)
    eight.bind('<Enter>',eight_hover)
    eight.bind('<Leave>',eight_over)
    nine.bind('<Enter>',nine_hover)
    nine.bind('<Leave>',nine_over)
    ten.bind('<Enter>',ten_hover)
    ten.bind('<Leave>',ten_over)
    eleven.bind('<Enter>',eleven_hover)
    eleven.bind('<Leave>',eleven_over)
    twelve.bind('<Enter>',twelve_hover)
    twelve.bind('<Leave>',twelve_over)
    thirteen.bind('<Enter>',thirteen_hover)
    thirteen.bind('<Leave>',thirteen_over)
    fourteen.bind('<Enter>',fourteen_hover)
    fourteen.bind('<Leave>',fourteen_over)   

    tricep.mainloop()

def hellouser_window():
#window starts here
    bg='#b2b1b0'
    hello=Tk()
    hello.iconbitmap('icon.ico')
    hello.title('Workout Planner')
    hello.config(bg='#141414')
    width=400
    height=200
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    hello.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    hello.maxsize(400,200)
    hello_user_label=Label(hello,font="Bahnschrift 20 bold",bg='#141414',fg='white')
    hello_user_label.pack(pady=30)
    welcome_label=Label(hello,font="regular 12",bg='#141414',fg='white')
    welcome_label.pack(side=TOP)
    develop_label=Label(hello,font="regular 9 ",bg='#141414',fg='white')
    develop_label.pack(side=TOP)

    def update1():
        hello_user_label.config(text=f"Hello {user_details['Username']}")
        hello.update_idletasks()

    def update2():
        welcome_label.config(text='Welcome to workout planner')
        hello.update_idletasks()
    def update3():
        develop_label.config(text='Developed By- Rishi Bakshi')
    def update4():
        develop_label.config(font='regular 9 italic',fg='#25dae9')
    def update5():
        hello.destroy()
        view_excersises_window()
    hello.after(100,update1)
    hello.after(1000,update2)
    hello.after(2000,update3)
    hello.after(4000,update4)
    hello.after(5200,update5)


    hello.mainloop()

def legdisplay_windows():
#defining submit button here
    def legs_submit():
        workout_legs_dict={'leg press':Leg_press.get(),'leg extensions':Leg_extensions.get(),'leg curls':Leg_Curls.get(),'lunges':Lunges.get(),'calf raise':Calf_raise.get(),'front squats':Front_Squats.get(),'overhead lunges':Overhead_Lunges.get(),'squats':Squats.get(),'jumping squats':jumping_squats.get(),'barbell calf raise':Barbell_Calf_raise.get(),'walking lunges':walking_lunges.get(),'weighted wall sit':Weighted_Wall_Sit.get(),'barbell squats':Barbell_squats.get(),'seated calf raise':Seated_Calf_Raise.get()}
        with open('legs.py','w') as f:
            f.write(f'workout_legs_dict={workout_legs_dict}')
        legs.destroy()
        relaunch()      
#legs window here
    legs=Tk()
    legs.iconbitmap('icon.ico')
    legs.title('Select the excersies')
    width=400
    height=650
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    legs.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    legs.maxsize(400,650)
    legs.config(bg='#141414')
#making legs label here
    Label(legs,text='LEGS',font='comicsans 25 bold',pady=10,padx=130,bg='#141414',fg='white',relief=RAISED,bd=8).pack(anchor=CENTER,pady=12)
#making second frame here
    second_framE=Frame(legs,bg='#141414')
    second_framE.pack(fill='x')
#making submit buttton here
    submit_legs=Button(legs,text='Submit',command=legs_submit,font='Comicsans 12 bold',relief=SUNKEN,bd=4,bg='#141414',fg='white',padx=40,activebackground='#ffcc66',activeforeground='#141414')
    submit_legs.pack(anchor=CENTER,fill='x',pady=5)
#attributes of check buttons
    font_style='regular 16'
    bgcolor= '#141414'
    fgcolor=  '#ffcc66'    
#legs varibales here
    Leg_press=IntVar()
    Leg_extensions=IntVar()
    Leg_Curls=IntVar()
    Lunges=IntVar()
    Calf_raise=IntVar()
    Front_Squats=IntVar()
    Overhead_Lunges=IntVar()
    Squats=IntVar()
    jumping_squats=IntVar()
    Barbell_Calf_raise=IntVar()
    walking_lunges=IntVar()
    Weighted_Wall_Sit=IntVar()
    Barbell_squats=IntVar()
    Seated_Calf_Raise=IntVar()
#defining hoverups for submit button here
    def hover_submit(e):
        submit_legs.config(fg='#ffcc66')
    def over_submit(e):
        submit_legs.config(fg='white')
#binding submit button here
    submit_legs.bind('<Enter>',hover_submit)
    submit_legs.bind('<Leave>',over_submit)
#defining hoverups here:
    fg='#ffcc66'
    bg='#141414'
    hover_font='regular 19 '
    over_font='regular 16 '
    def one_hover(e):
        one.config(fg=bg,font=hover_font,bg=fg)
    def one_over(e):
        one.config(fg=fg,bg=bg,font=over_font)
    def two_hover(e):
        two.config(fg=bg,font=hover_font,bg=fg)
    def two_over(e):
        two.config(fg=fg,bg=bg,font=over_font)
    def three_hover(e):
        three.config(fg=bg,font=hover_font,bg=fg)
    def three_over(e):
        three.config(fg=fg,bg=bg,font=over_font)   
    def four_hover(e):
        four.config(fg=bg,font=hover_font,bg=fg)
    def four_over(e):
        four.config(fg=fg,bg=bg,font=over_font)
    def five_hover(e):
        five.config(fg=bg,font=hover_font,bg=fg)
    def five_over(e):
        five.config(fg=fg,bg=bg,font=over_font)
    def six_hover(e):
        six.config(fg=bg,font=hover_font,bg=fg)
    def six_over(e):
        six.config(fg=fg,bg=bg,font=over_font)
    def seven_hover(e):
        seven.config(fg=bg,font=hover_font,bg=fg)
    def seven_over(e):
        seven.config(fg=fg,bg=bg,font=over_font)
    def eight_hover(e):
        eight.config(fg=bg,font=hover_font,bg=fg)
    def eight_over(e):
        eight.config(fg=fg,bg=bg,font=over_font)
    def nine_hover(e):
        nine.config(fg=bg,font=hover_font,bg=fg)
    def nine_over(e):
        nine.config(fg=fg,bg=bg,font=over_font)
    def ten_hover(e):
        ten.config(fg=bg,font=hover_font,bg=fg)
    def ten_over(e):
        ten.config(fg=fg,bg=bg,font=over_font)
    def eleven_hover(e):
        eleven.config(fg=bg,font=hover_font,bg=fg)
    def eleven_over(e):
        eleven.config(fg=fg,bg=bg,font=over_font)
    def twelve_hover(e):
        twelve.config(fg=bg,font=hover_font,bg=fg)
    def twelve_over(e):
        twelve.config(fg=fg,bg=bg,font=over_font)
    def thirteen_hover(e):
        thirteen.config(fg=bg,font=hover_font,bg=fg)
    def thirteen_over(e):
        thirteen.config(fg=fg,bg=bg,font=over_font)
    def fourteen_hover(e):
        fourteen.config(fg=bg,font=hover_font,bg=fg)
    def fourteen_over(e):
        fourteen.config(fg=fg,bg=bg,font=over_font)
#legs checkbuttons here
    one=Checkbutton(second_framE,text='Leg Press',font=font_style,variable=Leg_press,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    one.pack(anchor=CENTER,fill='x')
    two=Checkbutton(second_framE,text='Leg Extensions',font=font_style,variable= Leg_extensions,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    two.pack(anchor=CENTER,fill='x')
    three=Checkbutton(second_framE,text='Leg Curls',variable=Leg_Curls,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    three.pack(anchor=CENTER,fill='x')
    four=Checkbutton(second_framE,text='Lunges',variable=Lunges,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    four.pack(anchor=CENTER,fill='x')
    five=Checkbutton(second_framE,text='Calf Raise',variable=Calf_raise,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    five.pack(anchor=CENTER,fill='x')
    six=Checkbutton(second_framE,text='Front Squats',variable=Front_Squats,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    six.pack(anchor=CENTER,fill='x')
    seven=Checkbutton(second_framE,text=' Overhead Lunges',variable= Overhead_Lunges,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    seven.pack(anchor=CENTER,fill='x')
    eight=Checkbutton(second_framE,text='Squats',variable=Squats,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    eight.pack(anchor=CENTER,fill='x')
    nine=Checkbutton(second_framE,text='Jumping Squats',variable=jumping_squats,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    nine.pack(anchor=CENTER,fill='x')
    ten=Checkbutton(second_framE,text='Barbell Calf Raise',variable=Barbell_Calf_raise,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    ten.pack(anchor=CENTER,fill='x')
    eleven=Checkbutton(second_framE,text='Walking Lunges',variable=walking_lunges,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    eleven.pack(anchor=CENTER,fill='x')
    twelve=Checkbutton(second_framE,text='Weighted Wall Sit',variable=Weighted_Wall_Sit,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    twelve.pack(anchor=CENTER,fill='x')
    thirteen=Checkbutton(second_framE,text='Barbell Squats',variable=Barbell_squats,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    thirteen.pack(anchor=CENTER,fill='x')
    fourteen=Checkbutton(second_framE,text='Seated Calf Raise',variable=Seated_Calf_Raise,font=font_style,bg=bgcolor,fg=fgcolor,activeforeground=fgcolor,activebackground=bgcolor)
    fourteen.pack(anchor=CENTER,fill='x')
#binding checkbuttons here
    one.bind('<Enter>',one_hover)
    one.bind('<Leave>',one_over)
    two.bind('<Enter>',two_hover)
    two.bind('<Leave>',two_over)
    three.bind('<Enter>',three_hover)
    three.bind('<Leave>',three_over)
    four.bind('<Enter>',four_hover)
    four.bind('<Leave>',four_over)
    five.bind('<Enter>',five_hover)
    five.bind('<Leave>',five_over)
    six.bind('<Enter>',six_hover)
    six.bind('<Leave>',six_over)
    seven.bind('<Enter>',seven_hover)
    seven.bind('<Leave>',seven_over)
    eight.bind('<Enter>',eight_hover)
    eight.bind('<Leave>',eight_over)
    nine.bind('<Enter>',nine_hover)
    nine.bind('<Leave>',nine_over)
    ten.bind('<Enter>',ten_hover)
    ten.bind('<Leave>',ten_over)
    eleven.bind('<Enter>',eleven_hover)
    eleven.bind('<Leave>',eleven_over)
    twelve.bind('<Enter>',twelve_hover)
    twelve.bind('<Leave>',twelve_over)
    thirteen.bind('<Enter>',thirteen_hover)
    thirteen.bind('<Leave>',thirteen_over)
    fourteen.bind('<Enter>',fourteen_hover)
    fourteen.bind('<Leave>',fourteen_over)   

    legs.mainloop()

def view_excersises_window():
#food_menu_function here
    def related_food_options(e):
        if food_menu.get() == 'Protien':
            food_menu_list.config(values=protien_foods)
            food_menu_list.current(0)
        elif food_menu.get() =='Carbohydrates':
            food_menu_list.config(values=carb_foods)
            food_menu_list.current(0)
        elif food_menu.get() =='Good Fats':
            food_menu_list.config(values=good_fats)
            food_menu_list.current(0)
#update excercises function here
    def update_excersises(f):
        excersises.delete(0,END)
        if muscles.get(ANCHOR)=='Chest':
            chest_excersises=[i for i in workout_chest_dict if workout_chest_dict[i]==1]
            for item in chest_excersises:
                excersises.insert(END,item)
        
        elif muscles.get(ANCHOR)=='Back':
            back_excersises=[i for i in workout_back_dict if workout_back_dict[i]==1]
            for item in back_excersises:
                excersises.insert(END,item)
        
        elif muscles.get(ANCHOR)=='Biceps':
            bicep_excersises=[i for i in workout_bicep_dict if workout_bicep_dict[i]==1]
            for item in bicep_excersises:
                excersises.insert(END,item)
        
        elif muscles.get(ANCHOR)=='Shoulders':
            shoulder_excersises=[i for i in workout_shoulder_dict if workout_shoulder_dict[i]==1]
            for item in shoulder_excersises:
                excersises.insert(END,item)
        
        elif muscles.get(ANCHOR)=='Triceps':
            tricep_excersises=[i for i in workout_tricep_dict if workout_tricep_dict[i]==1]
            for item in tricep_excersises:
                excersises.insert(END,item)
        
        elif muscles.get(ANCHOR)=='Legs':
            legs_excersises=[i for i in workout_legs_dict if workout_legs_dict[i]==1]
            for item in legs_excersises:
                excersises.insert(END,item)                   
#window starts here
    view=Tk() 
    view.iconbitmap('icon.ico')
    view.title('Workout Planner')
    width=800
    height=700
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    view.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    view.maxsize(width,height)   
    view.config(bg='#141414')   
    f1=Frame(view,bg='#141414')
    f1.pack(fill='x')
#making welcome label here
    welcome_label=Label(f1,text='Welcome to Workout Planner',bg='#141414',fg='white',font='Bahnschrift 25 bold')
    welcome_label.pack(anchor=CENTER)
#browse food options label
    bg='#141414'
    fg='#f86263'    
    browsefood_label=Label(view,text='Browse Food Options',font='Bahnschrift 30',bg=bg,padx=130,fg=fg)
    browsefood_label.pack(anchor=NW,pady=20,fill='x')
#defining hoverups for browse food here
    def onhover(e):
        browsefood_label.config(bg=fg,fg=bg)
    def over(e):
        browsefood_label.config(bg=bg,fg=fg)
#binding browse food options label
    browsefood_label.bind('<Enter>',onhover)
    browsefood_label.bind('<Leave>',over)
#food options frame
    food_options_frame=Frame(view,bg='#141414')
    food_options_frame.pack(anchor=NW)
#making combobox here
    food_menu=ttk.Combobox(food_options_frame,values=food_and_nutrients_list)
    food_menu.pack(pady=20,anchor=NW,padx=250)
    food_menu.current(0)
    food_menu.bind('<<ComboboxSelected>>',related_food_options)
    food_menu_list=ttk.Combobox(food_options_frame,values=protien_foods)
    food_menu_list.current(0)
    food_menu_list.pack(pady=20,anchor=NW,padx=250)
#browse excercises label here
    bg1='#141414'
    fg1='#ffa157'
    browseexcercises_label=Label(view,text='Browse Excercises',font='Bahnschrift 30',bg=bg1,padx=130,fg=fg1)
    browseexcercises_label.pack(anchor=NW,pady=20,fill='x')  
#defining hoverups for browse excersises label
    def onhover1(event):
        browseexcercises_label.config(bg=fg1,fg=bg1)
    def over1(e):
        browseexcercises_label.config(bg=bg1,fg=fg1)
#binding browse excersises label here
    browseexcercises_label.bind('<Enter>',onhover1)
    browseexcercises_label.bind('<Leave>',over1)
#making listbox frame here
    f3=Frame(view,bg='#141414')
    f3.pack(pady=50)
#making listboxes here
    muscles=Listbox(f3)
    muscles.grid(row=0, column=0)
    excersises=Listbox(f3)
    excersises.grid(row=0, column=1, padx=20)
#inserting item in muscles listbox
    for item in muscle_groups_list:
        muscles.insert(END,item)
#binding the listbox
    muscles.bind('<<ListboxSelect>>',update_excersises)
#making user details frame here
    f4=Frame(view,bg='#141414',pady=2)
    f4.pack(fill='x',side=BOTTOM)
#making user details label here
    padx=10
    bg_user='#141414'
    fg_user='#25dae9'
    name_label=Label(f4,text=f"Name- {user_details['Username']}",bg=bg_user,fg=fg_user)
    name_label.pack(side=LEFT,padx=5)
    age_label=Label(f4,text=f"Age- {user_details['Age']}",bg=bg_user,fg=fg_user,padx=padx)
    age_label.pack(side=LEFT)
    height_label=Label(f4,text=f"Height- {user_details['Height']}",bg=bg_user,fg=fg_user,padx=padx)
    height_label.pack(side=LEFT)
    weight_label=Label(f4,text=f"Weight- {user_details['Weight']} ",bg=bg_user,fg=fg_user,padx=padx)
    weight_label.pack(side=LEFT)
    email_label=Label(f4,text=f"E-Mail- {user_details['E-Mail']}",bg=bg_user,fg=fg_user,padx=padx)
    email_label.pack(side=LEFT)
    phone_label=Label(f4,text=f"Phone Number- {user_details['Contact']}",bg=bg_user,fg=fg_user,padx=padx)
    phone_label.pack(side=LEFT)
#defiing hoverups for user details 
    def user_hover(e):
        name_label.config(fg=bg_user,bg=fg_user)
    def user_over(e):
        name_label.config(fg=fg_user,bg=bg_user)
    def user_hover1(e):
        age_label.config(fg=bg_user,bg=fg_user)
    def user_over1(e):
        age_label.config(fg=fg_user,bg=bg_user)
    def user_hover2(e):
        height_label.config(fg=bg_user,bg=fg_user)
    def user_over2(e):
        height_label.config(fg=fg_user,bg=bg_user)
    def user_hover3(e):
        weight_label.config(fg=bg_user,bg=fg_user)
    def user_over3(e):
        weight_label.config(fg=fg_user,bg=bg_user)
    def user_hover4(e):
        email_label.config(fg=bg_user,bg=fg_user)
    def user_over4(e):
        email_label.config(fg=fg_user,bg=bg_user)
    def user_hover5(e):
        phone_label.config(fg=bg_user,bg=fg_user)
    def user_over5(e):
        phone_label.config(fg=fg_user,bg=bg_user)
#binding user details labels here
    name_label.bind('<Enter>',user_hover)
    name_label.bind('<Leave>',user_over)
    age_label.bind('<Enter>',user_hover1)
    age_label.bind('<Leave>',user_over1)
    height_label.bind('<Enter>',user_hover2)
    height_label.bind('<Leave>',user_over2)
    weight_label.bind('<Enter>',user_hover3)
    weight_label.bind('<Leave>',user_over3)
    email_label.bind('<Enter>',user_hover4)
    email_label.bind('<Leave>',user_over4)
    phone_label.bind('<Enter>',user_hover5)
    phone_label.bind('<Leave>',user_over5)
#defining reset command  heredw
    def reset_workout_planner():
        def reset_app():
            reset=Tk()
            reset.config(bg='#141414')
            reset.title('Workout Planner')
            width=500
            height=250
            x=(1920/2)-(width/2)
            y=(1080/2)-(height/2)
            Label(reset,text='RE-LAUNCH Workout Planner',font=12,bg='#141414',fg='white').pack(anchor=CENTER,pady=90)
            reset.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
            reset.mainloop()
        user_response=tmsg.askyesno('Confirmation Window','Do you want to reset workout planner')
        if user_response==True:
            f=open('user_details.py','w')
            f.write('')
            view.destroy()
            reset_app()
        elif user_response==False:
            pass
#defining reselect command here
    def reselect_excersises():
        user_response=tmsg.askyesno('Confirmation Window','Do you want to reselect excersises?')
        if user_response==True:
            view.destroy()
            chestdisplay_window()
        elif user_response==False:
            pass
#defining google search command here
    def google_search():
        search=google_search_widget.get()
        pywhatkit.search(search)
#making buttons frame here
    f5=Frame(view,bg='#141414')
    f5.pack(fill='x',side=BOTTOM)
#reset button
    reset_bg='#f86263'
    reset_fg='#141414'
    reset_button=Button(f5,text='Reset Workout Planner',command=reset_workout_planner,font='bahnschrift 10',bg=reset_bg,fg=reset_fg,activebackground=reset_bg,activeforeground=reset_fg)
    reset_button.pack(side=RIGHT)
#defining hoverups for reset button here
    def reset_hover(e):
        reset_button.config(bg=reset_fg,fg=reset_bg)
    def reset_over(e):
        reset_button.config(bg=reset_bg,fg=reset_fg)
#binding reset button here
    reset_button.bind('<Enter>',reset_hover)
    reset_button.bind('<Leave>',reset_over)
#reselect button
    reselect_bg='#ffa157'
    reselect_fg='#141414'
    reselect_button=Button(f5,text='Reselect excersises',command=reselect_excersises,font='bahnschrift 10',bg=reselect_bg,fg=reselect_fg,activebackground=reselect_bg,activeforeground=reselect_fg)
    reselect_button.pack(side=RIGHT)
#defining hoverups for reselect button here
    def reselect_hover(e):
        reselect_button.config(bg=reselect_fg,fg=reselect_bg)
    def reselect_over(e):
        reselect_button.config(bg=reselect_bg,fg=reselect_fg)
#binding reselect button here
    reselect_button.bind('<Enter>',reselect_hover)
    reselect_button.bind('<Leave>',reselect_over)
#googlesearch widget
    google_search_widget=Entry(f5,textvariable=None,font= 10 ,bg='white')
    google_search_widget.pack(side=LEFT,fill='y')
#defining hoverups for google search widget here
    def google_search_hover(e):
        google_search_widget.config(bg='#a9a9aa')
    def google_search_over(e):
        google_search_widget.config(bg='white')
#binding google search widget here
    google_search_widget.bind('<Enter>',google_search_hover)
    google_search_widget.bind('<Leave>',google_search_over)
#search button
    search_button=Button(f5,text='Search',command=google_search,font='bahnschrift 10',bg='#141414',fg='white',activeforeground='white',activebackground='#141414')
    search_button.pack(side=LEFT,fill='y')
#making hoverups for search button here
    def search_hover(e):
        search_button.config(fg='#f86263')
    def search_over(e):
        search_button.config(fg='white')
#binding search button here
    search_button.bind('<Enter>',search_hover)
    search_button.bind('<Leave>',search_over)
    view.mainloop()

def relaunch():
#defining updates here
    def update1():
        text_label.config(text='Configuring the selected excersises')
    def update2():
        text_label.config(text='Analyzing submit form')
    def update3():
        text_label.config(text='Creating Directories on your PC')
    def update4():
        text_label.config(text='')
        my_progress.destroy()
        updating_information.destroy()
        text_label.config(text='RE-LAUNCH Workout Planner',pady=90)
        talk('Now please relaunch workout planner')
        rl.update_idletasks()
    def update5():
        updating_information.config(text='Updating Information')
#defining progress bar here
    def start_progress_bar():
        for x in range(200):
            my_progress['value']+=0.5
            rl.update_idletasks()
            time.sleep(0.01)
#window starts here
    rl=Tk()
    rl.iconbitmap('icon.ico')
    width=500
    height=250
    x=(1920/2)-(width/2)
    y=(1080/2)-(height/2)
    rl.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    rl.title('Information Processing')
    rl.maxsize(500,250)
    rl.minsize(500,250)
    rl.config(bg='#141414')
#making text label here
    text_label=Label(rl,text='',font=12,bg='#141414',fg='white')
    text_label.pack(anchor=CENTER,pady=70)
#making updating label here
    updating_information=Label(rl,text='',font=12,bg='#141414',fg='white')
    updating_information.pack()
#making progress bar here
    my_progress =ttk.Progressbar(rl,orient=HORIZONTAL,length=300,mode='determinate')
    my_progress.pack()
#giving updates here
    rl.after(300,update1)
    rl.after(2500,update2)
    rl.after(5000,update3)
    rl.after(7000,update5)
    rl.after(7500,start_progress_bar)
    rl.after(11000,update4)

    rl.mainloop()


#checking if the user is new or already registered
if os. stat('user_details.py').st_size == 0:
    newuser_window()
elif os.stat('user_details.py').st_size !=0:
    hellouser_window()




