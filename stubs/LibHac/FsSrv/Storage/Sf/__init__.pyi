import typing, clr, abc
from LibHac.FsSrv.Sf import IStorage, IEventNotifier
from LibHac import Result
from LibHac.Common import SharedRef_1
from System import IDisposable
from LibHac.Sf import InBuffer, OutBuffer

class IStorageDevice(IStorage, typing.Protocol):
    @abc.abstractmethod
    def GetHandle(self, handle: clr.Reference[int]) -> Result: ...
    @abc.abstractmethod
    def IsHandleValid(self, isValid: clr.Reference[bool]) -> Result: ...
    @abc.abstractmethod
    def OpenOperator(self, outDeviceOperator: clr.Reference[SharedRef_1[IStorageDeviceOperator]]) -> Result: ...


class IStorageDeviceManager(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def Invalidate(self) -> Result: ...
    @abc.abstractmethod
    def IsHandleValid(self, isValid: clr.Reference[bool], handle: int) -> Result: ...
    @abc.abstractmethod
    def IsInserted(self, isInserted: clr.Reference[bool]) -> Result: ...
    @abc.abstractmethod
    def OpenDetectionEvent(self, outEventNotifier: clr.Reference[SharedRef_1[IEventNotifier]]) -> Result: ...
    @abc.abstractmethod
    def OpenDevice(self, outStorageDevice: clr.Reference[SharedRef_1[IStorageDevice]], attribute: int) -> Result: ...
    @abc.abstractmethod
    def OpenOperator(self, outDeviceOperator: clr.Reference[SharedRef_1[IStorageDeviceOperator]]) -> Result: ...
    @abc.abstractmethod
    def OpenStorage(self, outStorage: clr.Reference[SharedRef_1[IStorage]], attribute: int) -> Result: ...


class IStorageDeviceOperator(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def Operate(self, operationId: int) -> Result: ...
    @abc.abstractmethod
    def OperateIn(self, buffer: InBuffer, offset: int, size: int, operationId: int) -> Result: ...
    @abc.abstractmethod
    def OperateIn2Out(self, bytesWritten: clr.Reference[int], outBuffer: OutBuffer, inBuffer1: InBuffer, inBuffer2: InBuffer, offset: int, size: int, operationId: int) -> Result: ...
    @abc.abstractmethod
    def OperateInOut(self, bytesWritten: clr.Reference[int], outBuffer: OutBuffer, inBuffer: InBuffer, offset: int, size: int, operationId: int) -> Result: ...
    @abc.abstractmethod
    def OperateOut(self, bytesWritten: clr.Reference[int], buffer: OutBuffer, operationId: int) -> Result: ...
    @abc.abstractmethod
    def OperateOut2(self, bytesWrittenBuffer1: clr.Reference[int], buffer1: OutBuffer, bytesWrittenBuffer2: clr.Reference[int], buffer2: OutBuffer, operationId: int) -> Result: ...

