import abc
from LibHac import Result

class ResultCmif(abc.ABC):
    ModuleSf : int
    @classmethod
    @property
    def CmifProxyAllocationFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCmifHeaderSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCmifInHeader(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCmifOutHeader(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidInObject(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidInObjectCount(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidInRawSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidOutObjectCount(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidOutRawSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfDomainEntry(cls) -> Result.Base: ...
    @classmethod
    @property
    def TargetObjectNotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnknownMethodId(cls) -> Result.Base: ...

