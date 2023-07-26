#!/usr/bin/env python3
''' inherits from BaseCaching and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Defines a LFU cachning system"""
    __usage = {}

    def __init__(self):
        """Initialize an Instance"""
        super().__init__()

    def put(self, key, item):
        """Caches the given data using LFU algorithm"""
        if key and item:
            cache = self.cache_data
            if cache.get(key):
                del cache[key]
            cache[key] = item
            if len(cache) > self.MAX_ITEMS:
                minUsageValue = min(self.__usage.values())
                minUsageKeys = [k for k in self.__usage.keys()
                                if self.__usage[k] == minUsageValue]
                trash = minUsageKeys[0]
                cache.pop(trash)
                self.__usage.pop(trash)
                print('DISCARD: {}'.format(trash))
            if key in self.__usage:
                self.__usage[key] += 1
            else:
                self.__usage[key] = 0

    def get(self, key):
        """Returns the value of key from self.cache_data"""
        if not self.cache_data.get(key):
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        self.__usage[key] += 1

        return self.cache_data[key]
