import typing, clr, abc
from LibHac.Fs import IStorage, SubStorage, OpenMode, Path, OperationId, NxFileAttributes, DirectoryEntry
from System import Array_1, Span_1, ReadOnlySpan_1
from LibHac import Result
from LibHac.Fs.Fsa import IDirectory, IFileSystem, OpenDirectoryMode, IFile, CreateFileOptions
from LibHac.Common import UniqueRef_1, U8String, SharedRef_1, IProgressReport, Validity, U8Span
from System.Collections.Generic import IList_1, IEnumerable_1
from System.IO import FileAttributes, Stream, BinaryReader, SeekOrigin, FileAccess
from LibHac.Tools.Fs import DirectoryEntryEx
from LibHac.FsSystem import PartitionFileSystemType

class Aes128CtrExStorage(Aes128CtrStorage):
    def __init__(self, baseStorage: IStorage, nodeStorage: SubStorage, entryStorage: SubStorage, entryCount: int, key: Array_1[int], counter: Array_1[int], leaveOpen: bool) -> None: ...
    NodeSize : int
    @property
    def SectorCount(self) -> int: ...
    @property
    def SectorSize(self) -> int: ...
    def Flush(self) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...

    class Entry:
        Generation : int
        Offset : int
        Reserved : int



class Aes128CtrStorage(SectorStorage):
    @typing.overload
    def __init__(self, baseStorage: IStorage, key: Array_1[int], counter: Array_1[int], leaveOpen: bool) -> None: ...
    @typing.overload
    def __init__(self, baseStorage: IStorage, key: Array_1[int], counterOffset: int, counterHi: Array_1[int], leaveOpen: bool) -> None: ...
    @property
    def SectorCount(self) -> int: ...
    @property
    def SectorSize(self) -> int: ...
    @staticmethod
    def CreateCounter(hiBytes: int, offset: int) -> Array_1[int]: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class Aes128CtrTransform:
    def __init__(self, key: Array_1[int], counter: Array_1[int]) -> None: ...
    Counter : Array_1[int]
    @staticmethod
    def FillDecryptedCounter(buffer: Span_1[int]) -> None: ...
    def TransformBlock(self, data: Span_1[int]) -> int: ...


class Aes128XtsStorage(SectorStorage):
    @typing.overload
    def __init__(self, baseStorage: IStorage, key: Span_1[int], sectorSize: int, leaveOpen: bool, decryptRead: bool = ...) -> None: ...
    @typing.overload
    def __init__(self, baseStorage: IStorage, key1: Span_1[int], key2: Span_1[int], sectorSize: int, leaveOpen: bool, decryptRead: bool = ...) -> None: ...
    @property
    def SectorCount(self) -> int: ...
    @property
    def SectorSize(self) -> int: ...
    def Flush(self) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class Aes128XtsTransform:
    def __init__(self, key1: Array_1[int], key2: Array_1[int], decrypting: bool) -> None: ...
    def TransformBlock(self, buffer: Array_1[int], offset: int, count: int, sector: int) -> int: ...


class AesCbcStorage(SectorStorage):
    def __init__(self, baseStorage: IStorage, key: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int], leaveOpen: bool) -> None: ...
    @property
    def SectorCount(self) -> int: ...
    @property
    def SectorSize(self) -> int: ...
    def Flush(self) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class AesXtsDirectory(IDirectory):
    def __init__(self, baseFs: IFileSystem, baseDir: clr.Reference[UniqueRef_1[IDirectory]], path: U8String, mode: OpenDirectoryMode) -> None: ...
    def Dispose(self) -> None: ...


class AesXtsFile(IFile):
    def __init__(self, mode: OpenMode, baseFile: clr.Reference[UniqueRef_1[IFile]], path: U8String, kekSeed: ReadOnlySpan_1[int], verificationKey: ReadOnlySpan_1[int], blockSize: int) -> None: ...
    @property
    def Header(self) -> AesXtsFileHeader: ...
    def Dispose(self) -> None: ...
    def GetKey(self) -> Array_1[int]: ...


