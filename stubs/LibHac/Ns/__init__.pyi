import typing
from LibHac.Common.FixedArrays import Array8_1, Array65_1, Array16_1, Array37_1, Array32_1, Array2_1, Array4_1, Array3000_1, Array6_1, Array512_1, Array256_1
from LibHac.Common import U8Span

class ApplicationControlProperty:
    AccessibleLaunchRequiredVersion : ApplicationControlProperty.AccessibleLaunchRequiredVersionValue
    AddOnContentBaseId : int
    AddOnContentRegistrationType : ApplicationControlProperty.AddOnContentRegistrationTypeValue
    ApplicationErrorCodeCategory : Array8_1[int]
    AttributeFlag : ApplicationControlProperty.AttributeFlagValue
    BcatDeliveryCacheStorageSize : int
    BcatPassphrase : Array65_1[int]
    CacheStorageDataAndJournalSizeMax : int
    CacheStorageIndexMax : int
    CacheStorageJournalSize : int
    CacheStorageSize : int
    ContentsAvailabilityTransitionPolicy : int
    CrashReport : ApplicationControlProperty.CrashReportValue
    CrashScreenshotForDev : ApplicationControlProperty.CrashScreenshotForDevValue
    CrashScreenshotForProd : ApplicationControlProperty.CrashScreenshotForProdValue
    DataLossConfirmation : ApplicationControlProperty.DataLossConfirmationValue
    DeviceSaveDataJournalSize : int
    DeviceSaveDataJournalSizeMax : int
    DeviceSaveDataSize : int
    DeviceSaveDataSizeMax : int
    DisplayVersion : Array16_1[int]
    Hdcp : ApplicationControlProperty.HdcpValue
    Isbn : Array37_1[int]
    JitConfiguration : ApplicationControlProperty.ApplicationJitConfiguration
    LocalCommunicationId : Array8_1[int]
    LogoHandling : ApplicationControlProperty.LogoHandlingValue
    LogoType : ApplicationControlProperty.LogoTypeValue
    NeighborDetectionClientConfiguration : ApplicationControlProperty.ApplicationNeighborDetectionClientConfiguration
    ParentalControlFlag : ApplicationControlProperty.ParentalControlFlagValue
    PlayLogPolicy : ApplicationControlProperty.PlayLogPolicyValue
    PlayLogQueryableApplicationId : Array16_1[int]
    PlayLogQueryCapability : ApplicationControlProperty.PlayLogQueryCapabilityValue
    PlayReportPermission : ApplicationControlProperty.PlayReportPermissionValue
    PresenceGroupId : int
    ProgramIndex : int
    RatingAge : Array32_1[int]
    RepairFlag : ApplicationControlProperty.RepairFlagValue
    RequiredAddOnContentsSetBinaryDescriptors : ApplicationControlProperty.RequiredAddOnContentsSetBinaryDescriptor
    RequiredNetworkServiceLicenseOnLaunchFlag : ApplicationControlProperty.RequiredNetworkServiceLicenseOnLaunchValue
    Reserved30F4 : Array2_1[int]
    Reserved318A : int
    Reserved3214 : Array4_1[int]
    Reserved3404 : Array4_1[int]
    Reserved3448 : Array3000_1[int]
    ReservedForUserAccountSaveDataOperation : Array6_1[int]
    RuntimeAddOnContentInstall : ApplicationControlProperty.RuntimeAddOnContentInstallValue
    RuntimeParameterDelivery : ApplicationControlProperty.RuntimeParameterDeliveryValue
    RuntimeUpgrade : int
    SaveDataOwnerId : int
    Screenshot : ApplicationControlProperty.ScreenshotValue
    SeedForPseudoDeviceId : int
    StartupUserAccount : ApplicationControlProperty.StartupUserAccountValue
    StartupUserAccountOption : ApplicationControlProperty.StartupUserAccountOptionFlagValue
    SupportedLanguageFlag : int
    SupportingLimitedLicenses : int
    TemporaryStorageSize : int
    Title : Array16_1[ApplicationControlProperty.ApplicationTitle]
    UserAccountSaveDataJournalSize : int
    UserAccountSaveDataJournalSizeMax : int
    UserAccountSaveDataSize : int
    UserAccountSaveDataSizeMax : int
    UserAccountSwitchLock : ApplicationControlProperty.UserAccountSwitchLockValue
    VideoCapture : ApplicationControlProperty.VideoCaptureValue
    @property
    def ApplicationErrorCodeCategoryString(self) -> U8Span: ...
    @property
    def BcatPassphraseString(self) -> U8Span: ...
    @property
    def DisplayVersionString(self) -> U8Span: ...
    @property
    def IsbnString(self) -> U8Span: ...

    class AccessibleLaunchRequiredVersionValue:
        ApplicationId : Array8_1[int]


    class AddOnContentRegistrationTypeValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        AllOnLaunch : ApplicationControlProperty.AddOnContentRegistrationTypeValue # 0
        OnDemand : ApplicationControlProperty.AddOnContentRegistrationTypeValue # 1


    class ApplicationJitConfiguration:
        Flags : ApplicationControlProperty.JitConfigurationFlag
        MemorySize : int


    class ApplicationNeighborDetectionClientConfiguration:
        ReceivableGroupConfigurations : Array16_1[ApplicationControlProperty.ApplicationNeighborDetectionGroupConfiguration]
        SendGroupConfiguration : ApplicationControlProperty.ApplicationNeighborDetectionGroupConfiguration


    class ApplicationNeighborDetectionGroupConfiguration:
        GroupId : int
        Key : Array16_1[int]


    class ApplicationTitle:
        Name : Array512_1[int]
        Publisher : Array256_1[int]
        @property
        def NameString(self) -> U8Span: ...
        @property
        def PublisherString(self) -> U8Span: ...


    class AttributeFlagValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.AttributeFlagValue # 0
        Demo : ApplicationControlProperty.AttributeFlagValue # 1
        RetailInteractiveDisplay : ApplicationControlProperty.AttributeFlagValue # 2


    class CrashReportValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Deny : ApplicationControlProperty.CrashReportValue # 0
        Allow : ApplicationControlProperty.CrashReportValue # 1


    class CrashScreenshotForDevValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Deny : ApplicationControlProperty.CrashScreenshotForDevValue # 0
        Allow : ApplicationControlProperty.CrashScreenshotForDevValue # 1


    class CrashScreenshotForProdValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Deny : ApplicationControlProperty.CrashScreenshotForProdValue # 0
        Allow : ApplicationControlProperty.CrashScreenshotForProdValue # 1


    class DataLossConfirmationValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.DataLossConfirmationValue # 0
        Required : ApplicationControlProperty.DataLossConfirmationValue # 1


    class HdcpValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.HdcpValue # 0
        Required : ApplicationControlProperty.HdcpValue # 1


    class JitConfigurationFlag(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.JitConfigurationFlag # 0
        Enabled : ApplicationControlProperty.JitConfigurationFlag # 1


    class Language(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        AmericanEnglish : ApplicationControlProperty.Language # 0
        BritishEnglish : ApplicationControlProperty.Language # 1
        Japanese : ApplicationControlProperty.Language # 2
        French : ApplicationControlProperty.Language # 3
        German : ApplicationControlProperty.Language # 4
        LatinAmericanSpanish : ApplicationControlProperty.Language # 5
        Spanish : ApplicationControlProperty.Language # 6
        Italian : ApplicationControlProperty.Language # 7
        Dutch : ApplicationControlProperty.Language # 8
        CanadianFrench : ApplicationControlProperty.Language # 9
        Portuguese : ApplicationControlProperty.Language # 10
        Russian : ApplicationControlProperty.Language # 11
        Korean : ApplicationControlProperty.Language # 12
        TraditionalChinese : ApplicationControlProperty.Language # 13
        SimplifiedChinese : ApplicationControlProperty.Language # 14
        BrazilianPortuguese : ApplicationControlProperty.Language # 15


    class LogoHandlingValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Auto : ApplicationControlProperty.LogoHandlingValue # 0
        Manual : ApplicationControlProperty.LogoHandlingValue # 1


    class LogoTypeValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        LicensedByNintendo : ApplicationControlProperty.LogoTypeValue # 0
        DistributedByNintendo : ApplicationControlProperty.LogoTypeValue # 1
        Nintendo : ApplicationControlProperty.LogoTypeValue # 2


    class Organization(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        CERO : ApplicationControlProperty.Organization # 0
        GRACGCRB : ApplicationControlProperty.Organization # 1
        GSRMR : ApplicationControlProperty.Organization # 2
        ESRB : ApplicationControlProperty.Organization # 3
        ClassInd : ApplicationControlProperty.Organization # 4
        USK : ApplicationControlProperty.Organization # 5
        PEGI : ApplicationControlProperty.Organization # 6
        PEGIPortugal : ApplicationControlProperty.Organization # 7
        PEGIBBFC : ApplicationControlProperty.Organization # 8
        Russian : ApplicationControlProperty.Organization # 9
        ACB : ApplicationControlProperty.Organization # 10
        OFLC : ApplicationControlProperty.Organization # 11
        IARCGeneric : ApplicationControlProperty.Organization # 12


    class ParentalControlFlagValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.ParentalControlFlagValue # 0
        FreeCommunication : ApplicationControlProperty.ParentalControlFlagValue # 1


    class PlayLogPolicyValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Open : ApplicationControlProperty.PlayLogPolicyValue # 0
        All : ApplicationControlProperty.PlayLogPolicyValue # 0
        LogOnly : ApplicationControlProperty.PlayLogPolicyValue # 1
        None_ : ApplicationControlProperty.PlayLogPolicyValue # 2
        Closed : ApplicationControlProperty.PlayLogPolicyValue # 3


    class PlayLogQueryCapabilityValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.PlayLogQueryCapabilityValue # 0
        WhiteList : ApplicationControlProperty.PlayLogQueryCapabilityValue # 1
        All : ApplicationControlProperty.PlayLogQueryCapabilityValue # 2


    class PlayReportPermissionValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.PlayReportPermissionValue # 0
        TargetMarketing : ApplicationControlProperty.PlayReportPermissionValue # 1


    class RepairFlagValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.RepairFlagValue # 0
        SuppressGameCardAccess : ApplicationControlProperty.RepairFlagValue # 1


    class RequiredAddOnContentsSetBinaryDescriptor:
        Descriptors : Array32_1[int]


    class RequiredNetworkServiceLicenseOnLaunchValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.RequiredNetworkServiceLicenseOnLaunchValue # 0
        Common : ApplicationControlProperty.RequiredNetworkServiceLicenseOnLaunchValue # 1


    class RuntimeAddOnContentInstallValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Deny : ApplicationControlProperty.RuntimeAddOnContentInstallValue # 0
        AllowAppend : ApplicationControlProperty.RuntimeAddOnContentInstallValue # 1
        AllowAppendButDontDownloadWhenUsingNetwork : ApplicationControlProperty.RuntimeAddOnContentInstallValue # 2


    class RuntimeParameterDeliveryValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Always : ApplicationControlProperty.RuntimeParameterDeliveryValue # 0
        AlwaysIfUserStateMatched : ApplicationControlProperty.RuntimeParameterDeliveryValue # 1
        OnRestart : ApplicationControlProperty.RuntimeParameterDeliveryValue # 2


    class ScreenshotValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Allow : ApplicationControlProperty.ScreenshotValue # 0
        Deny : ApplicationControlProperty.ScreenshotValue # 1


    class StartupUserAccountOptionFlagValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.StartupUserAccountOptionFlagValue # 0
        IsOptional : ApplicationControlProperty.StartupUserAccountOptionFlagValue # 1


    class StartupUserAccountValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : ApplicationControlProperty.StartupUserAccountValue # 0
        Required : ApplicationControlProperty.StartupUserAccountValue # 1
        RequiredWithNetworkServiceAccountAvailable : ApplicationControlProperty.StartupUserAccountValue # 2


    class UserAccountSwitchLockValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Disable : ApplicationControlProperty.UserAccountSwitchLockValue # 0
        Enable : ApplicationControlProperty.UserAccountSwitchLockValue # 1


    class VideoCaptureValue(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Disable : ApplicationControlProperty.VideoCaptureValue # 0
        Manual : ApplicationControlProperty.VideoCaptureValue # 1
        Enable : ApplicationControlProperty.VideoCaptureValue # 2


