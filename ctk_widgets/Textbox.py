from customtkinter import CTkTextbox
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkTextbox(CTkTextbox):
    def __init__(self, master, gridargs: GridArgsT, text: str, pos: float, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk textbox
        self.textbox = CTkTextbox(master)
        self.textbox.grid(**gridargs)
        self.textbox.insert(pos, text)