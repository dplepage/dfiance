from abc import abstractmethod

from base import Dictifier

class NestedDictifier(Dictifier):
    @abstractmethod
    def sub(self, val, key):
        raise NotImplementedError()

    @abstractmethod
    def sub_df(self, key):
        raise NotImplementedError()

    @abstractmethod
    def keys(self, val):
        raise NotImplementedError()

    @classmethod
    def __instancecheck__(cls, inst):
        if super(NestedDictifier, cls).__instancecheck__(inst):
            return True
        attrs = ['sub', 'sub_df', 'keys', 'dictify', 'undictify', 'validate']
        if all(hasattr(inst, x) for x in attrs):
            return True
        return False
