import typing, clr, abc
from System import Span_1, ReadOnlySpan_1, Exception, IComparable, IComparable_1, IEquatable_1, Attribute, IDisposable, Array_1
from LibHac import Result
from System.Collections import IDictionary
from System.Reflection import MethodBase
from System.IO import Stream, BinaryReader, BinaryWriter
from System.Text import StringBuilder

class BlitSpan_GenericClasses(abc.ABCMeta):
    Generic_BlitSpan_GenericClasses_BlitSpan_1_T = typing.TypeVar('Generic_BlitSpan_GenericClasses_BlitSpan_1_T')
    def __getitem__(self, types : typing.Type[Generic_BlitSpan_GenericClasses_BlitSpan_1_T]) -> typing.Type[BlitSpan_1[Generic_BlitSpan_GenericClasses_BlitSpan_1_T]]: ...

BlitSpan : BlitSpan_GenericClasses

BlitSpan_1_T = typing.TypeVar('BlitSpan_1_T')
class BlitSpan_1(typing.Generic[BlitSpan_1_T]):
    @typing.overload
    def __init__(self, data: Span_1[BlitSpan_1_T]) -> None: ...
    @typing.overload
    def __init__(self, data: Span_1[int]) -> None: ...
    @typing.overload
    def __init__(self, data: clr.Reference[BlitSpan_1_T]) -> None: ...
    @property
    def Item(self) -> clr.Reference[BlitSpan_1_T]: ...
    @property
    def Length(self) -> int: ...
    @property
    def Span(self) -> Span_1[BlitSpan_1_T]: ...
    @property
    def Value(self) -> clr.Reference[BlitSpan_1_T]: ...
    @staticmethod
    def QueryByteLength(elementCount: int) -> int: ...
    # Skipped GetByteSpan due to it being static, abstract and generic.

    GetByteSpan : GetByteSpan_MethodGroup[BlitSpan_1_T]
    GetByteSpan_MethodGroup_BlitSpan_1_T = typing.TypeVar('GetByteSpan_MethodGroup_BlitSpan_1_T')
    class GetByteSpan_MethodGroup(typing.Generic[GetByteSpan_MethodGroup_BlitSpan_1_T]):
        GetByteSpan_MethodGroup_BlitSpan_1_T = BlitSpan_1.GetByteSpan_MethodGroup_BlitSpan_1_T
        @typing.overload
        def __call__(self) -> Span_1[int]:...
        @typing.overload
        def __call__(self, elementIndex: int) -> Span_1[int]:...



class BlitStruct_GenericClasses(abc.ABCMeta):
    Generic_BlitStruct_GenericClasses_BlitStruct_1_T = typing.TypeVar('Generic_BlitStruct_GenericClasses_BlitStruct_1_T')
    def __getitem__(self, types : typing.Type[Generic_BlitStruct_GenericClasses_BlitStruct_1_T]) -> typing.Type[BlitStruct_1[Generic_BlitStruct_GenericClasses_BlitStruct_1_T]]: ...

BlitStruct : BlitStruct_GenericClasses

BlitStruct_1_T = typing.TypeVar('BlitStruct_1_T')
class BlitStruct_1(typing.Generic[BlitStruct_1_T]):
    def __init__(self, elementCount: int) -> None: ...
    @property
    def BlitSpan(self) -> BlitSpan_1[BlitStruct_1_T]: ...
    @property
    def ByteSpan(self) -> Span_1[int]: ...
    @property
    def Length(self) -> int: ...
    @property
    def Span(self) -> Span_1[BlitStruct_1_T]: ...
    @property
    def Value(self) -> clr.Reference[BlitStruct_1_T]: ...
    @staticmethod
    def QueryByteLength(elementCount: int) -> int: ...


class Box_GenericClasses(abc.ABCMeta):
    Generic_Box_GenericClasses_Box_1_T = typing.TypeVar('Generic_Box_GenericClasses_Box_1_T')
    def __getitem__(self, types : typing.Type[Generic_Box_GenericClasses_Box_1_T]) -> typing.Type[Box_1[Generic_Box_GenericClasses_Box_1_T]]: ...

Box : Box_GenericClasses

Box_1_T = typing.TypeVar('Box_1_T')
class Box_1(typing.Generic[Box_1_T]):
    def __init__(self) -> None: ...
    @property
    def Value(self) -> clr.Reference[Box_1_T]: ...


class Buffer16:
    @property
    def Bytes(self) -> Span_1[int]: ...
    @property
    def Item(self) -> int: ...
    @Item.setter
    def Item(self, value: int) -> int: ...
    # Operator not supported op_Implicit(value: Buffer16&)
    # Operator not supported op_Implicit(value: Buffer16&)
    def ToString(self) -> str: ...
    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Type[As_1_T1]) -> As_1[As_1_T1]: ...

        As_1_T1 = typing.TypeVar('As_1_T1')
        class As_1(typing.Generic[As_1_T1]):
            As_1_T = Buffer16.As_MethodGroup.As_1_T1
            def __call__(self) -> clr.Reference[As_1_T]:...


    # Skipped AsReadOnlySpan due to it being static, abstract and generic.

    AsReadOnlySpan : AsReadOnlySpan_MethodGroup
    class AsReadOnlySpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsReadOnlySpan_1_T1]) -> AsReadOnlySpan_1[AsReadOnlySpan_1_T1]: ...

        AsReadOnlySpan_1_T1 = typing.TypeVar('AsReadOnlySpan_1_T1')
        class AsReadOnlySpan_1(typing.Generic[AsReadOnlySpan_1_T1]):
            AsReadOnlySpan_1_T = Buffer16.AsReadOnlySpan_MethodGroup.AsReadOnlySpan_1_T1
            def __call__(self) -> ReadOnlySpan_1[AsReadOnlySpan_1_T]:...


    # Skipped AsSpan due to it being static, abstract and generic.

    AsSpan : AsSpan_MethodGroup
    class AsSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSpan_1_T1]) -> AsSpan_1[AsSpan_1_T1]: ...

        AsSpan_1_T1 = typing.TypeVar('AsSpan_1_T1')
        class AsSpan_1(typing.Generic[AsSpan_1_T1]):
            AsSpan_1_T = Buffer16.AsSpan_MethodGroup.AsSpan_1_T1
            def __call__(self) -> Span_1[AsSpan_1_T]:...




class Buffer32:
    @property
    def Bytes(self) -> Span_1[int]: ...
    @property
    def Item(self) -> int: ...
    @Item.setter
    def Item(self, value: int) -> int: ...
    # Operator not supported op_Implicit(value: Buffer32&)
    # Operator not supported op_Implicit(value: Buffer32&)
    def ToString(self) -> str: ...
    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Type[As_1_T1]) -> As_1[As_1_T1]: ...

        As_1_T1 = typing.TypeVar('As_1_T1')
        class As_1(typing.Generic[As_1_T1]):
            As_1_T = Buffer32.As_MethodGroup.As_1_T1
            def __call__(self) -> clr.Reference[As_1_T]:...


    # Skipped AsReadOnlySpan due to it being static, abstract and generic.

    AsReadOnlySpan : AsReadOnlySpan_MethodGroup
    class AsReadOnlySpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsReadOnlySpan_1_T1]) -> AsReadOnlySpan_1[AsReadOnlySpan_1_T1]: ...

        AsReadOnlySpan_1_T1 = typing.TypeVar('AsReadOnlySpan_1_T1')
        class AsReadOnlySpan_1(typing.Generic[AsReadOnlySpan_1_T1]):
            AsReadOnlySpan_1_T = Buffer32.AsReadOnlySpan_MethodGroup.AsReadOnlySpan_1_T1
            def __call__(self) -> ReadOnlySpan_1[AsReadOnlySpan_1_T]:...


    # Skipped AsSpan due to it being static, abstract and generic.

    AsSpan : AsSpan_MethodGroup
    class AsSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSpan_1_T1]) -> AsSpan_1[AsSpan_1_T1]: ...

        AsSpan_1_T1 = typing.TypeVar('AsSpan_1_T1')
        class AsSpan_1(typing.Generic[AsSpan_1_T1]):
            AsSpan_1_T = Buffer32.AsSpan_MethodGroup.AsSpan_1_T1
            def __call__(self) -> Span_1[AsSpan_1_T]:...




