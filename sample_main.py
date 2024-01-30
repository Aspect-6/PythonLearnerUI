import tkinter
import customtkinter
from ctk_widgets.CTk import CTkTabview, CTkLabel, CTkOptionMenu, CTkButton, CTkRadioButton, CTkProgressBar, CTkSlider, CTkSwitch, CTkCheckBox, CTkSegmentedButton, CTkTextbox, CTkEntry, CTkTabview, CTkLabel, CTkOptionMenu, CTkButton


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


# Main app class that runs everything
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Learn Python")
        self.geometry(f"{1100}x{580}")

        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Create sidebar
        self.sidebar_frame = customtkinter.CTkFrame(master=self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Create sidebar title
        self.logo_label = customtkinter.CTkLabel(
            master=self.sidebar_frame, text="Python App", font=customtkinter.CTkFont(size=20, weight="bold"))
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

        # Create main entry and button
        self.main_entry = CTkEntry(master=self, placeholder_text="CTkEntry", gridargs={
                "row": 3,
                "column": 1,
                "columnspan": 2,
                "padx": (20, 0),
                "pady": (20, 20),
                "sticky": "nsew"
            }
        )

        self.entry_button = CTkButton(master=self, gridargs={
                "row": 3,
                "column": 3,
                "padx": (20, 20),
                "pady": (20, 20),
                "sticky": "nsew"
            }, command=lambda *args: None
        )

        # Create textbox
        self.textbox = CTkTextbox(master=self, width=250, gridargs={
                "row": 0,
                "column": 1,
                "padx": (20, 0),
                "pady": (20, 0),
                "sticky": "nsew"
            }
        )
        self.textbox.insert("0.0", "CTkTextbox\n\n" +
                            "Drew Everley is stoopid.\n\n" * 20)

        # Create tabview
        self.tabview = CTkTabview(master=self, gridargs={
            "row": 0,
            "column": 2,
            "columnspan": 1,
            "padx": (20, 0),
            "pady": (20, 0),
            "sticky": "nsew"
        }, tabs=["CTkTabview", "Tab 1", "Tab 2"])

        # Create radiobutton frame and group
        self.radiobutton_frame = customtkinter.CTkFrame(master=self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = CTkLabel(master=self.radiobutton_frame,
            text="CTkRadioButton Group:", gridargs={
                "row": 0,
                "column": 2,
                "columnspan": 1,
                "padx": 10,
                "pady": 10,
                "sticky": ""
            }
        )

        # Create radiobuttons
        self.radio_button_1 = CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
            gridargs={
                "row": 1,
                "column": 2,
                "padx": 10,
                "pady": 10,
                "sticky": "n"
            },
            value=0
        )
        self.radio_button_2 = CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
            gridargs={
                "row": 2,
                "column": 2,
                "padx": 10,
                "pady": 10,
                "sticky": "n"
            },
            value=1
        )
        self.radio_button_3 = CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
            gridargs={
                "row": 3,
                "column": 2,
                "padx": 10,
                "pady": 10,
                "sticky": "n"
            },
            value=2
        )

        # Create progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(master=self)
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # Create segmented button
        self.seg_button_1 = CTkSegmentedButton(master=self.slider_progressbar_frame, gridargs={
                "row": 0,
                "column": 0,
                "padx": (20, 10),
                "pady": (10, 10),
                "sticky": "ew"
            }, values=["CTkSegmentedButton", "Value 2", "Value 3"]
        )
        
        # Create progressbars
        self.progressbar_1 = CTkProgressBar(master=self.slider_progressbar_frame, gridargs={
                "row": 1,
                "column": 0,
                "padx": (20, 10),
                "pady": (10, 10),
                "sticky": "ew"
            }, orientation="horizontal"
        )
        self.progressbar_2 = CTkProgressBar(master=self.slider_progressbar_frame, gridargs={
                "row": 2,
                "column": 0,
                "padx": (20, 10),
                "pady": (10, 10),
                "sticky": "ew"
            }, orientation="horizontal"
        )
        self.progressbar_3 = CTkProgressBar(master=self.slider_progressbar_frame, gridargs={
                "row": 0,
                "column": 2,
                "rowspan": 5,
                "padx": (10, 20),
                "pady": (10, 10),
                "sticky": "ns"
            }, orientation="vertical"
        )

        # Create sliders
        self.slider_1 = CTkSlider(master=self.slider_progressbar_frame, gridargs={
                "row": 3,
                "column": 0,
                "padx": (20, 10),
                "pady": (10, 10),
                "sticky": "ew"
            }, orientation="horizontal"
        )
        self.slider_2 = CTkSlider(master=self.slider_progressbar_frame, gridargs={
                "row": 0,
                "rowspan": 5,
                "column": 1,
                "padx": (10, 10),
                "pady": (10, 10),
                "sticky": "ns"
            }, orientation="vertical"
        )        

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Add CTkSwitches to the CTkScrollable frame
        self.switch_1 = CTkSwitch(master=self.scrollable_frame, gridargs={
                "row": 0,
                "column": 0,
                "padx": 10,
                "pady": (0, 20),
            }, text=f"CTkSwitch 1"
        )
        self.switch_2 = CTkSwitch(master=self.scrollable_frame, gridargs={
                "row": 1,
                "column": 0,
                "padx": 10,
                "pady": (0, 20),
            }, text=f"CTkSwitch 2"
        )
        self.switch_3 = CTkSwitch(master=self.scrollable_frame, gridargs={
                "row": 2,
                "column": 0,
                "padx": 10,
                "pady": (0, 20),
            }, text=f"CTkSwitch 3"
        )

        # Create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(master=self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        # Create checkboxes
        self.checkbox_1 = CTkCheckBox(master=self.checkbox_slider_frame, gridargs={
                "row": 1,
                "column": 0,
                "padx": 20,
                "pady": (20, 0),
                "sticky": "n"
            }, text="CTkCheckBox 1"
        )
        self.checkbox_1.select()
        self.checkbox_2 = CTkCheckBox(master=self.checkbox_slider_frame, gridargs={
                "row": 2,
                "column": 0,
                "padx": 20,
                "pady": (20, 0),
                "sticky": "n"
            }, text="CTkCheckBox 2"
        )
        self.checkbox_3 = CTkCheckBox(master=self.checkbox_slider_frame, gridargs={
                "row": 3,
                "column": 0,
                "padx": 20,
                "pady": (20, 0),
                "sticky": "n"
            }, text="CTkCheckBox 3"
        )
        
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