class AesXtsFileHeader:
    @typing.overload
    def __init__(self, aesXtsFile: IFile) -> None: ...
    @typing.overload
    def __init__(self, key: Array_1[int], fileSize: int, path: str, kekSeed: Array_1[int], verificationKey: Array_1[int]) -> None: ...
    @property
    def DecryptedKey1(self) -> Array_1[int]: ...
    @property
    def DecryptedKey2(self) -> Array_1[int]: ...
    @property
    def EncryptedKey1(self) -> Array_1[int]: ...
    @property
    def EncryptedKey2(self) -> Array_1[int]: ...
    @property
    def Kek1(self) -> Array_1[int]: ...
    @property
    def Kek2(self) -> Array_1[int]: ...
    @property
    def Magic(self) -> int: ...
    @property
    def Signature(self) -> Array_1[int]: ...
    @Signature.setter
    def Signature(self, value: Array_1[int]) -> Array_1[int]: ...
    @property
    def Size(self) -> int: ...
    @Size.setter
    def Size(self, value: int) -> int: ...
    def EncryptHeader(self, path: str, kekSeed: Array_1[int], verificationKey: Array_1[int]) -> None: ...
    def SetSize(self, size: int, verificationKey: Array_1[int]) -> None: ...
    def ToBytes(self, writeDecryptedKey: bool) -> Array_1[int]: ...
    def TryDecryptHeader(self, path: str, kekSeed: Array_1[int], verificationKey: Array_1[int]) -> bool: ...


class AesXtsFileSystem(IFileSystem):
    @typing.overload
    def __init__(self, fs: clr.Reference[SharedRef_1[IFileSystem]], keys: Array_1[int], blockSize: int) -> None: ...
    @typing.overload
    def __init__(self, fs: IFileSystem, keys: Array_1[int], blockSize: int) -> None: ...
    @property
    def BlockSize(self) -> int: ...
    def CreateFile(self, path: clr.Reference[Path], size: int, options: CreateFileOptions, key: Array_1[int]) -> Result: ...
    def Dispose(self) -> None: ...


