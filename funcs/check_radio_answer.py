import customtkinter

def check_radio_answer(
    radio_buttons: list[customtkinter.CTkRadioButton],
    q_btn: customtkinter.CTkButton,
    q_var: customtkinter.IntVar,
    correct_answer: int
):
    if q_var.get() == correct_answer:
        q_btn.configure(text="Correct! ✅", state="disabled")
        [radio.configure(state="disabled") for radio in radio_buttons]
    else:
        q_btn.configure(text="Incorrect ❌")