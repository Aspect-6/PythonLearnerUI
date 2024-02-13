import customtkinter

def print_color_coded(colors: list[str], textbox: customtkinter.CTkTextbox, segments: dict[str, str]):
    """
    This function takes a list of colors, a textbox widget, and a string that represents a segment of the strings dictionary.
    It loops through each key in the specified segment of the strings dictionary, and if the key contains one of the colors specified in the colors list,
    it inserts the key's value into the textbox widget with the corresponding color.
    The function then sets the textbox widget's state to "disabled" to prevent further user input.

    Parameters:
    colors (list[str]): A list of colors to highlight in the textbox.
    textbox (customtkinter.CTkTextbox): The textbox widget to insert highlighted text into.
    segments (str): The string that represents a segment of the strings dictionary.

    Returns:
    None

    """
    for key in segments:
        if not isinstance(key, int):
            for color in colors:
                if color == "white":
                    textbox.insert("end", segments.get(key))
                if color in key:
                    textbox.insert("end", segments.get(key), color)
        else:
            textbox.insert("end", segments.get(key))
    textbox.configure(state="disabled")
