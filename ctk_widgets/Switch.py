from customtkinter import CTkSwitch
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkSwitch(CTkSwitch):
    def __init__(self, master, gridargs: GridArgsT, text: str, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk switch
        self.switch = CTkSwitch(master, **kwargs)
        self.switch.grid(**gridargs)