class CachedStorage(IStorage):
    @typing.overload
    def __init__(self, baseStorage: IStorage, blockSize: int, cacheSize: int, leaveOpen: bool) -> None: ...
    @typing.overload
    def __init__(self, baseStorage: SectorStorage, cacheSize: int, leaveOpen: bool) -> None: ...
    def Dispose(self) -> None: ...
    def Flush(self) -> Result: ...
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    def OperateRange(self, outBuffer: Span_1[int], operationId: OperationId, offset: int, size: int, inBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class ConcatenationStorage(IStorage):
    def __init__(self, sources: IList_1[IStorage], leaveOpen: bool) -> None: ...
    def Dispose(self) -> None: ...
    def Flush(self) -> Result: ...
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    def OperateRange(self, outBuffer: Span_1[int], operationId: OperationId, offset: int, size: int, inBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class ConcatenationStorageBuilder:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, segments: IEnumerable_1[ConcatenationStorageSegment]) -> None: ...
    def Add(self, storage: IStorage, offset: int) -> None: ...
    def Build(self) -> ConcatenationStorage: ...


class ConcatenationStorageSegment:
    def __init__(self, storage: IStorage, offset: int) -> None: ...
    @property
    def Offset(self) -> int: ...
    @property
    def Storage(self) -> IStorage: ...


class Delta:
    @typing.overload
    def __init__(self, deltaStorage: IStorage) -> None: ...
    @typing.overload
    def __init__(self, deltaStorage: IStorage, originalData: IStorage) -> None: ...
    @property
    def Header(self) -> DeltaHeader: ...
    def GetPatchedStorage(self) -> IStorage: ...
    def SetBaseStorage(self, baseStorage: IStorage) -> None: ...


class DeltaHeader:
    def __init__(self, header: IFile) -> None: ...
    @property
    def BodySize(self) -> int: ...
    @property
    def HeaderSize(self) -> int: ...
    @property
    def Magic(self) -> str: ...
    @property
    def NewSize(self) -> int: ...
    @property
    def OriginalSize(self) -> int: ...


class FileReader:
    @typing.overload
    def __init__(self, file: IFile) -> None: ...
    @typing.overload
    def __init__(self, file: IFile, start: int) -> None: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> int: ...
    @staticmethod
    def SignExtend32(value: int, bits: int) -> int: ...
    # Skipped ReadAscii due to it being static, abstract and generic.

    ReadAscii : ReadAscii_MethodGroup
    class ReadAscii_MethodGroup:
        @typing.overload
        def __call__(self, length: int) -> str:...
        @typing.overload
        def __call__(self, offset: int, length: int) -> str:...
        @typing.overload
        def __call__(self, offset: int, length: int, updatePosition: bool) -> str:...

    # Skipped ReadBytes due to it being static, abstract and generic.

    ReadBytes : ReadBytes_MethodGroup
    class ReadBytes_MethodGroup:
        @typing.overload
        def __call__(self, length: int) -> Array_1[int]:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> None:...
        @typing.overload
        def __call__(self, offset: int, length: int) -> Array_1[int]:...
        @typing.overload
        def __call__(self, destination: Span_1[int], offset: int) -> None:...
        @typing.overload
        def __call__(self, offset: int, length: int, updatePosition: bool) -> Array_1[int]:...
        @typing.overload
        def __call__(self, destination: Span_1[int], offset: int, updatePosition: bool) -> None:...

    # Skipped ReadDouble due to it being static, abstract and generic.

    ReadDouble : ReadDouble_MethodGroup
    class ReadDouble_MethodGroup:
        @typing.overload
        def __call__(self) -> float:...
        @typing.overload
        def __call__(self, offset: int) -> float:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> float:...

    # Skipped ReadInt16 due to it being static, abstract and generic.

    ReadInt16 : ReadInt16_MethodGroup
    class ReadInt16_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadInt24 due to it being static, abstract and generic.

    ReadInt24 : ReadInt24_MethodGroup
    class ReadInt24_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadInt32 due to it being static, abstract and generic.

    ReadInt32 : ReadInt32_MethodGroup
    class ReadInt32_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadInt64 due to it being static, abstract and generic.

    ReadInt64 : ReadInt64_MethodGroup
    class ReadInt64_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadInt8 due to it being static, abstract and generic.

    ReadInt8 : ReadInt8_MethodGroup
    class ReadInt8_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadSingle due to it being static, abstract and generic.

    ReadSingle : ReadSingle_MethodGroup
    class ReadSingle_MethodGroup:
        @typing.overload
        def __call__(self) -> float:...
        @typing.overload
        def __call__(self, offset: int) -> float:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> float:...

    # Skipped ReadUInt16 due to it being static, abstract and generic.

    ReadUInt16 : ReadUInt16_MethodGroup
    class ReadUInt16_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadUInt24 due to it being static, abstract and generic.

    ReadUInt24 : ReadUInt24_MethodGroup
    class ReadUInt24_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadUInt32 due to it being static, abstract and generic.

    ReadUInt32 : ReadUInt32_MethodGroup
    class ReadUInt32_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadUInt64 due to it being static, abstract and generic.

    ReadUInt64 : ReadUInt64_MethodGroup
    class ReadUInt64_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...

    # Skipped ReadUInt8 due to it being static, abstract and generic.

    ReadUInt8 : ReadUInt8_MethodGroup
    class ReadUInt8_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, offset: int) -> int:...
        @typing.overload
        def __call__(self, offset: int, updatePosition: bool) -> int:...



