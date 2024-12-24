import typing, clr, abc
from System import ReadOnlySpan_1, IDisposable, Span_1
from LibHac.Os import OsState
from LibHac.Svc import Handle
from LibHac import Result

class InArray_GenericClasses(abc.ABCMeta):
    Generic_InArray_GenericClasses_InArray_1_T = typing.TypeVar('Generic_InArray_GenericClasses_InArray_1_T')
    def __getitem__(self, types : typing.Type[Generic_InArray_GenericClasses_InArray_1_T]) -> typing.Type[InArray_1[Generic_InArray_GenericClasses_InArray_1_T]]: ...

InArray : InArray_GenericClasses

InArray_1_T = typing.TypeVar('InArray_1_T')
class InArray_1(typing.Generic[InArray_1_T]):
    def __init__(self, array: ReadOnlySpan_1[InArray_1_T]) -> None: ...
    @property
    def Array(self) -> ReadOnlySpan_1[InArray_1_T]: ...
    @property
    def Item(self) -> clr.Reference[InArray_1_T]: ...
    @property
    def Size(self) -> int: ...


class InBuffer:
    def __init__(self, buffer: ReadOnlySpan_1[int]) -> None: ...
    @property
    def Buffer(self) -> ReadOnlySpan_1[int]: ...
    @property
    def Size(self) -> int: ...
    # Skipped FromSpan due to it being static, abstract and generic.

    FromSpan : FromSpan_MethodGroup
    class FromSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[FromSpan_1_T1]) -> FromSpan_1[FromSpan_1_T1]: ...

        FromSpan_1_T1 = typing.TypeVar('FromSpan_1_T1')
        class FromSpan_1(typing.Generic[FromSpan_1_T1]):
            FromSpan_1_T = InBuffer.FromSpan_MethodGroup.FromSpan_1_T1
            def __call__(self, buffer: ReadOnlySpan_1[FromSpan_1_T]) -> InBuffer:...


    # Skipped FromStruct due to it being static, abstract and generic.

    FromStruct : FromStruct_MethodGroup
    class FromStruct_MethodGroup:
        def __getitem__(self, t:typing.Type[FromStruct_1_T1]) -> FromStruct_1[FromStruct_1_T1]: ...

        FromStruct_1_T1 = typing.TypeVar('FromStruct_1_T1')
        class FromStruct_1(typing.Generic[FromStruct_1_T1]):
            FromStruct_1_T = InBuffer.FromStruct_MethodGroup.FromStruct_1_T1
            def __call__(self, value: clr.Reference[FromStruct_1_T]) -> InBuffer:...




class NativeHandle(IDisposable):
    @typing.overload
    def __init__(self, os: OsState, handle: Handle) -> None: ...
    @typing.overload
    def __init__(self, os: OsState, handle: Handle, isManaged: bool) -> None: ...
    @property
    def Handle(self) -> Handle: ...
    @Handle.setter
    def Handle(self, value: Handle) -> Handle: ...
    @property
    def IsManaged(self) -> bool: ...
    @IsManaged.setter
    def IsManaged(self, value: bool) -> bool: ...
    def Dispose(self) -> None: ...


class OutArray_GenericClasses(abc.ABCMeta):
    Generic_OutArray_GenericClasses_OutArray_1_T = typing.TypeVar('Generic_OutArray_GenericClasses_OutArray_1_T')
    def __getitem__(self, types : typing.Type[Generic_OutArray_GenericClasses_OutArray_1_T]) -> typing.Type[OutArray_1[Generic_OutArray_GenericClasses_OutArray_1_T]]: ...

OutArray : OutArray_GenericClasses

OutArray_1_T = typing.TypeVar('OutArray_1_T')
class OutArray_1(typing.Generic[OutArray_1_T]):
    def __init__(self, array: Span_1[OutArray_1_T]) -> None: ...
    @property
    def Array(self) -> Span_1[OutArray_1_T]: ...
    @property
    def Item(self) -> clr.Reference[OutArray_1_T]: ...
    @property
    def Size(self) -> int: ...


class OutBuffer:
    def __init__(self, buffer: Span_1[int]) -> None: ...
    @property
    def Buffer(self) -> Span_1[int]: ...
    @property
    def Size(self) -> int: ...
    # Skipped FromSpan due to it being static, abstract and generic.

    FromSpan : FromSpan_MethodGroup
    class FromSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[FromSpan_1_T1]) -> FromSpan_1[FromSpan_1_T1]: ...

        FromSpan_1_T1 = typing.TypeVar('FromSpan_1_T1')
        class FromSpan_1(typing.Generic[FromSpan_1_T1]):
            FromSpan_1_T = OutBuffer.FromSpan_MethodGroup.FromSpan_1_T1
            def __call__(self, buffer: Span_1[FromSpan_1_T]) -> OutBuffer:...


    # Skipped FromStruct due to it being static, abstract and generic.

    FromStruct : FromStruct_MethodGroup
    class FromStruct_MethodGroup:
        def __getitem__(self, t:typing.Type[FromStruct_1_T1]) -> FromStruct_1[FromStruct_1_T1]: ...

        FromStruct_1_T1 = typing.TypeVar('FromStruct_1_T1')
        class FromStruct_1(typing.Generic[FromStruct_1_T1]):
            FromStruct_1_T = OutBuffer.FromStruct_MethodGroup.FromStruct_1_T1
            def __call__(self, value: clr.Reference[FromStruct_1_T]) -> OutBuffer:...




class ResultSf(abc.ABC):
    ModuleSf : int
    @classmethod
    @property
    def MemoryAllocationFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotSupported(cls) -> Result.Base: ...
    @classmethod
    @property
    def PreconditionViolation(cls) -> Result.Base: ...
    @classmethod
    @property
    def RequestDeferred(cls) -> Result.Base.Abstract: ...
    @classmethod
    @property
    def RequestDeferredByUser(cls) -> Result.Base: ...

