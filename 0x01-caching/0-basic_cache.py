#!/usr/bin/env python3
''' Inherits from BaseCaching and is a caching system'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Inherits from BaseCaching and is a caching system '''
    def __init__(self):
        ''' Calls the base class init method'''
        super().__init__()

    def put(self, key, item):
        ''' Assigns to the dictionary self.cache_data the item value'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' Must return the value in self.cache_data linked key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
