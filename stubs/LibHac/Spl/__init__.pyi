import typing, abc
from System import IEquatable_1, ReadOnlySpan_1
from LibHac import Result

class AccessKey(IEquatable_1[AccessKey]):
    def __init__(self, bytes: ReadOnlySpan_1[int]) -> None: ...
    @property
    def Value(self) -> ReadOnlySpan_1[int]: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: AccessKey, right: AccessKey) -> bool: ...
    def __ne__(self, left: AccessKey, right: AccessKey) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: AccessKey) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class ResultSpl(abc.ABC):
    ModuleSpl : int
    @classmethod
    @property
    def BootReasonAlreadySet(cls) -> Result.Base: ...
    @classmethod
    @property
    def BootReasonNotSet(cls) -> Result.Base: ...
    @classmethod
    @property
    def DecryptionFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidKeySlot(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfKeySlots(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorBusy(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorError(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorInvalidArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorInvalidAsyncOperation(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorNoAsyncOperation(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorNotImplemented(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorNotInitialized(cls) -> Result.Base: ...
    @classmethod
    @property
    def SecureMonitorNotPermitted(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnknownSecureMonitorError(cls) -> Result.Base: ...

