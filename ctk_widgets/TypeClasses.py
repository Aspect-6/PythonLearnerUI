from typing import TypedDict, Union, Tuple, Optional

class GridArgsT(TypedDict):
    row: int
    column: int
    padx: Union[int, Tuple[int, int]]
    pady: Union[int, Tuple[int, int]]
    rowspan: Optional[int]
    columnspan: Optional[int]
    sticky: Optional[Union[int, str]]
