from customtkinter import CTkEntry
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkEntry(CTkEntry):
    def __init__(self, master, gridargs: GridArgsT, placeholder_text: str, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk entry
        self.entry = CTkEntry(master, placeholder_text=placeholder_text)
        self.entry.grid(**gridargs)
