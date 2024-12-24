import typing, clr, abc
from System import Span_1, IEquatable_1, IComparable_1, IDisposable, ReadOnlySpan_1, Array_1
from LibHac import Result, MemoryResource
from LibHac.Fs import FileSystemClient
from LibHac.Common import U8Span
from LibHac.Mem import Buffer

class BoundedString_GenericClasses(abc.ABCMeta):
    Generic_BoundedString_GenericClasses_BoundedString_1_TSize = typing.TypeVar('Generic_BoundedString_GenericClasses_BoundedString_1_TSize')
    def __getitem__(self, types : typing.Type[Generic_BoundedString_GenericClasses_BoundedString_1_TSize]) -> typing.Type[BoundedString_1[Generic_BoundedString_GenericClasses_BoundedString_1_TSize]]: ...

BoundedString : BoundedString_GenericClasses

BoundedString_1_TSize = typing.TypeVar('BoundedString_1_TSize')
class BoundedString_1(typing.Generic[BoundedString_1_TSize]):
    def Get(self) -> Span_1[int]: ...
    def GetLength(self) -> int: ...


class FlatMapKeyValueStore_GenericClasses(abc.ABCMeta):
    Generic_FlatMapKeyValueStore_GenericClasses_FlatMapKeyValueStore_1_TKey = typing.TypeVar('Generic_FlatMapKeyValueStore_GenericClasses_FlatMapKeyValueStore_1_TKey', bound=Union[IEquatable_1[FlatMapKeyValueStore_GenericClasses_FlatMapKeyValueStore_1_TKey], IComparable_1[FlatMapKeyValueStore_GenericClasses_FlatMapKeyValueStore_1_TKey]])
    def __getitem__(self, types : typing.Type[Generic_FlatMapKeyValueStore_GenericClasses_FlatMapKeyValueStore_1_TKey]) -> typing.Type[FlatMapKeyValueStore_1[Generic_FlatMapKeyValueStore_GenericClasses_FlatMapKeyValueStore_1_TKey]]: ...

FlatMapKeyValueStore : FlatMapKeyValueStore_GenericClasses