class FileSystemExtensions(abc.ABC):
    @staticmethod
    def ApplyNxAttributes(attributes: FileAttributes, nxAttributes: NxFileAttributes) -> FileAttributes: ...
    @staticmethod
    def AsIFile(stream: Stream, mode: OpenMode) -> IFile: ...
    @staticmethod
    def AsStorage(file: IFile) -> IStorage: ...
    @staticmethod
    def CleanDirectoryRecursivelyGeneric(fileSystem: IFileSystem, path: str) -> None: ...
    @staticmethod
    def CopyDirectory(sourceFs: IFileSystem, destFs: IFileSystem, sourcePath: str, destPath: str, logger: IProgressReport = ..., options: CreateFileOptions = ...) -> Result: ...
    @staticmethod
    def CopyDirectoryRecursively(destinationFileSystem: IFileSystem, sourceFileSystem: IFileSystem, destinationPath: clr.Reference[Path], sourcePath: clr.Reference[Path], dirEntry: clr.Reference[DirectoryEntry], workBuffer: Span_1[int], logger: IProgressReport = ..., option: CreateFileOptions = ...) -> Result: ...
    @staticmethod
    def CopyFile(destFileSystem: IFileSystem, sourceFileSystem: IFileSystem, destPath: clr.Reference[Path], sourcePath: clr.Reference[Path], workBuffer: Span_1[int], logger: IProgressReport = ..., option: CreateFileOptions = ...) -> Result: ...
    @staticmethod
    def CopyTo(file: IFile, dest: IFile, logger: IProgressReport = ...) -> None: ...
    @staticmethod
    def CreateOrOverwriteFile(fileSystem: IFileSystem, path: clr.Reference[Path], size: int, option: CreateFileOptions = ...) -> Result: ...
    @staticmethod
    def DirectoryExists(fs: IFileSystem, path: str) -> bool: ...
    @staticmethod
    def EnsureDirectoryExists(fs: IFileSystem, path: str) -> Result: ...
    @staticmethod
    def Extract(source: IFileSystem, destinationPath: str, logger: IProgressReport = ...) -> None: ...
    @staticmethod
    def FileExists(fs: IFileSystem, path: str) -> bool: ...
    @staticmethod
    def GetEntryCount(fs: IFileSystem, mode: OpenDirectoryMode) -> int: ...
    @staticmethod
    def GetEntryCountRecursive(fs: IFileSystem, path: str, mode: OpenDirectoryMode) -> int: ...
    @staticmethod
    def Read(file: IFile, bytesRead: clr.Reference[int], offset: int, destination: Span_1[int]) -> Result: ...
    @staticmethod
    def SetConcatenationFileAttribute(fs: IFileSystem, path: str) -> None: ...
    @staticmethod
    def ToFatAttributes(attributes: NxFileAttributes) -> FileAttributes: ...
    @staticmethod
    def ToNxAttributes(attributes: FileAttributes) -> NxFileAttributes: ...
    @staticmethod
    def Write(file: IFile, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...
    # Skipped AsStream due to it being static, abstract and generic.

    AsStream : AsStream_MethodGroup
    class AsStream_MethodGroup:
        @typing.overload
        def __call__(self, file: IFile) -> Stream:...
        @typing.overload
        def __call__(self, file: IFile, mode: OpenMode, keepOpen: bool) -> Stream:...

    # Skipped EnumerateEntries due to it being static, abstract and generic.

    EnumerateEntries : EnumerateEntries_MethodGroup
    class EnumerateEntries_MethodGroup:
        @typing.overload
        def __call__(self, fileSystem: IFileSystem) -> IEnumerable_1[DirectoryEntryEx]:...
        @typing.overload
        def __call__(self, fileSystem: IFileSystem, searchPattern: str, searchOptions: SearchOptions) -> IEnumerable_1[DirectoryEntryEx]:...
        @typing.overload
        def __call__(self, fileSystem: IFileSystem, path: str, searchPattern: str) -> IEnumerable_1[DirectoryEntryEx]:...
        @typing.overload
        def __call__(self, fileSystem: IFileSystem, path: str, searchPattern: str, searchOptions: SearchOptions) -> IEnumerable_1[DirectoryEntryEx]:...



class HierarchicalIntegrityVerificationStorage(IStorage):
    @typing.overload
    def __init__(self, header: IvfcHeader, levels: IList_1[IStorage], type: IntegrityStorageType, integrityCheckLevel: IntegrityCheckLevel, leaveOpen: bool) -> None: ...
    @typing.overload
    def __init__(self, header: IvfcHeader, masterHash: IStorage, data: IStorage, type: IntegrityStorageType, integrityCheckLevel: IntegrityCheckLevel, leaveOpen: bool) -> None: ...
    @typing.overload
    def __init__(self, levelInfo: Array_1[IntegrityVerificationInfo], integrityCheckLevel: IntegrityCheckLevel, leaveOpen: bool) -> None: ...
    @property
    def DataLevel(self) -> IStorage: ...
    @property
    def IntegrityCheckLevel(self) -> IntegrityCheckLevel: ...
    @property
    def Levels(self) -> Array_1[IStorage]: ...
    @property
    def LevelValidities(self) -> Array_1[Array_1[Validity]]: ...
    def Dispose(self) -> None: ...
    def Flush(self) -> Result: ...
    def FsTrim(self) -> None: ...
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    def OperateRange(self, outBuffer: Span_1[int], operationId: OperationId, offset: int, size: int, inBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Validate(self, returnOnError: bool, logger: IProgressReport = ...) -> Validity: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class HierarchicalIntegrityVerificationStorageExtensions(abc.ABC):
    pass


class IntegrityCheckLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : IntegrityCheckLevel # 0
    IgnoreOnInvalid : IntegrityCheckLevel # 1
    ErrorOnInvalid : IntegrityCheckLevel # 2


class IntegrityStorageType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Save : IntegrityStorageType # 0
    RomFs : IntegrityStorageType # 1
    PartitionFs : IntegrityStorageType # 2


class IntegrityVerificationInfo:
    def __init__(self) -> None: ...
    @property
    def BlockSize(self) -> int: ...
    @BlockSize.setter
    def BlockSize(self, value: int) -> int: ...
    @property
    def Data(self) -> IStorage: ...
    @Data.setter
    def Data(self, value: IStorage) -> IStorage: ...
    @property
    def Salt(self) -> Array_1[int]: ...
    @Salt.setter
    def Salt(self, value: Array_1[int]) -> Array_1[int]: ...
    @property
    def Type(self) -> IntegrityStorageType: ...
    @Type.setter
    def Type(self, value: IntegrityStorageType) -> IntegrityStorageType: ...


class IntegrityVerificationStorage(SectorStorage):
    def __init__(self, info: IntegrityVerificationInfo, hashStorage: IStorage, integrityCheckLevel: IntegrityCheckLevel, leaveOpen: bool) -> None: ...
    @property
    def BlockValidities(self) -> Array_1[Validity]: ...
    @property
    def IntegrityCheckLevel(self) -> IntegrityCheckLevel: ...
    @property
    def SectorCount(self) -> int: ...
    @property
    def SectorSize(self) -> int: ...
    def Flush(self) -> Result: ...
    def FsTrim(self) -> None: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...
    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        @typing.overload
        def __call__(self, offset: int, destination: Span_1[int]) -> Result:...
        @typing.overload
        def __call__(self, offset: int, destination: Span_1[int], integrityCheckLevel: IntegrityCheckLevel) -> Result:...



class IvfcHeader:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, reader: BinaryReader) -> None: ...
    @typing.overload
    def __init__(self, storage: IStorage) -> None: ...
    LevelHeaders : Array_1[IvfcLevelHeader]
    Magic : str
    MasterHash : Array_1[int]
    MasterHashSize : int
    NumLevels : int
    SaltSource : Array_1[int]
    Version : int


class IvfcLevelHeader:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, reader: BinaryReader) -> None: ...
    BlockSizePower : int
    HashValidity : Validity
    Offset : int
    Reserved : int
    Size : int


