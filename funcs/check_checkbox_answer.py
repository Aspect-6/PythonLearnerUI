import customtkinter
from termcolor import colored
from custom.debug_patterns import question, text

def check_checkbox_answer(
    filename: str,
    checkboxes: list[customtkinter.CTkCheckBox],
    q_btn: customtkinter.CTkButton,
    correct_answer: list[int]
):
    # Debugging
    is_correct =            [checkbox.get() for checkbox in checkboxes] == correct_answer
    is_correct_text = "Correct" if is_correct else "Incorrect", "green" if is_correct else "red"
    LOG_TITLE =             colored(text["Question"]["LOG_TITLE"]               , **question["log_title_pattern"])
    FILENAME_LABEL =        colored(text["Question"]["FILENAME_LABEL"]          , **question["label_pattern"])
    FILENAME =              colored(filename                                    , **question["filename_pattern"])
    CORRECT_ANSWERS_LABEL = colored(text["Question"]["CORRECT_ANSWERS_LABEL"]   , **question["label_pattern"])
    CORRECT_ANSWERS =       colored(correct_answer                              , **question["correct_answers_pattern"])
    USER_INPUT_LABEL =      colored(text["Question"]["USER_INPUT_LABEL"]        , **question["label_pattern"])
    USER_INPUT =            colored([checkbox.get() for checkbox in checkboxes] , **question["user_input_pattern"])
    QUESTION_STATUS_LABEL = colored(text["Question"]["QUESTION_STATUS_LABEL"]   , **question["label_pattern"])
    QUESTION_STATUS =       colored(is_correct_text                             , **question["question_status_pattern"])
    print(f"{LOG_TITLE}  |  {FILENAME_LABEL}: {FILENAME} | {CORRECT_ANSWERS_LABEL}: {CORRECT_ANSWERS}, {USER_INPUT_LABEL}: {USER_INPUT}, {QUESTION_STATUS_LABEL}: {QUESTION_STATUS}")

    if [checkbox.get() for checkbox in checkboxes] == correct_answer:
        q_btn.configure(text="Correct! ✅", state="disabled")
        [checkbox.configure(state="disabled") for checkbox in checkboxes]
    else:
        q_btn.configure(text="Incorrect ❌")