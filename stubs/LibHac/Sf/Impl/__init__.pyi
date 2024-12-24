import abc
from LibHac import Result

class ResultSfImpl(abc.ABC):
    ModuleSf : int
    @classmethod
    @property
    def RequestContextChanged(cls) -> Result.Base.Abstract: ...
    @classmethod
    @property
    def RequestInvalidated(cls) -> Result.Base.Abstract: ...
    @classmethod
    @property
    def RequestInvalidatedByUser(cls) -> Result.Base: ...

