from collections import OrderedDict
import re


def generate_dict(colors_dict: dict, name: str, pre_run=None, post_run=None):
    color_counts = {
        "red": 1,
        "orange": 1,
        "yellow": 1,
        "green": 1,
        "blue": 1,
        "purple": 1,
    }
    non_color_count = 1

    split_string = colors_dict[name]["str"].split()

    if pre_run is not None:
        split_string: list[str] = pre_run(split_string)

    return_dict = OrderedDict()

    flat_dict = {item: key for key in colors_dict[name]["dict"] for item in colors_dict[name]["dict"][key]}
    
    concat_string = ""

    for word in split_string:
        found_color: bool = False
        word_lower = word.lower()
        for item, color in flat_dict.items():
            if not concat_string == "":
                return_dict[non_color_count] = concat_string
                non_color_count += 1
                concat_string = ""
            if item in word or item in word_lower:
                return_dict[f"{color}_{color_counts[color]}"] = f"{word} "
                color_counts[color] += 1
                found_color = True
                break
        if not found_color:
            concat_string += word + " "

    return_dict[non_color_count] = concat_string

    if post_run is not None:
        return_dict = post_run(return_dict)

    return return_dict