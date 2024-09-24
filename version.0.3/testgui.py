
import customtkinter as ctk
import pandas as pd

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
window = ctk.CTk()
window.title('Student Infomations')
width_window = window.winfo_screenwidth()-10
height_window = window.winfo_screenheight()-80
window.geometry("{0}x{1}+0+0".format(width_window, height_window))
window.title('Student Infomations')

frame = ctk.CTkFrame(master=window, width=width_window, height=height_window)
frame.pack()

read_file = pd.read_excel ("testexcel.xlsx") 
df = pd.DataFrame(read_file)

window.mainloop()