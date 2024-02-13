import tkinter
import tkinter
import customtkinter
from ctk_widgets.CTk import CTkLabel, CTkButton, CTkOptionMenu
from frames import OutputFrame, StoringDataFrame

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

class MainTabview(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add tabs
        self.add("Output & Storing Data")
        self.add("Temporary")

        # Configure grid for "Output & Storing Data" tab
        self.tab("Output & Storing Data").grid_rowconfigure(0, weight=1)
        self.tab("Temporary").grid_columnconfigure(0, weight=1)

        self.output_frame = OutputFrame(master=self.tab("Output & Storing Data"), width=420, fg_color="#373737")
        self.output_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")
        self.output_frame.grid_columnconfigure(2, weight=1)

        self.data_frame = StoringDataFrame(master=self.tab("Output & Storing Data"), width=420, fg_color="#373737")
        self.data_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsw")
        self.data_frame.grid_columnconfigure(2, weight=1)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    
        # Ger user screen dimensions
        self.win_height = customtkinter.CTk.winfo_screenheight(self)

        # Configure window size
        self.title("Learn Python")
        self.geometry(f"{1155}x{self.win_height}")
        self.minsize(1155, self.win_height-120)

        # Configure grid layout
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar
        self.sidebar_frame = customtkinter.CTkFrame(master=self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Create sidebar title
        self.logo_label = customtkinter.CTkLabel(master=self.sidebar_frame, text="Python App", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create sidebar buttons
        self.sidebar_button_1 = CTkButton(
            master=self.sidebar_frame, gridargs={
                "row": 1,
                "column": 0,
                "padx": 20,
                "pady": (10, 0)
            },
            command=lambda *args: None
        )
        self.sidebar_button_2 = CTkButton(
            master=self.sidebar_frame, gridargs={
                "row": 2,
                "column": 0,
                "padx": 20,
                "pady": (10, 0)
            },
            command=lambda *args: None
        )
        self.sidebar_button_3 = CTkButton(
            master=self.sidebar_frame, gridargs={
                "row": 3,
                "column": 0,
                "padx": 20,
                "pady": (10, 0)
            },
            command=lambda *args: None
        )

        # Create appearance mode label and option meny
        self.appearance_mode_label = CTkLabel(
            master=self.sidebar_frame, gridargs={
                "row": 5,
                "column": 0,
                "padx": 20,
                "pady": (10, 0)
            }, text="Appearance Mode:"
        )
        self.appearance_mode_optionemenu = CTkOptionMenu(master=self.sidebar_frame, gridargs={
            "row": 6,
            "column": 0,
            "padx": 20,
            "pady": (10, 20)
        }, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event
        )

        self.main_tabview = MainTabview(master=self)
        self.main_tabview.grid(row=0, rowspan=3, column=1, columnspan=3, padx=20, pady=20, sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
