import typing, clr, abc
from LibHac.Crypto import AesKey, AesXtsKey, RsaKey, RsaFullKey
from LibHac.Common.FixedArrays import Array32_1, Array3_1, Array4_1, Array2_1, Array16_1, Array12_1
from LibHac.Boot import EncryptedKeyBlob, KeyBlob
from System.IO import Stream
from System.Collections.Generic import List_1
from LibHac.Common import IProgressReport, LibHacException
from System.Text import StringBuilder
from System import ReadOnlySpan_1, MulticastDelegate, IAsyncResult, AsyncCallback, Span_1, Exception
from System.Reflection import MethodInfo, MethodBase
from System.Security.Cryptography import RSAParameters
from LibHac.FsSrv import ExternalKeySet
from System.Collections import IDictionary

class AllKeys:
    DerivedKeysDev : DerivedKeys
    DerivedKeysProd : DerivedKeys
    DeviceKeys : DeviceKeys
    KeySeeds : KeySeeds
    RootKeysDev : RootKeys
    RootKeysProd : RootKeys
    RsaKeys : RsaKeys
    RsaSigningKeysDev : RsaSigningKeys
    RsaSigningKeysProd : RsaSigningKeys
    StoredKeysDev : StoredKeys
    StoredKeysProd : StoredKeys


class DerivedKeys:
    ETicketRsaKek : AesKey
    HeaderKey : AesXtsKey
    KeyAreaKeys : Array32_1[Array3_1[AesKey]]
    MasterKeks : Array32_1[AesKey]
    MasterKeys : Array32_1[AesKey]
    Package1Keys : Array32_1[AesKey]
    Package1MacKeys : Array32_1[AesKey]
    Package2Keys : Array32_1[AesKey]
    SslRsaKek : AesKey
    TitleKeks : Array32_1[AesKey]


class DeviceKeys:
    BisKeys : Array4_1[AesXtsKey]
    DeviceKey : AesKey
    DeviceUniqueSaveMacKeys : Array2_1[AesKey]
    EncryptedKeyBlobs : Array32_1[EncryptedKeyBlob]
    KeyBlobKeys : Array32_1[AesKey]
    KeyBlobMacKeys : Array32_1[AesKey]
    SdCardEncryptionKeys : Array3_1[AesXtsKey]
    SdCardEncryptionSeed : AesKey
    SecureBootKey : AesKey
    SeedUniqueSaveMacKey : AesKey
    TsecKey : AesKey


class ExternalKeyReader(abc.ABC):
    @staticmethod
    def ReadMainKeys(keySet: KeySet, reader: Stream, keyList: List_1[KeyInfo], logger: IProgressReport = ...) -> None: ...
    @staticmethod
    def ReadTitleKeys(keySet: KeySet, reader: Stream, logger: IProgressReport = ...) -> None: ...
    # Skipped ReadKeyFile due to it being static, abstract and generic.

    ReadKeyFile : ReadKeyFile_MethodGroup
    class ReadKeyFile_MethodGroup:
        @typing.overload
        def __call__(self, filename: str, titleKeysFilename: str = ..., consoleKeysFilename: str = ..., logger: IProgressReport = ..., mode: KeySet.Mode = ...) -> KeySet:...
        @typing.overload
        def __call__(self, keySet: KeySet, filename: str, titleKeysFilename: str = ..., consoleKeysFilename: str = ..., logger: IProgressReport = ...) -> None:...
        @typing.overload
        def __call__(self, keySet: KeySet, prodKeysFilename: str = ..., devKeysFilename: str = ..., titleKeysFilename: str = ..., consoleKeysFilename: str = ..., logger: IProgressReport = ...) -> None:...



