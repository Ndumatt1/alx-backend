#!/usr/bin/env python3
''' Inherits from BaseCaching and is a caching system'''


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' Implement Least Recently Used cache policy'''
    def __init__(self):
        '''Calls BaseCaching init method '''
        super().__init__()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item value
        for the key
        '''
        self.cache_data[key] = item

        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for keys in self.cache_data.keys():
                    del self.cache_data[keys]
                    print('DISCARD: {}'.format(keys))
                    break

    def get(self, key):
        ''' Return the value in self.cache_data linked to key '''
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
