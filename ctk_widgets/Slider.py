from typing import Optional
from customtkinter import CTkSlider
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkSlider(CTkSlider):
    def __init__(self, master, gridargs: GridArgsT, **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTK slider
        self.slider = CTkSlider(master, orientation="vertical")
        self.grid(**gridargs)