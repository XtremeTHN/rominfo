import typing, clr, abc
from System import IDisposable
from LibHac.Mem import Buffer
from LibHac.Fs import IBufferManager
from LibHac import Result
from LibHac.Common import Buffer32

class BlockCacheManager_GenericClasses(abc.ABCMeta):
    Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TEntry = typing.TypeVar('Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TEntry')
    Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TRange = typing.TypeVar('Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TRange')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TEntry], typing.Type[Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TRange]]) -> typing.Type[BlockCacheManager_2[Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TEntry, Generic_BlockCacheManager_GenericClasses_BlockCacheManager_2_TRange]]: ...

BlockCacheManager : BlockCacheManager_GenericClasses

BlockCacheManager_2_TEntry = typing.TypeVar('BlockCacheManager_2_TEntry')
BlockCacheManager_2_TRange = typing.TypeVar('BlockCacheManager_2_TRange')
class BlockCacheManager_2(typing.Generic[BlockCacheManager_2_TEntry, BlockCacheManager_2_TRange], IDisposable):
    def __init__(self) -> None: ...
    @property
    def Item(self) -> clr.Reference[BlockCacheManager_2_TEntry]: ...
    def AcquireCacheEntry(self, outEntry: clr.Reference[BlockCacheManager_2_TEntry], outBuffer: clr.Reference[Buffer], index: int) -> None: ...
    def Dispose(self) -> None: ...
    def FinalizeObject(self) -> None: ...
    def GetAllocator(self) -> IBufferManager: ...
    def GetCount(self) -> int: ...
    def GetEmptyCacheIndex(self, emptyIndex: clr.Reference[int], leastRecentlyUsedIndex: clr.Reference[int]) -> None: ...
    def Initialize(self, allocator: IBufferManager, maxCacheEntries: int) -> Result: ...
    def Invalidate(self) -> None: ...
    def InvalidateCacheEntry(self, index: int) -> None: ...
    def IsInitialized(self) -> bool: ...
    def RegisterCacheEntry(self, index: int, buffer: Buffer, attribute: IBufferManager.BufferAttribute) -> None: ...
    def SetFlushing(self, index: int, isFlushing: bool) -> None: ...
    def SetWriteBack(self, index: int, isWriteBack: bool) -> None: ...
    # Skipped ReleaseCacheEntry due to it being static, abstract and generic.

    ReleaseCacheEntry : ReleaseCacheEntry_MethodGroup[BlockCacheManager_2_TEntry, BlockCacheManager_2_TRange]
    ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TEntry = typing.TypeVar('ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TEntry')
    ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TRange = typing.TypeVar('ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TRange')
    class ReleaseCacheEntry_MethodGroup(typing.Generic[ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TEntry, ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TRange]):
        ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TEntry = BlockCacheManager_2.ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TEntry
        ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TRange = BlockCacheManager_2.ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TRange
        @typing.overload
        def __call__(self, index: int, buffer: Buffer) -> None:...
        @typing.overload
        def __call__(self, entry: clr.Reference[ReleaseCacheEntry_MethodGroup_BlockCacheManager_2_TEntry], buffer: Buffer) -> None:...

    # Skipped SetCacheEntry due to it being static, abstract and generic.

    SetCacheEntry : SetCacheEntry_MethodGroup[BlockCacheManager_2_TEntry, BlockCacheManager_2_TRange]
    SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry = typing.TypeVar('SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry')
    SetCacheEntry_MethodGroup_BlockCacheManager_2_TRange = typing.TypeVar('SetCacheEntry_MethodGroup_BlockCacheManager_2_TRange')
    class SetCacheEntry_MethodGroup(typing.Generic[SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry, SetCacheEntry_MethodGroup_BlockCacheManager_2_TRange]):
        SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry = BlockCacheManager_2.SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry
        SetCacheEntry_MethodGroup_BlockCacheManager_2_TRange = BlockCacheManager_2.SetCacheEntry_MethodGroup_BlockCacheManager_2_TRange
        @typing.overload
        def __call__(self, index: int, entry: clr.Reference[SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry], buffer: Buffer) -> bool:...
        @typing.overload
        def __call__(self, index: int, entry: clr.Reference[SetCacheEntry_MethodGroup_BlockCacheManager_2_TEntry], buffer: Buffer, attribute: IBufferManager.BufferAttribute) -> bool:...



class HashedEntry(IPartitionFileSystemEntry):
    Hash : Buffer32
    HashOffset : int
    HashSize : int
    NameOffset : int
    Offset : int
    Size : int


class IBlockCacheManagerEntry_GenericClasses(abc.ABCMeta):
    Generic_IBlockCacheManagerEntry_GenericClasses_IBlockCacheManagerEntry_1_TRange = typing.TypeVar('Generic_IBlockCacheManagerEntry_GenericClasses_IBlockCacheManagerEntry_1_TRange')
    def __getitem__(self, types : typing.Type[Generic_IBlockCacheManagerEntry_GenericClasses_IBlockCacheManagerEntry_1_TRange]) -> typing.Type[IBlockCacheManagerEntry_1[Generic_IBlockCacheManagerEntry_GenericClasses_IBlockCacheManagerEntry_1_TRange]]: ...

IBlockCacheManagerEntry : IBlockCacheManagerEntry_GenericClasses

IBlockCacheManagerEntry_1_TRange = typing.TypeVar('IBlockCacheManagerEntry_1_TRange')
class IBlockCacheManagerEntry_1(typing.Generic[IBlockCacheManagerEntry_1_TRange], typing.Protocol):
    @property
    def Age(self) -> int: ...
    @Age.setter
    def Age(self, value: int) -> int: ...
    @property
    def Buffer(self) -> Buffer: ...
    @Buffer.setter
    def Buffer(self, value: Buffer) -> Buffer: ...
    @property
    def Handle(self) -> int: ...
    @Handle.setter
    def Handle(self, value: int) -> int: ...
    @property
    def IsCached(self) -> bool: ...
    @IsCached.setter
    def IsCached(self, value: bool) -> bool: ...
    @property
    def IsFlushing(self) -> None: ...
    @IsFlushing.setter
    def IsFlushing(self, value: bool) -> None: ...
    @property
    def IsValid(self) -> bool: ...
    @IsValid.setter
    def IsValid(self, value: bool) -> bool: ...
    @property
    def IsWriteBack(self) -> bool: ...
    @IsWriteBack.setter
    def IsWriteBack(self, value: bool) -> bool: ...
    @property
    def Range(self) -> IBlockCacheManagerEntry_1_TRange: ...
    @abc.abstractmethod
    def Invalidate(self) -> None: ...
    @abc.abstractmethod
    def IsAllocated(self) -> bool: ...


class IBlockCacheManagerRange(typing.Protocol):
    @property
    def Offset(self) -> int: ...
    @abc.abstractmethod
    def GetEndOffset(self) -> int: ...


class IPartitionFileSystemEntry(typing.Protocol):
    @property
    def NameOffset(self) -> int: ...
    @property
    def Offset(self) -> int: ...
    @property
    def Size(self) -> int: ...


class StandardEntry(IPartitionFileSystemEntry):
    NameOffset : int
    Offset : int
    Size : int

