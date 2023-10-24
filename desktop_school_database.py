import customtkinter

people_list = [["Ivan Nikolov", "0001", "002-555-0100", "ivan@mail.com"],
               ["Nico Koehn", "1734", "202-555-0155", "nico1@mail.com"],
               ["Mark Kind", "7321", "202-555-0163", "mark@mail.com"],
               ["Kelly Walton", "9861", "202-555-0124", "kelly12@mail.com"],
               ["Jennifer Dawson", "5532", "202-555-0176", "dawson0@mail.com"],
               ["Glenn Carlson", "3251", "202-555-0140", "g.carlson@mail.com"]]

register_marks = [{
    "id_": "0001",
    "Math": [6.00, 5.50],
    "Physics": [5.00, 5.56, 4.52, 6.00]
}, {
    "id_": "1734",
    "Math": [5.56, 4.52],
    "Physics": [5.60]
}, {
    "id_": "7321",
    "Math": [5.49],
    "Physics": []
}, {
    "id_": "9861",
    "Math": [],
    "Physics": []
}, {
    "id_": "5532",
    "Math": [],
    "Physics": [2.99, 6.00]
}, {
    "id_": "3251",
    "Math": [4.50, 5.00],
    "Physics": [5.56, 4.52, 6.00, 4.49, 6.00]
}]

subjects = ["Math", "Physics"]


def textbox_subject_fill(index, textbox, subject):
    index -= 1
    textbox.configure(state="normal")
    textbox.delete(0.0, "end")

    if len(people_list) - 1 >= index:
        textbox.insert("0.0", f"{people_list[index][0]} |  ")
        id_ = people_list[index][1]

        for i in range(len(register_marks)):

            if register_marks[i]["id_"] == id_:

                for elements in register_marks[i][subject]:
                    textbox.insert("2.0", f"{elements:.02f}  ")

    textbox.configure(state="disabled")


def refresh_tab():
    textbox_subject_fill(1, textbox_1_Math, "Math")
    textbox_subject_fill(2, textbox_2_Math, "Math")
    textbox_subject_fill(3, textbox_3_Math, "Math")
    textbox_subject_fill(4, textbox_4_Math, "Math")
    textbox_subject_fill(5, textbox_5_Math, "Math")
    textbox_subject_fill(6, textbox_6_Math, "Math")
    textbox_subject_fill(7, textbox_7_Math, "Math")
    textbox_subject_fill(8, textbox_8_Math, "Math")
    textbox_subject_fill(9, textbox_9_Math, "Math")
    textbox_subject_fill(10, textbox_10_Math, "Math")
    textbox_subject_fill(11, textbox_11_Math, "Math")
    textbox_subject_fill(12, textbox_12_Math, "Math")
    textbox_subject_fill(12, textbox_13_Math, "Math")

    textbox_subject_fill(1, textbox_1_Physics, "Physics")
    textbox_subject_fill(2, textbox_2_Physics, "Physics")
    textbox_subject_fill(3, textbox_3_Physics, "Physics")
    textbox_subject_fill(4, textbox_4_Physics, "Physics")
    textbox_subject_fill(5, textbox_5_Physics, "Physics")
    textbox_subject_fill(6, textbox_6_Physics, "Physics")
    textbox_subject_fill(7, textbox_7_Physics, "Physics")
    textbox_subject_fill(8, textbox_8_Physics, "Physics")
    textbox_subject_fill(9, textbox_9_Physics, "Physics")
    textbox_subject_fill(10, textbox_10_Physics, "Physics")
    textbox_subject_fill(11, textbox_11_Physics, "Physics")
    textbox_subject_fill(12, textbox_12_Physics, "Physics")
    textbox_subject_fill(12, textbox_13_Physics, "Physics")


