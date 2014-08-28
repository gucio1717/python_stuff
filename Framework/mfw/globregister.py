

class GlobalRegister(object):
    '''
    GlobalRegister is a Singleton.
    It stores global variables accessible from anywhere in the program.
    Use with caution.
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GlobalRegister, cls).\
                __new__(cls, *args, **kwargs)
        return cls._instance

    def add(self, key, value):
        'rtype: GlobalRegister'
        if hasattr(self, key):
            raise Exception(key + 'is already registered in Global Register!!')
        setattr(self, key, value)
        return self

    def remove(self, key):
        'rtype: GlobalRegister'
        delattr(self, key)
        return self
