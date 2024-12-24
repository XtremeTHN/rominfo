import typing, clr, abc
from LibHac.Common.FixedArrays import Array256_1, Array4_1, Array12_1, Array8_1, Array16_1, Array48_1, Array32_1, Array28_1
from LibHac.Ncm import ProgramId
from LibHac import Result, HorizonClient
from System import ReadOnlySpan_1, Span_1
from LibHac.Fs import FileHandle
from LibHac.Common import ReadOnlyRef_1
from LibHac.Fs.Fsa import IFile

class AcidHeaderData:
    Flags : int
    FsAccessControlOffset : int
    FsAccessControlSize : int
    KernelCapabilityOffset : int
    KernelCapabilitySize : int
    Magic : int
    MagicValue : int
    Modulus : Array256_1[int]
    ProgramIdMax : ProgramId
    ProgramIdMin : ProgramId
    Reserved238 : Array4_1[int]
    ServiceAccessControlOffset : int
    ServiceAccessControlSize : int
    Signature : Array256_1[int]
    Size : int
    Version : int


class AciHeader:
    FsAccessControlOffset : int
    FsAccessControlSize : int
    KernelCapabilityOffset : int
    KernelCapabilitySize : int
    Magic : int
    MagicValue : int
    ProgramId : ProgramId
    Reserved04 : Array12_1[int]
    Reserved18 : Array8_1[int]
    Reserved38 : Array8_1[int]
    ServiceAccessControlOffset : int
    ServiceAccessControlSize : int


class Meta:
    AcidOffset : int
    AcidSize : int
    AciOffset : int
    AciSize : int
    DefaultCpuId : int
    Flags : int
    Magic : int
    MagicValue : int
    MainThreadPriority : int
    MainThreadStackSize : int
    ProductCode : Array16_1[int]
    ProgramName : Array16_1[int]
    Reserved08 : Array4_1[int]
    Reserved0D : int
    Reserved10 : Array4_1[int]
    Reserved40 : Array48_1[int]
    SignatureKeyGeneration : int
    SystemResourceSize : int
    Version : int


class MetaLoader:
    def __init__(self) -> None: ...
    def GetNpdm(self, npdm: clr.Reference[Npdm]) -> Result: ...
    @staticmethod
    def GetNpdmFromBuffer(npdm: clr.Reference[Npdm], npdmBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Load(self, npdmBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def LoadFromFile(self, hos: HorizonClient, file: FileHandle) -> Result: ...


class Npdm:
    Aci : ReadOnlyRef_1[AciHeader]
    Acid : ReadOnlyRef_1[AcidHeaderData]
    FsAccessControlData : ReadOnlySpan_1[int]
    FsAccessControlDescriptor : ReadOnlySpan_1[int]
    KernelCapabilityData : ReadOnlySpan_1[int]
    KernelCapabilityDescriptor : ReadOnlySpan_1[int]
    Meta : ReadOnlyRef_1[Meta]
    ServiceAccessControlData : ReadOnlySpan_1[int]
    ServiceAccessControlDescriptor : ReadOnlySpan_1[int]


class NsoHeader:
    ApiInfoOffset : int
    ApiInfoSize : int
    BssSize : int
    DataFileOffset : int
    DataFileSize : int
    DataHash : Array32_1[int]
    DataMemoryOffset : int
    DataSize : int
    DynStrOffset : int
    DynStrSize : int
    DynSymOffset : int
    DynSymSize : int
    Flags : NsoHeader.Flag
    Magic : int
    ModuleId : Array32_1[int]
    ModuleNameOffset : int
    ModuleNameSize : int
    Reserved08 : int
    Reserved6C : Array28_1[int]
    RoFileOffset : int
    RoFileSize : int
    RoHash : Array32_1[int]
    RoMemoryOffset : int
    RoSize : int
    SegmentCount : int
    TextFileOffset : int
    TextFileSize : int
    TextHash : Array32_1[int]
    TextMemoryOffset : int
    TextSize : int
    Version : int
    @property
    def CompressedSizes(self) -> Span_1[int]: ...
    @property
    def SegmentHashes(self) -> Span_1[Array32_1[int]]: ...
    @property
    def Segments(self) -> Span_1[NsoHeader.SegmentHeader]: ...

    class Flag(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        TextCompress : NsoHeader.Flag # 1
        RoCompress : NsoHeader.Flag # 2
        DataCompress : NsoHeader.Flag # 4
        TextHash : NsoHeader.Flag # 8
        RoHash : NsoHeader.Flag # 16
        DataHash : NsoHeader.Flag # 32


    class SegmentHeader:
        FileOffset : int
        MemoryOffset : int
        Size : int



class NsoReader:
    def __init__(self) -> None: ...
    Header : NsoHeader
    def GetSegmentSize(self, segment: NsoReader.SegmentType, size: clr.Reference[int]) -> Result: ...
    def Initialize(self, nsoFile: IFile) -> Result: ...
    def ReadSegment(self, segment: NsoReader.SegmentType, buffer: Span_1[int]) -> Result: ...

    class SegmentType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Text : NsoReader.SegmentType # 0
        Ro : NsoReader.SegmentType # 1
        Data : NsoReader.SegmentType # 2



class ResultLoader(abc.ABC):
    ModuleLoader : int
    @classmethod
    @property
    def InsufficientAddressSpace(cls) -> Result.Base: ...
    @classmethod
    @property
    def InsufficientNroRegistrations(cls) -> Result.Base: ...
    @classmethod
    @property
    def InsufficientNrrRegistrations(cls) -> Result.Base: ...
    @classmethod
    @property
    def InternalError(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidAcidSignature(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidAddress(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityApplicationType(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityDebugFlags(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityHandleTable(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityInterruptPair(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityKernelFlags(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityKernelVersion(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityMapPage(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilityMapRange(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCapabilitySyscallMask(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidMeta(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidNcaSignature(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidNro(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidNrr(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidNso(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPath(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidProcess(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidProgramId(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidSession(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidSignature(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidVersion(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotLoaded(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotPinned(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotRegistered(cls) -> Result.Base: ...
    @classmethod
    @property
    def NroAlreadyLoaded(cls) -> Result.Base: ...
    @classmethod
    @property
    def TooLargeMeta(cls) -> Result.Base: ...
    @classmethod
    @property
    def TooLongArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def TooManyArguments(cls) -> Result.Base: ...
    @classmethod
    @property
    def TooManyProcesses(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnknownCapability(cls) -> Result.Base: ...

