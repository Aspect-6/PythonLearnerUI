import customtkinter
from funcs import generate_dict
from custom.textbox import textbox_args, add_colors
from custom.label import label_args
from frames import SlideFrame

class DataTypesFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.colors_dict = {
            #region: View 1:
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
                    "green": ["number", "numbers", "floats"],
                    "blue": ["integers", "list"]
                }
            },
            "floats": {
                "str": "Floats are numbers that have a decimal point. They can be positive or negative, but they cannot be integers. Floats are used to represent numbers that are not whole numbers, such as the price of an item, the amount of liquid in a container, or the speed of a moving object.",
                "dict": {
                    "green": ["numbers", "integers", "price", "amount", "speed"],
                    "blue": ["floats"]
                }                
            },
            #endregion
            #region: View 2:
            "strings": {
                "str": "Strings are used to represent text. They can be used to store words, sentences, or even entire paragraphs. Strings are used to represent text that is not a number, such as the name of a person, the title of a book, or a paragraph of an article.",
                "dict": {
                    "green": ["words", "sentences", "paragraph", "paragraphs", "text", "number", "name", "title"],
                    "blue": ["strings"]
                
                }
            },
            "list": {
                "str": "Lists are used to store multiple items in a single variable. They can store any type of value, such as integers, floats, strings, other lists, dictionaries, or even other variables. Lists are used to represent collections of items, such as the names of people in a group, the scores of players in a game, or the items in a shopping cart.",
                "dict": {
                    "green": ["integers", "floats", "strings", "dictionaries", "variables", "items"],
                    "blue": ["lists"]
                }
            },
            "tuples": {
                "str": "Tuples are similar to lists, but they are immutable, which means that their values cannot be changed after they are created. Tuples are used to store collections of items that should not be changed, such as the coordinates of a point, the dimensions of a rectangle, or the RGB values of a color.",
                "dict": {
                    "green": ["lists", "immutable", "values", "collections", "coordinates", "dimensions", "RGB", "color"],
                    "blue": ["tuples"]
                }
            }
            #endregion
        }

        self.strings = {
            #region: View 1
            "view_1_title": "Basic data types in Python",
            "data_types_explanation_segments": generate_dict(self.colors_dict, "data_types"),
            "integer_title": "Integer data types in Python",
            "integer_explanation_segments": generate_dict(self.colors_dict, "integers"),
            "float_title": "Float data types in Python",
            "float_explanation_segments": generate_dict(self.colors_dict, "floats"),
            #endregion
            #region: View 2
            "string_title": "String data types in Python",
            "string_explanation_segments": generate_dict(self.colors_dict, "strings"),
            "list_title": "List data types in Python",
            "list_explanation_segments": generate_dict(self.colors_dict, "list"),
            "tuple_title": "Tuple data types in Python",
            "tuple_explanation_segments": generate_dict(self.colors_dict, "tuples"),
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
        self.data_types_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=124, **textbox_args)
        add_colors(self.data_types_explanation, {"green": "green", "blue": "#3d59d9"}, self.strings.get("data_types_explanation_segments"))
        
        # Integer data types section
        self.integer_section = SectionTypeComponent(master=self.view_1_frame, strings=self.strings, textbox_ht=104, type="integer")
        # Float data types section
        self.float_section = SectionTypeComponent(master=self.view_1_frame, strings=self.strings, textbox_ht=122, type="float")#endregion

        #region: View 2
        self.view_2_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_2_frame.grid_columnconfigure(0, weight=1)

        # Create view 2 title label
        self.view_2_title = customtkinter.CTkLabel(master=self.view_2_frame, text=self.strings.get("view_2_title"), **label_args)
        
        # String data types section
        self.string_section = SectionTypeComponent(master=self.view_2_frame, strings=self.strings, textbox_ht=104, type="string")
        # List data types section
        self.list_section = SectionTypeComponent(master=self.view_2_frame, strings=self.strings, textbox_ht=140, type="list")
        # Tuple data types section
        self.tuple_section = SectionTypeComponent(master=self.view_2_frame, strings=self.strings, textbox_ht=122, type="tuple")
        #endregion

        #region: View 3

        #endregion

        # Create slide frame
        self.slide_frame = SlideFrame(master=self, fg_color="transparent", views=[self.view_1_frame, self.view_2_frame])

        self.create_layout()

    def create_layout(self):
        self.elem_x: float = 0.5

        # Layout
        #region: View 1 frame layout
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")

        self.data_types_explanation.grid(row=1, column=0, pady=(5, 10), sticky="we")
        self.integer_section.grid(row=2, column=0, pady=(5, 10), sticky="we")
        self.float_section.grid(row=3, column=0, pady=(5, 10), sticky="we")
        #endregion
        
        # #region: View 2 frame layout
        self.view_2_frame.place(relx=self.elem_x+1, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.string_section.grid(row=1, column=0, pady=(5, 10), sticky="we")
        self.list_section.grid(row=2, column=0, pady=(5, 10), sticky="we")
        self.tuple_section.grid(row=3, column=0, pady=(5, 10), sticky="we")
        #endregion

class SectionTypeComponent(customtkinter.CTkFrame):
    def __init__(self, master, strings: dict, type: str, textbox_ht: int, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="transparent")

        # Create type label
        self.type_title = customtkinter.CTkLabel(master=self, text=strings.get(f"{type}_title"), **label_args)

        # Explanation of type
        self.type_explanation = customtkinter.CTkTextbox(master=self, height=textbox_ht, **textbox_args)
        add_colors(self.type_explanation, {"green": "green", "blue": "#3d59d9"}, strings.get(f"{type}_explanation_segments"))

        self.type_title.grid(row=0, column=0, pady=(0, 5), sticky="we") #(5, 5)
        self.type_explanation.grid(row=1, column=0, pady=(5, 0), sticky="we") #(5, 10)
