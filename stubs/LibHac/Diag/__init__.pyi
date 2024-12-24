import typing, clr, abc
from LibHac import Result, HorizonClient
from System import Span_1, ReadOnlySpan_1, MulticastDelegate, IAsyncResult, AsyncCallback
from LibHac.Common import UniqueRef_1, SharedRef_1, U8Span
from System.Reflection import MethodInfo

class Abort(abc.ABC):
    @staticmethod
    def DoAbortUnlessSuccess(result: Result, message: str = ...) -> None: ...
    @staticmethod
    def UnexpectedDefault(caller: str = ...) -> None: ...
    # Skipped DoAbort due to it being static, abstract and generic.

    DoAbort : DoAbort_MethodGroup
    class DoAbort_MethodGroup:
        @typing.overload
        def __call__(self, message: str = ...) -> None:...
        @typing.overload
        def __call__(self, result: Result, message: str = ...) -> None:...

    # Skipped DoAbortUnless due to it being static, abstract and generic.

    DoAbortUnless : DoAbortUnless_MethodGroup
    class DoAbortUnless_MethodGroup:
        @typing.overload
        def __call__(self, condition: bool, message: str = ...) -> None:...
        @typing.overload
        def __call__(self, condition: bool, result: Result, message: str = ...) -> None:...



class AbortInfo:
    AbortReason : AbortReason
    Condition : str
    FileName : str
    FunctionName : str
    LineNumber : int
    Message : str