class HorizonResultException(LibHacException):
    @typing.overload
    def __init__(self, result: Result) -> None: ...
    @typing.overload
    def __init__(self, result: Result, message: str) -> None: ...
    @typing.overload
    def __init__(self, result: Result, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def InnerMessage(self) -> str: ...
    @property
    def InternalResultValue(self) -> Result: ...
    @property
    def Message(self) -> str: ...
    @property
    def ResultValue(self) -> Result: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class Id128(IComparable, IComparable_1[Id128], IEquatable_1[Id128]):
    @typing.overload
    def __init__(self, high: int, low: int) -> None: ...
    @typing.overload
    def __init__(self, uid: ReadOnlySpan_1[int]) -> None: ...
    High : int
    Low : int
    @classmethod
    @property
    def Zero(cls) -> Id128: ...
    def AsBytes(self) -> ReadOnlySpan_1[int]: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: Id128, right: Id128) -> bool: ...
    def __gt__(self, left: Id128, right: Id128) -> bool: ...
    def __ge__(self, left: Id128, right: Id128) -> bool: ...
    def __ne__(self, left: Id128, right: Id128) -> bool: ...
    def __lt__(self, left: Id128, right: Id128) -> bool: ...
    def __le__(self, left: Id128, right: Id128) -> bool: ...
    def ToBytes(self, output: Span_1[int]) -> None: ...
    def ToString(self) -> str: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, other: Id128) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Id128) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class InteropWin32(abc.ABC):
    @staticmethod
    def FindClose(handle: int) -> bool: ...
    @staticmethod
    def MultiByteToWideChar(codePage: int, bytes: ReadOnlySpan_1[int], chars: Span_1[str]) -> int: ...
    # Skipped FindFirstFileW due to it being static, abstract and generic.

    FindFirstFileW : FindFirstFileW_MethodGroup
    class FindFirstFileW_MethodGroup:
        @typing.overload
        def __call__(self, fileName: ReadOnlySpan_1[str], findFileData: clr.Reference[InteropWin32.Win32FindData]) -> int:...
        @typing.overload
        def __call__(self, lpFileName: clr.Reference[str], lpFindFileData: clr.Reference[InteropWin32.Win32FindData]) -> int:...


    class Win32FindData:
        FileAttributes : int
        Reserved0 : int
        Reserved1 : int
        @property
        def AlternateFileName(self) -> Span_1[str]: ...
        @property
        def CreationTime(self) -> int: ...
        @property
        def FileName(self) -> Span_1[str]: ...
        @property
        def FileSize(self) -> int: ...
        @property
        def LastAccessTime(self) -> int: ...
        @property
        def LastWriteTime(self) -> int: ...

        class <_alternateFileName>e__FixedBuffer:
            FixedElementField : str


        class <_fileName>e__FixedBuffer:
            FixedElementField : str




class IProgressReport(typing.Protocol):
    @abc.abstractmethod
    def LogMessage(self, message: str) -> None: ...
    @abc.abstractmethod
    def Report(self, value: int) -> None: ...
    @abc.abstractmethod
    def ReportAdd(self, value: int) -> None: ...
    @abc.abstractmethod
    def SetTotal(self, value: int) -> None: ...