def register_student():
    def add_student_to_register():
        import random

        firs_name = (firs_name_entry.get()).strip()
        last_name = (last_name_entry.get()).strip()

        name = str(firs_name + " " + last_name)

        name = name.title()
        phone = phone_entry.get()
        mail = mail_entry.get()
        TEMPLATE = []

        while True:

            id_person = random.randint(1000, 9999)

            for i in range(len(people_list)):

                if id_person == people_list[i][1]:
                    break

            else:
                break

        id_person = str(id_person)
        TEMPLATE.append(name)
        TEMPLATE.append(id_person)
        TEMPLATE.append(phone)
        TEMPLATE.append(mail)

        people_list.append(TEMPLATE)
        template_2 = {"id_": id_person, "Math": [], "Physics": []}
        register_marks.append(template_2)
        refresh_tab()
        register_window.destroy()

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    register_window = customtkinter.CTk()
    register_window.title("Register Student")
    register_window.geometry(f"{400}x{300}")

    empty_label_register_student = customtkinter.CTkLabel(master=register_window, text=" ")
    empty_label_register_student.grid(row=0, column=0)

    name_frame = customtkinter.CTkFrame(master=register_window, fg_color="transparent")
    name_frame.grid(row=1, column=0)

    firs_name_entry = customtkinter.CTkEntry \
        (master=name_frame,
         placeholder_text="Firs Name",
         width=145,
         font=customtkinter.CTkFont(size=14))
    firs_name_entry.grid(row=0, column=0, padx=5, pady=10)

    last_name_entry = customtkinter.CTkEntry \
        (master=name_frame,
         placeholder_text="Last Name",
         width=145,
         font=customtkinter.CTkFont(size=14))
    last_name_entry.grid(row=0, column=1, padx=5, pady=10)

    phone_entry = customtkinter.CTkEntry \
        (master=register_window,
         placeholder_text="Phone",
         width=300,
         font=customtkinter.CTkFont(size=14))
    phone_entry.grid(row=2, column=0, padx=20, pady=10)

    mail_entry = customtkinter.CTkEntry \
        (master=register_window,
         placeholder_text="Mail",
         width=300,
         font=customtkinter.CTkFont(size=14))
    mail_entry.grid(row=3, column=0, padx=20, pady=10)

    frame_register_window = customtkinter.CTkFrame \
        (master=register_window,
         fg_color="transparent")
    frame_register_window.grid(row=4, column=0, padx=20, pady=20)

    button_register = customtkinter.CTkButton \
        (master=frame_register_window,
         text="Register",
         font=customtkinter.CTkFont(size=14),
         command=add_student_to_register)
    button_register.grid(row=0, column=0, padx=20, pady=20)

    button_cancel = customtkinter.CTkButton \
        (master=frame_register_window,
         text="Cancel",
         font=customtkinter.CTkFont(size=14),
         command=register_window.destroy)
    button_cancel.grid(row=0, column=1, padx=20, pady=20)

    register_window.mainloop()


