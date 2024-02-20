import customtkinter
from funcs import print_color_coded, generate_dict
from frames import SlideFrame
import math

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
            "data_types_explanation_segments": generate_dict(self.colors_dict, "data_types", None, None),
            #endregion
            
            #region: View 2
            "integer_title": "Integer data types in Python",
            "integer_explanation_segments": generate_dict(self.colors_dict, "integers", None, None)
            #endregion

            #region: View 3
            
            #endregion

        }
        
        #region: View 1
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_1_frame.grid_columnconfigure(0, weight=1)

        # Create view 1 title label
        self.view_1_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("view_1_title"), height=40, font=("Arial", 18), fg_color="#3669a0", text_color="#fff", corner_radius=5)
        
        # Explanation of data types
        self.data_types_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=142, fg_color="transparent", wrap="word", font=("Arial", 17))
        self.data_types_explanation.tag_config("green", foreground="green")
        self.data_types_explanation.tag_config("blue", foreground="#3d59d9")
        print_color_coded(["green", "blue"], self.data_types_explanation, self.strings.get("data_types_explanation_segments"))
        
        # Create integer title label
        self.integer_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("integer_title"), height=40, font=("Arial", 18), fg_color="#3669a0", text_color="#fff", corner_radius=5)
        
        # Explanation of integersdata types
        self.integer_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=142, fg_color="transparent", wrap="word", font=("Arial", 17))
        self.integer_explanation.tag_config("green", foreground="green")
        self.integer_explanation.tag_config("blue", foreground="#3d59d9")
        print_color_coded(["green", "blue"], self.integer_explanation, self.strings.get("integer_explanation_segments"))

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
        # View 1 frame layout
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.data_types_explanation.grid(row=1, column=0, pady=10, sticky="we")

        #region: View 1
        self.integer_title.grid(row=3, column=0, pady=(0, 5), sticky="we")
        self.integer_explanation.grid(row=4, column=0, pady=10, sticky="we")
        #endregion
