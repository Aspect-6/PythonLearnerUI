textbox_args = { "fg_color": "transparent", "wrap": "word", "font": ("Arial", 16) }

COLORS = {
    "RED": "red",
    "ORANGE": "orange",
    "YELLOW": "yellow",
    "GREEN": "green",
    "TEAL": "teal",
    "BLUE": "#3d59d9",
    "PURPLE": "#bf00dd",
}

syntax_highlight_colors = {
    'Token.Keyword': COLORS["PURPLE"],
    'Token.Literal.String.Double': COLORS["ORANGE"],
    'Token.Name.Function': COLORS["TEAL"],
    'Token.Name.Builtin': COLORS["TEAL"],
    'Token.Name': COLORS["PURPLE"],
    'Token.Literal.Number.Integer': COLORS["GREEN"],
    'Token.Literal.Number.Float': COLORS["GREEN"],
}