def assess():
    def button_confirm_function():

        index_ = "0001"
        student = OptionMenu_name.get()
        subject = OptionMenu_subject.get()
        mark = ComboBox_mark.get()

        for search_for_id in range(len(people_list)):

            if people_list[search_for_id][0] == student:
                index_ = people_list[search_for_id][1]
                break

        for search_for_person_index in range(len(register_marks)):

            if register_marks[search_for_person_index]["id_"] == str(index_):
                register_marks[search_for_person_index][subject].append(float(mark))

        refresh_tab()
        assess_window.destroy()

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    assess_window = customtkinter.CTk()
    assess_window.title("Assess Student")
    assess_window.geometry(f"{600}x{250}")

    criteria = customtkinter.CTkFrame(master=assess_window,
                                      height=150,
                                      width=520)
    criteria.grid(row=0, column=0, padx=20, pady=20)

    name_list = []
    for i in range(len(people_list)):
        name_list.insert(i, people_list[i][0])

    OptionMenu_name = customtkinter.CTkOptionMenu \
        (master=criteria,
         values=name_list,
         button_color="#323232",
         fg_color="#262626",
         button_hover_color="#333333")
    OptionMenu_name.grid(row=0, column=0, padx=20, pady=20)
    OptionMenu_name.set("Student Name")

    OptionMenu_subject = customtkinter.CTkOptionMenu \
        (master=criteria,
         values=subjects,
         button_color="#323232",
         fg_color="#262626",
         button_hover_color="#333333")
    OptionMenu_subject.grid(row=0, column=1, padx=20, pady=20)
    OptionMenu_subject.set("Subject")
    ComboBox_mark = customtkinter.CTkComboBox \
        (master=criteria,
         values=["6", "5", "4", "3", "2"],
         button_color="#323232",
         fg_color="#262626",
         button_hover_color="#333333",
         border_color="#262626")
    ComboBox_mark.grid(row=0, column=2, padx=20, pady=20)
    ComboBox_mark.set("Mark")

    button_frame = customtkinter.CTkFrame(master=assess_window,
                                          fg_color="transparent")
    button_frame.grid(row=1, column=0, padx=20, pady=20)
    button_confirm = customtkinter.CTkButton \
        (master=button_frame,
         text="Confirm",
         font=customtkinter.CTkFont(size=14),
         command=button_confirm_function)
    button_confirm.grid(row=0, column=0, padx=20, pady=20)

    button_cancel = customtkinter.CTkButton \
        (master=button_frame,
         text="Cancel",
         font=customtkinter.CTkFont(size=14),
         command=assess_window.destroy)
    button_cancel.grid(row=0, column=1, padx=20, pady=20)

    assess_window.mainloop()


def button_student_reference_function():
    def fill_textbox():

        math_mark_print = ""
        physics_mark_print = ""

        name_list = OptionMenu_name1.get()
        name = (name_list.split())[0] + " " + (name_list.split())[1]

        for person_list in people_list:
            if name == person_list[0]:
                person_id_in_button_reference = person_list[1]
                Phone = person_list[2]
                Mail = person_list[3]
                break

        for index_in_register_mark in register_marks:
            if index_in_register_mark["id_"] == person_id_in_button_reference:
                for mark_get in index_in_register_mark["Math"]:
                    math_mark_print = math_mark_print + "  " + str(f"{mark_get:.02f}")

        for index_in_register_mark in register_marks:
            if index_in_register_mark["id_"] == person_id_in_button_reference:
                for mark_get in index_in_register_mark["Physics"]:
                    physics_mark_print = physics_mark_print + "  " + str(f"{mark_get:.02f}")

        textbox_data_for_person.configure(state="normal")
        textbox_data_for_person.delete(0.0, "end")
        textbox_data_for_person.insert \
            (0.0, f"""
        Name:  {name}
        Tag:  {(name_list.split())[3]}
        Phone:  {Phone}
        Mail:  {Mail}
        Math Marks:  {math_mark_print}
        Physics Marks:  {physics_mark_print}
      """)
        textbox_data_for_person.configure(state="disabled")

    student_reference = customtkinter.CTk()
    student_reference.title("Student Reference")
    student_reference.geometry(f"{585}x{320}")

    visibul_frame = customtkinter.CTkFrame(master=student_reference,
                                           height=150,
                                           width=520)
    visibul_frame.grid(row=0, column=0, padx=20, pady=20)

    criteria_reference = customtkinter.CTkFrame(master=visibul_frame,
                                                fg_color="transparent")
    criteria_reference.grid(row=0, column=0, padx=20, pady=20)

    name_list = []
    for i in range(len(people_list)):
        TEMPLATE = ""
        TEMPLATE = people_list[i][0] + " | " + people_list[i][1]
        name_list.insert(i, TEMPLATE)

    OptionMenu_name1 = customtkinter.CTkOptionMenu \
        (master=criteria_reference,
         values=name_list,
         button_color="#323232",
         fg_color="#262626",
         button_hover_color="#333333")
    OptionMenu_name1.grid(row=0, column=0, padx=20, pady=20)
    OptionMenu_name1.set("Student Name")

    Button_Reference = customtkinter.CTkButton \
        (master=criteria_reference,
         text="Get Info",
         font=customtkinter.CTkFont(size=14),
         command=fill_textbox)
    Button_Reference.grid(row=0, column=2, padx=20, pady=20)

    textbox_data_for_person = customtkinter.CTkTextbox(master=visibul_frame, height=150, width=520)
    textbox_data_for_person.grid(row=1, column=0, padx=10, pady=10)

    student_reference.mainloop()


