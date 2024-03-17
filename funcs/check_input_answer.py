import customtkinter

def check_input_answer(
    correct_answers: list[str] | str,
    input: str,
    btn: customtkinter.CTkButton,
    update_textbox: bool,
    new_ht: int = None,
    textbox: customtkinter.CTkTextbox = None,
    tag: str = ""
):
    if isinstance(correct_answers, list):
        for answer in correct_answers:
            if input.strip() == answer:
                if textbox is not None and update_textbox is True:
                    textbox.configure(state="normal")
                    textbox.insert("end", f"\n{answer}", tag)
                    textbox.configure(state="disabled")
                if new_ht is not None:
                    textbox.configure(height=new_ht)
                btn.configure(state="disabled")
    elif input.strip() == correct_answers:
        if textbox is not None and update_textbox is True:
            textbox.configure(state="normal")
            textbox.insert("end", f"\n{correct_answers}", tag)
            textbox.configure(state="disabled")
        if new_ht is not None:
            textbox.configure(height=new_ht)
        btn.configure(state="disabled")