import customtkinter

def add_colors(textbox: customtkinter.CTkTextbox, colors: dict[str, str], segments: dict):
    for key in colors:
        textbox.tag_config(key, foreground=colors[key])

    for segment in segments:
        if not isinstance(segment, int):
            for key in colors:
                if key in segment:
                    textbox.insert("end", segments.get(segment), key)
        else:
            textbox.insert("end", segments.get(segment))
    textbox.configure(state="disabled")