class Key128(IEquatable_1[Key128]):
    def __init__(self, bytes: ReadOnlySpan_1[int]) -> None: ...
    @property
    def Value(self) -> Span_1[int]: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: Key128, right: Key128) -> bool: ...
    def __ne__(self, left: Key128, right: Key128) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Key128) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class LibHacException(Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class NonCopyableAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NonCopyableDisposableAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ProgressBar(IProgressReport, IDisposable):
    def __init__(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetRateString(self) -> str: ...
    def LogMessage(self, message: str) -> None: ...
    def PauseStopWatch(self) -> None: ...
    def Report(self, value: int) -> None: ...
    def ReportAdd(self, value: int) -> None: ...
    def ResumeStopWatch(self) -> None: ...
    def SetTotal(self, value: int) -> None: ...
    def StartNewStopWatch(self) -> None: ...


class ReadOnlyRef_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlyRef_GenericClasses_ReadOnlyRef_1_T = typing.TypeVar('Generic_ReadOnlyRef_GenericClasses_ReadOnlyRef_1_T')
    def __getitem__(self, types : typing.Type[Generic_ReadOnlyRef_GenericClasses_ReadOnlyRef_1_T]) -> typing.Type[ReadOnlyRef_1[Generic_ReadOnlyRef_GenericClasses_ReadOnlyRef_1_T]]: ...

ReadOnlyRef : ReadOnlyRef_GenericClasses

ReadOnlyRef_1_T = typing.TypeVar('ReadOnlyRef_1_T')
class ReadOnlyRef_1(typing.Generic[ReadOnlyRef_1_T]):
    @typing.overload
    def __init__(self, pointer: clr.Reference[None]) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[ReadOnlyRef_1_T]) -> None: ...
    @property
    def IsNull(self) -> bool: ...
    @property
    def Value(self) -> clr.Reference[ReadOnlyRef_1_T]: ...
    # Operator not supported op_Implicit(reference: ReadOnlyRef`1)


class Ref_GenericClasses(abc.ABCMeta):
    Generic_Ref_GenericClasses_Ref_1_T = typing.TypeVar('Generic_Ref_GenericClasses_Ref_1_T')
    def __getitem__(self, types : typing.Type[Generic_Ref_GenericClasses_Ref_1_T]) -> typing.Type[Ref_1[Generic_Ref_GenericClasses_Ref_1_T]]: ...

Ref : Ref_GenericClasses

Ref_1_T = typing.TypeVar('Ref_1_T')
class Ref_1(typing.Generic[Ref_1_T]):
    @typing.overload
    def __init__(self, pointer: clr.Reference[None]) -> None: ...
    @typing.overload
    def __init__(self, value: clr.Reference[Ref_1_T]) -> None: ...
    @property
    def IsNull(self) -> bool: ...
    @property
    def Value(self) -> clr.Reference[Ref_1_T]: ...
    # Operator not supported op_Implicit(reference: Ref`1)


class RentedArray_GenericClasses(abc.ABCMeta):
    Generic_RentedArray_GenericClasses_RentedArray_1_T = typing.TypeVar('Generic_RentedArray_GenericClasses_RentedArray_1_T')
    def __getitem__(self, types : typing.Type[Generic_RentedArray_GenericClasses_RentedArray_1_T]) -> typing.Type[RentedArray_1[Generic_RentedArray_GenericClasses_RentedArray_1_T]]: ...

RentedArray : RentedArray_GenericClasses

RentedArray_1_T = typing.TypeVar('RentedArray_1_T')
class RentedArray_1(typing.Generic[RentedArray_1_T]):
    def __init__(self, minimumSize: int) -> None: ...
    @property
    def Array(self) -> Array_1[RentedArray_1_T]: ...
    @property
    def Span(self) -> Span_1[RentedArray_1_T]: ...
    def Dispose(self) -> None: ...


class ResultLibHac(abc.ABC):
    ModuleLibHac : int
    @classmethod
    @property
    def ArgumentOutOfRange(cls) -> Result.Base: ...
    @classmethod
    @property
    def BufferTooSmall(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidData(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidIni(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidIniFileSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidIniMagic(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidIniProcessCount(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidInitialProcessData(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidKip(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidKipFileSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidKipMagic(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidKipSegmentSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage1(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage1MarikoBodySize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage1Pk11Size(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage1SectionSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2HeaderSignature(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaEntryPointAlignment(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaEntryPointNotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaKeyGeneration(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaMagic(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaPayloadAlignment(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaPayloadSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaPayloadSizeAlignment(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaPayloadsOverlap(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaSizeA(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaSizeB(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2MetaTotalSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPackage2PayloadCorrupted(cls) -> Result.Base: ...
    @classmethod
    @property
    def KipSegmentDecompressionFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotImplemented(cls) -> Result.Base: ...
    @classmethod
    @property
    def NullArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def ServiceNotInitialized(cls) -> Result.Base: ...


class Shared(abc.ABC):
    # Skipped Move due to it being static, abstract and generic.

    Move : Move_MethodGroup
    class Move_MethodGroup:
        def __getitem__(self, t:typing.Type[Move_1_T1]) -> Move_1[Move_1_T1]: ...

        Move_1_T1 = typing.TypeVar('Move_1_T1')
        class Move_1(typing.Generic[Move_1_T1]):
            Move_1_T = Shared.Move_MethodGroup.Move_1_T1
            @typing.overload
            def __call__(self, value: clr.Reference[Move_1_T]) -> Move_1_T:...
            @typing.overload
            def __call__(self, dest: clr.Reference[Move_1_T], value: clr.Reference[Move_1_T]) -> None:...




class SharedRef_GenericClasses(abc.ABCMeta):
    Generic_SharedRef_GenericClasses_SharedRef_1_T = typing.TypeVar('Generic_SharedRef_GenericClasses_SharedRef_1_T')
    def __getitem__(self, types : typing.Type[Generic_SharedRef_GenericClasses_SharedRef_1_T]) -> typing.Type[SharedRef_1[Generic_SharedRef_GenericClasses_SharedRef_1_T]]: ...

SharedRef : SharedRef_GenericClasses

SharedRef_1_T = typing.TypeVar('SharedRef_1_T')
class SharedRef_1(typing.Generic[SharedRef_1_T], IDisposable):
    def __init__(self, value: SharedRef_1_T) -> None: ...
    @property
    def Get(self) -> SharedRef_1_T: ...
    @property
    def HasValue(self) -> bool: ...
    @property
    def UseCount(self) -> int: ...
    def Destroy(self) -> None: ...
    def Dispose(self) -> None: ...
    def Swap(self, other: clr.Reference[SharedRef_1[SharedRef_1_T]]) -> None: ...
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup[SharedRef_1_T]
    Create_MethodGroup_SharedRef_1_T = typing.TypeVar('Create_MethodGroup_SharedRef_1_T')
    class Create_MethodGroup(typing.Generic[Create_MethodGroup_SharedRef_1_T]):
        Create_MethodGroup_SharedRef_1_T = SharedRef_1.Create_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_MethodGroup_SharedRef_1_T, Create_1_T1]: ...

        Create_1_SharedRef_1_T = typing.TypeVar('Create_1_SharedRef_1_T')
        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_SharedRef_1_T, Create_1_T1]):
            Create_1_SharedRef_1_T = SharedRef_1.Create_MethodGroup.Create_1_SharedRef_1_T
            Create_1_TFrom = SharedRef_1.Create_MethodGroup.Create_1_T1
            @typing.overload
            def __call__(self, other: clr.Reference[WeakRef_1[Create_1_TFrom]]) -> SharedRef_1[Create_1_SharedRef_1_T]:...
            @typing.overload
            def __call__(self, other: clr.Reference[UniqueRef_1[Create_1_TFrom]]) -> SharedRef_1[Create_1_SharedRef_1_T]:...


    # Skipped CreateCopy due to it being static, abstract and generic.

    CreateCopy : CreateCopy_MethodGroup[SharedRef_1_T]
    CreateCopy_MethodGroup_SharedRef_1_T = typing.TypeVar('CreateCopy_MethodGroup_SharedRef_1_T')
    class CreateCopy_MethodGroup(typing.Generic[CreateCopy_MethodGroup_SharedRef_1_T]):
        CreateCopy_MethodGroup_SharedRef_1_T = SharedRef_1.CreateCopy_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[CreateCopy_1_T1]) -> CreateCopy_1[CreateCopy_MethodGroup_SharedRef_1_T, CreateCopy_1_T1]: ...

        CreateCopy_1_SharedRef_1_T = typing.TypeVar('CreateCopy_1_SharedRef_1_T')
        CreateCopy_1_T1 = typing.TypeVar('CreateCopy_1_T1')
        class CreateCopy_1(typing.Generic[CreateCopy_1_SharedRef_1_T, CreateCopy_1_T1]):
            CreateCopy_1_SharedRef_1_T = SharedRef_1.CreateCopy_MethodGroup.CreateCopy_1_SharedRef_1_T
            CreateCopy_1_TFrom = SharedRef_1.CreateCopy_MethodGroup.CreateCopy_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[CreateCopy_1_TFrom]]) -> SharedRef_1[CreateCopy_1_SharedRef_1_T]:...


    # Skipped CreateMove due to it being static, abstract and generic.

    CreateMove : CreateMove_MethodGroup[SharedRef_1_T]
    CreateMove_MethodGroup_SharedRef_1_T = typing.TypeVar('CreateMove_MethodGroup_SharedRef_1_T')
    class CreateMove_MethodGroup(typing.Generic[CreateMove_MethodGroup_SharedRef_1_T]):
        CreateMove_MethodGroup_SharedRef_1_T = SharedRef_1.CreateMove_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[CreateMove_1_T1]) -> CreateMove_1[CreateMove_MethodGroup_SharedRef_1_T, CreateMove_1_T1]: ...

        CreateMove_1_SharedRef_1_T = typing.TypeVar('CreateMove_1_SharedRef_1_T')
        CreateMove_1_T1 = typing.TypeVar('CreateMove_1_T1')
        class CreateMove_1(typing.Generic[CreateMove_1_SharedRef_1_T, CreateMove_1_T1]):
            CreateMove_1_SharedRef_1_T = SharedRef_1.CreateMove_MethodGroup.CreateMove_1_SharedRef_1_T
            CreateMove_1_TFrom = SharedRef_1.CreateMove_MethodGroup.CreateMove_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[CreateMove_1_TFrom]]) -> SharedRef_1[CreateMove_1_SharedRef_1_T]:...


    # Skipped Reset due to it being static, abstract and generic.

    Reset : Reset_MethodGroup[SharedRef_1_T]
    Reset_MethodGroup_SharedRef_1_T = typing.TypeVar('Reset_MethodGroup_SharedRef_1_T')
    class Reset_MethodGroup(typing.Generic[Reset_MethodGroup_SharedRef_1_T]):
        Reset_MethodGroup_SharedRef_1_T = SharedRef_1.Reset_MethodGroup_SharedRef_1_T
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, value: Reset_MethodGroup_SharedRef_1_T) -> None:...

    # Skipped Set due to it being static, abstract and generic.

    Set : Set_MethodGroup[SharedRef_1_T]
    Set_MethodGroup_SharedRef_1_T = typing.TypeVar('Set_MethodGroup_SharedRef_1_T')
    class Set_MethodGroup(typing.Generic[Set_MethodGroup_SharedRef_1_T]):
        Set_MethodGroup_SharedRef_1_T = SharedRef_1.Set_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[Set_1_T1]) -> Set_1[Set_MethodGroup_SharedRef_1_T, Set_1_T1]: ...

        Set_1_SharedRef_1_T = typing.TypeVar('Set_1_SharedRef_1_T')
        Set_1_T1 = typing.TypeVar('Set_1_T1')
        class Set_1(typing.Generic[Set_1_SharedRef_1_T, Set_1_T1]):
            Set_1_SharedRef_1_T = SharedRef_1.Set_MethodGroup.Set_1_SharedRef_1_T
            Set_1_TFrom = SharedRef_1.Set_MethodGroup.Set_1_T1
            def __call__(self, other: clr.Reference[UniqueRef_1[Set_1_TFrom]]) -> None:...


    # Skipped SetByCopy due to it being static, abstract and generic.

    SetByCopy : SetByCopy_MethodGroup[SharedRef_1_T]
    SetByCopy_MethodGroup_SharedRef_1_T = typing.TypeVar('SetByCopy_MethodGroup_SharedRef_1_T')
    class SetByCopy_MethodGroup(typing.Generic[SetByCopy_MethodGroup_SharedRef_1_T]):
        SetByCopy_MethodGroup_SharedRef_1_T = SharedRef_1.SetByCopy_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[SetByCopy_1_T1]) -> SetByCopy_1[SetByCopy_MethodGroup_SharedRef_1_T, SetByCopy_1_T1]: ...

        SetByCopy_1_SharedRef_1_T = typing.TypeVar('SetByCopy_1_SharedRef_1_T')
        SetByCopy_1_T1 = typing.TypeVar('SetByCopy_1_T1')
        class SetByCopy_1(typing.Generic[SetByCopy_1_SharedRef_1_T, SetByCopy_1_T1]):
            SetByCopy_1_SharedRef_1_T = SharedRef_1.SetByCopy_MethodGroup.SetByCopy_1_SharedRef_1_T
            SetByCopy_1_TFrom = SharedRef_1.SetByCopy_MethodGroup.SetByCopy_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[SetByCopy_1_TFrom]]) -> None:...


    # Skipped SetByMove due to it being static, abstract and generic.

    SetByMove : SetByMove_MethodGroup[SharedRef_1_T]
    SetByMove_MethodGroup_SharedRef_1_T = typing.TypeVar('SetByMove_MethodGroup_SharedRef_1_T')
    class SetByMove_MethodGroup(typing.Generic[SetByMove_MethodGroup_SharedRef_1_T]):
        SetByMove_MethodGroup_SharedRef_1_T = SharedRef_1.SetByMove_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[SetByMove_1_T1]) -> SetByMove_1[SetByMove_MethodGroup_SharedRef_1_T, SetByMove_1_T1]: ...

        SetByMove_1_SharedRef_1_T = typing.TypeVar('SetByMove_1_SharedRef_1_T')
        SetByMove_1_T1 = typing.TypeVar('SetByMove_1_T1')
        class SetByMove_1(typing.Generic[SetByMove_1_SharedRef_1_T, SetByMove_1_T1]):
            SetByMove_1_SharedRef_1_T = SharedRef_1.SetByMove_MethodGroup.SetByMove_1_SharedRef_1_T
            SetByMove_1_TFrom = SharedRef_1.SetByMove_MethodGroup.SetByMove_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[SetByMove_1_TFrom]]) -> None:...


    # Skipped TryCastSet due to it being static, abstract and generic.

    TryCastSet : TryCastSet_MethodGroup[SharedRef_1_T]
    TryCastSet_MethodGroup_SharedRef_1_T = typing.TypeVar('TryCastSet_MethodGroup_SharedRef_1_T')
    class TryCastSet_MethodGroup(typing.Generic[TryCastSet_MethodGroup_SharedRef_1_T]):
        TryCastSet_MethodGroup_SharedRef_1_T = SharedRef_1.TryCastSet_MethodGroup_SharedRef_1_T
        def __getitem__(self, t:typing.Type[TryCastSet_1_T1]) -> TryCastSet_1[TryCastSet_MethodGroup_SharedRef_1_T, TryCastSet_1_T1]: ...

        TryCastSet_1_SharedRef_1_T = typing.TypeVar('TryCastSet_1_SharedRef_1_T')
        TryCastSet_1_T1 = typing.TypeVar('TryCastSet_1_T1')
        class TryCastSet_1(typing.Generic[TryCastSet_1_SharedRef_1_T, TryCastSet_1_T1]):
            TryCastSet_1_SharedRef_1_T = SharedRef_1.TryCastSet_MethodGroup.TryCastSet_1_SharedRef_1_T
            TryCastSet_1_TFrom = SharedRef_1.TryCastSet_MethodGroup.TryCastSet_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[TryCastSet_1_TFrom]]) -> bool:...




class SharedRefExtensions(abc.ABC):
    # Skipped Ref due to it being static, abstract and generic.

    Ref : Ref_MethodGroup
    class Ref_MethodGroup:
        def __getitem__(self, t:typing.Type[Ref_1_T1]) -> Ref_1[Ref_1_T1]: ...

        Ref_1_T1 = typing.TypeVar('Ref_1_T1')
        class Ref_1(typing.Generic[Ref_1_T1]):
            Ref_1_T = SharedRefExtensions.Ref_MethodGroup.Ref_1_T1
            @typing.overload
            def __call__(self, value: clr.Reference[SharedRef_1[Ref_1_T]]) -> clr.Reference[SharedRef_1[Ref_1_T]]:...
            @typing.overload
            def __call__(self, value: clr.Reference[WeakRef_1[Ref_1_T]]) -> clr.Reference[WeakRef_1[Ref_1_T]]:...




class SpanExtensions(abc.ABC):
    # Skipped At due to it being static, abstract and generic.

    At : At_MethodGroup
    class At_MethodGroup:
        @typing.overload
        def __call__(self, span: clr.Reference[ReadOnlySpan_1[int]], i: int) -> int:...
        @typing.overload
        def __call__(self, span: clr.Reference[Span_1[int]], i: int) -> int:...



class SpanHelpers(abc.ABC):
    # Skipped AsByteSpan due to it being static, abstract and generic.

    AsByteSpan : AsByteSpan_MethodGroup
    class AsByteSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsByteSpan_1_T1]) -> AsByteSpan_1[AsByteSpan_1_T1]: ...

        AsByteSpan_1_T1 = typing.TypeVar('AsByteSpan_1_T1')
        class AsByteSpan_1(typing.Generic[AsByteSpan_1_T1]):
            AsByteSpan_1_T = SpanHelpers.AsByteSpan_MethodGroup.AsByteSpan_1_T1
            def __call__(self, reference: clr.Reference[AsByteSpan_1_T]) -> Span_1[int]:...


    # Skipped AsReadOnlyByteSpan due to it being static, abstract and generic.

    AsReadOnlyByteSpan : AsReadOnlyByteSpan_MethodGroup
    class AsReadOnlyByteSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsReadOnlyByteSpan_1_T1]) -> AsReadOnlyByteSpan_1[AsReadOnlyByteSpan_1_T1]: ...

        AsReadOnlyByteSpan_1_T1 = typing.TypeVar('AsReadOnlyByteSpan_1_T1')
        class AsReadOnlyByteSpan_1(typing.Generic[AsReadOnlyByteSpan_1_T1]):
            AsReadOnlyByteSpan_1_T = SpanHelpers.AsReadOnlyByteSpan_MethodGroup.AsReadOnlyByteSpan_1_T1
            def __call__(self, reference: clr.Reference[AsReadOnlyByteSpan_1_T]) -> ReadOnlySpan_1[int]:...


    # Skipped AsReadOnlySpan due to it being static, abstract and generic.

    AsReadOnlySpan : AsReadOnlySpan_MethodGroup
    class AsReadOnlySpan_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[AsReadOnlySpan_1_T1]) -> AsReadOnlySpan_1[AsReadOnlySpan_1_T1]: ...

        AsReadOnlySpan_1_T1 = typing.TypeVar('AsReadOnlySpan_1_T1')
        class AsReadOnlySpan_1(typing.Generic[AsReadOnlySpan_1_T1]):
            AsReadOnlySpan_1_T = SpanHelpers.AsReadOnlySpan_MethodGroup.AsReadOnlySpan_1_T1
            def __call__(self, reference: clr.Reference[AsReadOnlySpan_1_T]) -> ReadOnlySpan_1[AsReadOnlySpan_1_T]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[AsReadOnlySpan_2_T1], typing.Type[AsReadOnlySpan_2_T2]]) -> AsReadOnlySpan_2[AsReadOnlySpan_2_T1, AsReadOnlySpan_2_T2]: ...

        AsReadOnlySpan_2_T1 = typing.TypeVar('AsReadOnlySpan_2_T1')
        AsReadOnlySpan_2_T2 = typing.TypeVar('AsReadOnlySpan_2_T2')
        class AsReadOnlySpan_2(typing.Generic[AsReadOnlySpan_2_T1, AsReadOnlySpan_2_T2]):
            AsReadOnlySpan_2_TStruct = SpanHelpers.AsReadOnlySpan_MethodGroup.AsReadOnlySpan_2_T1
            AsReadOnlySpan_2_TSpan = SpanHelpers.AsReadOnlySpan_MethodGroup.AsReadOnlySpan_2_T2
            def __call__(self, reference: clr.Reference[AsReadOnlySpan_2_TStruct]) -> ReadOnlySpan_1[AsReadOnlySpan_2_TSpan]:...


    # Skipped AsReadOnlyStruct due to it being static, abstract and generic.

    AsReadOnlyStruct : AsReadOnlyStruct_MethodGroup
    class AsReadOnlyStruct_MethodGroup:
        def __getitem__(self, t:typing.Type[AsReadOnlyStruct_1_T1]) -> AsReadOnlyStruct_1[AsReadOnlyStruct_1_T1]: ...

        AsReadOnlyStruct_1_T1 = typing.TypeVar('AsReadOnlyStruct_1_T1')
        class AsReadOnlyStruct_1(typing.Generic[AsReadOnlyStruct_1_T1]):
            AsReadOnlyStruct_1_T = SpanHelpers.AsReadOnlyStruct_MethodGroup.AsReadOnlyStruct_1_T1
            def __call__(self, span: ReadOnlySpan_1[int]) -> clr.Reference[AsReadOnlyStruct_1_T]:...


    # Skipped AsSpan due to it being static, abstract and generic.

    AsSpan : AsSpan_MethodGroup
    class AsSpan_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[AsSpan_1_T1]) -> AsSpan_1[AsSpan_1_T1]: ...

        AsSpan_1_T1 = typing.TypeVar('AsSpan_1_T1')
        class AsSpan_1(typing.Generic[AsSpan_1_T1]):
            AsSpan_1_T = SpanHelpers.AsSpan_MethodGroup.AsSpan_1_T1
            def __call__(self, reference: clr.Reference[AsSpan_1_T]) -> Span_1[AsSpan_1_T]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[AsSpan_2_T1], typing.Type[AsSpan_2_T2]]) -> AsSpan_2[AsSpan_2_T1, AsSpan_2_T2]: ...

        AsSpan_2_T1 = typing.TypeVar('AsSpan_2_T1')
        AsSpan_2_T2 = typing.TypeVar('AsSpan_2_T2')
        class AsSpan_2(typing.Generic[AsSpan_2_T1, AsSpan_2_T2]):
            AsSpan_2_TStruct = SpanHelpers.AsSpan_MethodGroup.AsSpan_2_T1
            AsSpan_2_TSpan = SpanHelpers.AsSpan_MethodGroup.AsSpan_2_T2
            def __call__(self, reference: clr.Reference[AsSpan_2_TStruct]) -> Span_1[AsSpan_2_TSpan]:...


    # Skipped AsStruct due to it being static, abstract and generic.

    AsStruct : AsStruct_MethodGroup
    class AsStruct_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[AsStruct_1_T1]) -> AsStruct_1[AsStruct_1_T1]: ...

        AsStruct_1_T1 = typing.TypeVar('AsStruct_1_T1')
        class AsStruct_1(typing.Generic[AsStruct_1_T1]):
            AsStruct_1_T = SpanHelpers.AsStruct_MethodGroup.AsStruct_1_T1
            def __call__(self, span: Span_1[int]) -> clr.Reference[AsStruct_1_T]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[AsStruct_2_T1], typing.Type[AsStruct_2_T2]]) -> AsStruct_2[AsStruct_2_T1, AsStruct_2_T2]: ...

        AsStruct_2_T1 = typing.TypeVar('AsStruct_2_T1')
        AsStruct_2_T2 = typing.TypeVar('AsStruct_2_T2')
        class AsStruct_2(typing.Generic[AsStruct_2_T1, AsStruct_2_T2]):
            AsStruct_2_TFrom = SpanHelpers.AsStruct_MethodGroup.AsStruct_2_T1
            AsStruct_2_TTo = SpanHelpers.AsStruct_MethodGroup.AsStruct_2_T2
            @typing.overload
            def __call__(self, span: Span_1[AsStruct_2_TFrom]) -> clr.Reference[AsStruct_2_TTo]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[AsStruct_2_TFrom]) -> clr.Reference[AsStruct_2_TTo]:...


    # Skipped CreateReadOnlySpan due to it being static, abstract and generic.

    CreateReadOnlySpan : CreateReadOnlySpan_MethodGroup
    class CreateReadOnlySpan_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateReadOnlySpan_1_T1]) -> CreateReadOnlySpan_1[CreateReadOnlySpan_1_T1]: ...

        CreateReadOnlySpan_1_T1 = typing.TypeVar('CreateReadOnlySpan_1_T1')
        class CreateReadOnlySpan_1(typing.Generic[CreateReadOnlySpan_1_T1]):
            CreateReadOnlySpan_1_T = SpanHelpers.CreateReadOnlySpan_MethodGroup.CreateReadOnlySpan_1_T1
            def __call__(self, reference: clr.Reference[CreateReadOnlySpan_1_T], length: int) -> ReadOnlySpan_1[CreateReadOnlySpan_1_T]:...


    # Skipped CreateSpan due to it being static, abstract and generic.

    CreateSpan : CreateSpan_MethodGroup
    class CreateSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateSpan_1_T1]) -> CreateSpan_1[CreateSpan_1_T1]: ...

        CreateSpan_1_T1 = typing.TypeVar('CreateSpan_1_T1')
        class CreateSpan_1(typing.Generic[CreateSpan_1_T1]):
            CreateSpan_1_T = SpanHelpers.CreateSpan_MethodGroup.CreateSpan_1_T1
            def __call__(self, reference: clr.Reference[CreateSpan_1_T], length: int) -> Span_1[CreateSpan_1_T]:...




