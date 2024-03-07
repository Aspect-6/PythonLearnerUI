import customtkinter
from frames import OutputFrame, DataTypesFrame, StoringDataFrame, EmbeddedShell

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class MainTabview(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add tabs
        self.add("Output & Data Types")
        self.add("Temporary")

        # Configure grid for "Output & Data Types" tab
        self.tab("Output & Data Types").grid_rowconfigure(0, weight=1)
        self.tab("Temporary").grid_columnconfigure(0, weight=1)

        self.output_frame = OutputFrame(master=self.tab("Output & Data Types"), width=420, fg_color="#373737")
        self.output_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")
        self.output_frame.grid_columnconfigure(2, weight=1)

        self.data_frame = DataTypesFrame(master=self.tab("Output & Data Types"), width=420, fg_color="#373737")
        self.data_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsw")
        self.data_frame.grid_columnconfigure(2, weight=1)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Ger user screen dimensions
        self.win_height = customtkinter.CTk.winfo_screenheight(self)

        # Configure window size
        self.title("Learn Python")
        self.geometry(f"{1155}x{780}")
        self.minsize(1155, 780)

        # Configure grid layout
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)

        #region: Sidebar

        # Create sidebar
        self.sidebar_frame = customtkinter.CTkFrame(master=self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Create sidebar title
        self.logo_label = customtkinter.CTkLabel(master=self.sidebar_frame, text="Python App", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create sidebar buttons
        self.sidebar_button_1 = customtkinter.CTkButton(master=self.sidebar_frame, text="Terminal Overlay", command=self.append_terminal)
        self.sidebar_button_2 = customtkinter.CTkButton(master=self.sidebar_frame, text="Python Shell Overlay", command=self.append_pythonshell)
        self.sidebar_button_3 = customtkinter.CTkButton(master=self.sidebar_frame, text="Button 3", command=lambda *args: None)

        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=(10, 0))

        # Create appearance mode label and option meny
        self.appearance_mode_label = customtkinter.CTkLabel(master=self.sidebar_frame, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=self.sidebar_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))
        #endregion

        self.main_tabview = MainTabview(master=self)
        self.main_tabview.grid(row=0, rowspan=3, column=1, columnspan=3, padx=20, pady=20, sticky="nsew")

        # Create shell frame
        self.shell_frame = customtkinter.CTkFrame(master=self)
        self.shell_frame.grid_columnconfigure(0, weight=1)
        self.shell_frame.grid_rowconfigure(0, weight=1)

        # Create embedded terminal and python shell
        self.embedded_terminal = EmbeddedShell(master=self.shell_frame, ispythonshell=False)
        self.pythonshell = EmbeddedShell(master=self.shell_frame, ispythonshell=True)

    def append_terminal(self):
        # If the shell frame is not in the grid
        if self.shell_frame.grid_info() == {}:
            # Add the shell frame to the grid
            self.shell_frame.grid(row=0, rowspan=3, column=1, columnspan=3, padx=20, pady=20, sticky="nsew")
            # Add the embedded terminal to the shell frame
            self.pythonshell.grid_forget()
            self.embedded_terminal.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        elif self.pythonshell.grid_info() != {}:
            # If the python shell is in the shell frame, remove it, and add the embedded terminal
            self.embedded_terminal.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.pythonshell.grid_forget()
        else:
            self.shell_frame.grid_forget()

    def append_pythonshell(self):
        # If the shell frame is not in the grid
        if self.shell_frame.grid_info() == {}:
            # Add the shell frame to the grid
            self.shell_frame.grid(row=0, rowspan=3, column=1, columnspan=3, padx=20, pady=20, sticky="nsew")
            # Add the embedded terminal to the shell frame
            self.embedded_terminal.grid_forget()
            self.pythonshell.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        elif self.embedded_terminal.grid_info() != {}:
            # If the embedded terminal is in the shell frame, remove it, and add the python shell
            self.pythonshell.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.embedded_terminal.grid_forget()
        else:
            self.shell_frame.grid_forget()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
