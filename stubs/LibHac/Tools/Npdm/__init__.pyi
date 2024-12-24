import typing
from System.IO import Stream
from LibHac.Common.Keys import KeySet
from System import Array_1, Tuple_2
from LibHac.Common import Validity
from System.Collections.Generic import List_1

class Aci0:
    def __init__(self, stream: Stream, offset: int) -> None: ...
    Magic : str
    @property
    def FsPermissionsBitmask(self) -> int: ...
    @property
    def FsVersion(self) -> int: ...
    @property
    def KernelAccess(self) -> KernelAccessControl: ...
    @property
    def ServiceAccess(self) -> ServiceAccessControl: ...
    @property
    def TitleId(self) -> int: ...


class Acid:
    @typing.overload
    def __init__(self, stream: Stream, offset: int) -> None: ...
    @typing.overload
    def __init__(self, stream: Stream, offset: int, keySet: KeySet) -> None: ...
    Magic : str
    @property
    def Flags(self) -> int: ...
    @property
    def FsAccess(self) -> FsAccessControl: ...
    @property
    def KernelAccess(self) -> KernelAccessControl: ...
    @property
    def Rsa2048Modulus(self) -> Array_1[int]: ...
    @property
    def Rsa2048Signature(self) -> Array_1[int]: ...
    @property
    def ServiceAccess(self) -> ServiceAccessControl: ...
    @property
    def SignatureValidity(self) -> Validity: ...
    @property
    def Size(self) -> int: ...
    @property
    def TitleIdRangeMax(self) -> int: ...
    @property
    def TitleIdRangeMin(self) -> int: ...


class FsAccessControl:
    def __init__(self, stream: Stream, offset: int) -> None: ...
    @property
    def PermissionsBitmask(self) -> int: ...
    @property
    def Unknown1(self) -> int: ...
    @property
    def Unknown2(self) -> int: ...
    @property
    def Unknown3(self) -> int: ...
    @property
    def Unknown4(self) -> int: ...
    @property
    def Version(self) -> int: ...


class FsAccessHeader:
    def __init__(self, stream: Stream, offset: int) -> None: ...
    @property
    def PermissionsBitmask(self) -> int: ...
    @property
    def Version(self) -> int: ...