class U8Span:
    @typing.overload
    def __init__(self, value: ReadOnlySpan_1[int]) -> None: ...
    @typing.overload
    def __init__(self, value: str) -> None: ...
    @classmethod
    @property
    def Empty(cls) -> U8Span: ...
    @property
    def Item(self) -> int: ...
    @property
    def Length(self) -> int: ...
    @property
    def Value(self) -> ReadOnlySpan_1[int]: ...
    def GetOrNull(self, i: int) -> int: ...
    def GetUnsafe(self, i: int) -> int: ...
    def IsEmpty(self) -> bool: ...
    def IsNull(self) -> bool: ...
    # Operator not supported op_Explicit(value: String)
    # Operator not supported op_Explicit(value: U8Span&)
    # Operator not supported op_Implicit(value: U8Span&)
    def ToString(self) -> str: ...
    def ToU8String(self) -> U8String: ...
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup
    class Slice_MethodGroup:
        @typing.overload
        def __call__(self, start: int) -> U8Span:...
        @typing.overload
        def __call__(self, start: int, length: int) -> U8Span:...



class U8SpanMutable:
    @typing.overload
    def __init__(self, value: Span_1[int]) -> None: ...
    @typing.overload
    def __init__(self, value: str) -> None: ...
    @property
    def Item(self) -> int: ...
    @Item.setter
    def Item(self, value: int) -> int: ...
    @property
    def Length(self) -> int: ...
    @property
    def Value(self) -> Span_1[int]: ...
    def GetOrNull(self, i: int) -> int: ...
    def GetUnsafe(self, i: int) -> int: ...
    def IsEmpty(self) -> bool: ...
    def IsNull(self) -> bool: ...
    # Operator not supported op_Explicit(value: U8SpanMutable)
    # Operator not supported op_Explicit(value: String)
    # Operator not supported op_Implicit(value: U8SpanMutable)
    # Operator not supported op_Implicit(value: U8SpanMutable)
    # Operator not supported op_Implicit(value: U8SpanMutable)
    def ToString(self) -> str: ...
    def ToU8String(self) -> U8StringMutable: ...
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup
    class Slice_MethodGroup:
        @typing.overload
        def __call__(self, start: int) -> U8SpanMutable:...
        @typing.overload
        def __call__(self, start: int, length: int) -> U8SpanMutable:...



