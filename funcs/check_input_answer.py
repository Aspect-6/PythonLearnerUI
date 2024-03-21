import customtkinter
from termcolor import colored
from custom.debug_patterns import question, text

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
    is_correct =            any([input.strip() == answer for answer in correct_answers])
    is_correct_text =       "Correct" if is_correct else "Incorrect", "green" if is_correct else "red"
    LOG_TITLE =             colored(text["Question"]["LOG_TITLE"]               , **question["log_title_pattern"])
    FILENAME_LABEL =        colored(text["Question"]["FILENAME_LABEL"]          , **question["label_pattern"])
    FILENAME =              colored(filename                                    , **question["filename_pattern"])
    CORRECT_ANSWERS_LABEL = colored(text["Question"]["CORRECT_ANSWERS_LABEL"]   , **question["label_pattern"])
    CORRECT_ANSWERS =       colored(correct_answers                             , **question["correct_answers_pattern"])
    USER_INPUT_LABEL =      colored(text["Question"]["USER_INPUT_LABEL"]        , **question["label_pattern"])
    USER_INPUT =            colored(input                                       , **question["user_input_pattern"])
    QUESTION_STATUS_LABEL = colored(text["Question"]["QUESTION_STATUS_LABEL"]   , **question["label_pattern"])
    QUESTION_STATUS =       colored(is_correct_text                             , **question["question_status_pattern"])
    print(f"{LOG_TITLE}  |  {FILENAME_LABEL}: {FILENAME} | {CORRECT_ANSWERS_LABEL}: {CORRECT_ANSWERS}, {USER_INPUT_LABEL}: {USER_INPUT}, {QUESTION_STATUS_LABEL}: {QUESTION_STATUS}")

    for answer in correct_answers:
        if input.strip() == answer:
            if textbox is not None and update_textbox is True:
                textbox.configure(state="normal")
                textbox.insert("end", f"\n{answer}", tag)
                textbox.configure(state="disabled")
            if new_ht is not None:
                textbox.configure(height=new_ht)
            btn.configure(state="disabled")