# -----------------------------------------------------------------

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry(f"{1100}x{580}")

sidebar_frame = customtkinter.CTkFrame(master=root,
                                       width=200,
                                       height=580,
                                       corner_radius=0)
sidebar_frame.grid(row=0, column=0)
sidebar_frame.grid_rowconfigure(10, weight=1)

label_profile = customtkinter.CTkLabel \
    (master=sidebar_frame,
     text="Shkolo",
     font=customtkinter.CTkFont(size=20, weight="bold"))
label_profile.grid(row=0, column=0, padx=20, pady=20)

button_assess = customtkinter.CTkButton \
    (master=sidebar_frame,
     text="Assess",
     text_color="white",
     font=customtkinter.CTkFont(size=14),
     command=assess)
button_assess.grid(row=1, column=0, padx=20, pady=10)
button_student_reference = customtkinter.CTkButton \
    (master=sidebar_frame,
     text="Student Reference",
     text_color="white",
     font=customtkinter.CTkFont(size=14),
     command=button_student_reference_function)
button_student_reference.grid(row=2, column=0, padx=20, pady=10)

empty_label = customtkinter.CTkLabel(master=sidebar_frame, text="   ")
empty_label.grid(row=3, column=0, padx=20, pady=116)

button_register_student = customtkinter.CTkButton \
    (master=sidebar_frame,
     text="Register Student",
     text_color="white",
     font=customtkinter.CTkFont(size=14),
     command=register_student)
button_register_student.grid(row=4, column=0, padx=20, pady=10)
button_refresh = customtkinter.CTkButton \
    (master=sidebar_frame,
     text="Refresh",
     text_color="white",
     font=customtkinter.CTkFont(size=14),
     command=refresh_tab)
button_refresh.grid(row=5, column=0, padx=20, pady=10)
button_register_subject = customtkinter.CTkButton \
    (master=sidebar_frame,
     text="Register Subject",
     text_color="white",
     font=customtkinter.CTkFont(size=14),
     state="disabled")
button_register_subject.grid(row=6, column=0, padx=20, pady=15)

tab = customtkinter.CTkTabview(master=root, width=860, height=540)
tab.grid(row=0, column=1, padx=20, pady=20)

tab.add("Math")
tab.tab("Math").grid_rowconfigure(14, weight=1)

textbox_1_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_1_Math.grid(row=0, column=0, padx=14, pady=3)
textbox_subject_fill(1, textbox_1_Math, "Math")
textbox_2_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_2_Math.grid(row=1, column=0, padx=14, pady=3)
textbox_subject_fill(2, textbox_2_Math, "Math")
textbox_3_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_3_Math.grid(row=2, column=0, padx=14, pady=3)
textbox_subject_fill(3, textbox_3_Math, "Math")
textbox_4_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_4_Math.grid(row=3, column=0, padx=14, pady=3)
textbox_subject_fill(4, textbox_4_Math, "Math")
textbox_5_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_5_Math.grid(row=4, column=0, padx=14, pady=3)
textbox_subject_fill(5, textbox_5_Math, "Math")
textbox_6_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_6_Math.grid(row=5, column=0, padx=14, pady=3)
textbox_subject_fill(6, textbox_6_Math, "Math")
textbox_7_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_7_Math.grid(row=6, column=0, padx=14, pady=3)
textbox_subject_fill(7, textbox_7_Math, "Math")
textbox_8_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_8_Math.grid(row=7, column=0, padx=14, pady=3)
textbox_subject_fill(8, textbox_8_Math, "Math")
textbox_9_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                          height=10,
                                          width=820,
                                          text_color="silver")
