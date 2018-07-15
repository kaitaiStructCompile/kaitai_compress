class Lz4Context(KaitaiProcessorContext):
    __slots__=("obj", "meth", "data")
    def __init__(self, obj, meth, data):
        self.obj=obj
        self.meth=meth
        self.data=meth.compress(data)
      
    def __call__(self, slce:slice):
        return self.data[slce]

class Lz4(KaitaiProcessor):
    __slots__=("obj",)
    def __init__(self, block_size:bool=0, linker:bool=True, compression_level:int=0, content_checksum:bool=False, block_checksum:bool=False):
        import lz4.frame
        self.obj=lz4.frame.LZ4FrameCompressor(block_size=block_size, block_linker=linker, compression_level=compression_level, content_checksum=content_checksum, block_checksum=block_checksum, return_bytearray=False)
    def process(self, data:(bytes, bytearray)):
        return Lz4Context(self.obj, self.obj.decompress, data)
    def unprocess(self, data:(bytes, bytearray)):
        return Lz4Context(self.obj, self.obj.compress, data)
    def getArgs(self, data:(bytes, bytearray) ):
        import lz4.frame
        res=lz4.frame.get_frame_info(data)
        return (res["block_size"], res["linker"], res["compression_level"], res["conteht_checksum"], res["block_checksum"])





