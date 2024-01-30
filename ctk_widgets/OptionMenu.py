from customtkinter import CTkOptionMenu
from ctk_widgets.TypeClasses import GridArgsT

class CustomCTkOptionMenu(CTkOptionMenu):
    def __init__(self, master, gridargs: GridArgsT, values: list[str], command, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk optionmenu
        self.sidebar_optionmenu = CTkOptionMenu(
            master, values=values, command=command)
        self.sidebar_optionmenu.grid(**gridargs)
