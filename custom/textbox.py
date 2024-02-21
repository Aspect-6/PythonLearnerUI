import customtkinter
from funcs import print_color_coded

textbox_args = { "fg_color": "transparent", "wrap": "word", "font": ("Arial", 17) }

def add_colors(textbox: customtkinter.CTkTextbox, colors: dict[str, str], string: str):
    for key in colors:
        textbox.tag_config(key, foreground=colors[key])
    print_color_coded(list(colors.keys()), textbox, string)