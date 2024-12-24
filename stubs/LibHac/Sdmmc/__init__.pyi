import typing, abc
from LibHac import Result

class BusWidth(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Width1Bit : BusWidth # 0
    Width4Bit : BusWidth # 1
    Width8Bit : BusWidth # 2


class Port(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Mmc0 : Port # 0
    SdCard0 : Port # 1
    GcAsic0 : Port # 2


class ResultSdmmc(abc.ABC):
    ModuleSdmmc : int
    @classmethod
    @property
    def AbortCommandIssued(cls) -> Result.Base: ...
    @classmethod
    @property
    def AbortTransactionSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def AutoCommandResponseCrcError(cls) -> Result.Base: ...
    @classmethod
    @property
    def AutoCommandResponseEndBitError(cls) -> Result.Base: ...
    @classmethod
    @property
    def AutoCommandResponseIndexError(cls) -> Result.Base: ...
    @classmethod
    @property
    def AutoCommandResponseTimeoutError(cls) -> Result.Base: ...
    @classmethod
    @property
    def BusySoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def CommandCompleteSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def CommandInhibitCmdSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def CommandInhibitDatSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def CommunicationError(cls) -> Result.Base: ...
    @classmethod
    @property
    def CommunicationNotAttained(cls) -> Result.Base: ...
    @classmethod
    @property
    def DataCrcError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DataEndBitError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DataTimeoutError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceRemoved(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusAddressMisaligned(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusAddressOutOfRange(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusBlockLenError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusCcError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusCidCsdOverwrite(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusComCrcError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusDeviceEccFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusEraseParam(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusEraseReset(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusEraseSeqError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusHasError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusIllegalCommand(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusLockUnlockFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusSwitchError(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusWpEraseSkip(cls) -> Result.Base: ...
    @classmethod
    @property
    def DeviceStatusWpViolation(cls) -> Result.Base: ...
    @classmethod
    @property
    def DriveStrengthCalibrationNotCompleted(cls) -> Result.Base: ...
    @classmethod
    @property
    def DriveStrengthCalibrationSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def HostControllerUnexpected(cls) -> Result.Base: ...
    @classmethod
    @property
    def InternalClockStableSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def InternalError(cls) -> Result.Base: ...
    @classmethod
    @property
    def IssueTuningCommandSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def MmcEraseSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def MmcInitializationSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def MmcNotSupportExtendedCsd(cls) -> Result.Base: ...
    @classmethod
    @property
    def NoDevice(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotActivated(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotAwakened(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotImplemented(cls) -> Result.Base: ...
    @classmethod
    @property
    def NotSupported(cls) -> Result.Base: ...
    @classmethod
    @property
    def NoWaitedInterrupt(cls) -> Result.Base: ...
    @classmethod
    @property
    def ResponseCrcError(cls) -> Result.Base: ...
    @classmethod
    @property
    def ResponseEndBitError(cls) -> Result.Base: ...
    @classmethod
    @property
    def ResponseIndexError(cls) -> Result.Base: ...
    @classmethod
    @property
    def ResponseTimeoutError(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardCannotSwitchAccessMode(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardFailedSwitchAccessMode(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardGetValidRcaSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardInitializationSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardNot4BitBusWidthAtUhsIMode(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardNotCompleteVoltageSwitch(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardNotReadyToVoltageSwitch(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardNotSupportAccessMode(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardNotSupportSdr104AndSdr50(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardNotSupportSwitchFunctionStatus(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardUnacceptableCurrentConsumption(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdCardValidationError(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdHostStandardFailSwitchTo18V(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdHostStandardUnknownAutoCmdError(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdHostStandardUnknownError(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdmmcCompOpen(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdmmcCompShortToGnd(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdmmcDllApplicationSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def SdmmcDllCalibrationSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def TransferCompleteSoftwareTimeout(cls) -> Result.Base: ...
    @classmethod
    @property
    def TuningFailed(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnexpectedDeviceCsdValue(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnexpectedDeviceState(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnexpectedMmcExtendedCsdValue(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnexpectedSdCardAcmdDisabled(cls) -> Result.Base: ...
    @classmethod
    @property
    def UnexpectedSdCardSwitchFunctionStatus(cls) -> Result.Base: ...
    @classmethod
    @property
    def WaitInterruptSoftwareTimeout(cls) -> Result.Base: ...


class SpeedMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MmcIdentification : SpeedMode # 0
    MmcLegacySpeed : SpeedMode # 1
    MmcHighSpeed : SpeedMode # 2
    MmcHs200 : SpeedMode # 3
    MmcHs400 : SpeedMode # 4
    SdCardIdentification : SpeedMode # 5
    SdCardDefaultSpeed : SpeedMode # 6
    SdCardHighSpeed : SpeedMode # 7
    SdCardSdr12 : SpeedMode # 8
    SdCardSdr25 : SpeedMode # 9
    SdCardSdr50 : SpeedMode # 10
    SdCardSdr104 : SpeedMode # 11
    SdCardDdr50 : SpeedMode # 12
    GcAsicFpgaSpeed : SpeedMode # 13
    GcAsicSpeed : SpeedMode # 14

