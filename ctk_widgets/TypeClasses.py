from typing import TypedDict, Union, Tuple, Optional

class GridArgsT(TypedDict):
    row: Union[int, Tuple[int, int]]
    column: Union[int, Tuple[int, int]]
    padx: Union[int, Tuple[int, int]]
    pady: Union[int, Tuple[int, int]]
    rowspan: Optional[Union[int, str]]
    columnspan: Optional[Union[int, str]]
    sticky: Optional[Union[int, str]]
