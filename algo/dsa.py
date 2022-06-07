from typing import Iterable, Any

class twodict:
    def __init__(self, keys: Iterable[Any] = [], values: Iterable[Any] = []):
        self.keys = set(keys)
        self.values = set(values)
        self._keyToVal = {}
        self._valToKey = {}

        for key, value in zip(keys, values):
            self._keyToVal[key] = value
            self._valToKey[value] = key

    def __setitem__(self, key, value):
        if(key in self.keys): self.values -= {self._keyToVal[key]}
        if(value in self.values): self.keys -= {self._valToKey[value]}
        self.keys.add(key)
        self.values.add(value)
        self._keyToVal[key] = value
        self._valToKey[value] = key
    
    def __getitem__(self, key):
        if key in self.keys:
            return self._keyToVal[key]
        if key in self.values:
            return self._valToKey[key]
    
    def getValue(self, key):
        if key in self.keys:
            return self._keyToVal[key]

    def getKey(self, value):
        if value in self.values:
            return self._valToKey[value]