class FsPermissionBool(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NULL : FsPermissionBool # 0
    GameCardCertificate : FsPermissionBool # 9223372036854775824
    GameCardIdSet : FsPermissionBool # 9223372036854775824
    SystemSaveDataCreate1 : FsPermissionBool # 9223372036854775840
    SystemSaveDataCreate0 : FsPermissionBool # 9223372036854775848
    SaveDataIterators0 : FsPermissionBool # 9223372036854775904
    SaveDataDelete0 : FsPermissionBool # 9223372036854775904
    BisCache : FsPermissionBool # 9223372036854775936
    EraseMmc : FsPermissionBool # 9223372036854775936
    GameCardAsic : FsPermissionBool # 9223372036854776320
    GameCardDriver : FsPermissionBool # 9223372036854776320
    PosixTime : FsPermissionBool # 9223372036854776832
    Unknown0x19 : FsPermissionBool # 9223372036854777856
    SaveDataCreate : FsPermissionBool # 9223372036854784032
    Unknown0x1A : FsPermissionBool # 9223372036854792224
    SaveDataIterators1 : FsPermissionBool # 9223372036854792224
    SaveDataDelete1 : FsPermissionBool # 9223372036854792232
    SaveDataExtraData : FsPermissionBool # 9223372036854792288
    SaveThumbnails : FsPermissionBool # 9223372036854906880
    GlobalMode : FsPermissionBool # 9223372036855300096
    SpeedEmulation : FsPermissionBool # 9223372036855300096
    Unknown0x16 : FsPermissionBool # 9223372036921884672
    Unknown0x17 : FsPermissionBool # 9223372036988993536
    Unknown0x18 : FsPermissionBool # 9223372037123211264
    PaddingFiles : FsPermissionBool # 13835058055290552320
    SaveData_Debug : FsPermissionBool # 13835058055298940928
    SaveData_SystemManagement : FsPermissionBool # 13835058055315718144


class FsPermissionRw(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unknown0x6 : FsPermissionRw # 9223372036854775808
    GameCardUser : FsPermissionRw # 9223372036854775824
    SystemSaveDataAccess1 : FsPermissionRw # 9223372036854775840
    SaveDataAccess1 : FsPermissionRw # 9223372036854775840
    SystemSaveDataAccess0 : FsPermissionRw # 9223372036854775848
    BisPartition32 : FsPermissionRw # 9223372036854775936
    BisPartition26 : FsPermissionRw # 9223372036854775936
    MountBisType29 : FsPermissionRw # 9223372036854775936
    BisPartition31 : FsPermissionRw # 9223372036854775936
    Unknown0xD : FsPermissionRw # 9223372036854775936
    BisPartition30 : FsPermissionRw # 9223372036854775936
    BisPartition29 : FsPermissionRw # 9223372036854775936
    BisPartition27 : FsPermissionRw # 9223372036854775940
    MountBisType28 : FsPermissionRw # 9223372036854775940
    BisPartition28 : FsPermissionRw # 9223372036854775940
    GameCard_System : FsPermissionRw # 9223372036854776064
    ContentStorageAccess : FsPermissionRw # 9223372036854777856
    MountContentType2 : FsPermissionRw # 9223372036854777857
    MountContentType5 : FsPermissionRw # 9223372036854777857
    MountContentType6 : FsPermissionRw # 9223372036854777857
    MountContentType4 : FsPermissionRw # 9223372036854777857
    MountContentType3 : FsPermissionRw # 9223372036854777857
    MountContentType7 : FsPermissionRw # 9223372036854777857
    ImageDirectoryAccess : FsPermissionRw # 9223372036854779904
    MountBisType31 : FsPermissionRw # 9223372036854808704
    MountBisType30 : FsPermissionRw # 9223372036854808704
    BisPartition25 : FsPermissionRw # 9223372036854841472
    BisPartition23 : FsPermissionRw # 9223372036854841472
    BisPartition24 : FsPermissionRw # 9223372036854841472
    BisPartition22 : FsPermissionRw # 9223372036854841472
    BisPartition10 : FsPermissionRw # 9223372036854841472
    BisPartition21 : FsPermissionRw # 9223372036854841472
    BisPartition20 : FsPermissionRw # 9223372036854841472
    BisPartition0 : FsPermissionRw # 9223372036854841474
    SaveDataAccess0 : FsPermissionRw # 9223372036855037984
    MountContent_System : FsPermissionRw # 9223372036855824392
    SdCardAccess : FsPermissionRw # 13835058055284260864
    Unknown0x23 : FsPermissionRw # 13835058055284260864
    HostAccess : FsPermissionRw # 13835058055286358016


class KernelAccessControl:
    def __init__(self, stream: Stream, offset: int, size: int) -> None: ...
    @property
    def Items(self) -> List_1[KernelAccessControlItem]: ...


class KernelAccessControlIrq:
    def __init__(self, irq0: int, irq1: int) -> None: ...
    @property
    def Irq0(self) -> int: ...
    @property
    def Irq1(self) -> int: ...


class KernelAccessControlItem:
    def __init__(self) -> None: ...
    @property
    def AllowDebug(self) -> bool: ...
    @AllowDebug.setter
    def AllowDebug(self, value: bool) -> bool: ...
    @property
    def AllowedSvcs(self) -> Array_1[bool]: ...
    @AllowedSvcs.setter
    def AllowedSvcs(self, value: Array_1[bool]) -> Array_1[bool]: ...
    @property
    def ApplicationType(self) -> int: ...
    @ApplicationType.setter
    def ApplicationType(self, value: int) -> int: ...
    @property
    def ForceDebug(self) -> bool: ...
    @ForceDebug.setter
    def ForceDebug(self, value: bool) -> bool: ...
    @property
    def HandleTableSize(self) -> int: ...
    @HandleTableSize.setter
    def HandleTableSize(self, value: int) -> int: ...
    @property
    def HasApplicationType(self) -> bool: ...
    @HasApplicationType.setter
    def HasApplicationType(self, value: bool) -> bool: ...
    @property
    def HasDebugFlags(self) -> bool: ...
    @HasDebugFlags.setter
    def HasDebugFlags(self, value: bool) -> bool: ...
    @property
    def HasHandleTableSize(self) -> bool: ...
    @HasHandleTableSize.setter
    def HasHandleTableSize(self, value: bool) -> bool: ...
    @property
    def HasKernelFlags(self) -> bool: ...
    @HasKernelFlags.setter
    def HasKernelFlags(self, value: bool) -> bool: ...
    @property
    def HasKernelVersion(self) -> bool: ...
    @HasKernelVersion.setter
    def HasKernelVersion(self, value: bool) -> bool: ...
    @property
    def HasSvcFlags(self) -> bool: ...
    @HasSvcFlags.setter
    def HasSvcFlags(self, value: bool) -> bool: ...
    @property
    def HighestCpuId(self) -> int: ...
    @HighestCpuId.setter
    def HighestCpuId(self, value: int) -> int: ...
    @property
    def HighestThreadPriority(self) -> int: ...
    @HighestThreadPriority.setter
    def HighestThreadPriority(self, value: int) -> int: ...
    @property
    def Irq(self) -> List_1[KernelAccessControlIrq]: ...
    @Irq.setter
    def Irq(self, value: List_1[KernelAccessControlIrq]) -> List_1[KernelAccessControlIrq]: ...
    @property
    def KernelVersionRelease(self) -> int: ...
    @KernelVersionRelease.setter
    def KernelVersionRelease(self, value: int) -> int: ...
    @property
    def LowestCpuId(self) -> int: ...
    @LowestCpuId.setter
    def LowestCpuId(self, value: int) -> int: ...
    @property
    def LowestThreadPriority(self) -> int: ...
    @LowestThreadPriority.setter
    def LowestThreadPriority(self, value: int) -> int: ...
    @property
    def NormalMmio(self) -> List_1[KernelAccessControlMmio]: ...
    @NormalMmio.setter
    def NormalMmio(self, value: List_1[KernelAccessControlMmio]) -> List_1[KernelAccessControlMmio]: ...
    @property
    def PageMmio(self) -> List_1[KernelAccessControlMmio]: ...
    @PageMmio.setter
    def PageMmio(self, value: List_1[KernelAccessControlMmio]) -> List_1[KernelAccessControlMmio]: ...


class KernelAccessControlMmio:
    def __init__(self, address: int, size: int, isro: bool, isnormal: bool) -> None: ...
    @property
    def Address(self) -> int: ...
    @property
    def IsNormal(self) -> bool: ...
    @IsNormal.setter
    def IsNormal(self, value: bool) -> bool: ...
    @property
    def IsRo(self) -> bool: ...
    @IsRo.setter
    def IsRo(self, value: bool) -> bool: ...
    @property
    def Size(self) -> int: ...
    @Size.setter
    def Size(self, value: int) -> int: ...


class NpdmBinary:
    @typing.overload
    def __init__(self, stream: Stream) -> None: ...
    @typing.overload
    def __init__(self, stream: Stream, keySet: KeySet) -> None: ...
    Magic : str
    @property
    def Aci0(self) -> Aci0: ...
    @property
    def AciD(self) -> Acid: ...
    @property
    def AddressSpaceWidth(self) -> int: ...
    @property
    def DefaultCpuId(self) -> int: ...
    @property
    def Is64Bits(self) -> bool: ...
    @property
    def MainEntrypointStackSize(self) -> int: ...
    @property
    def MainThreadPriority(self) -> int: ...
    @property
    def ProcessCategory(self) -> int: ...
    @property
    def ProductCode(self) -> Array_1[int]: ...
    @property
    def SystemResourceSize(self) -> int: ...
    @property
    def TitleName(self) -> str: ...


class ServiceAccessControl:
    def __init__(self, stream: Stream, offset: int, size: int) -> None: ...
    @property
    def Services(self) -> List_1[Tuple_2[str, bool]]: ...


class SvcName(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Reserved0 : SvcName # 0
    SetHeapSize : SvcName # 1
    SetMemoryPermission : SvcName # 2
    SetMemoryAttribute : SvcName # 3
    MapMemory : SvcName # 4
    UnmapMemory : SvcName # 5
    QueryMemory : SvcName # 6
    ExitProcess : SvcName # 7
    CreateThread : SvcName # 8
    StartThread : SvcName # 9
    ExitThread : SvcName # 10
    SleepThread : SvcName # 11
    GetThreadPriority : SvcName # 12
    SetThreadPriority : SvcName # 13
    GetThreadCoreMask : SvcName # 14
    SetThreadCoreMask : SvcName # 15
    GetCurrentProcessorNumber : SvcName # 16
    SignalEvent : SvcName # 17
    ClearEvent : SvcName # 18
    MapSharedMemory : SvcName # 19
    UnmapSharedMemory : SvcName # 20
    CreateTransferMemory : SvcName # 21
    CloseHandle : SvcName # 22
    ResetSignal : SvcName # 23
    WaitSynchronization : SvcName # 24
    CancelSynchronization : SvcName # 25
    ArbitrateLock : SvcName # 26
    ArbitrateUnlock : SvcName # 27
    WaitProcessWideKeyAtomic : SvcName # 28
    SignalProcessWideKey : SvcName # 29
    GetSystemTick : SvcName # 30
    ConnectToNamedPort : SvcName # 31
    SendSyncRequestLight : SvcName # 32
    SendSyncRequest : SvcName # 33
    SendSyncRequestWithUserBuffer : SvcName # 34
    SendAsyncRequestWithUserBuffer : SvcName # 35
    GetProcessId : SvcName # 36
    GetThreadId : SvcName # 37
    Break : SvcName # 38
    OutputDebugString : SvcName # 39
    ReturnFromException : SvcName # 40
    GetInfo : SvcName # 41
    FlushEntireDataCache : SvcName # 42
    FlushDataCache : SvcName # 43
    MapPhysicalMemory : SvcName # 44
    UnmapPhysicalMemory : SvcName # 45
    GetFutureThreadInfo : SvcName # 46
    GetLastThreadInfo : SvcName # 47
    GetResourceLimitLimitValue : SvcName # 48
    GetResourceLimitCurrentValue : SvcName # 49
    SetThreadActivity : SvcName # 50
    GetThreadContext3 : SvcName # 51
    WaitForAddress : SvcName # 52
    SignalToAddress : SvcName # 53
    Reserved1 : SvcName # 54
    Reserved2 : SvcName # 55
    Reserved3 : SvcName # 56
    Reserved4 : SvcName # 57
    Reserved5 : SvcName # 58
    Reserved6 : SvcName # 59
    DumpInfo : SvcName # 60
    DumpInfoNew : SvcName # 61
    Reserved7 : SvcName # 62
    Reserved8 : SvcName # 63
    CreateSession : SvcName # 64
    AcceptSession : SvcName # 65
    ReplyAndReceiveLight : SvcName # 66
    ReplyAndReceive : SvcName # 67
    ReplyAndReceiveWithUserBuffer : SvcName # 68
    CreateEvent : SvcName # 69
    Reserved9 : SvcName # 70
    Reserved10 : SvcName # 71
    MapPhysicalMemoryUnsafe : SvcName # 72
    UnmapPhysicalMemoryUnsafe : SvcName # 73
    SetUnsafeLimit : SvcName # 74
    CreateCodeMemory : SvcName # 75
    ControlCodeMemory : SvcName # 76
    SleepSystem : SvcName # 77
    ReadWriteRegister : SvcName # 78
    SetProcessActivity : SvcName # 79
    CreateSharedMemory : SvcName # 80
    MapTransferMemory : SvcName # 81
    UnmapTransferMemory : SvcName # 82
    CreateInterruptEvent : SvcName # 83
    QueryPhysicalAddress : SvcName # 84
    QueryIoMapping : SvcName # 85
    CreateDeviceAddressSpace : SvcName # 86
    AttachDeviceAddressSpace : SvcName # 87
    DetachDeviceAddressSpace : SvcName # 88
    MapDeviceAddressSpaceByForce : SvcName # 89
    MapDeviceAddressSpaceAligned : SvcName # 90
    MapDeviceAddressSpace : SvcName # 91
    UnmapDeviceAddressSpace : SvcName # 92
    InvalidateProcessDataCache : SvcName # 93
    StoreProcessDataCache : SvcName # 94
    FlushProcessDataCache : SvcName # 95
    DebugActiveProcess : SvcName # 96
    BreakDebugProcess : SvcName # 97
    TerminateDebugProcess : SvcName # 98
    GetDebugEvent : SvcName # 99
    ContinueDebugEvent : SvcName # 100
    GetProcessList : SvcName # 101
    GetThreadList : SvcName # 102
    GetDebugThreadContext : SvcName # 103
    SetDebugThreadContext : SvcName # 104
    QueryDebugProcessMemory : SvcName # 105
    ReadDebugProcessMemory : SvcName # 106
    WriteDebugProcessMemory : SvcName # 107
    SetHardwareBreakPoint : SvcName # 108
    GetDebugThreadParam : SvcName # 109
    Reserved11 : SvcName # 110
    GetSystemInfo : SvcName # 111
    CreatePort : SvcName # 112
    ManageNamedPort : SvcName # 113
    ConnectToPort : SvcName # 114
    SetProcessMemoryPermission : SvcName # 115
    MapProcessMemory : SvcName # 116
    UnmapProcessMemory : SvcName # 117
    QueryProcessMemory : SvcName # 118
    MapProcessCodeMemory : SvcName # 119
    UnmapProcessCodeMemory : SvcName # 120
    CreateProcess : SvcName # 121
    StartProcess : SvcName # 122
    TerminateProcess : SvcName # 123
    GetProcessInfo : SvcName # 124
    CreateResourceLimit : SvcName # 125
    SetResourceLimitLimitValue : SvcName # 126
    CallSecureMonitor : SvcName # 127

