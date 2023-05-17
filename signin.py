from tkinter import *
from tkinter import messagebox

# Function to open the sign-up window from the sign-in page
def open_signup_window():
    root.destroy()  # Close the sign-in window
    import signup

def signin():
    username = user.get()
    password = passcode.get()

    found = False

    with open("datasheet.txt", "r") as file:
        data = file.readlines()
        for line in data:
            if line.startswith("Username:"):
                stored_username = line.split(":")[1].strip()
                if stored_username == username:
                    found = True
            elif line.startswith("Password:"):
                stored_password = line.split(":")[1].strip()
                if found and stored_password == password:
                    messagebox.showinfo('Login', 'Login successful!')
                    return

    messagebox.showerror('Error', 'Invalid username or password.')


root = Tk()
root.title('Login')
root.resizable(1, 1)
root.geometry("925x500+300+200")
root.configure(bg="#fff")

img = PhotoImage(file='Login.png')
label1 = Label(root, image=img, bg='white')
label1.place(x=50, y=50)
frame1 = Frame(root, width=350, height=350, bg='white')
frame1.place(x=480, y=70)
heading1 = Label(frame1, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI light', 24, 'bold'))
heading1.place(x=100, y=5)
user = Entry(frame1, fg='black', bg='white', font=('Microsoft Yahei UI light', 11,), width=25, border=0)
user.place(x=30, y=80)
user.insert(0, "user")
Frame(frame1, width=295, height=2, bg='black').place(x=25, y=110)
passcode = Entry(frame1, fg='black', bg='white', font=('Microsoft Yahei UI light', 11,), width=25, border=0)
passcode.place(x=30, y=150)
passcode.insert(0, "Password")
Frame(frame1, width=295, height=2, bg='black').place(x=25, y=180)
button1 = Button(frame1, text='Sign In', fg='white', bg='#57a1f8', width=39, pady=5, border=0, command=signin)
button1.place(x=20, y=204)
label2 = Label(frame1, text="Don't have an account?", fg='black', bg="white", font=('Microsoft Yahei UI light', 9,))
label2.place(x=75, y=270)
button2 = Button(frame1, text='Sign Up', bg='white', fg='#57a1f8', width=6, border=0, command=open_signup_window)
button2.place(x=215, y=265)

root.mainloop()