textbox_9_Math.grid(row=8, column=0, padx=14, pady=3)
textbox_subject_fill(9, textbox_9_Math, "Math")
textbox_10_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                           height=10,
                                           width=820,
                                           text_color="silver")
textbox_10_Math.grid(row=9, column=0, padx=14, pady=3)
textbox_subject_fill(10, textbox_10_Math, "Math")
textbox_11_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                           height=10,
                                           width=820,
                                           text_color="silver")
textbox_11_Math.grid(row=10, column=0, padx=14, pady=3)
textbox_subject_fill(11, textbox_11_Math, "Math")
textbox_12_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                           height=10,
                                           width=820,
                                           text_color="silver")
textbox_12_Math.grid(row=11, column=0, padx=14, pady=3)
textbox_subject_fill(12, textbox_12_Math, "Math")
textbox_13_Math = customtkinter.CTkTextbox(master=tab.tab("Math"),
                                           height=10,
                                           width=820,
                                           text_color="silver")
textbox_13_Math.grid(row=12, column=0, padx=14, pady=3)
textbox_subject_fill(13, textbox_13_Math, "Math")

tab.add("Physics")
tab.tab("Physics").grid_rowconfigure(14, weight=1)

textbox_1_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_1_Physics.grid(row=0, column=0, padx=14, pady=3)
textbox_subject_fill(1, textbox_1_Physics, "Physics")
textbox_2_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_2_Physics.grid(row=1, column=0, padx=14, pady=3)
textbox_subject_fill(2, textbox_2_Physics, "Physics")
textbox_3_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_3_Physics.grid(row=2, column=0, padx=14, pady=3)
textbox_subject_fill(3, textbox_3_Physics, "Physics")
textbox_4_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_4_Physics.grid(row=3, column=0, padx=14, pady=3)
textbox_subject_fill(4, textbox_4_Physics, "Physics")
textbox_5_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_5_Physics.grid(row=4, column=0, padx=14, pady=3)
textbox_subject_fill(5, textbox_5_Physics, "Physics")
textbox_6_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_6_Physics.grid(row=5, column=0, padx=14, pady=3)
textbox_subject_fill(6, textbox_6_Physics, "Physics")
textbox_7_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_7_Physics.grid(row=6, column=0, padx=14, pady=3)
textbox_subject_fill(7, textbox_7_Physics, "Physics")
textbox_8_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_8_Physics.grid(row=7, column=0, padx=14, pady=3)
textbox_subject_fill(8, textbox_8_Physics, "Physics")
textbox_9_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                             height=10,
                                             width=820,
                                             text_color="silver")
textbox_9_Physics.grid(row=8, column=0, padx=14, pady=3)
textbox_subject_fill(9, textbox_9_Physics, "Physics")
textbox_10_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                              height=10,
                                              width=820,
                                              text_color="silver")
textbox_10_Physics.grid(row=9, column=0, padx=14, pady=3)
textbox_subject_fill(10, textbox_10_Physics, "Physics")
textbox_11_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                              height=10,
                                              width=820,
                                              text_color="silver")
textbox_11_Physics.grid(row=10, column=0, padx=14, pady=3)
textbox_subject_fill(11, textbox_11_Physics, "Physics")
textbox_12_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                              height=10,
                                              width=820,
                                              text_color="silver")
textbox_12_Physics.grid(row=11, column=0, padx=14, pady=3)
textbox_subject_fill(12, textbox_12_Physics, "Physics")
textbox_13_Physics = customtkinter.CTkTextbox(master=tab.tab("Physics"),
                                              height=10,
                                              width=820,
                                              text_color="silver")
textbox_13_Physics.grid(row=12, column=0, padx=14, pady=3)
textbox_subject_fill(13, textbox_13_Physics, "Physics")

root.mainloop()
