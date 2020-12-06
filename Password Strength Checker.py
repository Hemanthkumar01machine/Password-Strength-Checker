import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg


class Checker:
    def whole():

        value=0

        def check():
            global value
            rule()
            if value==0:
                match_lower=0
                match_upper=0
                match_special=0
                match_numbers=0
                choice=0

                password_checking=str(password.get())

                

                lower=re.findall(r"[a-z]",password_checking)

                for lowin in range(len(lower)):
                    match_lower+=1

                upper=re.findall(r"[A-Z]",password_checking)

                for upin in range(len(upper)):
                    match_upper+=1

                special=re.findall(r"[\W]",password_checking)

                for specin in range(len(special)):
                    match_special+=1

                number=re.findall(r"[0-9]",password_checking)

                for numin in range(len(number)):
                    match_numbers+=1

                if match_lower>=int(low.get()):
                    lowers_lbl["foreground"]="lime"
                    choice+=1
                else:
                    lowers_lbl["foreground"]="red"

                if match_upper>=int(up.get()):
                    uppers_lbl["foreground"]="lime"
                    choice+=1
                else:
                    uppers_lbl["foreground"]="red"

                if match_numbers>=int(num.get()):
                    numbers_lbl["foreground"]="lime"
                    choice+=1
                else:
                    numbers_lbl["foreground"]="red"

                if match_special>=int(spec.get()):
                    specials_lbl["foreground"]="lime"
                    choice+=1
                else:
                    specials_lbl["foreground"]="red"

                length=len(password_checking)

                len_user=str(character.get())

                if len_user=="1 - 4":
                    start=1
                    stop=4
                elif len_user=="5 - 8":
                    start=5
                    stop=8
                elif len_user=="9 - 16":
                    start=8
                    stop=16

                if length >=start and length<=stop:
                    characters_lbl["foreground"]="lime"
                    choice+=1
                else:
                    characters_lbl["foreground"]="red"

                if choice==0:
                    result="Null Password"
                elif choice==1:
                    result="Very Poor"
                elif choice==2:
                    result="Poor"
                elif choice==3:
                    result="Medium"
                elif choice==4:
                    result="Good"
                elif choice==5:
                    result="Strongest"

                basic["text"]="Your Results : Password Is "+result
                basic["foreground"]="#138535"

        def reset():
            basic["text"]="Rules"
            basic["foreground"]="brown"
            characters_lbl["foreground"]="black"
            lowers_lbl["foreground"]="black"
            uppers_lbl["foreground"]="black"
            specials_lbl["foreground"]="black"
            numbers_lbl["foreground"]="black"
            password.set("")

            character.set("9 - 16")
            spec.set("1")
            low.set("1")
            up.set("1")
            num.set("1")

        def quit():
            ch=msg.askyesno("Exit","Are You Sure You Want To Exit?")
            if ch==True:
                screen.quit()
            else:
                pass

        def rule():
            global value
            def changing():
                characters_lbl["text"]="* Characters Range = "+character.get()
                lowers_lbl["text"]="* Minimum Lowercase Letter = "+low.get()
                uppers_lbl["text"]="* Minimum Uppercase Letter = "+up.get()
                specials_lbl["text"]="* Minimum Special Character = "+spec.get()
                numbers_lbl["text"]="* Minimum Number = "+num.get()

            rangeing=str(character.get())
            value=False
    
            if " " in str(password.get()):
                value+=1
                msg.showerror("Warning","Password Dosent Contain Whitespaces")
                reset()
            if rangeing=="1 - 4" and int(low.get())==1 and int(up.get())==1 and int(spec.get())==1 and int(num.get())==1:
                changing()
            elif  rangeing=="5 - 8" and int(low.get())+int(up.get())+int(spec.get())+int(num.get())<=8 :
                changing()
            elif rangeing=="9 - 16" and  1<=int(low.get())<=3 and 1<=int(up.get())<=3 and 1<=int(spec.get())<=3 and 1<=int(num.get())<=3:
                changing()
            else : 
                value+=1
                msg.showwarning("Warning","Please Select The Appropriate Values In Minimum Settings")
                reset()

                


        def checking():
            pass

        screen=tk.Tk()
        screen.title("Password Strength Checker")
        screen.config(background="light blue")

        basic=tk.LabelFrame(screen,text="Rules ",font=(18),foreground="brown",background="white")
        basic.grid(row=2,column=0,padx=8,pady=20,columnspan=2,rowspan=3)

        setting_frame=tk.LabelFrame(screen,text="Minimum Settings :",font=(15),foreground="black",background="light blue")
        setting_frame.grid(row=5,column=0,padx=5,pady=10,columnspan=2)

        heding_lbl=tk.Label(screen,text="Password Strength Checker",foreground="yellow",background="blue",font=("jokerman",25)).grid(row=0,column=0,padx=20,pady=8,columnspan=5)
        password_lbl=tk.Label(screen,text="Enter Password :",font=("arialblack",18,"bold"),foreground="dark red",background="light blue").grid(row=1,column=0)

        password=tk.StringVar()
        password_entry=ttk.Entry(screen,textvariable=password,width=18,font=("arial",22,"bold"),foreground="violet").grid(row=1,column=1,padx=5)

        submit_btn=ttk.Button(screen,text="Check",command=check).grid(row=1,column=2)

        reset_btn=ttk.Button(screen,text="Reset",command=reset).grid(row=2,column=2)

        exit_btn=ttk.Button(screen,text="Exit",command=quit).grid(row=3,column=2)

        character=tk.StringVar()
        low=tk.StringVar()
        up=tk.StringVar()
        spec=tk.StringVar()
        num=tk.StringVar()

        character.set("9 - 16")
        low.set(1)
        up.set("1")
        spec.set("1")
        num.set("1")


        characters_lbl=tk.Label(basic,text="* Characters Range = "+character.get(),font=(18),background="white")
        characters_lbl.grid(row=0,column=0,padx=10,sticky="W",pady=3)
        lowers_lbl=tk.Label(basic,text="* Minimum Lowercase Letter = "+low.get(),font=(18),background="white")
        lowers_lbl.grid(row=1,column=0,padx=10,sticky="W",pady=3)
        uppers_lbl=tk.Label(basic,text="* Minimum Uppercase Letter = "+up.get(),font=(18),background="white")
        uppers_lbl.grid(row=2,column=0,padx=10,sticky="W",pady=3)
        specials_lbl=tk.Label(basic,text="* Minimum Special Character = "+spec.get(),font=(18),background="white")
        specials_lbl.grid(row=3,column=0,padx=10,sticky="W",pady=3)
        numbers_lbl=tk.Label(basic,text="* Minimum Number = "+num.get(),font=(18),background="white")
        numbers_lbl.grid(row=4,column=0,padx=10,sticky="W",pady=3)

        character_lbl=tk.Label(setting_frame,text="Character range :",font=(13),foreground="green",background="light blue")
        character_lbl.grid(row=0,column=0)
        character_entry=ttk.Combobox(setting_frame,textvariable=character,width=5,font=(15))
        character_entry["values"]=["1 - 4","5 - 8","9 - 16"]
        character_entry.grid(row=0,column=1)

        low_lbl=tk.Label(setting_frame,text="Lowercase :",font=(13),foreground="green",background="light blue").grid(row=0,column=2,padx=5)
        low_entry=ttk.Combobox(setting_frame,textvariable=low,font=(15),width=3)
        low_entry["values"]=["1","2","3"]
        low_entry.grid(row=0,column=3)

        up_lbl=tk.Label(setting_frame,text="Uppercase :",font=(13),foreground="green",background="light blue").grid(row=0,column=4,padx=5)
        up_entry=ttk.Combobox(setting_frame,textvariable=up,font=(15),width=3)
        up_entry["values"]=["1","2","3"]
        up_entry.grid(row=0,column=5)

        spec_lbl=tk.Label(setting_frame,text="Special Character :",font=(13),foreground="green",background="light blue").grid(row=1,column=0,pady=10)
        spec_entry=ttk.Combobox(setting_frame,textvariable=spec,font=(15),width=3)
        spec_entry["values"]=["1","2","3"]
        spec_entry.grid(row=1,column=1)

        num_lbl=tk.Label(setting_frame,text="Number :",font=(13),foreground="green",background="light blue").grid(row=1,column=2,padx=5)
        num_entry=ttk.Combobox(setting_frame,textvariable=num,font=(15),width=3)
        num_entry["values"]=["1","2","3"]
        num_entry.grid(row=1,column=3)



        screen.mainloop()
if __name__==__name__:
    obj=Checker
    obj.whole()
    