import customtkinter as ct

#sets the default color theme to dark-blue
ct.set_default_color_theme('dark-blue')
#sets the default appearance mode to dark
ct.set_appearance_mode('dark')
#creates the root window
root1 = ct.CTk()
#sets the geometry of the root window
root1.geometry("800x800")
#sets the title of the root window
root1.title("acceess granted")
frame = ct.CTkFrame(master=root1)
#packs the frame with pad and fill
frame.pack(pady=20  , padx=50, fill="both", expand=True)
label1 = ct.CTkLabel(master=frame, text="access granted", font=("roboto", 20))
label1.pack(pady=120,padx=10)
root1.mainloop()
exit()