class U8String:
    @typing.overload
    def __init__(self, value: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, value: str) -> None: ...
    @property
    def Item(self) -> int: ...
    @property
    def Length(self) -> int: ...
    @property
    def Value(self) -> ReadOnlySpan_1[int]: ...
    def IsEmpty(self) -> bool: ...
    def IsNull(self) -> bool: ...
    # Operator not supported op_Explicit(value: U8String)
    # Operator not supported op_Explicit(value: String)
    # Operator not supported op_Implicit(value: U8String)
    # Operator not supported op_Implicit(value: U8String)
    def ToString(self) -> str: ...
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup
    class Slice_MethodGroup:
        @typing.overload
        def __call__(self, start: int) -> U8String:...
        @typing.overload
        def __call__(self, start: int, length: int) -> U8String:...



class U8StringBuilder:
    def __init__(self, buffer: Span_1[int], autoExpand: bool = ...) -> None: ...
    @property
    def AutoExpand(self) -> bool: ...
    @property
    def Buffer(self) -> Span_1[int]: ...
    @Buffer.setter
    def Buffer(self, value: Span_1[int]) -> Span_1[int]: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Length(self) -> int: ...
    @Length.setter
    def Length(self, value: int) -> int: ...
    @property
    def Overflowed(self) -> bool: ...
    @Overflowed.setter
    def Overflowed(self, value: bool) -> bool: ...
    def Dispose(self) -> None: ...
    def ToString(self) -> str: ...


