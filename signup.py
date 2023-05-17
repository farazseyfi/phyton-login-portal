from tkinter import *
from tkinter import messagebox

def open_signin_window():
    window.destroy()  # Close the sign-up window
    import signin

def signup():
    username = user.get()
    password = code.get()
    confirm_pass = code_confirm.get()

    if password == confirm_pass:
        with open("datasheet.txt", "a") as file:
            file.write("Username: {}\n".format(username))
            file.write("Password: {}\n".format(password))

        messagebox.showinfo('Sign up', 'Successfully signed up!')
    else:
        messagebox.showerror('Error', 'Passwords do not match.')

window = Tk()
window.title('Sign Up')
window.geometry('925x500+300+200')
window.resizable(0, 0)
window.configure(bg='#fff')

img = PhotoImage(file='signup.png')
label1 = Label(window, image=img, border=0, bg='white')
label1.place(x=50, y=90)
frame1 = Frame(window, width=350, height=390, bg='white')
frame1.place(x=480, y=50)
heading1 = Label(window, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI light', 23, 'bold'))
heading1.place(x=600, y=50)
user = Entry(frame1, width=25, border=0, fg='black', bg='white', font=('Microsoft Yahei UI light', 11))
user.place(x=30, y=80)
user.insert(0, 'username')
Frame(frame1, width=295, height=2, bg='black').place(x=25, y=110)
code = Entry(frame1, width=25, border=0, fg='black', bg='white', font=('Microsoft Yahei UI light', 11))
code.place(x=30, y=150)
code.insert(0, 'password')
Frame(frame1, width=295, height=2, bg='black').place(x=25, y=177)
code_confirm = Entry(frame1, width=25, border=0, fg='black', bg='white', font=('Microsoft Yahei UI light', 11))
code_confirm.place(x=30, y=220)
code_confirm.insert(0, 'confirm the password')
Frame(frame1, width=295, height=2, bg='black').place(x=25, y=247)
button1 = Button(frame1, text='Sign Up', width=35, pady=7, bg='#57a1f8', fg='white', border=0, command=signup)
button1.place(x=30, y=280)
label2 = Label(frame1, text="I have an account", border=0, fg='black', bg='white', cursor='hand2', font=('Microsoft Yahei UI light', 9,))
label2.place(x=90, y=340)
button2 = Button(frame1, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=open_signin_window)
button2.place(x=215, y=337)

window.mainloop()
