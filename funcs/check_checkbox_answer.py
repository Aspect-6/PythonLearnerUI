import customtkinter

def check_checkbox_answer(
    checkboxes: list[customtkinter.CTkCheckBox],
    q_btn: customtkinter.CTkButton,
    correct_answer: list[int]
):
    if [checkbox.get() for checkbox in checkboxes] == correct_answer:
        q_btn.configure(text="Correct! ✅", state="disabled")
        [checkbox.configure(state="disabled") for checkbox in checkboxes]
    else:
        q_btn.configure(text="Incorrect ❌")