import typing, clr, abc
from System import IDisposable, ReadOnlySpan_1, IEquatable_1
from LibHac import Result
from LibHac.Common import SharedRef_1

class IServiceObject(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def GetServiceObject(self, serviceObject: clr.Reference[SharedRef_1[IDisposable]]) -> Result: ...


class ResultSm(abc.ABC):
    ModuleSm : int
    @classmethod
    @property
    def AlreadyRegistered(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidClient(cls) -> Result.Base: ...
    @classmethod
    @property
    def InvalidServiceName(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotAllowed(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotRegistered(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfProcesses(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfServices(cls) -> Result.Base: ...
    @classmethod
    @property
    def OutOfSessions(cls) -> Result.Base: ...
    @classmethod
    @property
    def TooLargeAccessControl(cls) -> Result.Base: ...


class ServiceManagerClient:
    def RegisterService(self, serviceObject: IServiceObject, name: ReadOnlySpan_1[str]) -> Result: ...
    def UnregisterService(self, name: ReadOnlySpan_1[str]) -> Result: ...
    # Skipped GetService due to it being static, abstract and generic.

    GetService : GetService_MethodGroup
    class GetService_MethodGroup:
        def __getitem__(self, t:typing.Type[GetService_1_T1]) -> GetService_1[GetService_1_T1]: ...

        GetService_1_T1 = typing.TypeVar('GetService_1_T1')
        class GetService_1(typing.Generic[GetService_1_T1]):
            GetService_1_T = ServiceManagerClient.GetService_MethodGroup.GetService_1_T1
            def __call__(self, serviceObject: clr.Reference[SharedRef_1[GetService_1_T]], name: ReadOnlySpan_1[str]) -> Result:...




class ServiceName(IEquatable_1[ServiceName]):
    Name : int
    @staticmethod
    def Encode(name: ReadOnlySpan_1[str]) -> ServiceName: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: ServiceName, right: ServiceName) -> bool: ...
    def __ne__(self, left: ServiceName, right: ServiceName) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: ServiceName) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...


