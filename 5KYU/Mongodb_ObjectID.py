from datetime import datetime

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        if not isinstance(s, str) or len(s) != 24:
            return False
        for symb in s:
            if symb not in '0123456789abcdef':
                return False
        return True

    @classmethod
    def get_timestamp(cls, s):
        if cls.is_valid(s):
            return datetime.fromtimestamp(int(s[:8],base=16))
        return False