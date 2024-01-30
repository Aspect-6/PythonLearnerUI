from customtkinter import CTkRadioButton
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkRadioButton(CTkRadioButton):
    def __init__(self, master, gridargs: GridArgsT, variable, value, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk radiobutton
        self.radio_button = CTkRadioButton(master, variable=variable, value=value)
        self.radio_button.grid(**gridargs)