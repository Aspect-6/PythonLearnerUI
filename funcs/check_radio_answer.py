import customtkinter
from termcolor import colored
from custom.debug_patterns import *

def check_radio_answer(
    filename: str,
    radio_buttons: list[customtkinter.CTkRadioButton],
    q_btn: customtkinter.CTkButton,
    q_var: customtkinter.IntVar,
    correct_answer: int
):
    # Debugging
    LOG_TITLE =             colored(text["Question"]["LOG_TITLE"], **log_title_pattern)
    FILENAME_LABEL =        colored(text["Question"]["FILENAME_LABEL"], **label_pattern)
    FILENAME =              colored(filename, **filename_pattern)
    CORRECT_ANSWERS_LABEL = colored(text["Question"]["CORRECT_ANSWERS_LABEL"], **label_pattern)
    CORRECT_ANSWERS =       colored(correct_answer, **correct_answers_pattern)
    USER_INPUT_LABEL =      colored(text["Question"]["USER_INPUT_LABEL"], **label_pattern)
    USER_INPUT =            colored(q_var.get(), **user_input_pattern)
    QUESTION_STATUS_LABEL = colored(text["Question"]["QUESTION_STATUS_LABEL"], **label_pattern)
    is_correct =            q_var.get() == correct_answer
    QUESTION_STATUS =       colored("Correct" if is_correct else "Incorrect", "green" if is_correct else "red", **question_status_pattern)
    print(f"{LOG_TITLE}  |  {FILENAME_LABEL}: {FILENAME} | {CORRECT_ANSWERS_LABEL}: {CORRECT_ANSWERS}, {USER_INPUT_LABEL}: {USER_INPUT}, {QUESTION_STATUS_LABEL}: {QUESTION_STATUS}")


    if q_var.get() == correct_answer:
        q_btn.configure(text="Correct! ✅", state="disabled")
        [radio.configure(state="disabled") for radio in radio_buttons]
    else:
        q_btn.configure(text="Incorrect ❌")