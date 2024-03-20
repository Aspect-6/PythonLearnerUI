import customtkinter
from custom.textbox import textbox_args, COLORS
from custom.label import label_args
from funcs import generate_dict, generate_code_block, add_colors, check_input_answer, check_radio_answer, check_checkbox_answer
from frames import SlideFrame

class ConvertingTypesFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.strings = {
            #region: View 1
            "view_1_title": "Converting Between Data Types",
            #endregion
        }

        #region: Declare frames
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        
        self.views = [self.view_1_frame]
        for view in self.views: view.grid_columnconfigure(0, weight=1)        #endregion

        #region: View 1
        # Create view 1 title
        self.view_1_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("view_1_title"), **label_args)
        #endregion

        self.slide_frame = SlideFrame(master=self, fg_color="transparent", views=self.views)

        self.create_layout()

    def create_layout(self):
        self.elem_x: float = 0.5

        # Layout
        #region: View 1
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        #endregion