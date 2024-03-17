from pygments import lex
from pygments.lexers import PythonLexer
import customtkinter
from custom.textbox import syntax_highlight_colors

def generate_code_block(code: str, textbox: customtkinter.CTkTextbox, phrases: dict = None):
    # Use Pygments to split the code into tokens
    tokens = list(lex(code, PythonLexer()))

    # Configure the tags to use the colors defined in the color scheme
    for tag, color in syntax_highlight_colors.items():
        textbox.tag_config(tag, foreground=color)

    # Insert each token into the Text widget
    for ttype, tvalue in tokens:
        ttype_str = str(ttype).rstrip('\n')
        if ttype_str in syntax_highlight_colors:
            textbox.insert('end', tvalue, ttype_str)
        else:
            textbox.insert('end', tvalue)

    # If phrases is not None, apply the colors to the phrases that are not automatically colored by Pygments
    if phrases is not None:
        for color, phrase_list in phrases.items():
            for phrase in phrase_list:
                start_index = "1.0"
                while True:
                    index = textbox.search(phrase, start_index, stopindex='end')
                    if index:
                        end_index = f"{index}+{len(phrase)}c"
                        print(textbox.get(index, end_index))
                        textbox.delete(index, end_index)
                        textbox.insert(index, phrase, color)
                        start_index = end_index
                    else:
                        break
    
    # Remove the trailing whitespace and disable the textbox
    textbox.delete("end-1c", "end")
    textbox.configure(state="disabled")