class AbortReason(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    SdkAssert : AbortReason # 0
    SdkRequires : AbortReason # 1
    UserAssert : AbortReason # 2
    Abort : AbortReason # 3
    UnexpectedDefault : AbortReason # 4


class Assert(abc.ABC):
    @staticmethod
    def SdkAssert(condition: bool, message: str = ..., conditionText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None: ...
    @staticmethod
    def SdkRequires(condition: bool, message: str = ..., conditionText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None: ...
    @staticmethod
    def SetAssertionFailureHandler(assertionHandler: AssertionFailureHandler) -> None: ...
    @staticmethod
    def True(condition: bool, message: str = ..., conditionText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None: ...
    # Skipped Aligned due to it being static, abstract and generic.

    Aligned : Aligned_MethodGroup
    class Aligned_MethodGroup:
        def __call__(self, value: int, alignment: int, valueText: str = ..., alignmentText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
        # Method Aligned(value : UInt64, alignment : Int32, valueText : String, alignmentText : String, functionName : String, fileName : String, lineNumber : Int32) was skipped since it collides with above method

    # Skipped Equal due to it being static, abstract and generic.

    Equal : Equal_MethodGroup
    class Equal_MethodGroup:
        def __getitem__(self, t:typing.Type[Equal_1_T1]) -> Equal_1[Equal_1_T1]: ...

        Equal_1_T1 = typing.TypeVar('Equal_1_T1')
        class Equal_1(typing.Generic[Equal_1_T1]):
            Equal_1_T = Assert.Equal_MethodGroup.Equal_1_T1
            @typing.overload
            def __call__(self, lhs: Equal_1_T, rhs: Equal_1_T, lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, lhs: clr.Reference[Equal_1_T], rhs: clr.Reference[Equal_1_T], lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped Greater due to it being static, abstract and generic.

    Greater : Greater_MethodGroup
    class Greater_MethodGroup:
        def __getitem__(self, t:typing.Type[Greater_1_T1]) -> Greater_1[Greater_1_T1]: ...

        Greater_1_T1 = typing.TypeVar('Greater_1_T1')
        class Greater_1(typing.Generic[Greater_1_T1]):
            Greater_1_T = Assert.Greater_MethodGroup.Greater_1_T1
            def __call__(self, lhs: Greater_1_T, rhs: Greater_1_T, lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped GreaterEqual due to it being static, abstract and generic.

    GreaterEqual : GreaterEqual_MethodGroup
    class GreaterEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterEqual_1_T1]) -> GreaterEqual_1[GreaterEqual_1_T1]: ...

        GreaterEqual_1_T1 = typing.TypeVar('GreaterEqual_1_T1')
        class GreaterEqual_1(typing.Generic[GreaterEqual_1_T1]):
            GreaterEqual_1_T = Assert.GreaterEqual_MethodGroup.GreaterEqual_1_T1
            def __call__(self, lhs: GreaterEqual_1_T, rhs: GreaterEqual_1_T, lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped InRange due to it being static, abstract and generic.

    InRange : InRange_MethodGroup
    class InRange_MethodGroup:
        def __call__(self, value: int, lowerInclusive: int, upperExclusive: int, valueText: str = ..., lowerInclusiveText: str = ..., upperExclusiveText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
        # Method InRange(value : Int64, lowerInclusive : Int64, upperExclusive : Int64, valueText : String, lowerInclusiveText : String, upperExclusiveText : String, functionName : String, fileName : String, lineNumber : Int32) was skipped since it collides with above method

    # Skipped Less due to it being static, abstract and generic.

    Less : Less_MethodGroup
    class Less_MethodGroup:
        def __getitem__(self, t:typing.Type[Less_1_T1]) -> Less_1[Less_1_T1]: ...

        Less_1_T1 = typing.TypeVar('Less_1_T1')
        class Less_1(typing.Generic[Less_1_T1]):
            Less_1_T = Assert.Less_MethodGroup.Less_1_T1
            def __call__(self, lhs: Less_1_T, rhs: Less_1_T, lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped LessEqual due to it being static, abstract and generic.

    LessEqual : LessEqual_MethodGroup
    class LessEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[LessEqual_1_T1]) -> LessEqual_1[LessEqual_1_T1]: ...

        LessEqual_1_T1 = typing.TypeVar('LessEqual_1_T1')
        class LessEqual_1(typing.Generic[LessEqual_1_T1]):
            LessEqual_1_T = Assert.LessEqual_MethodGroup.LessEqual_1_T1
            def __call__(self, lhs: LessEqual_1_T, rhs: LessEqual_1_T, lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped NotEqual due to it being static, abstract and generic.

    NotEqual : NotEqual_MethodGroup
    class NotEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[NotEqual_1_T1]) -> NotEqual_1[NotEqual_1_T1]: ...

        NotEqual_1_T1 = typing.TypeVar('NotEqual_1_T1')
        class NotEqual_1(typing.Generic[NotEqual_1_T1]):
            NotEqual_1_T = Assert.NotEqual_MethodGroup.NotEqual_1_T1
            @typing.overload
            def __call__(self, lhs: NotEqual_1_T, rhs: NotEqual_1_T, lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, lhs: clr.Reference[NotEqual_1_T], rhs: clr.Reference[NotEqual_1_T], lhsText: str = ..., rhsText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped NotNull due to it being static, abstract and generic.

    NotNull : NotNull_MethodGroup
    class NotNull_MethodGroup:
        def __getitem__(self, t:typing.Type[NotNull_1_T1]) -> NotNull_1[NotNull_1_T1]: ...

        NotNull_1_T1 = typing.TypeVar('NotNull_1_T1')
        class NotNull_1(typing.Generic[NotNull_1_T1]):
            NotNull_1_T = Assert.NotNull_MethodGroup.NotNull_1_T1
            @typing.overload
            def __call__(self, value: Span_1[NotNull_1_T], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: ReadOnlySpan_1[NotNull_1_T], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: NotNull_1_T, valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: clr.Reference[UniqueRef_1[NotNull_1_T]], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: clr.Reference[SharedRef_1[NotNull_1_T]], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: clr.Reference[NotNull_1_T], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped NotNullOut due to it being static, abstract and generic.

    NotNullOut : NotNullOut_MethodGroup
    class NotNullOut_MethodGroup:
        def __getitem__(self, t:typing.Type[NotNullOut_1_T1]) -> NotNullOut_1[NotNullOut_1_T1]: ...

        NotNullOut_1_T1 = typing.TypeVar('NotNullOut_1_T1')
        class NotNullOut_1(typing.Generic[NotNullOut_1_T1]):
            NotNullOut_1_T = Assert.NotNullOut_MethodGroup.NotNullOut_1_T1
            def __call__(self, value: clr.Reference[NotNullOut_1_T], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped Null due to it being static, abstract and generic.

    Null : Null_MethodGroup
    class Null_MethodGroup:
        def __getitem__(self, t:typing.Type[Null_1_T1]) -> Null_1[Null_1_T1]: ...

        Null_1_T1 = typing.TypeVar('Null_1_T1')
        class Null_1(typing.Generic[Null_1_T1]):
            Null_1_T = Assert.Null_MethodGroup.Null_1_T1
            @typing.overload
            def __call__(self, value: Null_1_T, valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: clr.Reference[UniqueRef_1[Null_1_T]], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: clr.Reference[SharedRef_1[Null_1_T]], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
            @typing.overload
            def __call__(self, value: clr.Reference[Null_1_T], valueText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...


    # Skipped WithinMinMax due to it being static, abstract and generic.

    WithinMinMax : WithinMinMax_MethodGroup
    class WithinMinMax_MethodGroup:
        def __call__(self, value: int, min: int, max: int, valueText: str = ..., minText: str = ..., maxText: str = ..., functionName: str = ..., fileName: str = ..., lineNumber: int = ...) -> None:...
        # Method WithinMinMax(value : Int64, min : Int64, max : Int64, valueText : String, minText : String, maxText : String, functionName : String, fileName : String, lineNumber : Int32) was skipped since it collides with above method



class AssertionFailureHandler(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, assertionInfo: clr.Reference[AssertionInfo], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, assertionInfo: clr.Reference[AssertionInfo], result: IAsyncResult) -> AssertionFailureOperation: ...
    def Invoke(self, assertionInfo: clr.Reference[AssertionInfo]) -> AssertionFailureOperation: ...


class AssertionFailureOperation(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Abort : AssertionFailureOperation # 0
    Continue : AssertionFailureOperation # 1


class AssertionInfo:
    AssertionType : AssertionType
    Condition : str
    FileName : str
    FunctionName : str
    LineNumber : int
    Message : str


class AssertionType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    SdkAssert : AssertionType # 0
    SdkRequires : AssertionType # 1
    UserAssert : AssertionType # 2


class DiagClient:
    def __init__(self, horizonClient: HorizonClient) -> None: ...
    @property
    def Impl(self) -> DiagClientImpl: ...


class DiagClientImpl:
    pass


class Log(abc.ABC):
    @classmethod
    @property
    def EmptyModuleName(cls) -> ReadOnlySpan_1[int]: ...
    @staticmethod
    def PutImpl(diag: DiagClientImpl, metaData: clr.Reference[LogMetaData], message: ReadOnlySpan_1[int]) -> None: ...
    # Skipped LogImpl due to it being static, abstract and generic.

    LogImpl : LogImpl_MethodGroup
    class LogImpl_MethodGroup:
        @typing.overload
        def __call__(self, diag: DiagClientImpl, metaData: clr.Reference[LogMetaData], message: ReadOnlySpan_1[int]) -> None:...
        @typing.overload
        def __call__(self, diag: DiagClientImpl, moduleName: ReadOnlySpan_1[int], severity: LogSeverity, message: ReadOnlySpan_1[int], lineNumber: int = ..., fileName: str = ..., functionName: str = ...) -> None:...



class LogBody:
    IsHead : bool
    IsTail : bool
    Message : U8Span


class LogMetaData:
    AdditionalData : Span_1[int]
    ModuleName : U8Span
    Severity : LogSeverity
    SourceInfo : SourceInfo
    UseDefaultLocaleCharset : bool
    Verbosity : int


class LogObserver(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, metaData: clr.Reference[LogMetaData], body: clr.Reference[LogBody], arguments: typing.Any, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, metaData: clr.Reference[LogMetaData], body: clr.Reference[LogBody], result: IAsyncResult) -> None: ...
    def Invoke(self, metaData: clr.Reference[LogMetaData], body: clr.Reference[LogBody], arguments: typing.Any) -> None: ...


class LogObserverFuncs(abc.ABC):
    @staticmethod
    def InitializeLogObserverHolder(diag: DiagClient, holder: clr.Reference[LogObserverHolder], observer: LogObserver, arguments: typing.Any) -> None: ...
    @staticmethod
    def RegisterLogObserver(diag: DiagClient, observerHolder: LogObserverHolder) -> None: ...
    @staticmethod
    def UnregisterLogObserver(diag: DiagClient, observerHolder: LogObserverHolder) -> None: ...


class LogObserverHolder:
    def __init__(self) -> None: ...


class LogSeverity(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Trace : LogSeverity # 0
    Info : LogSeverity # 1
    Warn : LogSeverity # 2
    Error : LogSeverity # 3
    Fatal : LogSeverity # 4


class SourceInfo:
    FileName : str
    FunctionName : str
    LineNumber : int

