from customtkinter import CTkSegmentedButton
from ctk_widgets.TypeClasses import GridArgsT


class CustomCTkSegmentedButton(CTkSegmentedButton):
    def __init__(self, master, gridargs: GridArgsT, values: list[str], **kwargs):
        super().__init__(master, **kwargs)

        # Create custom CTk segmented button
        self.segmented_button = CTkSegmentedButton(master)
        self.segmented_button.grid(**gridargs)
        self.segmented_button.configure(values=values)
        self.segmented_button.set(values[0])