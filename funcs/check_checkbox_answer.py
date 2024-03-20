import customtkinter
from termcolor import colored
from custom.debug_patterns import *

def check_checkbox_answer(
    filename: str,
    checkboxes: list[customtkinter.CTkCheckBox],
    q_btn: customtkinter.CTkButton,
    correct_answer: list[int]
):
    # Debugging
    LOG_TITLE =             colored(text["LOG_TITLE"], **log_title_pattern)
    FILENAME_LABEL =        colored(text["FILENAME_LABEL"], **label_pattern)
    FILENAME =              colored(filename, **filename_pattern)
    CORRECT_ANSWERS_LABEL = colored(text["CORRECT_ANSWERS_LABEL"], **label_pattern)
    CORRECT_ANSWERS =       colored(correct_answer, **correct_answers_pattern)
    USER_INPUT_LABEL =      colored(text["USER_INPUT_LABEL"], **label_pattern)
    USER_INPUT =            colored([checkbox.get() for checkbox in checkboxes], **user_input_pattern)
    QUESTION_STATUS_LABEL = colored(text["QUESTION_STATUS_LABEL"], **label_pattern)
    is_correct =            [checkbox.get() for checkbox in checkboxes] == correct_answer
    QUESTION_STATUS =       colored("Correct" if is_correct else "Incorrect", "green" if is_correct else "red", **question_status_pattern)
    print(f"{LOG_TITLE}  |  {FILENAME_LABEL}: {FILENAME} | {CORRECT_ANSWERS_LABEL}: {CORRECT_ANSWERS}, {USER_INPUT_LABEL}: {USER_INPUT}, {QUESTION_STATUS_LABEL}: {QUESTION_STATUS}")

    if [checkbox.get() for checkbox in checkboxes] == correct_answer:
        q_btn.configure(text="Correct! ✅", state="disabled")
        [checkbox.configure(state="disabled") for checkbox in checkboxes]
    else:
        q_btn.configure(text="Incorrect ❌")