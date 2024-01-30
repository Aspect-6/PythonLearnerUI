from customtkinter import CTkButton
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkButton(CTkButton):
    def __init__(self, master, gridargs: GridArgsT, command, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk button
        self.sidebar_button = CTkButton(master, command=command)
        self.sidebar_button.grid(**gridargs)
