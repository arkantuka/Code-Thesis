import customtkinter as ctk
import pages.main_page as mp

class FaceRecognitionApp:    

    def __init__(self):
        # Appearance Mode
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_window_scaling(1.0)
        ctk.set_widget_scaling(1.0)
        
        # Window
        window = ctk.CTk()
        window.geometry("1920x1080")
        window.after(0, lambda: window.wm_state('zoomed'))
        window.title("Face Recognition App")
        
        mp.MainPage(window)
        window.mainloop()
    
if __name__ == "__main__":
    app = FaceRecognitionApp()