from LibHac.Common.FixedArrays import Array16_1
from System import Memory_1
from LibHac import Result

class FatAttribute:
    IsFatFormatNormalized : bool
    IsFatSafeEnabled : bool
    IsTimeStampUpdated : bool


class FatError:
    DriveId : int
    Error : int
    ErrorName : Array16_1[int]
    ExtraError : int
    Reserved : int


class FatFormatParam:
    IsSdCard : bool
    ProtectedAreaSectors : int
    WorkBuffer : Memory_1[int]
    WriteVerifyErrorResult : Result


class FatReport:
    DirectoryCurrentOpenCount : int
    DirectoryPeakOpenCount : int
    FileCurrentOpenCount : int
    FilePeakOpenCount : int


class FatReportInfo:
    DirectoryPeakOpenCount : int
    FilePeakOpenCount : int

