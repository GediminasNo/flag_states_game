from tkinter import *
from  tkinter import messagebox
from PIL import ImageTk, Image
from random import randint

root = Tk()





                        # main Window


root.geometry('504x460')
root.config(bg='floral white')

top_frame = Frame(root,width=500,height=230)
top_frame.grid(row=0)

bottom_frame = Frame(root,width=500,height=230,bg='floral white')
bottom_frame.grid(row=1)

main_frame_photo = ImageTk.PhotoImage(Image.open('photo/world.jpg'))
global label_image
global count
count = []

                        # main Window


    # aditional function to launc the game window

def game_window_start():
    global game_window_new
    game_window_new = Tk()
    game_window_new.geometry("395x440")
    game_window_new.title("Game window")
    game_window_new.config(bg="floral white")


    # aditional function to launc the game window


                    # The game window after login, shows

def gamewindow():

                # to check the score buton window

    def to_check_score_of_hit_func():

        score_window = Tk()
        score_window.geometry("300x200")
        score_window.title("Score window")
        score_window.config(bg="green yellow")

        list_count = set(count)
        uniq_list = (list(list_count))

        corect_answers = len(uniq_list)

        corect_answer_label_name = Label(score_window,bg="forest green",text=name_of_user+ " " +last_name_of_user +":"+" score:"+ " " + str(corect_answers),font=("helvetica",'16'),padx=10,pady=5)
        corect_answer_label_name.place(relx=0.5,rely=0.5,anchor=CENTER)



        # to check the score buton window



    # The game window after login, shows

    global name_of_user
    global last_name_of_user
    global score_buton
    global list_of_flag_names
    global random_number
    global random_photo
    global path_of_photo
    global correct_label
    global answ_entry_flag



    name_of_user = entry_name.get()
    last_name_of_user = entry_last_name.get()
    entry_name.delete(0,END)
    entry_last_name.delete(0,END)

                    # The game window after login, shows



                # button to check or the answer is correct

    def check_correct_answer():
        # global correct_label   # not used anymore reason beacuse decided to place messagebox

        global answ_entry_flag
        global list_of_flag_names
        global random_number
        global random_photo
        global path_of_photo

        answ_entry_flag = label_entry_flag.get()
        answ_entry_flag = answ_entry_flag.replace(" ","")

        if answ_entry_flag.lower() == list_of_flag_names[random_number]:
            messagebox.showinfo("correct answer",answ_entry_flag)
            label_entry_flag.delete(0, END)
            count.append(random_number)

            # correct_label.destroy() # not used anymore reason beacuse decided to place messagebox

            list_of_flag_names = ['denmark', 'finland', 'germany', 'ireland', 'italy', 'poland', 'spain', 'sweden', 'ukraine', 'unitedkingdom','france','morocco',
                                  'belarus','romania','bulgaria','greece','turkey','algeria','netherlands','hungary','latvia','estonia','egypt',
                                  'iran','iraq','pakistan','china','japan','australia','newzealand']
            random_number = randint(0, len(list_of_flag_names) - 1)
            path_of_photo = 'photo/' + list_of_flag_names[random_number] + ".png"

            random_photo = ImageTk.PhotoImage(Image.open(path_of_photo))

            label_image = Label(game_window_new, image=random_photo)
            label_image.grid(row=0, column=0, columnspan=2)


        else:
            messagebox.showerror("incorrect answer",answ_entry_flag)

            label_entry_flag.delete(0, END)



            # correct_label.destroy()   # not used anymore reason beacuse decided to place messagebox

            list_of_flag_names = ['denmark', 'finland', 'germany', 'ireland', 'italy', 'poland', 'spain', 'sweden','ukraine', 'unitedkingdom',
                                  'france', 'morocco','belarus', 'romania', 'bulgaria', 'greece', 'turkey', 'algeria', 'netherlands','hungary',
                                  'latvia','estonia','egypt','iran','iraq','pakistan','china','japan','australia','newzealand']
            random_number = randint(0, len(list_of_flag_names) - 1)
            path_of_photo = 'photo/' + list_of_flag_names[random_number] + ".png"

            random_photo = ImageTk.PhotoImage(Image.open(path_of_photo))

            label_image = Label(game_window_new, image=random_photo)
            label_image.grid(row=0, column=0, columnspan=2)




            # button to check or the answer is correct




             # forward buton to get new flag#    # not used anymore reason beacuse decided to place messagebox

    # def forward_photo():
    #     global answ_entry_flag
    #     global list_of_flag_names
    #     global random_number
    #     global random_photo
    #     global path_of_photo
    #     global correct_label
    #
    #
    #     answ_entry_flag = label_entry_flag.get()
    #     label_entry_flag.delete(0,END)
    #     correct_label.destroy()
    #
    #
    #     list_of_flag_names = ['denmark', 'finland', 'germany', 'ireland', 'italy', 'poland', 'spain', 'Sweden', 'Ukraine', 'united kingdom']
    #     random_number = randint(0, len(list_of_flag_names) - 1)
    #     path_of_photo = 'photo/' + list_of_flag_names[random_number] + ".png"
    #
    #     random_photo = ImageTk.PhotoImage(Image.open(path_of_photo))
    #
    #     label_image = Label(game_window_new, image=random_photo)
    #     label_image.grid(row=0, column=0, columnspan=2)

        # forward buton to get new flag#    # not used anymore reason beacuse decided to place messagebox


         # back  buton to get new flag#   # not used anymore reason beacuse decided to place messagebox

    # def back_photo():
    #     global answ_entry_flag
    #     global list_of_flag_names
    #     global random_number
    #     global random_photo
    #     global path_of_photo
    #     global correct_label
    #
    #     answ_entry_flag = label_entry_flag.get()
    #     label_entry_flag.delete(0, END)
    #     correct_label.destroy()
    #
    #     list_of_flag_names = ['denmark', 'finland', 'germany', 'ireland', 'italy', 'poland', 'spain', 'Sweden','Ukraine', 'united kingdom']
    #     random_number = randint(0, len(list_of_flag_names) - 1)
    #     path_of_photo = 'photo/' + list_of_flag_names[random_number] + ".png"
    #
    #     random_photo = ImageTk.PhotoImage(Image.open(path_of_photo))
    #
    #     label_image = Label(game_window_new, image=random_photo)
    #     label_image.grid(row=0, column=0, columnspan=2)

        # back  buton to get new flag#  # not used anymore reason beacuse decided to place messagebox


            # if statement corect # The game window after login shows

     if name_of_user !="" and last_name_of_user !="":
        root.destroy()
        game_window_start()

        list_of_flag_names = ['denmark', 'finland', 'germany', 'ireland', 'italy', 'poland', 'spain', 'sweden',
                              'ukraine', 'unitedkingdom', 'france', 'morocco',
                              'belarus', 'romania', 'bulgaria', 'greece', 'turkey', 'algeria', 'netherlands', 'hungary','latvia',
                              'estonia','egypt','iran','iraq','pakistan','china','japan','australia','newzealand']
        random_number  = randint(0,len(list_of_flag_names)-1)
        path_of_photo = 'photo/'+list_of_flag_names[random_number]+".png"

        random_photo = ImageTk.PhotoImage(Image.open(path_of_photo))

        label_image = Label(game_window_new,image=random_photo)
        label_image.grid(row=0,column=0,columnspan=2)

        label_reference = Label(game_window_new,text="Please type the name of Flag >>>",padx=10,pady=5,font=("helvetica",'11'),bg="floral white",fg="gray1")
        label_reference.grid(row=1,column=0)

        label_entry_flag= Entry(game_window_new)
        label_entry_flag.grid(row=1,column=1)

        score_buton = Button(game_window_new, text="Check the answer", command=check_correct_answer,padx=10,pady=5,bg="green2")
        score_buton.grid(row=4, column=1)

        to_check_score_of_hit = Button(game_window_new,text="To check the score",padx=10,pady=5,command=to_check_score_of_hit_func,bg="DarkGoldenrod1")
        to_check_score_of_hit.grid(row=6,column=1)



            # if statement corect # The game window after login shows


