import customtkinter
from termcolor import colored
from custom.debug_patterns import text, label_pattern, filename_pattern, correct_answers_pattern, user_input_pattern, question_status_pattern

def check_input_answer(
    filename: str,
    correct_answers: list[str] | str,
    input: str,
    btn: customtkinter.CTkButton,
    update_textbox: bool,
    new_ht: int = None,
    textbox: customtkinter.CTkTextbox = None,
    tag: str = "",
):
    # Debugging
    FILENAME_LABEL =        colored(text["FILENAME_LABEL"], **label_pattern)
    FILENAME =              colored(filename, **filename_pattern)
    CORRECT_ANSWERS_LABEL = colored(text["CORRECT_ANSWERS_LABEL"], **label_pattern)
    CORRECT_ANSWERS =       colored(correct_answers, **correct_answers_pattern)
    USER_INPUT_LABEL =      colored(text["USER_INPUT_LABEL"], **label_pattern)
    USER_INPUT =            colored(input, **user_input_pattern)
    QUESTION_STATUS_LABEL = colored(text["QUESTION_STATUS_LABEL"], **label_pattern)
    is_correct =            any([input.strip() == answer for answer in correct_answers])
    QUESTION_STATUS =       colored("Correct" if is_correct else "Incorrect", "green" if is_correct else "red", **question_status_pattern)
    print(f"{FILENAME_LABEL}: {FILENAME} | {CORRECT_ANSWERS_LABEL}: {CORRECT_ANSWERS}, {USER_INPUT_LABEL}: {USER_INPUT}, {QUESTION_STATUS_LABEL}: {QUESTION_STATUS}")

    for answer in correct_answers:
        if input.strip() == answer:
            if textbox is not None and update_textbox is True:
                textbox.configure(state="normal")
                textbox.insert("end", f"\n{answer}", tag)
                textbox.configure(state="disabled")
            if new_ht is not None:
                textbox.configure(height=new_ht)
            btn.configure(state="disabled")