from customtkinter import CTkCheckBox
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkCheckBox(CTkCheckBox):
    def __init__(self, master, gridargs: GridArgsT, text: str, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk checkbox
        self.checkbox = CTkCheckBox(master, text=text)
        self.checkbox.grid(**gridargs)