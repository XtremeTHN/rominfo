import typing, clr, abc
from LibHac import Result
from LibHac.Sdmmc import SpeedMode, BusWidth, Port

class Common(abc.ABC):
    @staticmethod
    def CheckConnection(outSpeedMode: clr.Reference[SpeedMode], outBusWidth: clr.Reference[BusWidth], port: Port) -> Result: ...


class MmcManagerOperationIdValue(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    GetAndClearErrorInfo : MmcManagerOperationIdValue # 1
    SuspendControl : MmcManagerOperationIdValue # 2
    ResumeControl : MmcManagerOperationIdValue # 3
    GetAndClearPatrolReadAllocateBufferCount : MmcManagerOperationIdValue # 4
    GetPatrolCount : MmcManagerOperationIdValue # 5
    SuspendPatrol : MmcManagerOperationIdValue # 6
    ResumePatrol : MmcManagerOperationIdValue # 7


class MmcOperationIdValue(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    GetSpeedMode : MmcOperationIdValue # 1
    GetCid : MmcOperationIdValue # 2
    GetPartitionSize : MmcOperationIdValue # 3
    GetExtendedCsd : MmcOperationIdValue # 4
    Erase : MmcOperationIdValue # 5


class SdCardManagerOperationIdValue(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    GetAndClearErrorInfo : SdCardManagerOperationIdValue # 1
    SuspendControl : SdCardManagerOperationIdValue # 2
    ResumeControl : SdCardManagerOperationIdValue # 3
    SimulateDetectionEventSignaled : SdCardManagerOperationIdValue # 4


class SdCardOperationIdValue(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    GetSpeedMode : SdCardOperationIdValue # 1
    GetCid : SdCardOperationIdValue # 2
    GetUserAreaNumSectors : SdCardOperationIdValue # 3
    GetUserAreaSize : SdCardOperationIdValue # 4
    GetProtectedAreaNumSectors : SdCardOperationIdValue # 5
    GetProtectedAreaSize : SdCardOperationIdValue # 6

