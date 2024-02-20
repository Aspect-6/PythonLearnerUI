import customtkinter
from funcs import print_color_coded, generate_dict
from frames import SlideFrame


class StoringDataFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def data_showcase_pre_run(split_string):
            for i, word in enumerate(split_string):
                if "print(" in word:
                    split_string[i:i+1] = ["print(", "my_var", ")\n"]
            return split_string
        def data_showcase_post_run(return_dict: dict):
            stop = False
            for key in return_dict:
                if stop:
                    return_dict[key] = "my_var"
                    break
                if not stop and 'print(' in return_dict[key]:
                    return_dict[key] = ">>> print("
                    return_dict[key+1] = ")\n"
                    stop = True
                if key == "green_1":
                    return_dict[key] = "10\n"
            return return_dict
        
        def var_explanation_pre_run(split_string):
            for i, word in enumerate(split_string):
                if 'print(' in word:
                    split_string[i:i+1] = ["\"print(", "my_var", "),\""]
            return split_string
        def var_explanation_post_run(return_dict: dict):
            stop = False
            for key in return_dict:
                if stop:
                    return_dict[key] = "my_var"
                    break
                if not stop and 'print(' in return_dict[key]:
                    return_dict[key] = "then you would type \"print("
                    stop = True
            return return_dict
        

        self.color_dicts = {
            "data_showcase": {
                "str": ">>> my_var = 10 >>> print(my_var) 10",
                "dict": {
                    "green": ["10"],
                    "purple": ["my_var"]
                }
            },
            "var_explanation": {
                "str": "Variables in python are used to store data for later use. They can store any type of value such as an integer, string, list, dictionary, expression, or even other variables. The way that you declare a  variable is by first coming up with a name. Next you put an = sign to tell python that whatever you are about to type should be stored under the name of the variable that you named. Finally, you type the value you wish to store. Later, if you need to access that value and use it, all you need to do is to reference the name of the variable. For example, if you wanted to print the value of the variable named, my_var, then you would type \"print(my_var)\", which would print the value of my_var to the terminal.",
                "dict": {
                    "green": ["integer", "string", "list", "dictionary", "expression", "="],
                    "blue": ["terminal"],
                    "purple": ["Variables", "variables.", "variable.","name.", "named.", "my_var"],
                },
            },
        }

        self.strings = {
            #region: View 1
            "view_1_title": "Storing Data in Python",
            "data_showcase_segments": generate_dict(self.color_dicts, "data_showcase", data_showcase_pre_run, data_showcase_post_run),
            "var_explanation_segments": generate_dict(self.color_dicts, "var_explanation", var_explanation_pre_run, var_explanation_post_run)
            #endregion
        }

        """
        # View 1: Storing Data in Python
        ----------------------------------------------------------------
        # Description here...
        """
        #region: View 1
        # View 1 frame
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_1_frame.grid_columnconfigure(0, weight=1)

        # Create view 1 title label
        self.view_1_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("view_1_title"), height=40, font=("Arial", 18), fg_color="#3669a0", text_color="#fff", corner_radius=5)
        
        # Showcase variables
        self.data_showcase = customtkinter.CTkTextbox(master=self.view_1_frame, height=62, wrap="none")
        self.data_showcase.tag_config("green", foreground="green")
        self.data_showcase.tag_config("purple", foreground="#bf00dd")
        print_color_coded(["green", "purple"], self.data_showcase, self.strings.get("data_showcase_segments"))
        
        # Explanation of variables
        self.var_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=314, fg_color="transparent", wrap="word", font=("Arial", 17))
        self.var_explanation.tag_config("green", foreground="green")
        self.var_explanation.tag_config("blue", foreground="#3d59d9")
        self.var_explanation.tag_config("purple", foreground="#bf00dd")
        print_color_coded(self.var_explanation.tag_names(), self.var_explanation, self.strings.get("var_explanation_segments"))
        #endregion

        #region: View 2
        self.view_2_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_2_frame.grid_columnconfigure(0, weight=1)

        
        #endregion

        #region: View 3
        #endregion


        # Create slide frame
        self.slide_frame = SlideFrame(master=self, fg_color="transparent", views=[self.view_1_frame])

        # Create layout
        self.create_layout()


    def create_layout(self):
        self.elem_x: float = 0.5

        # Layout
        # View 1 frame layout
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.data_showcase.grid(row=1, column=0, pady=10, sticky="we")
        self.var_explanation.grid(row=2, column=0, pady=10, sticky="we")
