import customtkinter
from custom.textbox import textbox_args, COLORS
from custom.label import label_args
from funcs import generate_dict, generate_code_block, add_colors, check_input_answer, check_radio_answer, check_checkbox_answer
from frames import SlideFrame

class StoringDataFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

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
            #region: View 1
            "data_showcase": {
                "str": ">>> my_var = 10 >>> print(my_var) 10",
                "dict": {
                    "green": ["10"],
                    "purple": ["my_var"]
                }
            },
            "var_explanation": {
                "str": "Variables in python are used to store data for later use. They can store any type of value such as an integer, string, list, dictionary, expression, or even other variables. The way that you declare a  variable is by first coming up with a name. Next you put an = sign to tell python that whatever you are about to type should be stored under the name of the variable that you named. Finally, you type the value you wish to store. Later, if you need to access that value and use it, all you need to do is to reference the name of the variable. For example, if you wanted to print the value of the variable named, my_var, then you would type \"print(my_var)\", which would print the value of my_var to the terminal. Variables are also case sensitive, so if you have a variable named my_var, then you would need to type my_var exactly as it is to access the value stored under it. If you were to type My_var, my_Var, or MY_VAR, then python would not recognize those as the same variable.",
                "dict": {
                    "green": ["integer", "string", "list", "dictionary", "expression", "="],
                    "blue": ["terminal", "python", "case", "sensitive"],
                    "purple": ["Variables", "variables.", "variable.","name.", "named.", "my_var"],
                },
            },
            #endregion
            #region: View 2
            "var_examples": {
                "Token.Literal.String.Double": ["Hello! How are you?"],
            },
            #endregion
            #region: View 4
            "problem1_code": {
                "Token.Literal.String.Double": ["Variables", "in", "Python"],
            },
            "problem3_code": {
                "Token.Literal.String.Double": ["Year", "Month", "Day"],
            }
            #endregion
        }

        self.strings = {
            #region: View 1
            "view_1_title": "Storing Data in Python",
            "data_showcase": ">>> my_var = 10\n>>> print(my_var)\n10",
            "var_explanation_segments": generate_dict(self.color_dicts, "var_explanation", var_explanation_pre_run, var_explanation_post_run),
            #endregion
            #region: View 2
            "view_2_title": "Examples of Storing Data in Python",
            "var_examples": ">>> my_number = 10\n>>> print(my_number)\n10\n>>>\n>>> greeting = \"Hello! How are you?\"\n>>> print(greeting)\nHello! How are you?\n>>>\n>>> shopping_list = [\"apples\", \"bananas\", \"milk\"]\n>>> print(shopping_list)\n[\"apples\", \"bananas\", \"milk\"]\n>>>\n>>> cart = {\"apples\": 1.49, \"bananas\": 1.69, \"milk\": 3.99}\n>>> print(cart)\n{\"apples\": 1.49, \"bananas\": 1.69, \"milk\": 3.99}\n>>>\n>>> num1 = 15\n>>> num2 = 9\n>>> num3 = num1 + num2\n>>> print(num3, num1 + num2)\n24 24",
            #endregion
            #region: View 3
            "view_3_title": "Time to Practice!",
            "q1": "1. What is the output of the following code?",
            "q1_code": ">>> x = 10\n>>> print(x)",
            "q1_ans": "10",
            "q2": "2. Which of the following will correctly assign the string \"Python\" to a variable named language?",
            "q2_opt1": "language = Python",
            "q2_opt2": "language = \"Python\"",
            "q2_opt3": "language: \"Python\"",
            "q2_ans": 2,
            "q3": "3. Check all that are true about variables in Python.",
            "q3_check1": "Variables can store strings",
            "q3_check2": "Variables can store numbers",
            "q3_check3": "Variables are NOT case sensitive",
            "q3_ans": [1, 1, 0],
            #endregion
            #region: View 4
            "view_4_title": "Now try it yourself!",
            "problem1": "1. Create a variable assignment statement with the variable name \"str\" that would result in the following code as its output when printed.",
            "problem1_code": "Variables in Python",
            "problem1_ans": "str = \"Variables in Python\"",
            "problem2": "2. Create a variable assignment statement with the variable name \"my_shopping_list\" that would result in the following code as its output when printed.",
            "problem2_code": "[\"apples\", \"oranges\", \"bananas\", \"milk\"]",
            "problem2_ans": "my_shopping_list = [\"apples\", \"oranges\", \"bananas\", \"milk\"]",
            "problem3": "3. Finally, create a variable assignment statement with the variable name \"user\" that would result in the following code as its output when printed.",
            "problem3_code": "{ \"id\": 1, \"name\": \"John\", \"age\": 30 }",
            "problem3_ans": "user = { \"id\": 1, \"name\": \"John\", \"age\": 30 }"
            #endregion
        }

        #region: Declare frames
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_1_frame.grid_columnconfigure(0, weight=1)
        self.view_2_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_2_frame.grid_columnconfigure(0, weight=1)
        self.view_3_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_3_frame.grid_columnconfigure(0, weight=1)
        self.view_4_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_4_frame.grid_columnconfigure(0, weight=1)
        #endregion

        #region: View 1
        # Create view 1 title label
        self.view_1_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("view_1_title"), **label_args)
        
        # Showcase variables
        self.data_showcase = customtkinter.CTkTextbox(master=self.view_1_frame, height=62)
        generate_code_block(code=self.strings.get("data_showcase"), textbox=self.data_showcase)
        
        # Explanation of variables
        self.var_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=392, **textbox_args)
        add_colors(self.var_explanation, {"green": COLORS["GREEN"], "blue": COLORS["BLUE"], "purple": COLORS["PURPLE"]}, self.strings.get("var_explanation_segments"))
        #endregion

        #region: View 2
        # Create view 2 title label
        self.view_2_title = customtkinter.CTkLabel(master=self.view_2_frame, text=self.strings.get("view_2_title"), **label_args)
        self.var_examples = customtkinter.CTkTextbox(master=self.view_2_frame, height=350)
        generate_code_block(code=self.strings.get("var_examples"), textbox=self.var_examples, phrases=self.color_dicts.get("var_examples"))
        #endregion

        #region: View 3
        # Create view 3 title label
        self.view_3_title = customtkinter.CTkLabel(master=self.view_3_frame, text=self.strings.get("view_3_title"), **label_args)

        #region: Question 1
        self.q1_frame = customtkinter.CTkFrame(master=self.view_3_frame, fg_color="transparent")
        self.q1_frame.grid_columnconfigure(0, weight=1)
        self.q1 = customtkinter.CTkLabel(master=self.q1_frame, text=self.strings.get("q1"), height=15, font=("Arial", 15), anchor="w")
        self.q1_code = customtkinter.CTkTextbox(master=self.q1_frame, height=46)
        self.q1_code.tag_config("green", foreground="green")
        generate_code_block(code=self.strings.get("q1_code"), textbox=self.q1_code, phrases=self.color_dicts.get("print_showcase"))
        self.q1_subframe = customtkinter.CTkFrame(master=self.q1_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.q1_input = customtkinter.CTkEntry(master=self.q1_subframe, placeholder_text="Answer")
        self.q1_btn = customtkinter.CTkButton(
            master=self.q1_subframe,
            text="Enter", width=80,
            command=lambda: check_input_answer(
                filename="storing_data_frame.py",
                correct_answers=[self.strings.get("q1_ans")],
                input=self.q1_input.get(),
                btn=self.q1_btn,
                update_textbox=True,
                new_ht=62,
                textbox=self.q1_code,
                tag="Token.Literal.Number.Integer"
            )
        )        # endregion
        #endregion

        #region: Question 2
        self.q2_frame = customtkinter.CTkFrame(master=self.view_3_frame, fg_color="transparent")
        self.q2_frame.grid_columnconfigure(0, weight=1)
        self.q2 = customtkinter.CTkLabel(master=self.q2_frame, text=self.strings.get("q2"), height=15, font=("Arial", 15), anchor="w", justify="left", wraplength=383)
        self.q2_radio_frame = customtkinter.CTkFrame(master=self.q2_frame, fg_color="transparent")
        self.q2_var = customtkinter.IntVar(value=0)
        self.q2_opt1 = customtkinter.CTkRadioButton(master=self.q2_radio_frame, text=self.strings.get("q2_opt1"), variable=self.q2_var, value=1)
        self.q2_opt2 = customtkinter.CTkRadioButton(self.q2_radio_frame, text=self.strings.get("q2_opt2"), variable=self.q2_var, value=2)
        self.q2_opt3 = customtkinter.CTkRadioButton(master=self.q2_radio_frame, text=self.strings.get("q2_opt3"), variable=self.q2_var, value=3)
        self.q2_btn = customtkinter.CTkButton(
            master=self.q2_frame,
            text="Enter",
            command=lambda: check_radio_answer(
                filename="storing_data_frame.py",
                radio_buttons=[self.q2_opt1, self.q2_opt2, self.q2_opt3],
                q_btn=self.q2_btn,
                q_var=self.q2_var,
                correct_answer=self.strings.get("q2_ans")
            )
        )
        # endregion

        #region: Question 3
        self.q3_frame = customtkinter.CTkFrame(master=self.view_3_frame, fg_color="transparent")
        self.q3_frame.grid_columnconfigure(0, weight=1)
        self.q3 = customtkinter.CTkLabel(master=self.q3_frame, text=self.strings.get("q3"), height=15, font=("Arial", 15), anchor="w")
        self.q3_check_frame = customtkinter.CTkFrame(master=self.q3_frame, fg_color="transparent")
        self.q3_check1 = customtkinter.CTkCheckBox(master=self.q3_check_frame, text=self.strings.get("q3_check1"))
        self.q3_check2 = customtkinter.CTkCheckBox(master=self.q3_check_frame, text=self.strings.get("q3_check2"))
        self.q3_check3 = customtkinter.CTkCheckBox(master=self.q3_check_frame, text=self.strings.get("q3_check3"))
        self.q3_btn = customtkinter.CTkButton(
            master=self.q3_frame,
            text="Enter",
            command=lambda: check_checkbox_answer(
                filename="storing_data_frame.py",
                checkboxes=[self.q3_check1, self.q3_check2, self.q3_check3],
                q_btn=self.q3_btn,
                correct_answer=self.strings.get("q3_ans")
            )
        )
        #endregion
        
        #endregion

        #region: View 4
        # Create view 4 title label
        self.view_4_title = customtkinter.CTkLabel(master=self.view_4_frame, text=self.strings.get("view_4_title"), **label_args)
        
        #region: Problem 1
        self.problem1_title = customtkinter.CTkLabel(master=self.view_4_frame, text=self.strings.get("problem1"), font=("Arial", 15), justify="left", wraplength=383)
        self.problem1_code = customtkinter.CTkTextbox(master=self.view_4_frame, height=15)
        self.problem1_code.tag_config("green", foreground="green")
        self.problem1_code.tag_config("orange", foreground="orange")
        generate_code_block(code=self.strings.get("problem1_code"), textbox=self.problem1_code, phrases=self.color_dicts.get("problem1_code"))
        self.problem1_subframe = customtkinter.CTkFrame(master=self.view_4_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.problem1_input = customtkinter.CTkEntry(master=self.problem1_subframe, placeholder_text="Answer")
        self.problem1_btn = customtkinter.CTkButton(
            master=self.problem1_subframe,
            text="Enter",
            width=80,
            command=lambda: check_input_answer(
                filename="storing_data_frame.py",
                correct_answers=[self.strings.get("problem1_ans")],
                input=self.problem1_input.get(),
                btn=self.problem1_btn,
                update_textbox=False
                
            )
        )
        # endregion

        #region: Problem 2
        self.problem2_title = customtkinter.CTkLabel(master=self.view_4_frame, text=self.strings.get("problem2"), font=("Arial", 15), justify="left", wraplength=383)
        self.problem2_code = customtkinter.CTkTextbox(master=self.view_4_frame, height=15)
        self.problem2_code.tag_config("green", foreground="green")
        self.problem2_code.tag_config("orange", foreground="orange")
        generate_code_block(code=self.strings.get("problem2_code"), textbox=self.problem2_code, phrases=self.color_dicts.get("problem2_code"))
        self.problem2_subframe = customtkinter.CTkFrame(master=self.view_4_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.problem2_input = customtkinter.CTkEntry(master=self.problem2_subframe, placeholder_text="Answer")
        self.problem2_btn = customtkinter.CTkButton(
            master=self.problem2_subframe,
            text="Enter",
            width=80,
            command=lambda: check_input_answer(
                filename="storing_data_frame.py",
                correct_answers=[self.strings.get("problem2_ans")],
                input=self.problem2_input.get(),
                btn=self.problem2_btn,
                update_textbox=False
            )
        )
        # endregion

        #region: Problem 3
        self.problem3_title = customtkinter.CTkLabel(master=self.view_4_frame, text=self.strings.get("problem3"), font=("Arial", 15), justify="left", wraplength=383)
        self.problem3_code = customtkinter.CTkTextbox(master=self.view_4_frame, height=15)
        self.problem3_code.tag_config("green", foreground="green")
        self.problem3_code.tag_config("orange", foreground="orange")
        generate_code_block(code=self.strings.get("problem3_code"), textbox=self.problem3_code, phrases=self.color_dicts.get("problem3_code"))
        self.problem3_subframe = customtkinter.CTkFrame(master=self.view_4_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.problem3_input = customtkinter.CTkEntry(master=self.problem3_subframe, placeholder_text="Answer")
        self.problem3_btn = customtkinter.CTkButton(
            master=self.problem3_subframe,
            text="Enter",
            width=80,
            command=lambda: check_input_answer(
                filename="storing_data_frame.py",
                correct_answers=[self.strings.get("problem3_ans")],
                input=self.problem3_input.get(),
                btn=self.problem3_btn,
                update_textbox=False
            )
        )
        # endregion

        #endregion

        # Create slide frame
        self.slide_frame = SlideFrame(master=self, fg_color="transparent", views=[self.view_1_frame, self.view_2_frame, self.view_3_frame, self.view_4_frame])

        # Create layout
        self.create_layout()

    def create_layout(self):
        self.elem_x: float = 0.5

        # Layout
        #region: View 1
        # View 1 frame layout
        self.view_1_frame.place(relx=self.elem_x, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.data_showcase.grid(row=1, column=0, pady=10, sticky="we")
        self.var_explanation.grid(row=2, column=0, pady=10, sticky="we")
        #endregion

        #region: View 2
        # View 2 frame layout
        self.view_2_frame.place(relx=self.elem_x+1, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_2_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.var_examples.grid(row=1, column=0, pady=10, sticky="we")
        #endregion

        #region: View 3
        # View 3 frame layout
        self.view_3_frame.place(relx=self.elem_x+2, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_3_title.grid(row=0, column=0, pady=(0, 5), sticky="we")

        #region: Question 1
        # Question 1 frame layout
        self.q1_frame.grid(row=1, column=0, pady=10, sticky="we")
        self.q1.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.q1_code.grid(row=1, column=0, pady=5, sticky="we")
        self.q1_subframe.grid(row=2, column=0, pady=(5, 0), sticky="we")
        self.q1_input.pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.q1_btn.pack(side="left")
        #endregion

        #region: Question 2
        # Question 2 frame layout
        self.q2_frame.grid(row=2, column=0, pady=(0, 5), sticky="we")
        self.q2.grid(row=0, column=0, pady=5, sticky="we")
        self.q2_radio_frame.grid(row=1, column=0, pady=5, sticky="we")
        self.q2_opt1.grid(row=2, column=0, pady=5, sticky="we")
        self.q2_opt2.grid(row=3, column=0, pady=5, sticky="we")
        self.q2_opt3.grid(row=4, column=0, pady=5, sticky="we")
        self.q2_btn.grid(row=5, column=0, pady=5, sticky="we")
        #endregion

        #region: Question 3
        # Question 3 frame layout
        self.q3_frame.grid(row=3, column=0, pady=(0, 5), sticky="we")
        self.q3.grid(row=0, column=0, pady=5, sticky="we")
        self.q3_check_frame.grid(row=1, column=0, pady=5, sticky="we")
        self.q3_check1.grid(row=2, column=0, pady=5, sticky="we")
        self.q3_check2.grid(row=3, column=0, pady=5, sticky="we")
        self.q3_check3.grid(row=4, column=0, pady=5, sticky="we")
        self.q3_btn.grid(row=5, column=0, pady=5, sticky="we")
        #endregion
        
        #endregion

        #region: View 4
        # View 4 frame layout
        self.view_4_frame.place(relx=self.elem_x+3, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_4_title.grid(row=0, column=0, pady=(0, 5), sticky="we")

        #region: Problem 1
        # Problem 1 frame layout
        self.problem1_title.grid(row=1, column=0, pady=(10, 5), sticky="we")
        self.problem1_code.grid(row=2, column=0, pady=5, sticky="we")
        self.problem1_subframe.grid(row=3, column=0, pady=(5, 0), sticky="we")
        self.problem1_input.pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.problem1_btn.pack(side="left")
        #endregion

        #region: Problem 2
        # Problem 2 frame layout
        self.problem2_title.grid(row=4, column=0, pady=(15, 5), sticky="we")
        self.problem2_code.grid(row=5, column=0, pady=5, sticky="we")
        self.problem2_subframe.grid(row=6, column=0, pady=(5, 0), sticky="we")
        self.problem2_input.pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.problem2_btn.pack(side="left")
        #endregion

        #region: Problem 3
        # Problem 3 frame layout
        self.problem3_title.grid(row=7, column=0, pady=(15, 5), sticky="we")
        self.problem3_code.grid(row=8, column=0, pady=5, sticky="we")
        self.problem3_subframe.grid(row=9, column=0, pady=(5, 0), sticky="we")
        self.problem3_input.pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.problem3_btn.pack(side="left")
        #endregion

        #endregion
