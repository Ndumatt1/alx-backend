#!/usr/bin/env python3
''' This module returns appropriate page of the dataset '''


import csv
import math
from typing import List, Dict, Optional, Union
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Returns appropriate page of dataset '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        indexes = index_range(page, page_size)
        start_index = indexes[0]
        end_index = indexes[1]
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page > total_pages:
            return []
        return dataset[start_index:end_index]
        return self.__dataset

    def get_hyper(
            self, page: int = 1, page_size: int = 10
            ) -> Dict[str, object]:
        ''' Returns a dictionary containing key value pairs '''
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        page_info = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return page_info
