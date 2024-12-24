import typing, clr, abc
from LibHac.Fs import IStorage
from System import IDisposable, Span_1, ReadOnlySpan_1
from LibHac import Result
from LibHac.Common import SharedRef_1, UniqueRef_1, U8Span
from LibHac.Common.FixedArrays import Array32_1, Array12_1

class IniExtract(abc.ABC):
    @staticmethod
    def TryGetIni1Offset(offset: clr.Reference[int], size: clr.Reference[int], kernelStorage: IStorage) -> bool: ...


class InitialProcessBinaryReader(IDisposable):
    def __init__(self) -> None: ...
    @property
    def Header(self) -> clr.Reference[InitialProcessBinaryReader.IniHeader]: ...
    @property
    def ProcessCount(self) -> int: ...
    def Dispose(self) -> None: ...
    def Initialize(self, binaryStorage: clr.Reference[SharedRef_1[IStorage]]) -> Result: ...
    def OpenKipStorage(self, outStorage: clr.Reference[UniqueRef_1[IStorage]], index: int) -> Result: ...

    class IniHeader:
        Magic : int
        ProcessCount : int
        Reserved : int
        Size : int



class KipHeader:
    AffinityMask : int
    BssFileSize : int
    BssMemoryOffset : int
    BssSize : int
    Capabilities : Array32_1[int]
    DataFileSize : int
    DataMemoryOffset : int
    DataSize : int
    Flags : KipHeader.Flag
    IdealCoreId : int
    Kip1Magic : int
    Magic : int
    Name : Array12_1[int]
    Priority : int
    ProgramId : int
    RoFileSize : int
    RoMemoryOffset : int
    RoSize : int
    SegmentCount : int
    StackSize : int
    TextFileSize : int
    TextMemoryOffset : int
    TextSize : int
    Version : int
    @property
    def IsValid(self) -> bool: ...
    @property
    def Segments(self) -> Span_1[KipHeader.SegmentHeader]: ...

    class Flag(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        TextCompress : KipHeader.Flag # 1
        RoCompress : KipHeader.Flag # 2
        DataCompress : KipHeader.Flag # 4
        Is64BitInstruction : KipHeader.Flag # 8
        ProcessAddressSpace64Bit : KipHeader.Flag # 16
        UseSecureMemory : KipHeader.Flag # 32


    class SegmentHeader:
        FileSize : int
        MemoryOffset : int
        Size : int



class KipReader(IDisposable):
    def __init__(self) -> None: ...
    @property
    def AffinityMask(self) -> int: ...
    @property
    def Capabilities(self) -> ReadOnlySpan_1[int]: ...
    @property
    def IdealCoreId(self) -> int: ...
    @property
    def Is64Bit(self) -> bool: ...
    @property
    def Is64BitAddressSpace(self) -> bool: ...
    @property
    def IsDataCompressed(self) -> bool: ...
    @property
    def IsRoCompressed(self) -> bool: ...
    @property
    def IsTextCompressed(self) -> bool: ...
    @property
    def Name(self) -> U8Span: ...
    @property
    def Priority(self) -> int: ...
    @property
    def ProgramId(self) -> int: ...
    @property
    def Segments(self) -> ReadOnlySpan_1[KipHeader.SegmentHeader]: ...
    @property
    def StackSize(self) -> int: ...
    @property
    def UsesSecureMemory(self) -> bool: ...
    @property
    def Version(self) -> int: ...
    def Dispose(self) -> None: ...
    def GetFileSize(self) -> int: ...
    def GetRawData(self, outKipData: clr.Reference[UniqueRef_1[IStorage]]) -> Result: ...
    def GetSegmentSize(self, segment: KipReader.SegmentType, size: clr.Reference[int]) -> Result: ...
    def GetUncompressedSize(self) -> int: ...
    def Initialize(self, kipData: clr.Reference[SharedRef_1[IStorage]]) -> Result: ...
    def ReadSegment(self, segment: KipReader.SegmentType, buffer: Span_1[int]) -> Result: ...
    def ReadUncompressedKip(self, buffer: Span_1[int]) -> Result: ...

    class SegmentType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Text : KipReader.SegmentType # 0
        Ro : KipReader.SegmentType # 1
        Data : KipReader.SegmentType # 2
        Bss : KipReader.SegmentType # 3
        Reserved1 : KipReader.SegmentType # 4
        Reserved2 : KipReader.SegmentType # 5


