import tkinter
import customtkinter
from custom.textbox import textbox_args, add_colors
from custom.label import label_args
from frames import SlideFrame
from funcs import generate_dict, generate_code_block


class OutputFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.color_dicts = {
            #region: View 1
            "print_showcase": {
                "Token.Literal.String.Double": ["Hello World!"],
            },
            "print_explanation": {
                "str": "The \"print()\" statement is a built-in function in python that writes a message to the terminal. It takes in any type of value such as an integer, string, list, dictionary, a variable, or even an expression. The syntax of the \"print()\" statement is the word \"print\", followed by \"()\", and then the value that you wish to print between the parentheses. The print statement can also be used to print multiple values. All you have to do is separate each value you wish to print with a comma. The output will be each value separated by a space.",
                "dict": {
                    "green": ["print()", "integer", "string", "list", "dictionary", "variable", "expression", "print", "\"()\"", "comma", "value", "space"],
                    "blue": ["built-in", "terminal", "output"]
                }
            },
            "print_examples": {
                "Token.Literal.String.Double": ["Python is awesome!"],
            },
            #endregion
            #region: View 3
            "problem1_code": {
                "Token.Literal.String.Double": ["Hello!"],
            },
            "problem2_code": {
                "Token.Literal.String.Double": ["Learning Python"],
            },
            "problem3_code": {
                "Token.Literal.String.Double": ["Year", "Month", "Day"],
            }
            #endregion
        }

        self.strings = {
            # region: View 1
            "view_1_title": "Rendering Output in the Terminal",
            "print_showcase": ">>> print(\"Hello World!\")\nHello World!",
            "print_explanation_segments": generate_dict(self.color_dicts, "print_explanation"),
            "print_examples_title": "Examples of Printing Different Values",
            "print_examples": ">>> print(10)\n10\n>>> print(\"Python is awesome!\")\nPython is awesome!\n>>> print(10, \"Python is awesome!\")\n10 Python is awesome!",
            # endregion
            # region: View 2
            "view_2_title": "Time to Practice!",
            "q1": "1. What is the output of the following code?",
            "q1_code": ">>> print(5)",
            "q2": "2. Which of the following will print the output: \"Python\"?",
            "q2_opt1": "print(Python)",
            "q2_opt2": "print(\"Python\")",
            "q2_opt3": "print(\"Python)",
            "q3": "3. Check all that is true about the print() statement.",
            "q3_check1": "It can print strings",
            "q3_check2": "It CANNOT print multiple values",
            "q3_check3": "It shows output to the user",
            # endregion
            # region: View 3
            "view_3_title": "Now try it Yourself!",
            "problem1": "1. Create a print() statement would print following code as its output.",
            "problem1_code": "Hello! 351",
            "problem1_ans": "print(\"Hello!\", 351)",
            "problem2": "2. Create a print() statement would print following code as its output. *Hint: There are multiple correct answers",
            "problem2_code": "124 Learning Python 435",
            "problem2_ans1": "print(124, \"Learning\", \"Python\", 435)",
            "problem2_ans2": "print(124, \"Learning Python\", 435)",
            "problem3": "3. Finally, create a print() statement would print code as its output.",
            "problem3_code": "Year 1975 Month 5 Day 8",
            "problem3_ans": "print(\"Year\", 1975, \"Month\", 5, \"Day\", 8)"
            # endregion
        }

        """
        # View 1: Rendering output in the terminal
        ----------------------------------------------------------------
        # Learning about what the print statement does, what it can take
        # in as arguments, and the correct syntax of the print statement
        # and its arguments.
        """
        # region: View 1
        # View 1 frame
        self.view_1_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_1_frame.grid_columnconfigure(0, weight=1)

        # Create view 1 title label
        self.view_1_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("view_1_title"), **label_args)

        # Showcase print() statement
        self.print_showcase = customtkinter.CTkTextbox(master=self.view_1_frame, height=46, wrap="word")
        generate_code_block(code=self.strings.get("print_showcase"), textbox=self.print_showcase, phrases=self.color_dicts.get("print_showcase"))

        # Explanation of print() statement
        self.print_explanation = customtkinter.CTkTextbox(master=self.view_1_frame, height=230, **textbox_args)
        add_colors(self.print_explanation, {"green": "green", "blue": "#3d59d9"}, self.strings.get("print_explanation_segments"))

        # Example title
        self.example_title = customtkinter.CTkLabel(master=self.view_1_frame, text=self.strings.get("print_examples_title"), **label_args)
        # Examples of print() statement
        self.print_examples = customtkinter.CTkTextbox(master=self.view_1_frame, height=110, wrap="word")
        # add_colors(self.print_examples, {"green": "green", "orange": "orange"}, self.strings.get("print_examples_segments"))
        
        generate_code_block(code=self.strings.get("print_examples"), textbox=self.print_examples, phrases=self.color_dicts.get("print_examples"))
        # endregion

        """
        # View 2: Time to practice!
        ----------------------------------------------------------------
        # Determining the output of a print statement, selecting the
        # correct syntax of a print statement, and determining all true
        # properties about the print statement.
        """
        # region: View 2
        # View 2 frame
        self.view_2_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_2_frame.grid_columnconfigure(0, weight=1)

        # Create view 2 title label
        self.view_2_title = customtkinter.CTkLabel(master=self.view_2_frame, text=self.strings.get("view_2_title"), **label_args)

        # region: Question 1
        self.q1_frame = customtkinter.CTkFrame(master=self.view_2_frame, fg_color="transparent")
        self.q1_frame.grid_columnconfigure(0, weight=1)
        self.q1 = customtkinter.CTkLabel(master=self.q1_frame, text=self.strings.get( "q1"), height=15, font=("Arial", 15), anchor="w")
        self.q1_code = customtkinter.CTkTextbox(master=self.q1_frame, height=15)
        self.q1_code.tag_config("green", foreground="green")
        generate_code_block(code=self.strings.get("q1_code"), textbox=self.q1_code, phrases=self.color_dicts.get("print_showcase"))
        self.q1_subframe = customtkinter.CTkFrame(master=self.q1_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.q1_input = customtkinter.CTkEntry(master=self.q1_subframe, placeholder_text="Answer")
        self.q1_btn = customtkinter.CTkButton(master=self.q1_subframe, text="Enter", width=80, command=lambda: self.check_input_answer(["5"], self.q1_input.get(), self.q1_btn, True, self.q1_code, "green"))
        # endregion

        # region: Question 2
        self.q2_frame = customtkinter.CTkFrame(master=self.view_2_frame, fg_color="transparent")
        self.q2_frame.grid_columnconfigure(0, weight=1)
        self.q2 = customtkinter.CTkLabel(master=self.q2_frame, text=self.strings.get( "q2"), height=15, font=("Arial", 15), anchor="w")
        self.q2_radio_frame = customtkinter.CTkFrame(master=self.q2_frame, fg_color="transparent")
        self.q2_var = tkinter.IntVar(value=0)
        self.q2_opt1 = customtkinter.CTkRadioButton(master=self.q2_radio_frame, text=self.strings.get("q2_opt1"), variable=self.q2_var, value=1)
        self.q2_opt2 = customtkinter.CTkRadioButton(self.q2_radio_frame, text=self.strings.get("q2_opt2"), variable=self.q2_var, value=2)
        self.q2_opt3 = customtkinter.CTkRadioButton(master=self.q2_radio_frame, text=self.strings.get("q2_opt3"), variable=self.q2_var, value=3)
        self.q2_btn = customtkinter.CTkButton(master=self.q2_frame, text="Enter")
        # endregion

        # region: Question 3
        self.q3_frame = customtkinter.CTkFrame(master=self.view_2_frame, fg_color="transparent")
        self.q3_frame.grid_columnconfigure(0, weight=1)
        self.q3 = customtkinter.CTkLabel(master=self.q3_frame, text=self.strings.get("q3"), height=15, font=("Arial", 15), anchor="w")
        self.q3_check_frame = customtkinter.CTkFrame(master=self.q3_frame, fg_color="transparent")
        self.q3_check1 = customtkinter.CTkCheckBox(master=self.q3_check_frame, text=self.strings.get("q3_check1"))
        self.q3_check2 = customtkinter.CTkCheckBox(master=self.q3_check_frame, text=self.strings.get("q3_check2"))
        self.q3_check3 = customtkinter.CTkCheckBox(master=self.q3_check_frame, text=self.strings.get("q3_check3"))
        self.q3_btn = customtkinter.CTkButton(master=self.q3_frame, text="Enter")
        # endregion

        # endregion

        """
        # View 3: Now try it yourself!
        ----------------------------------------------------------------
        # Building print statements to output given lines of text.
        """
        # region: View 3
        # View 3 frame
        self.view_3_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.view_3_frame.grid_columnconfigure(0, weight=1)

        # Create view 3 title label
        self.view_3_title = customtkinter.CTkLabel(master=self.view_3_frame, text=self.strings.get("view_3_title"), **label_args)

        # region: Problem 1
        self.problem1_title = customtkinter.CTkLabel(master=self.view_3_frame, text=self.strings.get("problem1"), font=("Arial", 15), justify="left", wraplength=383)
        self.problem1_code = customtkinter.CTkTextbox(master=self.view_3_frame, height=15)
        self.problem1_code.tag_config("green", foreground="green")
        self.problem1_code.tag_config("orange", foreground="orange")
        generate_code_block(code=self.strings.get("problem1_code"), textbox=self.problem1_code, phrases=self.color_dicts.get("problem1_code"))
        self.problem1_subframe = customtkinter.CTkFrame(master=self.view_3_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.problem1_input = customtkinter.CTkEntry(master=self.problem1_subframe, placeholder_text="Answer")
        self.problem1_btn = customtkinter.CTkButton(master=self.problem1_subframe, text="Enter", width=80,
                                                    command=lambda: self.check_input_answer([self.strings.get("problem1_ans")], self.problem1_input.get(), self.problem1_btn, False))
        # endregion

        # region: Problem 2
        self.problem2_title = customtkinter.CTkLabel(master=self.view_3_frame, text=self.strings.get("problem2"), font=("Arial", 15), justify="left", wraplength=383)
        self.problem2_code = customtkinter.CTkTextbox(master=self.view_3_frame, height=15)
        self.problem2_code.tag_config("green", foreground="green")
        self.problem2_code.tag_config("orange", foreground="orange")
        generate_code_block(code=self.strings.get("problem2_code"), textbox=self.problem2_code, phrases=self.color_dicts.get("problem2_code"))
        self.problem2_subframe = customtkinter.CTkFrame(master=self.view_3_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.problem2_input = customtkinter.CTkEntry(master=self.problem2_subframe, placeholder_text="Answer")
        self.problem2_btn = customtkinter.CTkButton(master=self.problem2_subframe, text="Enter", width=80,
                                                    command=lambda: self.check_input_answer([self.strings.get("problem2_ans1"), self.strings.get("problem2_ans2")], self.problem2_input.get(), self.problem2_btn, False))
        # endregion

        # region: Problem 3
        self.problem3_title = customtkinter.CTkLabel(master=self.view_3_frame, text=self.strings.get("problem3"), font=("Arial", 15), justify="left", wraplength=383)
        self.problem3_code = customtkinter.CTkTextbox(master=self.view_3_frame, height=15)
        self.problem3_code.tag_config("green", foreground="green")
        self.problem3_code.tag_config("orange", foreground="orange")
        generate_code_block(code=self.strings.get("problem3_code"), textbox=self.problem3_code, phrases=self.color_dicts.get("problem3_code"))
        self.problem3_subframe = customtkinter.CTkFrame(master=self.view_3_frame, fg_color="transparent")
        self.q1_subframe.grid_columnconfigure(0, weight=1)
        self.problem3_input = customtkinter.CTkEntry(master=self.problem3_subframe, placeholder_text="Answer")
        self.problem3_btn = customtkinter.CTkButton(master=self.problem3_subframe, text="Enter", width=80,
                                                    command=lambda: self.check_input_answer([self.strings.get("problem3_ans")], self.problem3_input.get(), self.problem3_btn, False))
        # endregion

        # endregion

        # Create slide frame
        SlideFrame(master=self, fg_color="transparent", views=[self.view_1_frame, self.view_2_frame, self.view_3_frame])

        # Create layout
        self.create_layout()

    def check_input_answer(self, correct_answers: list[str], input: str, btn: customtkinter.CTkButton, updateTextbox: bool, textbox: customtkinter.CTkTextbox = None, color: str = ""):
        if isinstance(correct_answers, list):
            for correct in correct_answers:
                if input == correct:
                    if textbox is not None:
                        if updateTextbox is True:
                            textbox.configure(state="normal")
                            textbox.insert("end", f"\n{correct}", color)
                            textbox.configure(state="disabled", height=46)
                    btn.configure(state="disabled")
        elif input == correct_answers:
            if textbox is not None:
                textbox.configure(state="normal")
                textbox.insert("end", f"\n{correct_answers}", color)
                textbox.configure(state="disabled", height=46)
            btn.configure(state="disabled")

    def check_radio_answer(self): pass

    def create_layout(self):
        # Layout

        #region: View 1
        # View 1 frame layout
        self.view_1_frame.place(relx=0.5, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_1_title.grid(row=0, column=0, pady=(0, 5), sticky="we")
        self.print_showcase.grid(row=1, column=0, pady=10, sticky="we")
        self.print_explanation.grid(row=2, column=0, pady=(5, 10), sticky="we")
        self.example_title.grid(row=3, column=0, pady=10, sticky="we")
        self.print_examples.grid(row=4, column=0, pady=10, sticky="we")
        #endregion

        #region: View 2
        # View 2 frame layout
        self.view_2_frame.place(relx=1.5, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_2_title.grid(row=0, column=0, pady=(0, 5), sticky="we")

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
        self.q2_frame.grid(row=2, column=0, pady=(10, 5), sticky="we")
        self.q2.grid(row=0, column=0, pady=5, sticky="we")
        self.q2_radio_frame.grid(row=1, column=0, pady=5, sticky="we")
        self.q2_opt1.grid(row=2, column=0, pady=5, sticky="we")
        self.q2_opt2.grid(row=3, column=0, pady=5, sticky="we")
        self.q2_opt3.grid(row=4, column=0, pady=5, sticky="we")
        self.q2_btn.grid(row=5, column=0, pady=5, sticky="we")
        #endregion

        #region: Question 3
        # Question 3 frame layout
        self.q3_frame.grid(row=3, column=0, pady=(10, 5), sticky="we")
        self.q3.grid(row=0, column=0, pady=5, sticky="we")
        self.q3_check_frame.grid(row=1, column=0, pady=5, sticky="we")
        self.q3_check1.grid(row=2, column=0, pady=5, sticky="we")
        self.q3_check2.grid(row=3, column=0, pady=5, sticky="we")
        self.q3_check3.grid(row=4, column=0, pady=5, sticky="we")
        self.q3_btn.grid(row=5, column=0, pady=5, sticky="we")
        #endregion

        #endregion

        #region: View 3
        # View 3 frame layout
        self.view_3_frame.place(relx=2.5, rely=0.5, relheight=0.95, relwidth=0.9, anchor="center")
        self.view_3_title.grid(row=0, column=0, pady=(0, 5), sticky="we")

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