class LayeredFileSystem(IFileSystem):
    @typing.overload
    def __init__(self, lowerFileSystem: IFileSystem, upperFileSystem: IFileSystem) -> None: ...
    @typing.overload
    def __init__(self, sourceFileSystems: IList_1[IFileSystem]) -> None: ...


class NullFile(IFile):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, length: int) -> None: ...


class NullStorage(IStorage):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, length: int) -> None: ...
    def Flush(self) -> Result: ...
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    def OperateRange(self, outBuffer: Span_1[int], operationId: OperationId, offset: int, size: int, inBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class NxFileStream(Stream):
    @typing.overload
    def __init__(self, baseFile: IFile, leaveOpen: bool) -> None: ...
    @typing.overload
    def __init__(self, baseFile: IFile, mode: OpenMode, leaveOpen: bool) -> None: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanTimeout(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> int: ...
    @property
    def ReadTimeout(self) -> int: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> int: ...
    @property
    def WriteTimeout(self) -> int: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> int: ...
    def Flush(self) -> None: ...
    def Read(self, buffer: Array_1[int], offset: int, count: int) -> int: ...
    def Seek(self, offset: int, origin: SeekOrigin) -> int: ...
    def SetLength(self, value: int) -> None: ...
    def Write(self, buffer: Array_1[int], offset: int, count: int) -> None: ...


class PartitionFileSystemBuilder:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, input: IFileSystem) -> None: ...
    def AddFile(self, filename: str, file: IFile) -> None: ...
    def Build(self, type: PartitionFileSystemType) -> IStorage: ...


class PathParser:
    def __init__(self, path: ReadOnlySpan_1[int]) -> None: ...
    def GetCurrent(self) -> ReadOnlySpan_1[int]: ...
    def IsFinished(self) -> bool: ...
    def MoveNext(self) -> bool: ...
    def TryGetNext(self, name: clr.Reference[ReadOnlySpan_1[int]]) -> bool: ...


class PathTools(abc.ABC):
    @staticmethod
    def Combine(path1: str, path2: str) -> str: ...
    @staticmethod
    def GetFileName(path: ReadOnlySpan_1[int]) -> ReadOnlySpan_1[int]: ...
    @staticmethod
    def GetLastSegment(path: ReadOnlySpan_1[int]) -> ReadOnlySpan_1[int]: ...
    @staticmethod
    def GetMountName(path: str, mountName: clr.Reference[str]) -> Result: ...
    @staticmethod
    def GetMountNameLength(path: str, length: clr.Reference[int]) -> Result: ...
    @staticmethod
    def MatchesPattern(searchPattern: str, name: str, ignoreCase: bool) -> bool: ...
    # Skipped GetParentDirectory due to it being static, abstract and generic.

    GetParentDirectory : GetParentDirectory_MethodGroup
    class GetParentDirectory_MethodGroup:
        @typing.overload
        def __call__(self, path: ReadOnlySpan_1[int]) -> ReadOnlySpan_1[int]:...
        @typing.overload
        def __call__(self, path: str) -> str:...

    # Skipped IsNormalized due to it being static, abstract and generic.

    IsNormalized : IsNormalized_MethodGroup
    class IsNormalized_MethodGroup:
        @typing.overload
        def __call__(self, path: ReadOnlySpan_1[str]) -> bool:...
        @typing.overload
        def __call__(self, path: ReadOnlySpan_1[int]) -> bool:...

    # Skipped IsSubPath due to it being static, abstract and generic.

    IsSubPath : IsSubPath_MethodGroup
    class IsSubPath_MethodGroup:
        @typing.overload
        def __call__(self, path1: ReadOnlySpan_1[str], path2: ReadOnlySpan_1[str]) -> bool:...
        @typing.overload
        def __call__(self, path1: ReadOnlySpan_1[int], path2: ReadOnlySpan_1[int]) -> bool:...

    # Skipped Normalize due to it being static, abstract and generic.

    Normalize : Normalize_MethodGroup
    class Normalize_MethodGroup:
        @typing.overload
        def __call__(self, inPath: str) -> str:...
        @typing.overload
        def __call__(self, normalizedPath: clr.Reference[U8Span], path: U8Span) -> Result:...



class SearchOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : SearchOptions # 0
    RecurseSubdirectories : SearchOptions # 1
    CaseInsensitive : SearchOptions # 2


class SectorStorage(IStorage):
    def __init__(self, baseStorage: IStorage, sectorSize: int, leaveOpen: bool) -> None: ...
    @property
    def SectorCount(self) -> int: ...
    @SectorCount.setter
    def SectorCount(self, value: int) -> int: ...
    @property
    def SectorSize(self) -> int: ...
    def Dispose(self) -> None: ...
    def Flush(self) -> Result: ...
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    def OperateRange(self, outBuffer: Span_1[int], operationId: OperationId, offset: int, size: int, inBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...


class StorageExtensions(abc.ABC):
    @staticmethod
    def AsFile(storage: IStorage, mode: OpenMode) -> IFile: ...
    @staticmethod
    def CopyTo(input: IStorage, output: IStorage, progress: IProgressReport = ..., bufferSize: int = ...) -> None: ...
    @staticmethod
    def WriteAllBytes(input: IStorage, filename: str, progress: IProgressReport = ...) -> None: ...
    # Skipped AsStorage due to it being static, abstract and generic.

    AsStorage : AsStorage_MethodGroup
    class AsStorage_MethodGroup:
        @typing.overload
        def __call__(self, stream: Stream) -> IStorage:...
        @typing.overload
        def __call__(self, stream: Stream, start: int) -> IStorage:...
        # Method AsStorage(stream : Stream, keepOpen : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, stream: Stream, start: int, length: int) -> IStorage:...
        @typing.overload
        def __call__(self, stream: Stream, start: int, length: int, keepOpen: bool) -> IStorage:...

    # Skipped AsStream due to it being static, abstract and generic.

    AsStream : AsStream_MethodGroup
    class AsStream_MethodGroup:
        @typing.overload
        def __call__(self, storage: IStorage) -> Stream:...
        @typing.overload
        def __call__(self, storage: IStorage, access: FileAccess) -> Stream:...
        @typing.overload
        def __call__(self, storage: IStorage, access: FileAccess, keepOpen: bool) -> Stream:...

    # Skipped CopyToStream due to it being static, abstract and generic.

    CopyToStream : CopyToStream_MethodGroup
    class CopyToStream_MethodGroup:
        @typing.overload
        def __call__(self, input: IStorage, output: Stream, bufferSize: int = ...) -> None:...
        @typing.overload
        def __call__(self, input: IStorage, output: Stream, length: int, progress: IProgressReport = ..., bufferSize: int = ...) -> None:...

    # Skipped Fill due to it being static, abstract and generic.

    Fill : Fill_MethodGroup
    class Fill_MethodGroup:
        @typing.overload
        def __call__(self, input: IStorage, value: int, progress: IProgressReport = ...) -> None:...
        @typing.overload
        def __call__(self, input: IStorage, value: int, offset: int, count: int, progress: IProgressReport = ...) -> None:...

    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup
    class Slice_MethodGroup:
        @typing.overload
        def __call__(self, storage: IStorage, start: int) -> IStorage:...
        @typing.overload
        def __call__(self, storage: IStorage, start: int, length: int) -> IStorage:...
        @typing.overload
        def __call__(self, storage: IStorage, start: int, length: int, leaveOpen: bool) -> IStorage:...

    # Skipped ToArray due to it being static, abstract and generic.

    ToArray : ToArray_MethodGroup
    class ToArray_MethodGroup:
        def __getitem__(self, t:typing.Type[ToArray_1_T1]) -> ToArray_1[ToArray_1_T1]: ...

        ToArray_1_T1 = typing.TypeVar('ToArray_1_T1')
        class ToArray_1(typing.Generic[ToArray_1_T1]):
            ToArray_1_T = StorageExtensions.ToArray_MethodGroup.ToArray_1_T1
            def __call__(self, storage: IStorage) -> Array_1[ToArray_1_T]:...

        def __call__(self, storage: IStorage) -> Array_1[int]:...



class StorageStream(Stream):
    def __init__(self, baseStorage: IStorage, access: FileAccess, leaveOpen: bool) -> None: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanTimeout(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> int: ...
    @property
    def ReadTimeout(self) -> int: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> int: ...
    @property
    def WriteTimeout(self) -> int: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> int: ...
    def Flush(self) -> None: ...
    def Read(self, buffer: Array_1[int], offset: int, count: int) -> int: ...
    def Seek(self, offset: int, origin: SeekOrigin) -> int: ...
    def SetLength(self, value: int) -> None: ...
    def Write(self, buffer: Array_1[int], offset: int, count: int) -> None: ...


class StreamFile(IFile):
    def __init__(self, baseStream: Stream, mode: OpenMode) -> None: ...


class StreamStorage(IStorage):
    def __init__(self, baseStream: Stream, leaveOpen: bool) -> None: ...
    def Dispose(self) -> None: ...
    def Flush(self) -> Result: ...
    def GetSize(self, size: clr.Reference[int]) -> Result: ...
    def OperateRange(self, outBuffer: Span_1[int], operationId: OperationId, offset: int, size: int, inBuffer: ReadOnlySpan_1[int]) -> Result: ...
    def Read(self, offset: int, destination: Span_1[int]) -> Result: ...
    def SetSize(self, size: int) -> Result: ...
    def Write(self, offset: int, source: ReadOnlySpan_1[int]) -> Result: ...

