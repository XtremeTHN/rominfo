import typing
from LibHac.Common.FixedArrays import Array256_1, Array48_1, Array464_1, Array32_1, Array16_1, Array8_1, Array4_1, Array2_1, Array56_1, Array452_1, Array12_1, Array7_1, Array512_1, Array192_1

class AccessControl1ClockRate(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ClockRate50MHz : AccessControl1ClockRate # 10551312
    ClockRate25MHz : AccessControl1ClockRate # 10551313


class Ca10Certificate:
    Modulus : Array256_1[int]
    Signature : Array256_1[int]
    Unk100 : Array48_1[int]
    Unk230 : Array464_1[int]


class CardHeader:
    BackupAreaStartPage : int
    EncryptedData : CardHeaderEncryptedData
    Flags : int
    InitialDataHash : Array32_1[int]
    Iv : Array16_1[int]
    KeyIndex : int
    LimAreaPage : int
    Magic : int
    PackageId : Array8_1[int]
    PartitionFsHeaderAddress : int
    PartitionFsHeaderHash : Array32_1[int]
    PartitionFsHeaderSize : int
    Reserved11C : Array4_1[int]
    RomAreaStartPage : int
    RomSize : int
    SelKey : int
    SelSec : int
    SelT1Key : int
    ValidDataEndPage : int
    Version : int
    @classmethod
    @property
    def HeaderMagic(cls) -> int: ...


class CardHeaderEncryptedData:
    AccCtrl1 : int
    CompatibilityType : int
    CupId : int
    CupVersion : int
    FwMode : int
    FwVersion : Array2_1[int]
    Reserved25 : int
    Reserved26 : int
    Reserved27 : int
    Reserved38 : Array56_1[int]
    UppHash : Array8_1[int]
    Wait1TimeRead : int
    Wait1TimeWrite : int
    Wait2TimeRead : int
    Wait2TimeWrite : int


class CardHeaderWithSignature:
    Data : CardHeader
    Signature : Array256_1[int]


class CardId1:
    MakerCode : int
    MemoryCapacity : MemoryCapacity
    MemoryType : int
    Reserved : int


class CardId2:
    CardSecurityNumber : int
    CardType : int
    Reserved : Array2_1[int]


class CardId3:
    Reserved : Array4_1[int]


class CardInitialData:
    Padding : Array452_1[int]
    Payload : CardInitialDataPayload


class CardInitialDataPayload:
    AuthData : Array16_1[int]
    AuthMac : Array16_1[int]
    AuthNonce : Array12_1[int]
    PackageId : Array8_1[int]
    Reserved : Array8_1[int]


class FwVersion(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ForDev : FwVersion # 0
    Since1_0_0 : FwVersion # 1
    Since4_0_0 : FwVersion # 2
    Since9_0_0 : FwVersion # 3
    Since11_0_0 : FwVersion # 4
    Since12_0_0 : FwVersion # 5


class KekIndex(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Version0 : KekIndex # 0
    ForDev : KekIndex # 1


class MemoryCapacity(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Capacity8GB : MemoryCapacity # 224
    Capacity16GB : MemoryCapacity # 225
    Capacity32GB : MemoryCapacity # 226
    Capacity4GB : MemoryCapacity # 240
    Capacity2GB : MemoryCapacity # 248
    Capacity1GB : MemoryCapacity # 250


class SelSec(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    T1 : SelSec # 1
    T2 : SelSec # 2


class T1CardCertificate:
    Flags : Array7_1[int]
    HwKey : Array16_1[int]
    Iv : Array16_1[int]
    KekIndex : int
    Magic : int
    Padding : Array512_1[int]
    Reserved : Array192_1[int]
    Signature : Array256_1[int]
    T1CardDeviceId : Array16_1[int]
    Version : int
    @classmethod
    @property
    def CertMagic(cls) -> int: ...