class U8StringBuilderExtensions(abc.ABC):
    @staticmethod
    def PadLeft(sb: clr.Reference[U8StringBuilder], paddingCharacter: int, paddedLength: int) -> clr.Reference[U8StringBuilder]: ...
    @staticmethod
    def PadRight(sb: clr.Reference[U8StringBuilder], paddingCharacter: int, paddedLength: int) -> clr.Reference[U8StringBuilder]: ...
    # Skipped Append due to it being static, abstract and generic.

    Append : Append_MethodGroup
    class Append_MethodGroup:
        @typing.overload
        def __call__(self, sb: clr.Reference[U8StringBuilder], value: int) -> clr.Reference[U8StringBuilder]:...
        @typing.overload
        def __call__(self, sb: clr.Reference[U8StringBuilder], value: ReadOnlySpan_1[int]) -> clr.Reference[U8StringBuilder]:...

    # Skipped AppendFormat due to it being static, abstract and generic.

    AppendFormat : AppendFormat_MethodGroup
    class AppendFormat_MethodGroup:
        def __call__(self, sb: clr.Reference[U8StringBuilder], value: float, format: str = ..., precision: int = ...) -> clr.Reference[U8StringBuilder]:...
        # Method AppendFormat(sb : U8StringBuilder&, value : Double, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : Byte, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : SByte, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : UInt16, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : Int16, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : UInt32, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : Int32, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : UInt64, format : Char, precision : Byte) was skipped since it collides with above method
        # Method AppendFormat(sb : U8StringBuilder&, value : Int64, format : Char, precision : Byte) was skipped since it collides with above method



class U8StringHelpers(abc.ABC):
    @staticmethod
    def ToU8Span(value: str) -> U8Span: ...
    @staticmethod
    def ToU8String(value: str) -> U8String: ...


class U8StringMutable:
    @typing.overload
    def __init__(self, value: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, value: str) -> None: ...
    @property
    def Item(self) -> int: ...
    @Item.setter
    def Item(self, value: int) -> int: ...
    @property
    def Length(self) -> int: ...
    @property
    def Value(self) -> Span_1[int]: ...
    def IsEmpty(self) -> bool: ...
    def IsNull(self) -> bool: ...
    # Operator not supported op_Explicit(value: U8StringMutable)
    # Operator not supported op_Explicit(value: String)
    # Operator not supported op_Implicit(value: U8StringMutable)
    # Operator not supported op_Implicit(value: U8StringMutable)
    # Operator not supported op_Implicit(value: U8StringMutable)
    # Operator not supported op_Implicit(value: U8StringMutable)
    # Operator not supported op_Implicit(value: U8StringMutable)
    def ToString(self) -> str: ...
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup
    class Slice_MethodGroup:
        @typing.overload
        def __call__(self, start: int) -> U8StringMutable:...
        @typing.overload
        def __call__(self, start: int, length: int) -> U8StringMutable:...



class UniqueRef_GenericClasses(abc.ABCMeta):
    Generic_UniqueRef_GenericClasses_UniqueRef_1_T = typing.TypeVar('Generic_UniqueRef_GenericClasses_UniqueRef_1_T')
    def __getitem__(self, types : typing.Type[Generic_UniqueRef_GenericClasses_UniqueRef_1_T]) -> typing.Type[UniqueRef_1[Generic_UniqueRef_GenericClasses_UniqueRef_1_T]]: ...

UniqueRef : UniqueRef_GenericClasses

UniqueRef_1_T = typing.TypeVar('UniqueRef_1_T')
class UniqueRef_1(typing.Generic[UniqueRef_1_T], IDisposable):
    @typing.overload
    def __init__(self, other: clr.Reference[UniqueRef_1[UniqueRef_1_T]]) -> None: ...
    @typing.overload
    def __init__(self, value: UniqueRef_1_T) -> None: ...
    @property
    def Get(self) -> clr.Reference[UniqueRef_1_T]: ...
    @property
    def HasValue(self) -> bool: ...
    def Destroy(self) -> None: ...
    def Dispose(self) -> None: ...
    def Release(self) -> UniqueRef_1_T: ...
    def Swap(self, other: clr.Reference[UniqueRef_1[UniqueRef_1_T]]) -> None: ...
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup[UniqueRef_1_T]
    Create_MethodGroup_UniqueRef_1_T = typing.TypeVar('Create_MethodGroup_UniqueRef_1_T')
    class Create_MethodGroup(typing.Generic[Create_MethodGroup_UniqueRef_1_T]):
        Create_MethodGroup_UniqueRef_1_T = UniqueRef_1.Create_MethodGroup_UniqueRef_1_T
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_MethodGroup_UniqueRef_1_T, Create_1_T1]: ...

        Create_1_UniqueRef_1_T = typing.TypeVar('Create_1_UniqueRef_1_T')
        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_UniqueRef_1_T, Create_1_T1]):
            Create_1_UniqueRef_1_T = UniqueRef_1.Create_MethodGroup.Create_1_UniqueRef_1_T
            Create_1_TFrom = UniqueRef_1.Create_MethodGroup.Create_1_T1
            def __call__(self, other: clr.Reference[UniqueRef_1[Create_1_TFrom]]) -> UniqueRef_1[Create_1_UniqueRef_1_T]:...


    # Skipped Reset due to it being static, abstract and generic.

    Reset : Reset_MethodGroup[UniqueRef_1_T]
    Reset_MethodGroup_UniqueRef_1_T = typing.TypeVar('Reset_MethodGroup_UniqueRef_1_T')
    class Reset_MethodGroup(typing.Generic[Reset_MethodGroup_UniqueRef_1_T]):
        Reset_MethodGroup_UniqueRef_1_T = UniqueRef_1.Reset_MethodGroup_UniqueRef_1_T
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, value: Reset_MethodGroup_UniqueRef_1_T) -> None:...

    # Skipped Set due to it being static, abstract and generic.

    Set : Set_MethodGroup[UniqueRef_1_T]
    Set_MethodGroup_UniqueRef_1_T = typing.TypeVar('Set_MethodGroup_UniqueRef_1_T')
    class Set_MethodGroup(typing.Generic[Set_MethodGroup_UniqueRef_1_T]):
        Set_MethodGroup_UniqueRef_1_T = UniqueRef_1.Set_MethodGroup_UniqueRef_1_T
        def __getitem__(self, t:typing.Type[Set_1_T1]) -> Set_1[Set_MethodGroup_UniqueRef_1_T, Set_1_T1]: ...

        Set_1_UniqueRef_1_T = typing.TypeVar('Set_1_UniqueRef_1_T')
        Set_1_T1 = typing.TypeVar('Set_1_T1')
        class Set_1(typing.Generic[Set_1_UniqueRef_1_T, Set_1_T1]):
            Set_1_UniqueRef_1_T = UniqueRef_1.Set_MethodGroup.Set_1_UniqueRef_1_T
            Set_1_TFrom = UniqueRef_1.Set_MethodGroup.Set_1_T1
            def __call__(self, other: clr.Reference[UniqueRef_1[Set_1_TFrom]]) -> None:...

        def __call__(self, other: clr.Reference[UniqueRef_1[Set_MethodGroup_UniqueRef_1_T]]) -> None:...



class UniqueRefExtensions(abc.ABC):
    # Skipped Ref due to it being static, abstract and generic.

    Ref : Ref_MethodGroup
    class Ref_MethodGroup:
        def __getitem__(self, t:typing.Type[Ref_1_T1]) -> Ref_1[Ref_1_T1]: ...

        Ref_1_T1 = typing.TypeVar('Ref_1_T1')
        class Ref_1(typing.Generic[Ref_1_T1]):
            Ref_1_T = UniqueRefExtensions.Ref_MethodGroup.Ref_1_T1
            def __call__(self, value: clr.Reference[UniqueRef_1[Ref_1_T]]) -> clr.Reference[UniqueRef_1[Ref_1_T]]:...




