from customtkinter import CTkLabel
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkLabel(CTkLabel):
    def __init__(self, master, gridargs: GridArgsT, text: str, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk label
        self.sidebar_label = CTkLabel(
            master, text=text
        )
        self.sidebar_label.grid(**gridargs)
