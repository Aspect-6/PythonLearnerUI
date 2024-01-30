from customtkinter import CTkTextbox
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkTextbox(CTkTextbox):
    def __init__(self, master, gridargs: GridArgsT, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk textbox
        self.textbox = CTkTextbox(master)
        self.textbox.grid(**gridargs)
        self.textbox.insert("0.0", "CTkTextbox\n\n" +
                            "Drew Everley is stoopid.\n\n" * 20)