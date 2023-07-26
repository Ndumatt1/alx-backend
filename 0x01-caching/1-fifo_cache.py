#!/usr/bin/env python3
''' LIFOCache inherits from BaseCaching and is a cachine system'''


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    Inherits from BaseCaching and is a caching
    '''
    def __init__(self):
        ''' Calls the init method of the  Base class '''
        super().__init__()

    def put(self, key, item):
        '''
        Assign to the dictionary self.cache_data the item value for the key
        '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for keys in self.cache_data.keys():
                    del self.cache_data[keys]
                    print('DISCARD: {}'.format(keys))
                    break

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
