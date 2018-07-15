class ZlibProcessorContext(KaitaiProcessorContext):
    def __init__(self, obj, meth, data):
        self.obj=obj
        self.meth=meth
        self.data=meth(data)
    def __call__(seld, slc:slice):
        return self.data[slc]

class Zlib(KaitaiProcessor):
    __slots__ = ("params", "dO", "cO")
    def __init__(self, level:int=-1, method:(str, int)="deflated", window_size:int=15, mem_level:(str, int)="DEF_MEM_LEVEL", strategy:(str, int)="Z_DEFAULT_STRATEGY", zdict:bytes=None):
        import zlib
        if isinstance(method, str):
            method=getattr(zlib, method.upper())
        if isinstance(memLevel, str):
            memLevel=getattr(zlib, memLevel)
        if isinstance(strategy , str):
            strategy=getattr(zlib, strategy)
        self.params=(level,  method, window_size, mem_level, strategy, zdict)
    def process(self, data:(bytes, bytearray), slce:slice):
        dO=zlib.decompressobj(*self.params)
        return ZlibProcessorContext( dO, dO.decompress, data)
    def unprocess(self, data:(bytes, bytearray), slce:slice):
        cO=zlib.compressobj(*self.params)
        return ZlibProcessorContext( cO, cO.compress, data)
    """
    def getArgs(self, data):
        try:
            z=ksZlib(data)
            return tuple(( getattr(z, a) for a in ("level",  "method", "window_size", "mem_level", "strategy", "zdict") ))
        except:
            pass
        raise NotImplementedException("The header is not p resent, and there is no way to extract an arg")
    """
