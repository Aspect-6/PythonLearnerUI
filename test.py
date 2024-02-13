# from pprint import pprint
# from collections import OrderedDict


# def color_code_text(input_text: str, colors_dict: dict[str, list[str]]):
    
#     # Create default color values
#     color_counts = {
#         "red": 1,
#         "orange": 1,
#         "yellow": 1,
#         "green": 1,
#         "blue": 1,
#         "purple": 1
#     }
#     non_color_count = 1
    
#     split_string = input_text.split()

#     return_dict = OrderedDict()

#     concat_string = ""

#     for word in split_string:
#         found_color = False
#         for key in colors_dict:
#             for item in colors_dict[key]:
#                 if item in word:
#                     if not concat_string == "":
#                         return_dict[non_color_count] = concat_string
#                         non_color_count += 1
#                         concat_string = ""
#                     return_dict[f"{key}_{color_counts[key]}"] = word
#                     color_counts[key] += 1
#                     found_color = True
#                     break  # Exit the loop once a color is found
#         if not found_color:
#             concat_string += word + " "

#     return return_dict


# string = "Variables in python are used to store data for later use. They can store any type of value such as an integer, string, list, dictionary, expression, or even other variables. The way that you declare a  variable is by first coming up with a name. Next you put an = sign to tell python that whatever you are about to type should be stored under the name of the variable that you named. Finally, you type the value you wish to store. Later, if you need to access that value and use it, all you need to do is to reference the name of the variable. For example, if you wanted to print the value of the variable named, my_var, then you would type print(my_var), which would print the value of my_var to the terminal."

# colors_dict = {
#     "green": ["integer", "string", "list", "dictionary", "expression", "="],
#     "blue": ["terminal"],
#     "purple": ["Variables", "variables.", "variable.","name.", "named.", "my_var"]
# }

# result = color_code_text(string, colors_dict)
# pprint(result)

input_string = 'Variables in python are used to store data for later use. They can store any type of value such as an integer, string, list, dictionary, expression, or even other variables. The way that you declare a variable is by first coming up with a name. Next you put an = sign to tell python that whatever you are about to type should be stored under the name of the variable that you named. Finally, you type the value you wish to store. Later, if you need to access that value and use it, all you need to do is to reference the name of the variable. For example, if you wanted to print the value of the variable named, my_var, then you would type "print(my_var)", which would print the value of my_var to the terminal.'

# Replace the specific value with the desired list of words
# input_string = input_string.replace('"print(my_var)",', 'print(my_var),')

# Split the string into a list of words
split_string = input_string.split()

# Iterate through the list and replace the modified value
for i, word in enumerate(split_string):
    if 'print(' in word:
        split_string[i:i+1] = ['"print(', 'my_var', ')",']

print(split_string)