# not used anymore reason beacuse decided to place messagebox

        # buton_to_forward = Button(game_window_new, text="Forward >>>",padx=10,pady=5,command=forward_photo)
        # buton_to_forward.grid(row=2,column=1)
        #
        # buton_to_back = Button(game_window_new,text="<<< Back ",padx=10,pady=5,command=back_photo)
        # buton_to_back.grid(row=2, column=0)
        #
        # correct_label = Label(game_window_new, text="")
        # correct_label.grid(row=3, column=0)

# not used anymore reason beacuse decided to place messagebox



        # if statement not  corect # The game window after login shows
    else:
        messagebox.showerror("Showerror","please type your Name and Last name")

                    # The game window after login shows




                                # main Window
photo_main_label = Label(top_frame,image=main_frame_photo)
photo_main_label.grid(row=0,column=0)

name_label = Label(bottom_frame,text="Username",padx=10,pady=5,font=("helvetica",'12'),bg='floral white')
name_label.grid(row=0,column=0)

last_label = Label(bottom_frame,text="Last name",padx=10,pady=5 , font=("helvetica",'12'),bg='floral white')
last_label.grid(row=1,column=0)

entry_name = Entry(bottom_frame)
entry_name.grid(row=0,column=1)

entry_last_name = Entry(bottom_frame)
entry_last_name.grid(row=1,column=1)


Login_buton  = Button(bottom_frame,text="Login",padx=15,pady=5,font=("helvetica",'12'),command=gamewindow,bg='sky blue')
Login_buton.grid(row=2,column=1)

                                # main Window




root.mainloop()
