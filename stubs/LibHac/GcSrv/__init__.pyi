import typing, abc
from System import ReadOnlySpan_1

class GameCardManagerOperationIdValue(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Finalize : GameCardManagerOperationIdValue # 1
    GetHandle : GameCardManagerOperationIdValue # 2
    IsGameCardActivationValid : GameCardManagerOperationIdValue # 3
    GetInitializationResult : GameCardManagerOperationIdValue # 4
    GetGameCardErrorInfo : GameCardManagerOperationIdValue # 5
    GetGameCardErrorReportInfo : GameCardManagerOperationIdValue # 6
    SetVerifyEnableFlag : GameCardManagerOperationIdValue # 7
    GetGameCardAsicInfo : GameCardManagerOperationIdValue # 8
    GetGameCardDeviceIdForProdCard : GameCardManagerOperationIdValue # 9
    EraseAndWriteParamDirectly : GameCardManagerOperationIdValue # 10
    ReadParamDirectly : GameCardManagerOperationIdValue # 11
    WriteToGameCardDirectly : GameCardManagerOperationIdValue # 12
    ForceErase : GameCardManagerOperationIdValue # 13
    SimulateDetectionEventSignaled : GameCardManagerOperationIdValue # 14


class GameCardOperationIdValue(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    EraseGameCard : GameCardOperationIdValue # 1
    GetGameCardIdSet : GameCardOperationIdValue # 2
    GetGameCardDeviceId : GameCardOperationIdValue # 3
    GetGameCardImageHash : GameCardOperationIdValue # 4
    GetGameCardDeviceCertificate : GameCardOperationIdValue # 5
    ChallengeCardExistence : GameCardOperationIdValue # 6
    GetGameCardStatus : GameCardOperationIdValue # 7


class IGameCardKeyManager(typing.Protocol):
    @abc.abstractmethod
    def PresetInternalKeys(self, gameCardKey: ReadOnlySpan_1[int], gameCardCertificate: ReadOnlySpan_1[int]) -> None: ...


class OpenGameCardAttribute(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ReadOnly : OpenGameCardAttribute # 0
    SecureReadOnly : OpenGameCardAttribute # 1
    WriteOnly : OpenGameCardAttribute # 2