FlatMapKeyValueStore_1_TKey = typing.TypeVar('FlatMapKeyValueStore_1_TKey', bound=Union[IEquatable_1[FlatMapKeyValueStore_1_TKey], IComparable_1[FlatMapKeyValueStore_1_TKey]])
class FlatMapKeyValueStore_1(typing.Generic[FlatMapKeyValueStore_1_TKey], IDisposable):
    def __init__(self) -> None: ...
    @property
    def Count(self) -> int: ...
    def Delete(self, key: clr.Reference[FlatMapKeyValueStore_1_TKey]) -> Result: ...
    def Dispose(self) -> None: ...
    def FixIterator(self, iterator: clr.Reference[FlatMapKeyValueStore_1.Iterator_1[FlatMapKeyValueStore_1_TKey]], key: clr.Reference[FlatMapKeyValueStore_1_TKey]) -> None: ...
    def Get(self, valueSize: clr.Reference[int], key: clr.Reference[FlatMapKeyValueStore_1_TKey], valueBuffer: Span_1[int]) -> Result: ...
    def GetBeginIterator(self) -> FlatMapKeyValueStore_1.Iterator_1[FlatMapKeyValueStore_1_TKey]: ...
    def GetLowerBoundIterator(self, key: clr.Reference[FlatMapKeyValueStore_1_TKey]) -> FlatMapKeyValueStore_1.Iterator_1[FlatMapKeyValueStore_1_TKey]: ...
    def Initialize(self, fsClient: FileSystemClient, rootPath: U8Span, capacity: int, memoryResource: MemoryResource, autoBufferMemoryResource: MemoryResource) -> Result: ...
    def Load(self) -> Result: ...
    def Save(self) -> Result: ...
    def Set(self, key: clr.Reference[FlatMapKeyValueStore_1_TKey], value: ReadOnlySpan_1[int]) -> Result: ...

    ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey = typing.TypeVar('ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey', bound=Union[IEquatable_1[ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey], IComparable_1[ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey]])
    class ConstIterator_GenericClasses(typing.Generic[ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey], abc.ABCMeta):
        ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey = FlatMapKeyValueStore_1.ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey
        def __call__(self) -> FlatMapKeyValueStore_1.ConstIterator_1[ConstIterator_GenericClasses_FlatMapKeyValueStore_1_TKey]: ...

    ConstIterator : ConstIterator_GenericClasses[FlatMapKeyValueStore_1_TKey]

    ConstIterator_1_TKey = typing.TypeVar('ConstIterator_1_TKey', bound=Union[IEquatable_1[ConstIterator_1_TKey], IComparable_1[ConstIterator_1_TKey]])
    class ConstIterator_1(typing.Generic[ConstIterator_1_TKey]):
        ConstIterator_1_TKey = FlatMapKeyValueStore_1.ConstIterator_1_TKey
        def __init__(self, entries: Array_1[FlatMapKeyValueStore_1.KeyValue_1[ConstIterator_1_TKey]], startIndex: int, length: int) -> None: ...
        def Get(self) -> clr.Reference[FlatMapKeyValueStore_1.KeyValue_1[ConstIterator_1_TKey]]: ...
        def GetValue(self) -> ReadOnlySpan_1[int]: ...
        def IsEnd(self) -> bool: ...
        def Next(self) -> None: ...


    Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey = typing.TypeVar('Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey', bound=Union[IEquatable_1[Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey], IComparable_1[Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey]])
    class Iterator_GenericClasses(typing.Generic[Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey], abc.ABCMeta):
        Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey = FlatMapKeyValueStore_1.Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey
        def __call__(self) -> FlatMapKeyValueStore_1.Iterator_1[Iterator_GenericClasses_FlatMapKeyValueStore_1_TKey]: ...

    Iterator : Iterator_GenericClasses[FlatMapKeyValueStore_1_TKey]

    Iterator_1_TKey = typing.TypeVar('Iterator_1_TKey', bound=Union[IEquatable_1[Iterator_1_TKey], IComparable_1[Iterator_1_TKey]])
    class Iterator_1(typing.Generic[Iterator_1_TKey]):
        Iterator_1_TKey = FlatMapKeyValueStore_1.Iterator_1_TKey
        def Fix(self, entryIndex: int, newLength: int) -> None: ...
        def Get(self) -> clr.Reference[FlatMapKeyValueStore_1.KeyValue_1[Iterator_1_TKey]]: ...
        def IsEnd(self) -> bool: ...
        def Next(self) -> None: ...
        # Skipped GetValue due to it being static, abstract and generic.

        GetValue : GetValue_MethodGroup[Iterator_1_TKey]
        GetValue_MethodGroup_Iterator_1_TKey = typing.TypeVar('GetValue_MethodGroup_Iterator_1_TKey', bound=Union[IEquatable_1[GetValue_MethodGroup_Iterator_1_TKey], IComparable_1[GetValue_MethodGroup_Iterator_1_TKey]])
        class GetValue_MethodGroup(typing.Generic[GetValue_MethodGroup_Iterator_1_TKey]):
            GetValue_MethodGroup_Iterator_1_TKey = FlatMapKeyValueStore_1.Iterator_1.GetValue_MethodGroup_Iterator_1_TKey
            def __getitem__(self, t:typing.Type[GetValue_1_T1]) -> GetValue_1[GetValue_MethodGroup_Iterator_1_TKey, GetValue_1_T1]: ...

            GetValue_1_Iterator_1_TKey = typing.TypeVar('GetValue_1_Iterator_1_TKey', bound=Union[IEquatable_1[GetValue_1_Iterator_1_TKey], IComparable_1[GetValue_1_Iterator_1_TKey]])
            GetValue_1_T1 = typing.TypeVar('GetValue_1_T1')
            class GetValue_1(typing.Generic[GetValue_1_Iterator_1_TKey, GetValue_1_T1]):
                GetValue_1_Iterator_1_TKey = FlatMapKeyValueStore_1.Iterator_1.GetValue_MethodGroup.GetValue_1_Iterator_1_TKey
                GetValue_1_T = FlatMapKeyValueStore_1.Iterator_1.GetValue_MethodGroup.GetValue_1_T1
                def __call__(self) -> clr.Reference[GetValue_1_T]:...

            def __call__(self) -> Span_1[int]:...



    KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey = typing.TypeVar('KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey', bound=Union[IEquatable_1[KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey], IComparable_1[KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey]])
    class KeyValue_GenericClasses(typing.Generic[KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey], abc.ABCMeta):
        KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey = FlatMapKeyValueStore_1.KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey
        def __call__(self) -> FlatMapKeyValueStore_1.KeyValue_1[KeyValue_GenericClasses_FlatMapKeyValueStore_1_TKey]: ...

    KeyValue : KeyValue_GenericClasses[FlatMapKeyValueStore_1_TKey]

    KeyValue_1_TKey = typing.TypeVar('KeyValue_1_TKey', bound=Union[IEquatable_1[KeyValue_1_TKey], IComparable_1[KeyValue_1_TKey]])
    class KeyValue_1(typing.Generic[KeyValue_1_TKey]):
        KeyValue_1_TKey = FlatMapKeyValueStore_1.KeyValue_1_TKey
        def __init__(self, key: clr.Reference[KeyValue_1_TKey], value: Buffer) -> None: ...
        Key : KeyValue_1_TKey
        Value : Buffer



class KeyValueArchiveHeader:
    def __init__(self, entryCount: int) -> None: ...
    EntryCount : int
    ExpectedMagic : int
    Magic : int
    Reserved : int
    def IsValid(self) -> bool: ...


class ResultKvdb(abc.ABC):
    ModuleKvdb : int
    @classmethod
    @property
    def AllocationFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def BufferInsufficient(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidFileSystemState(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidKeyValue(cls) -> Result.Base: ...
    @classmethod
    @property
    def KeyNotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotCreated(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfKeyResource(cls) -> Result.Base: ...

