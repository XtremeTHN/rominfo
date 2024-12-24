import typing, clr, abc
from System import IDisposable, Span_1
from LibHac import Result, ApplicationId
from LibHac.Bcat import DirectoryName, DeliveryCacheDirectoryEntry, Digest, FileName
from LibHac.Common import SharedRef_1

class IDeliveryCacheDirectoryService(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def GetCount(self, count: clr.Reference[int]) -> Result: ...
    @abc.abstractmethod
    def Open(self, name: clr.Reference[DirectoryName]) -> Result: ...
    @abc.abstractmethod
    def Read(self, entriesRead: clr.Reference[int], entryBuffer: Span_1[DeliveryCacheDirectoryEntry]) -> Result: ...


class IDeliveryCacheFileService(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def GetDigest(self, digest: clr.Reference[Digest]) -> Result: ...
    @abc.abstractmethod
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    @abc.abstractmethod
    def Open(self, directoryName: clr.Reference[DirectoryName], fileName: clr.Reference[FileName]) -> Result: ...
    @abc.abstractmethod
    def Read(self, bytesRead: clr.Reference[int], offset: int, destination: Span_1[int]) -> Result: ...


class IDeliveryCacheStorageService(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def CreateDirectoryService(self, outDirectoryService: clr.Reference[SharedRef_1[IDeliveryCacheDirectoryService]]) -> Result: ...
    @abc.abstractmethod
    def CreateFileService(self, outFileService: clr.Reference[SharedRef_1[IDeliveryCacheFileService]]) -> Result: ...
    @abc.abstractmethod
    def EnumerateDeliveryCacheDirectory(self, namesRead: clr.Reference[int], nameBuffer: Span_1[DirectoryName]) -> Result: ...


class IServiceCreator(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def CreateDeliveryCacheStorageService(self, outService: clr.Reference[SharedRef_1[IDeliveryCacheStorageService]], processId: int) -> Result: ...
    @abc.abstractmethod
    def CreateDeliveryCacheStorageServiceWithApplicationId(self, outService: clr.Reference[SharedRef_1[IDeliveryCacheStorageService]], applicationId: ApplicationId) -> Result: ...

