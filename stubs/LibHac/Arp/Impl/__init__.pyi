import typing, clr, abc
from System import IDisposable
from LibHac import Result, ApplicationId
from LibHac.Ns import ApplicationControlProperty
from LibHac.Arp import ApplicationLaunchProperty

class IReader(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def GetApplicationControlProperty(self, controlProperty: clr.Reference[ApplicationControlProperty], processId: int) -> Result: ...
    @abc.abstractmethod
    def GetApplicationControlPropertyWithApplicationId(self, controlProperty: clr.Reference[ApplicationControlProperty], applicationId: ApplicationId) -> Result: ...
    @abc.abstractmethod
    def GetApplicationLaunchProperty(self, launchProperty: clr.Reference[ApplicationLaunchProperty], processId: int) -> Result: ...
    @abc.abstractmethod
    def GetApplicationLaunchPropertyWithApplicationId(self, launchProperty: clr.Reference[ApplicationLaunchProperty], applicationId: ApplicationId) -> Result: ...

