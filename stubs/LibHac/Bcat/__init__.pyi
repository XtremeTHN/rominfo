import typing, clr, abc
from LibHac import HorizonClient, Result
from LibHac.Common.FixedArrays import Array16_1, Array32_1

class BcatServer:
    def __init__(self, horizonClient: HorizonClient) -> None: ...


class BcatServiceType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    BcatU : BcatServiceType # 0
    BcatS : BcatServiceType # 1
    BcatM : BcatServiceType # 2
    BcatA : BcatServiceType # 3


class DeliveryCacheDirectoryEntry:
    def __init__(self, name: clr.Reference[FileName], size: int, digest: clr.Reference[Digest]) -> None: ...
    Digest : Digest
    Name : FileName
    Size : int


class Digest:
    Value : Array16_1[int]
    def ToString(self) -> str: ...


class DirectoryName:
    Value : Array32_1[int]
    def IsValid(self) -> bool: ...
    def ToString(self) -> str: ...


class FileName:
    Value : Array32_1[int]
    def IsValid(self) -> bool: ...
    def ToString(self) -> str: ...


class ResultBcat(abc.ABC):
    ModuleBcat : int
    @classmethod
    @property
    def AllocationFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def AlreadyOpen(cls) -> Result.Base: ...
    @classmethod
    @property
    def DataVerificationFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def InternetRequestDenied(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidDeliveryCacheStorageFile(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidOperation(cls) -> Result.Base: ...
    @classmethod
    @property
    def NetworkServiceAccountNotAvailable(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotOpen(cls) -> Result.Base: ...
    @classmethod
    @property
    def PassphrasePathNotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def PermissionDenied(cls) -> Result.Base: ...
    @classmethod
    @property
    def SaveDataNotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def ServiceOpenLimitReached(cls) -> Result.Base: ...
    @classmethod
    @property
    def StorageOpenLimitReached(cls) -> Result.Base: ...
    @classmethod
    @property
    def TargetAlreadyMounted(cls) -> Result.Base: ...
    @classmethod
    @property
    def TargetLocked(cls) -> Result.Base: ...
    @classmethod
    @property
    def TargetNotMounted(cls) -> Result.Base: ...