class ExternalKeyWriter(abc.ABC):
    @staticmethod
    def PrintAllKeys(keySet: KeySet) -> str: ...
    @staticmethod
    def PrintAllSeeds(keySet: KeySet) -> str: ...
    @staticmethod
    def PrintCommonKeys(keySet: KeySet) -> str: ...
    @staticmethod
    def PrintCommonKeysWithDev(keySet: KeySet) -> str: ...
    @staticmethod
    def PrintDeviceKeys(keySet: KeySet) -> str: ...
    @staticmethod
    def PrintKeys(keySet: KeySet, sb: StringBuilder, keys: List_1[KeyInfo], filter: KeyInfo.KeyType, isDev: bool) -> None: ...
    @staticmethod
    def PrintTitleKeys(keySet: KeySet) -> str: ...


class KeyInfo:
    @typing.overload
    def __init__(self, group: int, type: KeyInfo.KeyType, name: str, rangeStart: int, rangeEnd: int, retrieveFunc: KeyInfo.KeyGetter) -> None: ...
    @typing.overload
    def __init__(self, group: int, type: KeyInfo.KeyType, name: str, retrieveFunc: KeyInfo.KeyGetter) -> None: ...
    Getter : KeyInfo.KeyGetter
    Group : int
    Name : str
    RangeEnd : int
    RangeStart : int
    RangeType : KeyInfo.KeyRangeType
    Type : KeyInfo.KeyType
    @property
    def NameLength(self) -> int: ...
    def Matches(self, keyName: ReadOnlySpan_1[str], keyIndex: clr.Reference[int], isDev: clr.Reference[bool]) -> bool: ...

    class KeyGetter(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, keySet: KeySet, i: int, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> Span_1[int]: ...
        def Invoke(self, keySet: KeySet, i: int) -> Span_1[int]: ...


    class KeyRangeType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Single : KeyInfo.KeyRangeType # 0
        Range : KeyInfo.KeyRangeType # 1


    class KeyType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Common : KeyInfo.KeyType # 1
        Device : KeyInfo.KeyType # 2
        Root : KeyInfo.KeyType # 4
        CommonRoot : KeyInfo.KeyType # 5
        DeviceRoot : KeyInfo.KeyType # 6
        Seed : KeyInfo.KeyType # 8
        CommonSeed : KeyInfo.KeyType # 9
        Derived : KeyInfo.KeyType # 16
        CommonDrvd : KeyInfo.KeyType # 17
        DeviceDrvd : KeyInfo.KeyType # 18
        DifferentDev : KeyInfo.KeyType # 32
        CommonSeedDiff : KeyInfo.KeyType # 41



class KeySeeds:
    AesKekGenerationSource : AesKey
    AesKeyGenerationSource : AesKey
    BisKekSource : AesKey
    BisKeySources : Array4_1[AesXtsKey]
    DeviceUniqueSaveMacKekSource : AesKey
    DeviceUniqueSaveMacKeySources : Array2_1[AesKey]
    HeaderKekSource : AesKey
    HeaderKeySource : AesXtsKey
    KeyAreaKeyApplicationSource : AesKey
    KeyAreaKeyOceanSource : AesKey
    KeyAreaKeySystemSource : AesKey
    KeyBlobKeySources : Array32_1[AesKey]
    KeyBlobMacKeySource : AesKey
    MarikoMasterKekSources : Array32_1[AesKey]
    MarikoMasterKekSourcesDev : Array32_1[AesKey]
    MasterKekSources : Array32_1[AesKey]
    MasterKeySource : AesKey
    Package2KeySource : AesKey
    PerConsoleKeySource : AesKey
    RetailSpecificAesKeySource : AesKey
    SdCardKekSource : AesKey
    SdCardKeySources : Array3_1[AesXtsKey]
    SeedUniqueSaveMacKekSource : AesKey
    SeedUniqueSaveMacKeySource : AesKey
    TitleKekSource : AesKey


class KeySet:
    def __init__(self) -> None: ...
    @property
    def AcidSigningKeyParams(self) -> Span_1[RSAParameters]: ...
    @property
    def AcidSigningKeys(self) -> Span_1[RsaKey]: ...
    @property
    def AesKekGenerationSource(self) -> clr.Reference[AesKey]: ...
    @property
    def AesKeyGenerationSource(self) -> clr.Reference[AesKey]: ...
    @property
    def BetaNca0KeyAreaKey(self) -> clr.Reference[RsaFullKey]: ...
    @property
    def BetaNca0KeyAreaKeyParams(self) -> clr.Reference[RSAParameters]: ...
    @property
    def BisKekSource(self) -> clr.Reference[AesKey]: ...
    @property
    def BisKeys(self) -> Span_1[AesXtsKey]: ...
    @property
    def BisKeySources(self) -> Span_1[AesXtsKey]: ...
    @property
    def CurrentMode(self) -> KeySet.Mode: ...
    @property
    def DeviceKey(self) -> clr.Reference[AesKey]: ...
    @property
    def DeviceUniqueSaveMacKekSource(self) -> clr.Reference[AesKey]: ...
    @property
    def DeviceUniqueSaveMacKeys(self) -> Span_1[AesKey]: ...
    @property
    def DeviceUniqueSaveMacKeySources(self) -> Span_1[AesKey]: ...
    @property
    def EncryptedKeyBlobs(self) -> Span_1[EncryptedKeyBlob]: ...
    @property
    def ETicketExtKeyRsa(self) -> RSAParameters: ...
    @ETicketExtKeyRsa.setter
    def ETicketExtKeyRsa(self, value: RSAParameters) -> RSAParameters: ...
    @property
    def ETicketRsaKek(self) -> clr.Reference[AesKey]: ...
    @property
    def ExternalKeySet(self) -> ExternalKeySet: ...
    @property
    def GcTitleKeyKeks(self) -> Span_1[AesKey]: ...
    @property
    def HeaderKekSource(self) -> clr.Reference[AesKey]: ...
    @property
    def HeaderKey(self) -> clr.Reference[AesXtsKey]: ...
    @property
    def HeaderKeySource(self) -> clr.Reference[AesXtsKey]: ...
    @property
    def KeyAreaKeyApplicationSource(self) -> clr.Reference[AesKey]: ...
    @property
    def KeyAreaKeyOceanSource(self) -> clr.Reference[AesKey]: ...
    @property
    def KeyAreaKeys(self) -> Span_1[Array3_1[AesKey]]: ...
    @property
    def KeyAreaKeySystemSource(self) -> clr.Reference[AesKey]: ...
    @property
    def KeyBlobKeys(self) -> Span_1[AesKey]: ...
    @property
    def KeyBlobKeySources(self) -> Span_1[AesKey]: ...
    @property
    def KeyBlobMacKeys(self) -> Span_1[AesKey]: ...
    @property
    def KeyBlobMacKeySource(self) -> clr.Reference[AesKey]: ...
    @property
    def KeyBlobs(self) -> Span_1[KeyBlob]: ...
    @property
    def KeyStruct(self) -> clr.Reference[AllKeys]: ...
    @property
    def MarikoAesClassKeys(self) -> Span_1[AesKey]: ...
    @property
    def MarikoBek(self) -> clr.Reference[AesKey]: ...
    @property
    def MarikoKek(self) -> clr.Reference[AesKey]: ...
    @property
    def MarikoMasterKekSources(self) -> Span_1[AesKey]: ...
    @property
    def MasterKeks(self) -> Span_1[AesKey]: ...
    @property
    def MasterKekSources(self) -> Span_1[AesKey]: ...
    @property
    def MasterKeys(self) -> Span_1[AesKey]: ...
    @property
    def MasterKeySource(self) -> clr.Reference[AesKey]: ...
    @property
    def NcaHeaderSigningKeyParams(self) -> Span_1[RSAParameters]: ...
    @property
    def NcaHeaderSigningKeys(self) -> Span_1[RsaKey]: ...
    @property
    def Package1Kek(self) -> clr.Reference[AesKey]: ...
    @property
    def Package1Keys(self) -> Span_1[AesKey]: ...
    @property
    def Package1MacKek(self) -> clr.Reference[AesKey]: ...
    @property
    def Package1MacKeys(self) -> Span_1[AesKey]: ...
    @property
    def Package2Keys(self) -> Span_1[AesKey]: ...
    @property
    def Package2KeySource(self) -> clr.Reference[AesKey]: ...
    @property
    def Package2SigningKey(self) -> clr.Reference[RsaKey]: ...
    @property
    def Package2SigningKeyParams(self) -> clr.Reference[RSAParameters]: ...
    @property
    def PerConsoleKeySource(self) -> clr.Reference[AesKey]: ...
    @property
    def RetailSpecificAesKeySource(self) -> clr.Reference[AesKey]: ...
    @property
    def SdCardEncryptionKeys(self) -> Span_1[AesXtsKey]: ...
    @property
    def SdCardEncryptionSeed(self) -> clr.Reference[AesKey]: ...
    @property
    def SdCardKekSource(self) -> clr.Reference[AesKey]: ...
    @property
    def SdCardKeySources(self) -> Span_1[AesXtsKey]: ...
    @property
    def SecureBootKey(self) -> clr.Reference[AesKey]: ...
    @property
    def SeedUniqueSaveMacKekSource(self) -> clr.Reference[AesKey]: ...
    @property
    def SeedUniqueSaveMacKey(self) -> clr.Reference[AesKey]: ...
    @property
    def SeedUniqueSaveMacKeySource(self) -> clr.Reference[AesKey]: ...
    @property
    def SslRsaKek(self) -> clr.Reference[AesKey]: ...
    @property
    def TitleKeks(self) -> Span_1[AesKey]: ...
    @property
    def TitleKekSource(self) -> clr.Reference[AesKey]: ...
    @property
    def TsecAuthSignatures(self) -> Span_1[AesKey]: ...
    @property
    def TsecKey(self) -> clr.Reference[AesKey]: ...
    @property
    def TsecRootKek(self) -> clr.Reference[AesKey]: ...
    @property
    def TsecRootKeys(self) -> Span_1[AesKey]: ...
    @property
    def XciHeaderKey(self) -> clr.Reference[AesKey]: ...
    @staticmethod
    def CreateDefaultKeySet() -> KeySet: ...
    @staticmethod
    def CreateKeyInfoList() -> List_1[KeyInfo]: ...
    def DeriveKeys(self, logger: IProgressReport = ...) -> None: ...
    def DeriveSdCardKeys(self) -> None: ...
    def SetMode(self, mode: KeySet.Mode) -> None: ...
    def SetSdSeed(self, sdSeed: ReadOnlySpan_1[int]) -> None: ...

    class Mode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Dev : KeySet.Mode # 0
        Prod : KeySet.Mode # 1



class KeyType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : KeyType # 0
    Common : KeyType # 1
    Unique : KeyType # 2
    Title : KeyType # 3


class MissingKeyException(LibHacException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, name: str, keyType: KeyType) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def Type(self) -> KeyType: ...


class RootKeys:
    GcTitleKeyKeks : Array16_1[AesKey]
    KeyBlobs : Array32_1[KeyBlob]
    MarikoAesClassKeys : Array12_1[AesKey]
    MarikoBek : AesKey
    MarikoKek : AesKey
    Package1Kek : AesKey
    Package1MacKek : AesKey
    TsecAuthSignatures : Array32_1[AesKey]
    TsecRootKek : AesKey
    TsecRootKeys : Array32_1[AesKey]


class RsaKeys:
    BetaNca0KeyAreaKey : RsaFullKey


class RsaSigningKeys:
    AcidSigningKeys : Array2_1[RsaKey]
    NcaHeaderSigningKeys : Array2_1[RsaKey]
    Package2SigningKey : RsaKey


class StoredKeys:
    XciHeaderKey : AesKey

