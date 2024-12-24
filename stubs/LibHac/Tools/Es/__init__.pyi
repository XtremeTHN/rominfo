import typing
from System.IO import BinaryReader, Stream
from System import Array_1
from LibHac.Common.Keys import KeySet

class LicenseType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Permanent : LicenseType # 0
    Demo : LicenseType # 1
    Trial : LicenseType # 2
    Rental : LicenseType # 3
    Subscription : LicenseType # 4
    Service : LicenseType # 5


class PropertyFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    PreInstall : PropertyFlags # 1
    SharedTitle : PropertyFlags # 2
    AllowAllContent : PropertyFlags # 4


class Ticket:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, reader: BinaryReader) -> None: ...
    @typing.overload
    def __init__(self, stream: Stream) -> None: ...
    @property
    def AccountId(self) -> int: ...
    @AccountId.setter
    def AccountId(self, value: int) -> int: ...
    @property
    def CryptoType(self) -> int: ...
    @CryptoType.setter
    def CryptoType(self, value: int) -> int: ...
    @property
    def DeviceId(self) -> int: ...
    @DeviceId.setter
    def DeviceId(self, value: int) -> int: ...
    @property
    def File(self) -> Array_1[int]: ...
    @property
    def FormatVersion(self) -> int: ...
    @FormatVersion.setter
    def FormatVersion(self, value: int) -> int: ...
    @property
    def Issuer(self) -> str: ...
    @Issuer.setter
    def Issuer(self, value: str) -> str: ...
    @property
    def LicenseType(self) -> LicenseType: ...
    @LicenseType.setter
    def LicenseType(self, value: LicenseType) -> LicenseType: ...
    @property
    def PropertyMask(self) -> PropertyFlags: ...
    @PropertyMask.setter
    def PropertyMask(self, value: PropertyFlags) -> PropertyFlags: ...
    @property
    def RightsId(self) -> Array_1[int]: ...
    @RightsId.setter
    def RightsId(self, value: Array_1[int]) -> Array_1[int]: ...
    @property
    def SectEntrySize(self) -> int: ...
    @SectEntrySize.setter
    def SectEntrySize(self, value: int) -> int: ...
    @property
    def SectHeaderOffset(self) -> int: ...
    @SectHeaderOffset.setter
    def SectHeaderOffset(self, value: int) -> int: ...
    @property
    def SectNum(self) -> int: ...
    @SectNum.setter
    def SectNum(self, value: int) -> int: ...
    @property
    def SectTotalSize(self) -> int: ...
    @SectTotalSize.setter
    def SectTotalSize(self, value: int) -> int: ...
    @property
    def Signature(self) -> Array_1[int]: ...
    @Signature.setter
    def Signature(self, value: Array_1[int]) -> Array_1[int]: ...
    @property
    def SignatureType(self) -> TicketSigType: ...
    @SignatureType.setter
    def SignatureType(self, value: TicketSigType) -> TicketSigType: ...
    @property
    def TicketId(self) -> int: ...
    @TicketId.setter
    def TicketId(self, value: int) -> int: ...
    @property
    def TicketVersion(self) -> int: ...
    @TicketVersion.setter
    def TicketVersion(self, value: int) -> int: ...
    @property
    def TitleKeyBlock(self) -> Array_1[int]: ...
    @TitleKeyBlock.setter
    def TitleKeyBlock(self, value: Array_1[int]) -> Array_1[int]: ...
    @property
    def TitleKeyType(self) -> TitleKeyType: ...
    @TitleKeyType.setter
    def TitleKeyType(self, value: TitleKeyType) -> TitleKeyType: ...
    def GetBytes(self) -> Array_1[int]: ...
    def GetTitleKey(self, keySet: KeySet) -> Array_1[int]: ...


class TicketSigType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Rsa4096Sha1 : TicketSigType # 65536
    Rsa2048Sha1 : TicketSigType # 65537
    EcdsaSha1 : TicketSigType # 65538
    Rsa4096Sha256 : TicketSigType # 65539
    Rsa2048Sha256 : TicketSigType # 65540
    EcdsaSha256 : TicketSigType # 65541


class TitleKeyType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Common : TitleKeyType # 0
    Personalized : TitleKeyType # 1
