from customtkinter import CTkTabview, CTkInputDialog
from ctk_widgets.TypeClasses import GridArgsT
from ctk_widgets.Button import CustomCTkButton as CTkButton
from ctk_widgets.OptionMenu import CustomCTkOptionMenu as CTkOptionMenu
from ctk_widgets.Label import CustomCTkLabel as CTkLabel


class CustomCTkTabview(CTkTabview):
    def __init__(self, master, gridargs: GridArgsT, tabs: list[str], **kwargs):
        super().__init__(master, **kwargs)

        # Create a CTkTabview widget with the specified width.
        self.tabview = CTkTabview(master, width=250)
        self.tabview.grid(**gridargs)

        # Add each tab from the 'tabs' list to the CTkTabview.
        for tab in tabs:
            self.tabview.add(tab)

        # # Configure the grid of individual tabs.
        # # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)
        # # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # # Create and place a CTkOptionMenu widget inside the "CTkTabview" tab.
        # self.optionmenu_1 = CTkOptionMenu(master=self.tabview.tab("CTkTabview"), gridargs={
        #         "row": 0,
        #         "column": 0,
        #         "padx": 20,
        #         "pady": (20, 10)
        #     }, 
        #     values=["Value 1", "Value 2", "Value Long Long Long"], command=lambda *args: None
        # )

        # # Create and place a CTkButton widget inside the "CTkTabview" tab.
        # self.string_input_button = CTkButton(master=self.tabview.tab("CTkTabview"), gridargs={
        #     "row": 2,
        #     "column": 0,
        #     "padx": 20,
        #     "pady": (10, 10)
        # }, text="Open CTkInputDialog", command=self.open_input_dialog_event)

        # # Create and place a CTkLabel widget inside the "Tab 2" tab.
        # self.label_tab_2 = CTkLabel(self.tabview.tab("Tab 2"), gridargs={
        #     "row": 0,
        #     "column": 0,
        #     "padx": 20,
        #     "pady": (10, 10)
        # }, text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

    def open_input_dialog_event(self):
        dialog = CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())