class UnsafeHelpers(abc.ABC):
    # Skipped SkipParamInit due to it being static, abstract and generic.

    SkipParamInit : SkipParamInit_MethodGroup
    class SkipParamInit_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[SkipParamInit_1_T1]) -> SkipParamInit_1[SkipParamInit_1_T1]: ...

        SkipParamInit_1_T1 = typing.TypeVar('SkipParamInit_1_T1')
        class SkipParamInit_1(typing.Generic[SkipParamInit_1_T1]):
            SkipParamInit_1_T = UnsafeHelpers.SkipParamInit_MethodGroup.SkipParamInit_1_T1
            def __call__(self, value: clr.Reference[SkipParamInit_1_T]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SkipParamInit_2_T1], typing.Type[SkipParamInit_2_T2]]) -> SkipParamInit_2[SkipParamInit_2_T1, SkipParamInit_2_T2]: ...

        SkipParamInit_2_T1 = typing.TypeVar('SkipParamInit_2_T1')
        SkipParamInit_2_T2 = typing.TypeVar('SkipParamInit_2_T2')
        class SkipParamInit_2(typing.Generic[SkipParamInit_2_T1, SkipParamInit_2_T2]):
            SkipParamInit_2_T1 = UnsafeHelpers.SkipParamInit_MethodGroup.SkipParamInit_2_T1
            SkipParamInit_2_T2 = UnsafeHelpers.SkipParamInit_MethodGroup.SkipParamInit_2_T2
            def __call__(self, value1: clr.Reference[SkipParamInit_2_T1], value2: clr.Reference[SkipParamInit_2_T2]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SkipParamInit_3_T1], typing.Type[SkipParamInit_3_T2], typing.Type[SkipParamInit_3_T3]]) -> SkipParamInit_3[SkipParamInit_3_T1, SkipParamInit_3_T2, SkipParamInit_3_T3]: ...

        SkipParamInit_3_T1 = typing.TypeVar('SkipParamInit_3_T1')
        SkipParamInit_3_T2 = typing.TypeVar('SkipParamInit_3_T2')
        SkipParamInit_3_T3 = typing.TypeVar('SkipParamInit_3_T3')
        class SkipParamInit_3(typing.Generic[SkipParamInit_3_T1, SkipParamInit_3_T2, SkipParamInit_3_T3]):
            SkipParamInit_3_T1 = UnsafeHelpers.SkipParamInit_MethodGroup.SkipParamInit_3_T1
            SkipParamInit_3_T2 = UnsafeHelpers.SkipParamInit_MethodGroup.SkipParamInit_3_T2
            SkipParamInit_3_T3 = UnsafeHelpers.SkipParamInit_MethodGroup.SkipParamInit_3_T3
            def __call__(self, value1: clr.Reference[SkipParamInit_3_T1], value2: clr.Reference[SkipParamInit_3_T2], value3: clr.Reference[SkipParamInit_3_T3]) -> None:...




class Utilities(abc.ABC):
    @staticmethod
    def CopyStream(input: Stream, output: Stream, length: int, progress: IProgressReport = ...) -> None: ...
    @staticmethod
    def GetBytesReadable(bytes: int) -> str: ...
    @staticmethod
    def GetKeyRevisionSummary(revision: int) -> str: ...
    @staticmethod
    def GetMasterKeyRevision(keyGeneration: int) -> int: ...
    @staticmethod
    def IncrementByteArray(array: Array_1[int]) -> None: ...
    @staticmethod
    def MediaToReal(media: int) -> int: ...
    @staticmethod
    def MemDump(sb: StringBuilder, prefix: str, data: Array_1[int]) -> None: ...
    @staticmethod
    def ReadAscii(reader: BinaryReader, size: int) -> str: ...
    @staticmethod
    def ReadAsciiZ(reader: BinaryReader, maxLength: int = ...) -> str: ...
    @staticmethod
    def ReadUtf8(reader: BinaryReader, size: int) -> str: ...
    @staticmethod
    def ReadUtf8Z(reader: BinaryReader, maxLength: int = ...) -> str: ...
    @staticmethod
    def WriteAllBytes(input: Stream, filename: str, progress: IProgressReport = ...) -> None: ...
    @staticmethod
    def WriteUTF8(writer: BinaryWriter, value: str) -> None: ...
    @staticmethod
    def WriteUTF8Z(writer: BinaryWriter, value: str) -> None: ...
    # Skipped ArraysEqual due to it being static, abstract and generic.

    ArraysEqual : ArraysEqual_MethodGroup
    class ArraysEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[ArraysEqual_1_T1]) -> ArraysEqual_1[ArraysEqual_1_T1]: ...

        ArraysEqual_1_T1 = typing.TypeVar('ArraysEqual_1_T1')
        class ArraysEqual_1(typing.Generic[ArraysEqual_1_T1]):
            ArraysEqual_1_T = Utilities.ArraysEqual_MethodGroup.ArraysEqual_1_T1
            def __call__(self, a1: Array_1[ArraysEqual_1_T], a2: Array_1[ArraysEqual_1_T]) -> bool:...


    # Skipped IsZeros due to it being static, abstract and generic.

    IsZeros : IsZeros_MethodGroup
    class IsZeros_MethodGroup:
        @typing.overload
        def __call__(self, array: Array_1[int]) -> bool:...
        @typing.overload
        def __call__(self, span: Span_1[int]) -> bool:...
        @typing.overload
        def __call__(self, span: ReadOnlySpan_1[int]) -> bool:...

    # Skipped SpansEqual due to it being static, abstract and generic.

    SpansEqual : SpansEqual_MethodGroup
    class SpansEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[SpansEqual_1_T1]) -> SpansEqual_1[SpansEqual_1_T1]: ...

        SpansEqual_1_T1 = typing.TypeVar('SpansEqual_1_T1')
        class SpansEqual_1(typing.Generic[SpansEqual_1_T1]):
            SpansEqual_1_T = Utilities.SpansEqual_MethodGroup.SpansEqual_1_T1
            @typing.overload
            def __call__(self, a1: Span_1[SpansEqual_1_T], a2: Span_1[SpansEqual_1_T]) -> bool:...
            @typing.overload
            def __call__(self, a1: ReadOnlySpan_1[SpansEqual_1_T], a2: ReadOnlySpan_1[SpansEqual_1_T]) -> bool:...


    # Skipped XorArrays due to it being static, abstract and generic.

    XorArrays : XorArrays_MethodGroup
    class XorArrays_MethodGroup:
        @typing.overload
        def __call__(self, transformData: Span_1[int], xorData: ReadOnlySpan_1[int]) -> None:...
        @typing.overload
        def __call__(self, output: Span_1[int], input1: ReadOnlySpan_1[int], input2: ReadOnlySpan_1[int]) -> None:...



