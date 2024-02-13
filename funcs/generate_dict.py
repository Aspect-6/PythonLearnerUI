from collections import OrderedDict
import re


def generate_dict(input_text: str, colors_dict: dict[str, list[str]], pre_run=None, post_run=None):
    
    # Create default color values
    color_counts = {
        "red": 1,
        "orange": 1,
        "yellow": 1,
        "green": 1,
        "blue": 1,
        "purple": 1,
        "white": 1,
    }
    non_color_count = 1

    split_string = re.split(r'\s', input_text)
    
    print(split_string, "\n")

    if pre_run is not None:
        split_string: list[str] = pre_run(split_string)

    return_dict = OrderedDict()

    concat_string = ""

    for word in split_string:
        found_color = False
        for key in colors_dict:
            for item in colors_dict[key]:
                if item in word:
                    if not concat_string == "":
                        print(concat_string, "\n")
                        return_dict[non_color_count] = concat_string
                        non_color_count += 1
                        concat_string = ""
                    return_dict[f"{key}_{color_counts[key]}"] = f"{word} "
                    color_counts[key] += 1
                    found_color = True
                    break  # Exit the loop once a color is found
        if not found_color:
            concat_string += word + " "

    if post_run is not None:
        return_dict = post_run(return_dict)

    print(concat_string)u0ktf96d9es,r5
    print(return_dict, "\n\n\n")
    return return_dict
