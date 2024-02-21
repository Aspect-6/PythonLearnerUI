import customtkinter
from funcs import generate_dict
from custom.textbox import textbox_args, add_colors
from custom.label import label_args
from frames import SlideFrame

class DataTypesFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.colors_dict = {
            "data_types": {
                "str": "The Python coding language has many different data types available, such as integers, floats, strings, lists, tuples, and dictionaries. In this section, you will learn about integers, floats, strings, and lists, the syntax of these data types, and how to use them.",
                "dict": {
                    "green": ["integers", "floats", "strings", "lists", "tuples", "dictionaries"],
                    "blue": ["data", "types"]
                }
            },
            "integers": {
                "str": "Integers are whole numbers. They can be positive or negative, but they cannot be floats. Integers are used to represent whole numbers, such as the number of people in a room, the number of items in a list, or the number of times a loop should run.",
                "dict": {
                    "green": ["loop", "number", "numbers"],
                    "blue": ["integers", "list", "floats"]
                }
            }
        }

        self.strings = {
            #region: View 1M
            "view_1_title": "Basic data types in Python",
            "data_types_explanation_segments": generate_dict(self.colors_dict, "data_types"),
            #endregion
            
            #region: View 2
            "integer_title": "Integer data types in Python",
            "integer_explanation_segments": generate_dict(self.colors_dict, "integers")
            #endregion

            #region: View 3
            
            #endregion

        }
        
        #region: View 1
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_1_frame.grid_columnconfigure(0, weight=1)

        # Create view 1 title label
        self.view_1_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("view_1_title"), **label_args)
        
        # Explanation of data types
        self.data_types_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=142, **textbox_args)
        add_colors(self.data_types_explanation, {"green": "green", "blue": "#3d59d9"}, self.strings.get("data_types_explanation_segments"))
        
        # Create integer title label
        self.integer_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("integer_title"), **label_args)
        
        # Explanation of integer data types
        self.integer_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=142, **textbox_args)
        add_colors(self.integer_explanation, {"green": "green", "blue": "#3d59d9"}, self.strings.get("integer_explanation_segments"))

        # Explanation of float data types
        self.float_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=142, **textbox_args)
        add_colors(self.float_explanation, {"green": "green", "blue": "#3d59d9"}, self.strings.get("integer_explanation_segments"))
        #endregion

        #region: View 2

        #endregion

        #region: View 3

        #endregion

        # Create slide frame
        self.slide_frame = SlideFrame(master=self, fg_color="transparent", views=[self.view_1_frame])

        self.create_layout()

    def create_layout(self):
        self.elem_x: float = 0.5

        # Layout
        #region: View 1 frame layout
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.data_types_explanation.grid(row=1, column=0, pady=10, sticky="we")

        self.integer_title.grid(row=3, column=0, pady=(0, 5), sticky="we")
        self.integer_explanation.grid(row=4, column=0, pady=10, sticky="we")
        #endregion
