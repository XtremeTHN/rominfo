import typing, clr
from LibHac import ApplicationId, Result
from LibHac.Ncm import StorageId
from System import IDisposable
from LibHac.Ns import ApplicationControlProperty

class ApplicationKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Application : ApplicationKind # 0
    MicroApplication : ApplicationKind # 1


class ApplicationLaunchProperty:
    ApplicationId : ApplicationId
    ApplicationKind : ApplicationKind
    PatchStorageId : StorageId
    StorageId : StorageId
    Version : int


class ArpClient(IDisposable):
    def Dispose(self) -> None: ...
    # Skipped GetApplicationControlProperty due to it being static, abstract and generic.

    GetApplicationControlProperty : GetApplicationControlProperty_MethodGroup
    class GetApplicationControlProperty_MethodGroup:
        @typing.overload
        def __call__(self, controlProperty: clr.Reference[ApplicationControlProperty], processId: int) -> Result:...
        @typing.overload
        def __call__(self, controlProperty: clr.Reference[ApplicationControlProperty], applicationId: ApplicationId) -> Result:...

    # Skipped GetApplicationLaunchProperty due to it being static, abstract and generic.

    GetApplicationLaunchProperty : GetApplicationLaunchProperty_MethodGroup
    class GetApplicationLaunchProperty_MethodGroup:
        @typing.overload
        def __call__(self, launchProperty: clr.Reference[ApplicationLaunchProperty], processId: int) -> Result:...
        @typing.overload
        def __call__(self, launchProperty: clr.Reference[ApplicationLaunchProperty], applicationId: ApplicationId) -> Result:...


