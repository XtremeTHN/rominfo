import typing, abc
from LibHac import Result

class Handle:
    def __init__(self, obj: typing.Any) -> None: ...
    Object : typing.Any


class ResultSvc(abc.ABC):
    ModuleSvc : int
    @classmethod
    @property
    def Busy(cls) -> Result.Base: ...
    @classmethod
    @property
    def Cancelled(cls) -> Result.Base: ...
    @classmethod
    @property
    def Debug(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidAddress(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidArgument(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCombination(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCoreId(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidCurrentMemory(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidEnumValue(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidHandle(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidId(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidMemoryPool(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidMemoryRegion(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidNewMemoryPermission(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPointer(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidPriority(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidProcessId(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidSize(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidState(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidThreadId(cls) -> Result.Base: ...
    @classmethod
    @property
    def LimitReached(cls) -> Result.Base: ...
    @classmethod
    @property
    def MessageTooLarge(cls) -> Result.Base: ...
    @classmethod
    @property
    def NoEvent(cls) -> Result.Base: ...
    @classmethod
    @property
    def NoSynchronizationObject(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotFound(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotHandled(cls) -> Result.Base: ...
    @classmethod
    @property
    def NoThread(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotImplemented(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotSupported(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfAddressSpace(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfHandles(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfMemory(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfRange(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfResource(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfSessions(cls) -> Result.Base: ...
    @classmethod
    @property
    def PortClosed(cls) -> Result.Base: ...
    @classmethod
    @property
    def ProcessTerminated(cls) -> Result.Base: ...
    @classmethod
    @property
    def ReceiveListBroken(cls) -> Result.Base: ...
    @classmethod
    @property
    def ReservedUsed(cls) -> Result.Base: ...
    @classmethod
    @property
    def SessionClosed(cls) -> Result.Base: ...
    @classmethod
    @property
    def StopProcessingException(cls) -> Result.Base: ...
    @classmethod
    @property
    def TerminationRequested(cls) -> Result.Base: ...
    @classmethod
    @property
    def TimedOut(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnknownThread(cls) -> Result.Base: ...
