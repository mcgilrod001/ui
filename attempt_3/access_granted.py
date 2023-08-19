import customtkinter as ct

#sets the default color theme to dark-blue
ct.set_default_color_theme('dark-blue')
#sets the default appearance mode to dark
ct.set_appearance_mode('dark')
#creates the root window
root = ct.CTk()
#sets the geometry of the root window
root.geometry("800x800")
#sets the title of the root window
root.title("acceess granted")
frame = ct.CTkFrame(master=root)
#packs the frame with pad and fill
frame.pack(pady=20  , padx=50, fill="both", expand=True)
label1 = ct.CTkLabel(master=frame, text="access granted", font=("roboto", 20))
label1.pack(pady=120,padx=10)
root.mainloop()