#!/usr/bin/env python3
''' Inherits from BaseCaching and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    Inherits from BaseCaching and is a caching system
    '''
    last_updated = []

    def __init__(self):
        ''' Calls Base class init method '''
        super().__init__()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item value
        for the key key
        '''
        if key and item:
            self.cache_data[key] = item
            self.last_updated.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_updated_key = self.last_updated[-2]
            del self.cache_data[last_updated_key]
            print('DISCARD: {}'.format(last_updated_key))

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
