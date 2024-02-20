from collections import OrderedDict
import re
from typing import Union


def generate_dict(colors_dict: dict, name: str, pre_run=None, post_run=None):

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

    split_string = re.split(r'\s', colors_dict[name]["str"])

    # print(split_string, "\n")

    if pre_run is not None:
        split_string: list[str] = pre_run(split_string)

    return_dict = OrderedDict()

    concat_string = ""

    for word in split_string:
        # print(word)
        found_color: bool = False
        for key in colors_dict[name]["dict"]:
            for item in colors_dict[name]["dict"][key]:
                if item in word:
                    if not concat_string == "":
                        return_dict[non_color_count] = concat_string
                        non_color_count += 1
                        concat_string = ""
                    return_dict[f"{key}_{color_counts[key]}"] = f"{word} "
                    color_counts[key] += 1
                    found_color = True
                    break  # Exit the loop once a color is found
        if not found_color:
            concat_string += word + " "

    return_dict[non_color_count] = concat_string

    if post_run is not None:
        return_dict = post_run(return_dict)

    return return_dict
