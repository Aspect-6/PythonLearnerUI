from customtkinter import CTkProgressBar
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkProgressBar(CTkProgressBar):
    def __init__(self, master, gridargs: GridArgsT, orientation, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk progressbar
        self.progressbar = CTkProgressBar(master, orientation=orientation)
        self.progressbar.grid(**gridargs)