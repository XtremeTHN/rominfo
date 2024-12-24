import typing, clr, abc
from System import IDisposable, IEquatable_1
from LibHac import Result
from LibHac.Common import SharedRef_1
from LibHac.FsSrv.Storage.Sf import IStorageDeviceManager
from LibHac.Sf import NativeHandle
from LibHac.FsSrv import FileSystemServer, StorageService
from LibHac.Common.FixedArrays import Array11_1

class IStorageDeviceManagerFactory(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def Create(self, outDeviceManager: clr.Reference[SharedRef_1[IStorageDeviceManager]], portId: StorageDevicePortId) -> Result: ...
    @abc.abstractmethod
    def SetReady(self, portId: StorageDevicePortId, handle: NativeHandle) -> Result: ...
    @abc.abstractmethod
    def UnsetReady(self, portId: StorageDevicePortId) -> Result: ...


class MmcServiceGlobalMethods(abc.ABC):
    @staticmethod
    def GetAndClearPatrolReadAllocateBufferCount(fsSrv: FileSystemServer, successCount: clr.Reference[int], failureCount: clr.Reference[int]) -> Result: ...


class StorageDeviceHandle(IEquatable_1[StorageDeviceHandle]):
    def __init__(self, value: int, portId: StorageDevicePortId) -> None: ...
    PortId : StorageDevicePortId
    Reserved : Array11_1[int]
    Value : int
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: StorageDeviceHandle, right: StorageDeviceHandle) -> bool: ...
    def __ne__(self, left: StorageDeviceHandle, right: StorageDeviceHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: StorageDeviceHandle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class StorageDeviceManagerFactoryApi(abc.ABC):
    @staticmethod
    def InitializeStorageDeviceManagerFactory(storage: StorageService, factory: IStorageDeviceManagerFactory) -> None: ...


class StorageDevicePortId(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Invalid : StorageDevicePortId # 0
    Mmc : StorageDevicePortId # 1
    SdCard : StorageDevicePortId # 2
    GameCard : StorageDevicePortId # 3

