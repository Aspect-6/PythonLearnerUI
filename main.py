import tkinter
import customtkinter
from ctk_widgets.CTk import CTkTabview, CTkLabel, CTkOptionMenu, CTkButton, CTkRadioButton, CTkProgressBar, CTkSlider, CTkSwitch, CTkCheckBox, CTkSegmentedButton, CTkTextbox, CTkEntry, CTkTabview, CTkLabel, CTkOptionMenu, CTkButton

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Learn Python")
        self.geometry(f"{1100}x{580}")

        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