class Validity(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unchecked : Validity # 0
    Invalid : Validity # 1
    Valid : Validity # 2
    MissingKey : Validity # 3


class WeakRef_GenericClasses(abc.ABCMeta):
    Generic_WeakRef_GenericClasses_WeakRef_1_T = typing.TypeVar('Generic_WeakRef_GenericClasses_WeakRef_1_T')
    def __getitem__(self, types : typing.Type[Generic_WeakRef_GenericClasses_WeakRef_1_T]) -> typing.Type[WeakRef_1[Generic_WeakRef_GenericClasses_WeakRef_1_T]]: ...

WeakRef : WeakRef_GenericClasses

WeakRef_1_T = typing.TypeVar('WeakRef_1_T')
class WeakRef_1(typing.Generic[WeakRef_1_T], IDisposable):
    def __init__(self, other: clr.Reference[SharedRef_1[WeakRef_1_T]]) -> None: ...
    @property
    def Expired(self) -> bool: ...
    @property
    def UseCount(self) -> int: ...
    def Destroy(self) -> None: ...
    def Dispose(self) -> None: ...
    def Lock(self) -> SharedRef_1[WeakRef_1_T]: ...
    def Reset(self) -> None: ...
    def Swap(self, other: clr.Reference[WeakRef_1[WeakRef_1_T]]) -> None: ...
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup[WeakRef_1_T]
    Create_MethodGroup_WeakRef_1_T = typing.TypeVar('Create_MethodGroup_WeakRef_1_T')
    class Create_MethodGroup(typing.Generic[Create_MethodGroup_WeakRef_1_T]):
        Create_MethodGroup_WeakRef_1_T = WeakRef_1.Create_MethodGroup_WeakRef_1_T
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_MethodGroup_WeakRef_1_T, Create_1_T1]: ...

        Create_1_WeakRef_1_T = typing.TypeVar('Create_1_WeakRef_1_T')
        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_WeakRef_1_T, Create_1_T1]):
            Create_1_WeakRef_1_T = WeakRef_1.Create_MethodGroup.Create_1_WeakRef_1_T
            Create_1_TFrom = WeakRef_1.Create_MethodGroup.Create_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[Create_1_TFrom]]) -> WeakRef_1[Create_1_WeakRef_1_T]:...


    # Skipped CreateCopy due to it being static, abstract and generic.

    CreateCopy : CreateCopy_MethodGroup[WeakRef_1_T]
    CreateCopy_MethodGroup_WeakRef_1_T = typing.TypeVar('CreateCopy_MethodGroup_WeakRef_1_T')
    class CreateCopy_MethodGroup(typing.Generic[CreateCopy_MethodGroup_WeakRef_1_T]):
        CreateCopy_MethodGroup_WeakRef_1_T = WeakRef_1.CreateCopy_MethodGroup_WeakRef_1_T
        def __getitem__(self, t:typing.Type[CreateCopy_1_T1]) -> CreateCopy_1[CreateCopy_MethodGroup_WeakRef_1_T, CreateCopy_1_T1]: ...

        CreateCopy_1_WeakRef_1_T = typing.TypeVar('CreateCopy_1_WeakRef_1_T')
        CreateCopy_1_T1 = typing.TypeVar('CreateCopy_1_T1')
        class CreateCopy_1(typing.Generic[CreateCopy_1_WeakRef_1_T, CreateCopy_1_T1]):
            CreateCopy_1_WeakRef_1_T = WeakRef_1.CreateCopy_MethodGroup.CreateCopy_1_WeakRef_1_T
            CreateCopy_1_TFrom = WeakRef_1.CreateCopy_MethodGroup.CreateCopy_1_T1
            def __call__(self, other: clr.Reference[WeakRef_1[CreateCopy_1_TFrom]]) -> WeakRef_1[CreateCopy_1_WeakRef_1_T]:...


    # Skipped CreateMove due to it being static, abstract and generic.

    CreateMove : CreateMove_MethodGroup[WeakRef_1_T]
    CreateMove_MethodGroup_WeakRef_1_T = typing.TypeVar('CreateMove_MethodGroup_WeakRef_1_T')
    class CreateMove_MethodGroup(typing.Generic[CreateMove_MethodGroup_WeakRef_1_T]):
        CreateMove_MethodGroup_WeakRef_1_T = WeakRef_1.CreateMove_MethodGroup_WeakRef_1_T
        def __getitem__(self, t:typing.Type[CreateMove_1_T1]) -> CreateMove_1[CreateMove_MethodGroup_WeakRef_1_T, CreateMove_1_T1]: ...

        CreateMove_1_WeakRef_1_T = typing.TypeVar('CreateMove_1_WeakRef_1_T')
        CreateMove_1_T1 = typing.TypeVar('CreateMove_1_T1')
        class CreateMove_1(typing.Generic[CreateMove_1_WeakRef_1_T, CreateMove_1_T1]):
            CreateMove_1_WeakRef_1_T = WeakRef_1.CreateMove_MethodGroup.CreateMove_1_WeakRef_1_T
            CreateMove_1_TFrom = WeakRef_1.CreateMove_MethodGroup.CreateMove_1_T1
            def __call__(self, other: clr.Reference[WeakRef_1[CreateMove_1_TFrom]]) -> WeakRef_1[CreateMove_1_WeakRef_1_T]:...


    # Skipped Set due to it being static, abstract and generic.

    Set : Set_MethodGroup[WeakRef_1_T]
    Set_MethodGroup_WeakRef_1_T = typing.TypeVar('Set_MethodGroup_WeakRef_1_T')
    class Set_MethodGroup(typing.Generic[Set_MethodGroup_WeakRef_1_T]):
        Set_MethodGroup_WeakRef_1_T = WeakRef_1.Set_MethodGroup_WeakRef_1_T
        def __getitem__(self, t:typing.Type[Set_1_T1]) -> Set_1[Set_MethodGroup_WeakRef_1_T, Set_1_T1]: ...

        Set_1_WeakRef_1_T = typing.TypeVar('Set_1_WeakRef_1_T')
        Set_1_T1 = typing.TypeVar('Set_1_T1')
        class Set_1(typing.Generic[Set_1_WeakRef_1_T, Set_1_T1]):
            Set_1_WeakRef_1_T = WeakRef_1.Set_MethodGroup.Set_1_WeakRef_1_T
            Set_1_TFrom = WeakRef_1.Set_MethodGroup.Set_1_T1
            def __call__(self, other: clr.Reference[SharedRef_1[Set_1_TFrom]]) -> None:...


    # Skipped SetCopy due to it being static, abstract and generic.

    SetCopy : SetCopy_MethodGroup[WeakRef_1_T]
    SetCopy_MethodGroup_WeakRef_1_T = typing.TypeVar('SetCopy_MethodGroup_WeakRef_1_T')
    class SetCopy_MethodGroup(typing.Generic[SetCopy_MethodGroup_WeakRef_1_T]):
        SetCopy_MethodGroup_WeakRef_1_T = WeakRef_1.SetCopy_MethodGroup_WeakRef_1_T
        def __getitem__(self, t:typing.Type[SetCopy_1_T1]) -> SetCopy_1[SetCopy_MethodGroup_WeakRef_1_T, SetCopy_1_T1]: ...

        SetCopy_1_WeakRef_1_T = typing.TypeVar('SetCopy_1_WeakRef_1_T')
        SetCopy_1_T1 = typing.TypeVar('SetCopy_1_T1')
        class SetCopy_1(typing.Generic[SetCopy_1_WeakRef_1_T, SetCopy_1_T1]):
            SetCopy_1_WeakRef_1_T = WeakRef_1.SetCopy_MethodGroup.SetCopy_1_WeakRef_1_T
            SetCopy_1_TFrom = WeakRef_1.SetCopy_MethodGroup.SetCopy_1_T1
            def __call__(self, other: clr.Reference[WeakRef_1[SetCopy_1_TFrom]]) -> None:...


    # Skipped SetMove due to it being static, abstract and generic.

    SetMove : SetMove_MethodGroup[WeakRef_1_T]
    SetMove_MethodGroup_WeakRef_1_T = typing.TypeVar('SetMove_MethodGroup_WeakRef_1_T')
    class SetMove_MethodGroup(typing.Generic[SetMove_MethodGroup_WeakRef_1_T]):
        SetMove_MethodGroup_WeakRef_1_T = WeakRef_1.SetMove_MethodGroup_WeakRef_1_T
        def __getitem__(self, t:typing.Type[SetMove_1_T1]) -> SetMove_1[SetMove_MethodGroup_WeakRef_1_T, SetMove_1_T1]: ...

        SetMove_1_WeakRef_1_T = typing.TypeVar('SetMove_1_WeakRef_1_T')
        SetMove_1_T1 = typing.TypeVar('SetMove_1_T1')
        class SetMove_1(typing.Generic[SetMove_1_WeakRef_1_T, SetMove_1_T1]):
            SetMove_1_WeakRef_1_T = WeakRef_1.SetMove_MethodGroup.SetMove_1_WeakRef_1_T
            SetMove_1_TFrom = WeakRef_1.SetMove_MethodGroup.SetMove_1_T1
            def __call__(self, other: clr.Reference[WeakRef_1[SetMove_1_TFrom]]) -> None:...



