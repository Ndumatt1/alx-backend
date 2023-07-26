#!/usr/bin/env python3
''' Inherits from BaseCaching and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' Implements Most Recently Used Caching Policy'''
    recently_used = []

    def __init__(self):
        ''' calls BaseCaching init method'''
        super().__init__()

    def put(self, key, item):
        '''
        Assign to the dictionary self.cache_data the item value
        for the key
        '''
        if key and item:
            self.cache_data[key] = item
            self.recently_used.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_to_discard = self.recently_used[-2]
            del self.cache_data[key_to_discard]
            print('DISCARD: {}'.format(key_to_discard))

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key '''
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
