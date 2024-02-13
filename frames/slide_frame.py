import customtkinter


class SlideFrame(customtkinter.CTkFrame):
    def __init__(self, master, views: list[customtkinter.CTkFrame], **kwargs):
        super().__init__(master, **kwargs)

        self.slide_frame = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.slide_frame.grid_columnconfigure(0, weight=1)
        self.back_button = customtkinter.CTkButton(master=self.slide_frame, text="Back", width=100, command=lambda: self.slide("left", views))
        self.next_button = customtkinter.CTkButton(master=self.slide_frame, text="Next", width=100, command=lambda: self.slide("right", views))

        # Slide frame and buttons layout
        self.slide_frame.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")
        self.back_button.grid(row=0, column=0, sticky="w")
        self.back_button.configure(state="disabled")
        self.next_button.grid(row=0, column=1, sticky="e")

        # View postitioning variables
        self.current_view = 1
        self.elem_x: float = 0.5
        self.slide_count: int = 0

    def slide(self, dir: str, views: list[customtkinter.CTkFrame]):
        if dir == "left": 
            if self.slide_count < 10:
                self.elem_x += 0.1
                for index, view in enumerate(views):
                    view.place(relx=self.elem_x+index, rely=0.5, relheight=0.95, anchor="center")
                self.lift()
                self.slide_count += 1
                self.after(10, lambda: self.slide("left", views))
            else:
                self.slide_count = 0
                self.current_view -= 1
                if self.current_view == 1:
                    self.back_button.configure(state="disabled")
                if self.current_view < len(views):
                    self.next_button.configure(state="normal")
                return
        if dir == "right":
            if self.slide_count < 10:
                self.elem_x -= 0.1
                for index, view in enumerate(views):
                    view.place(relx=self.elem_x+index, rely=0.5, relheight=0.95, anchor="center")
                self.lift()
                self.slide_count += 1
                self.after(10, lambda: self.slide("right", views))
            else:
                self.slide_count = 0
                self.current_view += 1
                if self.current_view == len(views):
                    self.next_button.configure(state="disabled")
                return
            self.back_button.configure(state="normal")
