#imports tkinter and customtkinter
import tkinter as tk
import customtkinter as ct
#sets the default color theme to dark-blue
ct.set_default_color_theme('dark-blue')
#sets the default appearance mode to dark
ct.set_appearance_mode('dark')
#creates the root window
root = ct.CTk()
#sets the geometry of the root window
root.geometry("500x450")
#sets the title of the root window
root.title("login to your account")
#test login funciton (will be replaced with a real login function)
def login():
    print("test")
#test forgot login details function (will be replaced with a real forgot login details function)
def forgor():
    print("ha ha fuck you")
#creates a frame in the root window
frame = ct.CTkFrame(master=root)
#packs the frame with pad and fill
frame.pack(pady=20  , padx=50, fill="both", expand=True)
#creates label that says login
label = ct.CTkLabel(master=frame, text="Login", font=("roboto", 20))
#packs label
label.pack(pady=12,padx=10)
#creates an imput box that has grey text that dissapears
entry1 = ct.CTkEntry(master=frame, placeholder_text="Username")

#packs entry1
entry1.pack(pady=12,padx=10)
#creates a second entry box that has grey placeholder text, also hides input text as '*'  
entry2 = ct.CTkEntry(master=frame, placeholder_text="password", show="*")
#packs entry2
entry2.pack(pady=12,padx=10)

#creates a checkbox that says remember me, currently does nothing
chb1 = ct.CTkCheckBox(master=frame, text="remember me")
#packs check box
chb1.pack(pady=12, padx=10)
#remove later
"""chb2 = ct.CTkCheckBox(master=frame, text="halo           ")
chb2.pack(pady=12, padx=10)"""
#creates a button inside fram that says login and runs the login function when clicked
button1 = ct.CTkButton(master=frame, text='login', command=login)
#packs button1
button1.pack(pady=12, padx=10)
#creates a button inside frame that says forgot login details and runs the foror command when clicked
button2 = ct.CTkButton(master=frame, text='forgot login details', command=forgor)
#packs button2
button2.pack(pady=12, padx=10)
#runs mainloop
root.mainloop()