import typing

from ..core import KaitaiCompressor, ProcessorContextStub

# pylint:disable=arguments-differ


class Implode(KaitaiCompressor):
    """PKWare implode format"""

    __slots__ = ()

    def __init__(self, *args, **kwargs) -> None:  # pylint:disable=unused-argument
        super().__init__()

    def process(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
        import pkblast

        return ProcessorContextStub(pkblast.decompressBytesWholeToBytes(data)[1])

    def unprocess(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
        raise NotImplementedError("pkimplode is needed, but not yet implemented")
