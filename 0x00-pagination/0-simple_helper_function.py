#!/usr/bin/python3
''' This module implements a simple helper function for pagination'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Retuns a tuple of size two containing start index and end index '''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
