class KaitaiProcessorContext:
       def __call__(self, slce:slice):
           raise NotImplementedException("Please implement process")

class KaitaiProcessor:
    """The base processor class"""
    def __init__(self, *args, **kwargs):
        raise NotImplementedException("Please implement __init__")
    def process(self, data:(bytes, bytearray), *args, **kwargs) -> KaitaiProcessorContext:
        raise NotImplementedException("Please implement process")
    def unprocess(self, data:(bytes, bytearray), *args, **kwargs ) -> KaitaiProcessorContext:
        raise NotImplementedException(self.__class__.__name__+" processing is not invertable")
    def getArgs(self, data:(bytes, bytearray) ):
        raise NotImplementedException("Cannot get args of "+self.__class__.__name__)
