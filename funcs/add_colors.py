import customtkinter

def add_colors(textbox: customtkinter.CTkTextbox, colors: dict[str, str], segments: dict):
    for key in colors:
        textbox.tag_config(key, foreground=colors[key])

    for key in segments:
        if not isinstance(key, int):
            for color in list(colors.keys()):
                if color in key:
                    textbox.insert("end", segments.get(key), color)
        else:
            textbox.insert("end", segments.get(key))
    textbox.configure(state="disabled")
