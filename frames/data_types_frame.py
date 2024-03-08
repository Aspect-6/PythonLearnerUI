import customtkinter
from funcs import generate_dict
from custom.textbox import textbox_args, add_colors
from custom.label import label_args
from frames import SlideFrame


class DataTypesFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.colors_dict = {
            # region: View 1:
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
            # endregion
            # region: View 2:
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
            },
            # endregion
            # region: View 3:
            "dictionaries": {
                "str": "Dictionaries are used to store key-value pairs. The key can be an integer or string, and the value behind it can store any type of value, such as integers, floats, strings, lists, tuples, variables, or even other dictionaries. Dictionaries are used to represent collections of items that are associated with a unique key, such as the properties of an object, the attributes of a person, or the details of a product.",
                "dict": {
                    "green": ["integers", "floats", "strings", "lists", "tuples", "variables", "items", "key", "value", "pairs", "collections", "properties", "attributes", "details"],
                    "blue": ["dictionaries"]
                }
            },
            # endregion
            # region: View 4:
            "integer_usage": {
                "str": "361",
                "dict": {"green": ["361"]}
            },
            "float_usage": {
                "str": "3.14",
                "dict": {"green": ["3.14"]}
            },
            "string_usage": {
                "str": "\"Hello World!\"",
                "dict": {"orange": ["\"Hello", "World!\""]}
            },
            "list_usage": {
                "str": "[ \"Learning\", \"Lists\", [ 259 ], 5.738 ]",
                "dict": {"green": ["259", "5.738"], "orange": ["\"Learning\"", "\"Lists\""]}
            },
            "tuple_usage": {
                "str": "( 1, \"Second\", 2 )",
                "dict": {"green": ["1", "2"], "orange": ["\"Second\""]}
            },
            "dictionary_usage": {
                "str": "{ \"name\": \"John\", \"age\": 30, \"kids\": [ \"Bob\", \"Sally\" ] }",
                "dict": {"green": ["30"], "orange": ["\"name\"", "\"John\"", "\"age\"", "\"kids\"", "\"Bob", "Sally\""]}
            }
            # endregion
        }

        self.replacements = {
            "list": {
                "repl": {
                    "[ ": "[",
                    " ]": "]",
                    "259 ": "259",
                    "5.738 ": "5.738"
                },
                "lambda": lambda val: None
            },
            "tuple": {
                "repl": {
                    "( ": "(",
                    "2 ": "2",
                },
                "lambda": lambda val: None
            },
            "dictionary": {
                "repl": {
                    "[ ": "[",
                    " ]": "]",
                    "\"Sally\" ": "\"Sally\""
                },
                "lambda": lambda val: val + "\n      " if (("Bob" not in val and "," in val) or ("{" in val)) else val + "\n" if ("]" in val) else None
            }
        }

        def post_run(return_dict: dict, key: str):
            type_repls = self.replacements[key]
            for key, val in return_dict.items():
                if type_repls["lambda"](val) is not None:
                    return_dict[key] = type_repls["lambda"](val)
                if val in type_repls["repl"]:
                    return_dict[key] = type_repls["repl"][val]

            return return_dict

        self.strings = {
            # region: View 1
            "view_1_title": "Basic data types in Python",
            "data_types_explanation_segments": generate_dict(self.colors_dict, "data_types"),
            "integer_title": "Integer data types in Python",
            "integer_explanation_segments": generate_dict(self.colors_dict, "integers"),
            "float_title": "Float data types in Python",
            "float_explanation_segments": generate_dict(self.colors_dict, "floats"),
            # endregion
            # region: View 2
            "string_title": "String data types in Python",
            "string_explanation_segments": generate_dict(self.colors_dict, "strings"),
            "list_title": "List data types in Python",
            "list_explanation_segments": generate_dict(self.colors_dict, "list"),
            "tuple_title": "Tuple data types in Python",
            "tuple_explanation_segments": generate_dict(self.colors_dict, "tuples"),
            # endregion
            # region: View 3
            "dictionary_title": "Dictionary data types in Python",
            "dictionary_explanation_segments": generate_dict(self.colors_dict, "dictionaries"),
            # endregion
            # region: View 4
            "view_4_title": "What do each of these data types look like?",
            "integer_data_type_explanation_segments": generate_dict(self.colors_dict, "integer_usage"),
            "float_data_type_explanation_segments": generate_dict(self.colors_dict, "float_usage"),
            "string_data_type_explanation_segments": generate_dict(self.colors_dict, "string_usage"),
            "list_data_type_explanation_segments": generate_dict(self.colors_dict, "list_usage", post_run=post_run, index_key="list"),
            "tuple_data_type_explanation_segments": generate_dict(self.colors_dict, "tuple_usage", post_run=post_run, index_key="tuple"),
            "dictionary_data_type_explanation_segments": generate_dict(self.colors_dict, "dictionary_usage", post_run=post_run, index_key="dictionary"),
            # endregion
        }

        # region: Declare views
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_1_frame.grid_columnconfigure(0, weight=1)
        self.view_2_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_2_frame.grid_columnconfigure(0, weight=1)
        self.view_3_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_3_frame.grid_columnconfigure(0, weight=1)
        self.view_4_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_4_frame.grid_columnconfigure(0, weight=1)
        # endregion

        self.type_examples = {
            "integer": {
                "master": self.view_4_frame,
                "strings": self.strings,
                "colors": {"green": "green"},
                "textbox_ht": 20,
            },
            "float": {
                "master": self.view_4_frame,
                "strings": self.strings,
                "colors": {"green": "green"},
                "textbox_ht": 20,
            },
            "string": {
                "master": self.view_4_frame,
                "strings": self.strings,
                "colors": {"orange": "orange"},
                "textbox_ht": 20,
            },
            "list": {
                "master": self.view_4_frame,
                "strings": self.strings,
                "colors": {"green": "green", "orange": "orange"},
                "textbox_ht": 20,
            },
            "tuple": {
                "master": self.view_4_frame,
                "strings": self.strings,
                "colors": {"green": "green", "orange": "orange"},
                "textbox_ht": 20,
            },
            "dictionary": {
                "master": self.view_4_frame,
                "strings": self.strings,
                "colors": {"green": "green", "orange": "orange"},
                "textbox_ht": 94,
            },
        }

        self.section_config = {
            "integer": {
                "master": self.view_1_frame,
                "strings": self.strings,
                "textbox_ht": 104
            },
            "float": {
                "master": self.view_1_frame,
                "strings": self.strings,
                "textbox_ht": 122
            },
            "string": {
                "master": self.view_2_frame,
                "strings": self.strings,
                "textbox_ht": 104
            },
            "list": {
                "master": self.view_2_frame,
                "strings": self.strings,
                "textbox_ht": 140
            },
            "tuple": {
                "master": self.view_2_frame,
                "strings": self.strings,
                "textbox_ht": 122
            },
            "dictionary": {
                "master": self.view_3_frame,
                "strings": self.strings,
                "textbox_ht": 176
            }
        }

        # region: View 1
        # Create view 1 title label
        self.view_1_title = customtkinter.CTkLabel(
            master=self.view_1_frame, text=self.strings.get("view_1_title"), **label_args)

        # Explanation of data types
        self.data_types_explanation = customtkinter.CTkTextbox(
            master=self.view_1_frame, height=124, **textbox_args)
        add_colors(self.data_types_explanation, {
                   "green": "green", "blue": "#3d59d9"}, self.strings.get("data_types_explanation_segments"))

        # Integer data types section
        self.integer_section = SectionTypeComponent(**self.section_config.get("integer"), type="integer")
        # Float data types section
        self.float_section = SectionTypeComponent(**self.section_config.get("float"), type="float")  # endregion
        # endregion

        # region: View 2
        # String data types section
        self.string_section = SectionTypeComponent(**self.section_config.get("string"), type="string")
        # List data types section
        self.list_section = SectionTypeComponent(**self.section_config.get("list"), type="list")
        # Tuple data types section
        self.tuple_section = SectionTypeComponent(**self.section_config.get("tuple"), type="tuple")
        # endregion

        # region: View 3
        # Dictionary data types section
        self.dictionary_section = SectionTypeComponent(**self.section_config.get("dictionary"), type="dictionary")
        # endregion

        # region: View 4
        self.view_4_title = customtkinter.CTkLabel(master=self.view_4_frame, text=self.strings.get("view_4_title"), **label_args)
        self.integer_example = DataTypeExampleComponent(**self.type_examples.get("integer"), type="integer")
        self.float_example = DataTypeExampleComponent(**self.type_examples.get("float"), type="float")
        self.string_example = DataTypeExampleComponent(**self.type_examples.get("string"), type="string")
        self.list_example = DataTypeExampleComponent(**self.type_examples.get("list"), type="list")
        self.tuple_example = DataTypeExampleComponent(**self.type_examples.get("tuple"), type="tuple")
        self.dictionary_example = DataTypeExampleComponent(**self.type_examples.get("dictionary"), type="dictionary")
        # endregion

        # Create slide frame
        self.slide_frame = SlideFrame(master=self, fg_color="transparent", views=[self.view_1_frame, self.view_2_frame, self.view_3_frame, self.view_4_frame])

        self.create_layout()

    def create_layout(self):
        self.elem_x: float = 0.5

        # Layout
        # region: View 1 frame layout
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")

        self.data_types_explanation.grid(row=1, column=0, pady=(5, 10), sticky="we")
        self.integer_section.grid(row=2, column=0, pady=(5, 10), sticky="we")
        self.float_section.grid(row=3, column=0, pady=(5, 10), sticky="we")
        # endregion

        # region: View 2 frame layout
        self.view_2_frame.place(relx=self.elem_x+1, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.string_section.grid(row=1, column=0, pady=(5, 10), sticky="we")
        self.list_section.grid(row=2, column=0, pady=(5, 10), sticky="we")
        self.tuple_section.grid(row=3, column=0, pady=(5, 10), sticky="we")
        # endregion

        # region: View 3 frame layout
        self.view_3_frame.place(relx=self.elem_x+2, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.dictionary_section.grid(row=4, column=0, pady=(5, 10), sticky="we")
        # endregion

        # region: View 4 frame layout
        self.view_4_frame.place(relx=self.elem_x+3, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_4_title.grid(row=0, column=0, pady=(0, 10), sticky="we")
        self.integer_example.grid(row=1, column=0, pady=(5, 0), sticky="we")
        self.float_example.grid(row=2, column=0, pady=(5, 0), sticky="we")
        self.string_example.grid(row=3, column=0, pady=(5, 0), sticky="we")
        self.list_example.grid(row=4, column=0, pady=(5, 0), sticky="we")
        self.tuple_example.grid(row=5, column=0, pady=(5, 0), sticky="we")
        self.dictionary_example.grid(row=6, column=0, pady=(5, 0), sticky="we")
        # endregion


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

        self.type_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.type_explanation.grid(row=1, column=0, pady=(5, 0), sticky="we")

class DataTypeExampleComponent(customtkinter.CTkFrame):
    def __init__(self, master, strings: dict, colors: dict[str, str], type: str, textbox_ht: int, **kwargs):
        super().__init__(master, **kwargs)

        # self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="transparent")

        # Create type label
        self.data_type = customtkinter.CTkLabel(master=self, text=f"{type.capitalize()} example:", font=("Arial", 18), anchor="w")

        # Explanation of type
        self.type_example = customtkinter.CTkTextbox(master=self, height=textbox_ht)
        add_colors(self.type_example, colors, strings.get(f"{type}_data_type_explanation_segments"))

        self.data_type.pack(side="left", fill="x", expand=True)
        self.type_example.pack(side="left", fill="x", expand=True)
