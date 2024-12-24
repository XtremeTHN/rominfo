import typing, clr, abc
from System import Attribute, IEquatable_1, Span_1, Guid, Delegate, Exception, IDisposable, UIntPtr, Decimal, MulticastDelegate, IAsyncResult, AsyncCallback, SystemException, MarshalByRefObject, RuntimeTypeHandle, Array, Array_1, ReadOnlyMemory_1, ReadOnlySpan_1, Memory_1, ArraySegment_1, ISpanFormattable, IComparable_1, IComparable, IFormatProvider, Action_1
from System.Collections.Generic import List_1, Dictionary_2, IEnumerable_1
from System.Collections import IDictionary
from System.Reflection import MethodBase, MethodInfo, Assembly, Module
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices.ComTypes import ITypeInfo
from System.Security import SecureString
from System.Globalization import NumberStyles
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid

class AllowReversePInvokeCallsAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ArrayWithOffset:
    def __init__(self, array: typing.Any, offset: int) -> None: ...
    def GetArray(self) -> typing.Any: ...
    def GetHashCode(self) -> int: ...
    def GetOffset(self) -> int: ...
    def __eq__(self, a: ArrayWithOffset, b: ArrayWithOffset) -> bool: ...
    def __ne__(self, a: ArrayWithOffset, b: ArrayWithOffset) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: ArrayWithOffset) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class BestFitMappingAttribute(Attribute):
    def __init__(self, BestFitMapping: bool) -> None: ...
    ThrowOnUnmappableChar : bool
    @property
    def BestFitMapping(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class BStrWrapper:
    @typing.overload
    def __init__(self, value: str) -> None: ...
    @typing.overload
    def __init__(self, value: typing.Any) -> None: ...
    @property
    def WrappedObject(self) -> str: ...


class CallingConvention(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Winapi : CallingConvention # 1
    Cdecl : CallingConvention # 2
    StdCall : CallingConvention # 3
    ThisCall : CallingConvention # 4
    FastCall : CallingConvention # 5


class CharSet(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CharSet # 1
    Ansi : CharSet # 2
    Unicode : CharSet # 3
    Auto : CharSet # 4


class ClassInterfaceAttribute(Attribute):
    @typing.overload
    def __init__(self, classInterfaceType: ClassInterfaceType) -> None: ...
    @typing.overload
    def __init__(self, classInterfaceType: int) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> ClassInterfaceType: ...


class ClassInterfaceType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ClassInterfaceType # 0
    AutoDispatch : ClassInterfaceType # 1
    AutoDual : ClassInterfaceType # 2


class CLong(IEquatable_1[CLong]):
    # Constructor .ctor(value : IntPtr) was skipped since it collides with above method
    def __init__(self, value: int) -> None: ...
    @property
    def Value(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: CLong) -> bool:...
        @typing.overload
        def __call__(self, o: typing.Any) -> bool:...



class CoClassAttribute(Attribute):
    def __init__(self, coClass: typing.Type[typing.Any]) -> None: ...
    @property
    def CoClass(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class CollectionsMarshal(abc.ABC):
    # Skipped AsSpan due to it being static, abstract and generic.

    AsSpan : AsSpan_MethodGroup
    class AsSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSpan_1_T1]) -> AsSpan_1[AsSpan_1_T1]: ...

        AsSpan_1_T1 = typing.TypeVar('AsSpan_1_T1')
        class AsSpan_1(typing.Generic[AsSpan_1_T1]):
            AsSpan_1_T = CollectionsMarshal.AsSpan_MethodGroup.AsSpan_1_T1
            def __call__(self, list: List_1[AsSpan_1_T]) -> Span_1[AsSpan_1_T]:...


    # Skipped GetValueRefOrAddDefault due to it being static, abstract and generic.

    GetValueRefOrAddDefault : GetValueRefOrAddDefault_MethodGroup
    class GetValueRefOrAddDefault_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GetValueRefOrAddDefault_2_T1], typing.Type[GetValueRefOrAddDefault_2_T2]]) -> GetValueRefOrAddDefault_2[GetValueRefOrAddDefault_2_T1, GetValueRefOrAddDefault_2_T2]: ...

        GetValueRefOrAddDefault_2_T1 = typing.TypeVar('GetValueRefOrAddDefault_2_T1')
        GetValueRefOrAddDefault_2_T2 = typing.TypeVar('GetValueRefOrAddDefault_2_T2')
        class GetValueRefOrAddDefault_2(typing.Generic[GetValueRefOrAddDefault_2_T1, GetValueRefOrAddDefault_2_T2]):
            GetValueRefOrAddDefault_2_TKey = CollectionsMarshal.GetValueRefOrAddDefault_MethodGroup.GetValueRefOrAddDefault_2_T1
            GetValueRefOrAddDefault_2_TValue = CollectionsMarshal.GetValueRefOrAddDefault_MethodGroup.GetValueRefOrAddDefault_2_T2
            def __call__(self, dictionary: Dictionary_2[GetValueRefOrAddDefault_2_TKey, GetValueRefOrAddDefault_2_TValue], key: GetValueRefOrAddDefault_2_TKey, exists: clr.Reference[bool]) -> clr.Reference[GetValueRefOrAddDefault_2_TValue]:...


    # Skipped GetValueRefOrNullRef due to it being static, abstract and generic.

    GetValueRefOrNullRef : GetValueRefOrNullRef_MethodGroup
    class GetValueRefOrNullRef_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GetValueRefOrNullRef_2_T1], typing.Type[GetValueRefOrNullRef_2_T2]]) -> GetValueRefOrNullRef_2[GetValueRefOrNullRef_2_T1, GetValueRefOrNullRef_2_T2]: ...

        GetValueRefOrNullRef_2_T1 = typing.TypeVar('GetValueRefOrNullRef_2_T1')
        GetValueRefOrNullRef_2_T2 = typing.TypeVar('GetValueRefOrNullRef_2_T2')
        class GetValueRefOrNullRef_2(typing.Generic[GetValueRefOrNullRef_2_T1, GetValueRefOrNullRef_2_T2]):
            GetValueRefOrNullRef_2_TKey = CollectionsMarshal.GetValueRefOrNullRef_MethodGroup.GetValueRefOrNullRef_2_T1
            GetValueRefOrNullRef_2_TValue = CollectionsMarshal.GetValueRefOrNullRef_MethodGroup.GetValueRefOrNullRef_2_T2
            def __call__(self, dictionary: Dictionary_2[GetValueRefOrNullRef_2_TKey, GetValueRefOrNullRef_2_TValue], key: GetValueRefOrNullRef_2_TKey) -> clr.Reference[GetValueRefOrNullRef_2_TValue]:...




class ComDefaultInterfaceAttribute(Attribute):
    def __init__(self, defaultInterface: typing.Type[typing.Any]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> typing.Type[typing.Any]: ...


class ComEventInterfaceAttribute(Attribute):
    def __init__(self, SourceInterface: typing.Type[typing.Any], EventProvider: typing.Type[typing.Any]) -> None: ...
    @property
    def EventProvider(self) -> typing.Type[typing.Any]: ...
    @property
    def SourceInterface(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ComEventsHelper(abc.ABC):
    @staticmethod
    def Combine(rcw: typing.Any, iid: Guid, dispid: int, d: Delegate) -> None: ...
    @staticmethod
    def Remove(rcw: typing.Any, iid: Guid, dispid: int, d: Delegate) -> Delegate: ...


class COMException(ExternalException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, errorCode: int) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def ErrorCode(self) -> int: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def ToString(self) -> str: ...


class ComImportAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ComInterfaceType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    InterfaceIsDual : ComInterfaceType # 0
    InterfaceIsIUnknown : ComInterfaceType # 1
    InterfaceIsIDispatch : ComInterfaceType # 2
    InterfaceIsIInspectable : ComInterfaceType # 3


class ComMemberType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Method : ComMemberType # 0
    PropGet : ComMemberType # 1
    PropSet : ComMemberType # 2


class ComSourceInterfacesAttribute(Attribute):
    @typing.overload
    def __init__(self, sourceInterface: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, sourceInterface1: typing.Type[typing.Any], sourceInterface2: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, sourceInterface1: typing.Type[typing.Any], sourceInterface2: typing.Type[typing.Any], sourceInterface3: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, sourceInterface1: typing.Type[typing.Any], sourceInterface2: typing.Type[typing.Any], sourceInterface3: typing.Type[typing.Any], sourceInterface4: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, sourceInterfaces: str) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> str: ...


class ComVisibleAttribute(Attribute):
    def __init__(self, visibility: bool) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> bool: ...


class ComWrappers(abc.ABC):
    def GetOrCreateComInterfaceForObject(self, instance: typing.Any, flags: CreateComInterfaceFlags) -> int: ...
    def GetOrCreateObjectForComInstance(self, externalComObject: int, flags: CreateObjectFlags) -> typing.Any: ...
    @staticmethod
    def RegisterForMarshalling(instance: ComWrappers) -> None: ...
    @staticmethod
    def RegisterForTrackerSupport(instance: ComWrappers) -> None: ...
    # Skipped GetOrRegisterObjectForComInstance due to it being static, abstract and generic.

    GetOrRegisterObjectForComInstance : GetOrRegisterObjectForComInstance_MethodGroup
    class GetOrRegisterObjectForComInstance_MethodGroup:
        @typing.overload
        def __call__(self, externalComObject: int, flags: CreateObjectFlags, wrapper: typing.Any) -> typing.Any:...
        @typing.overload
        def __call__(self, externalComObject: int, flags: CreateObjectFlags, wrapper: typing.Any, inner: int) -> typing.Any:...


    class ComInterfaceDispatch:
        Vtable : int
        # Skipped GetInstance due to it being static, abstract and generic.

        GetInstance : GetInstance_MethodGroup
        class GetInstance_MethodGroup:
            def __getitem__(self, t:typing.Type[GetInstance_1_T1]) -> GetInstance_1[GetInstance_1_T1]: ...

            GetInstance_1_T1 = typing.TypeVar('GetInstance_1_T1')
            class GetInstance_1(typing.Generic[GetInstance_1_T1]):
                GetInstance_1_T = ComWrappers.ComInterfaceDispatch.GetInstance_MethodGroup.GetInstance_1_T1
                def __call__(self, dispatchPtr: clr.Reference[ComWrappers.ComInterfaceDispatch]) -> GetInstance_1_T:...




    class ComInterfaceEntry:
        IID : Guid
        Vtable : int



class CreateComInterfaceFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CreateComInterfaceFlags # 0
    CallerDefinedIUnknown : CreateComInterfaceFlags # 1
    TrackerSupport : CreateComInterfaceFlags # 2


class CreateObjectFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CreateObjectFlags # 0
    TrackerObject : CreateObjectFlags # 1
    UniqueInstance : CreateObjectFlags # 2
    Aggregation : CreateObjectFlags # 4
    Unwrap : CreateObjectFlags # 8


class CriticalHandle(CriticalFinalizerObject, IDisposable):
    @property
    def IsClosed(self) -> bool: ...
    @property
    def IsInvalid(self) -> bool: ...
    def Close(self) -> None: ...
    def Dispose(self) -> None: ...
    def SetHandleAsInvalid(self) -> None: ...


class CULong(IEquatable_1[CULong]):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: UIntPtr) -> None: ...
    @property
    def Value(self) -> UIntPtr: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: CULong) -> bool:...
        @typing.overload
        def __call__(self, o: typing.Any) -> bool:...



class CurrencyWrapper:
    @typing.overload
    def __init__(self, obj: Decimal) -> None: ...
    @typing.overload
    def __init__(self, obj: typing.Any) -> None: ...
    @property
    def WrappedObject(self) -> Decimal: ...


class CustomQueryInterfaceMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Ignore : CustomQueryInterfaceMode # 0
    Allow : CustomQueryInterfaceMode # 1


class CustomQueryInterfaceResult(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Handled : CustomQueryInterfaceResult # 0
    NotHandled : CustomQueryInterfaceResult # 1
    Failed : CustomQueryInterfaceResult # 2


class DefaultCharSetAttribute(Attribute):
    def __init__(self, charSet: CharSet) -> None: ...
    @property
    def CharSet(self) -> CharSet: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DefaultDllImportSearchPathsAttribute(Attribute):
    def __init__(self, paths: DllImportSearchPath) -> None: ...
    @property
    def Paths(self) -> DllImportSearchPath: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DefaultParameterValueAttribute(Attribute):
    def __init__(self, value: typing.Any) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> typing.Any: ...


class DispatchWrapper:
    def __init__(self, obj: typing.Any) -> None: ...
    @property
    def WrappedObject(self) -> typing.Any: ...


class DispIdAttribute(Attribute):
    def __init__(self, dispId: int) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> int: ...


class DllImportAttribute(Attribute):
    def __init__(self, dllName: str) -> None: ...
    BestFitMapping : bool
    CallingConvention : CallingConvention
    CharSet : CharSet
    EntryPoint : str
    ExactSpelling : bool
    PreserveSig : bool
    SetLastError : bool
    ThrowOnUnmappableChar : bool
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> str: ...


class DllImportResolver(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, libraryName: str, assembly: Assembly, searchPath: typing.Optional[DllImportSearchPath], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> int: ...
    def Invoke(self, libraryName: str, assembly: Assembly, searchPath: typing.Optional[DllImportSearchPath]) -> int: ...


class DllImportSearchPath(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    LegacyBehavior : DllImportSearchPath # 0
    AssemblyDirectory : DllImportSearchPath # 2
    UseDllDirectoryForDependencies : DllImportSearchPath # 256
    ApplicationDirectory : DllImportSearchPath # 512
    UserDirectories : DllImportSearchPath # 1024
    System32 : DllImportSearchPath # 2048
    SafeDirectories : DllImportSearchPath # 4096


class DynamicInterfaceCastableImplementationAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ErrorWrapper:
    @typing.overload
    def __init__(self, e: Exception) -> None: ...
    @typing.overload
    def __init__(self, errorCode: int) -> None: ...
    @typing.overload
    def __init__(self, errorCode: typing.Any) -> None: ...
    @property
    def ErrorCode(self) -> int: ...


class ExternalException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, errorCode: int) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def ErrorCode(self) -> int: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def ToString(self) -> str: ...


class FieldOffsetAttribute(Attribute):
    def __init__(self, offset: int) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> int: ...


class GCHandle:
    @property
    def IsAllocated(self) -> bool: ...
    @property
    def Target(self) -> typing.Any: ...
    @Target.setter
    def Target(self, value: typing.Any) -> typing.Any: ...
    def AddrOfPinnedObject(self) -> int: ...
    def Equals(self, o: typing.Any) -> bool: ...
    def Free(self) -> None: ...
    @staticmethod
    def FromIntPtr(value: int) -> GCHandle: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, a: GCHandle, b: GCHandle) -> bool: ...
    # Operator not supported op_Explicit(value: IntPtr)
    # Operator not supported op_Explicit(value: GCHandle)
    def __ne__(self, a: GCHandle, b: GCHandle) -> bool: ...
    @staticmethod
    def ToIntPtr(value: GCHandle) -> int: ...
    # Skipped Alloc due to it being static, abstract and generic.

    Alloc : Alloc_MethodGroup
    class Alloc_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> GCHandle:...
        @typing.overload
        def __call__(self, value: typing.Any, type: GCHandleType) -> GCHandle:...



class GCHandleType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Weak : GCHandleType # 0
    WeakTrackResurrection : GCHandleType # 1
    Normal : GCHandleType # 2
    Pinned : GCHandleType # 3


class GuidAttribute(Attribute):
    def __init__(self, guid: str) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> str: ...


class HandleRef:
    def __init__(self, wrapper: typing.Any, handle: int) -> None: ...
    @property
    def Handle(self) -> int: ...
    @property
    def Wrapper(self) -> typing.Any: ...
    # Operator not supported op_Explicit(value: HandleRef)
    @staticmethod
    def ToIntPtr(value: HandleRef) -> int: ...


class ICustomAdapter(typing.Protocol):
    @abc.abstractmethod
    def GetUnderlyingObject(self) -> typing.Any: ...


class ICustomFactory(typing.Protocol):
    @abc.abstractmethod
    def CreateInstance(self, serverType: typing.Type[typing.Any]) -> MarshalByRefObject: ...


class ICustomMarshaler(typing.Protocol):
    @abc.abstractmethod
    def CleanUpManagedData(self, ManagedObj: typing.Any) -> None: ...
    @abc.abstractmethod
    def CleanUpNativeData(self, pNativeData: int) -> None: ...
    @abc.abstractmethod
    def GetNativeDataSize(self) -> int: ...
    @abc.abstractmethod
    def MarshalManagedToNative(self, ManagedObj: typing.Any) -> int: ...
    @abc.abstractmethod
    def MarshalNativeToManaged(self, pNativeData: int) -> typing.Any: ...


class ICustomQueryInterface(typing.Protocol):
    @abc.abstractmethod
    def GetInterface(self, iid: clr.Reference[Guid], ppv: clr.Reference[int]) -> CustomQueryInterfaceResult: ...


class IDynamicInterfaceCastable(typing.Protocol):
    @abc.abstractmethod
    def GetInterfaceImplementation(self, interfaceType: RuntimeTypeHandle) -> RuntimeTypeHandle: ...
    @abc.abstractmethod
    def IsInterfaceImplemented(self, interfaceType: RuntimeTypeHandle, throwIfNotImplemented: bool) -> bool: ...


class InAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class InterfaceTypeAttribute(Attribute):
    @typing.overload
    def __init__(self, interfaceType: ComInterfaceType) -> None: ...
    @typing.overload
    def __init__(self, interfaceType: int) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> ComInterfaceType: ...


class InvalidComObjectException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class InvalidOleVariantTypeException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class LayoutKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Sequential : LayoutKind # 0
    Explicit : LayoutKind # 2
    Auto : LayoutKind # 3


class LCIDConversionAttribute(Attribute):
    def __init__(self, lcid: int) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> int: ...


class Marshal(abc.ABC):
    SystemDefaultCharSize : int
    SystemMaxDBCSCharSize : int
    @staticmethod
    def AddRef(pUnk: int) -> int: ...
    @staticmethod
    def AllocCoTaskMem(cb: int) -> int: ...
    @staticmethod
    def AreComObjectsAvailableForCleanup() -> bool: ...
    @staticmethod
    def BindToMoniker(monikerName: str) -> typing.Any: ...
    @staticmethod
    def ChangeWrapperHandleStrength(otp: typing.Any, fIsWeak: bool) -> None: ...
    @staticmethod
    def CleanupUnusedObjectsInCurrentContext() -> None: ...
    @staticmethod
    def FinalReleaseComObject(o: typing.Any) -> int: ...
    @staticmethod
    def FreeBSTR(ptr: int) -> None: ...
    @staticmethod
    def FreeCoTaskMem(ptr: int) -> None: ...
    @staticmethod
    def FreeHGlobal(hglobal: int) -> None: ...
    @staticmethod
    def GenerateGuidForType(type: typing.Type[typing.Any]) -> Guid: ...
    @staticmethod
    def GenerateProgIdForType(type: typing.Type[typing.Any]) -> str: ...
    @staticmethod
    def GetComObjectData(obj: typing.Any, key: typing.Any) -> typing.Any: ...
    @staticmethod
    def GetEndComSlot(t: typing.Type[typing.Any]) -> int: ...
    @staticmethod
    def GetExceptionCode() -> int: ...
    @staticmethod
    def GetExceptionPointers() -> int: ...
    @staticmethod
    def GetHINSTANCE(m: Module) -> int: ...
    @staticmethod
    def GetHRForException(e: Exception) -> int: ...
    @staticmethod
    def GetHRForLastWin32Error() -> int: ...
    @staticmethod
    def GetIDispatchForObject(o: typing.Any) -> int: ...
    @staticmethod
    def GetIUnknownForObject(o: typing.Any) -> int: ...
    @staticmethod
    def GetLastPInvokeError() -> int: ...
    @staticmethod
    def GetLastSystemError() -> int: ...
    @staticmethod
    def GetLastWin32Error() -> int: ...
    @staticmethod
    def GetObjectForIUnknown(pUnk: int) -> typing.Any: ...
    @staticmethod
    def GetStartComSlot(t: typing.Type[typing.Any]) -> int: ...
    @staticmethod
    def GetTypedObjectForIUnknown(pUnk: int, t: typing.Type[typing.Any]) -> typing.Any: ...
    @staticmethod
    def GetTypeFromCLSID(clsid: Guid) -> typing.Type[typing.Any]: ...
    @staticmethod
    def GetTypeInfoName(typeInfo: ITypeInfo) -> str: ...
    @staticmethod
    def GetUniqueObjectForIUnknown(unknown: int) -> typing.Any: ...
    @staticmethod
    def InitHandle(safeHandle: SafeHandle, handle: int) -> None: ...
    @staticmethod
    def IsComObject(o: typing.Any) -> bool: ...
    @staticmethod
    def IsTypeVisibleFromCom(t: typing.Type[typing.Any]) -> bool: ...
    @staticmethod
    def Prelink(m: MethodInfo) -> None: ...
    @staticmethod
    def PrelinkAll(c: typing.Type[typing.Any]) -> None: ...
    @staticmethod
    def PtrToStringBSTR(ptr: int) -> str: ...
    @staticmethod
    def QueryInterface(pUnk: int, iid: clr.Reference[Guid], ppv: clr.Reference[int]) -> int: ...
    @staticmethod
    def ReAllocCoTaskMem(pv: int, cb: int) -> int: ...
    @staticmethod
    def ReAllocHGlobal(pv: int, cb: int) -> int: ...
    @staticmethod
    def Release(pUnk: int) -> int: ...
    @staticmethod
    def ReleaseComObject(o: typing.Any) -> int: ...
    @staticmethod
    def SecureStringToBSTR(s: SecureString) -> int: ...
    @staticmethod
    def SecureStringToCoTaskMemAnsi(s: SecureString) -> int: ...
    @staticmethod
    def SecureStringToCoTaskMemUnicode(s: SecureString) -> int: ...
    @staticmethod
    def SecureStringToGlobalAllocAnsi(s: SecureString) -> int: ...
    @staticmethod
    def SecureStringToGlobalAllocUnicode(s: SecureString) -> int: ...
    @staticmethod
    def SetComObjectData(obj: typing.Any, key: typing.Any, data: typing.Any) -> bool: ...
    @staticmethod
    def SetLastPInvokeError(error: int) -> None: ...
    @staticmethod
    def SetLastSystemError(error: int) -> None: ...
    @staticmethod
    def StringToBSTR(s: str) -> int: ...
    @staticmethod
    def StringToCoTaskMemAnsi(s: str) -> int: ...
    @staticmethod
    def StringToCoTaskMemAuto(s: str) -> int: ...
    @staticmethod
    def StringToCoTaskMemUni(s: str) -> int: ...
    @staticmethod
    def StringToCoTaskMemUTF8(s: str) -> int: ...
    @staticmethod
    def StringToHGlobalAnsi(s: str) -> int: ...
    @staticmethod
    def StringToHGlobalAuto(s: str) -> int: ...
    @staticmethod
    def StringToHGlobalUni(s: str) -> int: ...
    @staticmethod
    def ZeroFreeBSTR(s: int) -> None: ...
    @staticmethod
    def ZeroFreeCoTaskMemAnsi(s: int) -> None: ...
    @staticmethod
    def ZeroFreeCoTaskMemUnicode(s: int) -> None: ...
    @staticmethod
    def ZeroFreeCoTaskMemUTF8(s: int) -> None: ...
    @staticmethod
    def ZeroFreeGlobalAllocAnsi(s: int) -> None: ...
    @staticmethod
    def ZeroFreeGlobalAllocUnicode(s: int) -> None: ...
    # Skipped AllocHGlobal due to it being static, abstract and generic.

    AllocHGlobal : AllocHGlobal_MethodGroup
    class AllocHGlobal_MethodGroup:
        def __call__(self, cb: int) -> int:...
        # Method AllocHGlobal(cb : Int32) was skipped since it collides with above method

    # Skipped Copy due to it being static, abstract and generic.

    Copy : Copy_MethodGroup
    class Copy_MethodGroup:
        @typing.overload
        def __call__(self, source: int, destination: Array_1[float], startIndex: int, length: int) -> None:...
        # Method Copy(source : IntPtr, destination : Double[], startIndex : Int32, length : Int32) was skipped since it collides with above method
        # Method Copy(source : IntPtr, destination : Int32[], startIndex : Int32, length : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: int, destination: Array_1[str], startIndex: int, length: int) -> None:...
        # Method Copy(source : IntPtr, destination : Int16[], startIndex : Int32, length : Int32) was skipped since it collides with above method
        # Method Copy(source : IntPtr, destination : Int64[], startIndex : Int32, length : Int32) was skipped since it collides with above method
        # Method Copy(source : IntPtr, destination : Byte[], startIndex : Int32, length : Int32) was skipped since it collides with above method
        # Method Copy(source : IntPtr, destination : IntPtr[], startIndex : Int32, length : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: Array_1[float], startIndex: int, destination: int, length: int) -> None:...
        # Method Copy(source : Double[], startIndex : Int32, destination : IntPtr, length : Int32) was skipped since it collides with above method
        # Method Copy(source : Int32[], startIndex : Int32, destination : IntPtr, length : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: Array_1[str], startIndex: int, destination: int, length: int) -> None:...
        # Method Copy(source : Int16[], startIndex : Int32, destination : IntPtr, length : Int32) was skipped since it collides with above method
        # Method Copy(source : Int64[], startIndex : Int32, destination : IntPtr, length : Int32) was skipped since it collides with above method
        # Method Copy(source : Byte[], startIndex : Int32, destination : IntPtr, length : Int32) was skipped since it collides with above method
        # Method Copy(source : IntPtr[], startIndex : Int32, destination : IntPtr, length : Int32) was skipped since it collides with above method

    # Skipped CreateAggregatedObject due to it being static, abstract and generic.

    CreateAggregatedObject : CreateAggregatedObject_MethodGroup
    class CreateAggregatedObject_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateAggregatedObject_1_T1]) -> CreateAggregatedObject_1[CreateAggregatedObject_1_T1]: ...

        CreateAggregatedObject_1_T1 = typing.TypeVar('CreateAggregatedObject_1_T1')
        class CreateAggregatedObject_1(typing.Generic[CreateAggregatedObject_1_T1]):
            CreateAggregatedObject_1_T = Marshal.CreateAggregatedObject_MethodGroup.CreateAggregatedObject_1_T1
            def __call__(self, pOuter: int, o: CreateAggregatedObject_1_T) -> int:...

        def __call__(self, pOuter: int, o: typing.Any) -> int:...

    # Skipped CreateWrapperOfType due to it being static, abstract and generic.

    CreateWrapperOfType : CreateWrapperOfType_MethodGroup
    class CreateWrapperOfType_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[CreateWrapperOfType_2_T1], typing.Type[CreateWrapperOfType_2_T2]]) -> CreateWrapperOfType_2[CreateWrapperOfType_2_T1, CreateWrapperOfType_2_T2]: ...

        CreateWrapperOfType_2_T1 = typing.TypeVar('CreateWrapperOfType_2_T1')
        CreateWrapperOfType_2_T2 = typing.TypeVar('CreateWrapperOfType_2_T2')
        class CreateWrapperOfType_2(typing.Generic[CreateWrapperOfType_2_T1, CreateWrapperOfType_2_T2]):
            CreateWrapperOfType_2_T = Marshal.CreateWrapperOfType_MethodGroup.CreateWrapperOfType_2_T1
            CreateWrapperOfType_2_TWrapper = Marshal.CreateWrapperOfType_MethodGroup.CreateWrapperOfType_2_T2
            def __call__(self, o: CreateWrapperOfType_2_T) -> CreateWrapperOfType_2_TWrapper:...

        def __call__(self, o: typing.Any, t: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped DestroyStructure due to it being static, abstract and generic.

    DestroyStructure : DestroyStructure_MethodGroup
    class DestroyStructure_MethodGroup:
        def __getitem__(self, t:typing.Type[DestroyStructure_1_T1]) -> DestroyStructure_1[DestroyStructure_1_T1]: ...

        DestroyStructure_1_T1 = typing.TypeVar('DestroyStructure_1_T1')
        class DestroyStructure_1(typing.Generic[DestroyStructure_1_T1]):
            DestroyStructure_1_T = Marshal.DestroyStructure_MethodGroup.DestroyStructure_1_T1
            def __call__(self, ptr: int) -> None:...

        def __call__(self, ptr: int, structuretype: typing.Type[typing.Any]) -> None:...

    # Skipped GetComInterfaceForObject due to it being static, abstract and generic.

    GetComInterfaceForObject : GetComInterfaceForObject_MethodGroup
    class GetComInterfaceForObject_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GetComInterfaceForObject_2_T1], typing.Type[GetComInterfaceForObject_2_T2]]) -> GetComInterfaceForObject_2[GetComInterfaceForObject_2_T1, GetComInterfaceForObject_2_T2]: ...

        GetComInterfaceForObject_2_T1 = typing.TypeVar('GetComInterfaceForObject_2_T1')
        GetComInterfaceForObject_2_T2 = typing.TypeVar('GetComInterfaceForObject_2_T2')
        class GetComInterfaceForObject_2(typing.Generic[GetComInterfaceForObject_2_T1, GetComInterfaceForObject_2_T2]):
            GetComInterfaceForObject_2_T = Marshal.GetComInterfaceForObject_MethodGroup.GetComInterfaceForObject_2_T1
            GetComInterfaceForObject_2_TInterface = Marshal.GetComInterfaceForObject_MethodGroup.GetComInterfaceForObject_2_T2
            def __call__(self, o: GetComInterfaceForObject_2_T) -> int:...

        @typing.overload
        def __call__(self, o: typing.Any, T: typing.Type[typing.Any]) -> int:...
        @typing.overload
        def __call__(self, o: typing.Any, T: typing.Type[typing.Any], mode: CustomQueryInterfaceMode) -> int:...

    # Skipped GetDelegateForFunctionPointer due to it being static, abstract and generic.

    GetDelegateForFunctionPointer : GetDelegateForFunctionPointer_MethodGroup
    class GetDelegateForFunctionPointer_MethodGroup:
        def __getitem__(self, t:typing.Type[GetDelegateForFunctionPointer_1_T1]) -> GetDelegateForFunctionPointer_1[GetDelegateForFunctionPointer_1_T1]: ...

        GetDelegateForFunctionPointer_1_T1 = typing.TypeVar('GetDelegateForFunctionPointer_1_T1')
        class GetDelegateForFunctionPointer_1(typing.Generic[GetDelegateForFunctionPointer_1_T1]):
            GetDelegateForFunctionPointer_1_TDelegate = Marshal.GetDelegateForFunctionPointer_MethodGroup.GetDelegateForFunctionPointer_1_T1
            def __call__(self, ptr: int) -> GetDelegateForFunctionPointer_1_TDelegate:...

        def __call__(self, ptr: int, t: typing.Type[typing.Any]) -> Delegate:...

    # Skipped GetExceptionForHR due to it being static, abstract and generic.

    GetExceptionForHR : GetExceptionForHR_MethodGroup
    class GetExceptionForHR_MethodGroup:
        @typing.overload
        def __call__(self, errorCode: int) -> Exception:...
        @typing.overload
        def __call__(self, errorCode: int, errorInfo: int) -> Exception:...

    # Skipped GetFunctionPointerForDelegate due to it being static, abstract and generic.

    GetFunctionPointerForDelegate : GetFunctionPointerForDelegate_MethodGroup
    class GetFunctionPointerForDelegate_MethodGroup:
        def __getitem__(self, t:typing.Type[GetFunctionPointerForDelegate_1_T1]) -> GetFunctionPointerForDelegate_1[GetFunctionPointerForDelegate_1_T1]: ...

        GetFunctionPointerForDelegate_1_T1 = typing.TypeVar('GetFunctionPointerForDelegate_1_T1')
        class GetFunctionPointerForDelegate_1(typing.Generic[GetFunctionPointerForDelegate_1_T1]):
            GetFunctionPointerForDelegate_1_TDelegate = Marshal.GetFunctionPointerForDelegate_MethodGroup.GetFunctionPointerForDelegate_1_T1
            def __call__(self, d: GetFunctionPointerForDelegate_1_TDelegate) -> int:...

        def __call__(self, d: Delegate) -> int:...

    # Skipped GetNativeVariantForObject due to it being static, abstract and generic.

    GetNativeVariantForObject : GetNativeVariantForObject_MethodGroup
    class GetNativeVariantForObject_MethodGroup:
        def __getitem__(self, t:typing.Type[GetNativeVariantForObject_1_T1]) -> GetNativeVariantForObject_1[GetNativeVariantForObject_1_T1]: ...

        GetNativeVariantForObject_1_T1 = typing.TypeVar('GetNativeVariantForObject_1_T1')
        class GetNativeVariantForObject_1(typing.Generic[GetNativeVariantForObject_1_T1]):
            GetNativeVariantForObject_1_T = Marshal.GetNativeVariantForObject_MethodGroup.GetNativeVariantForObject_1_T1
            def __call__(self, obj: GetNativeVariantForObject_1_T, pDstNativeVariant: int) -> None:...

        def __call__(self, obj: typing.Any, pDstNativeVariant: int) -> None:...

    # Skipped GetObjectForNativeVariant due to it being static, abstract and generic.

    GetObjectForNativeVariant : GetObjectForNativeVariant_MethodGroup
    class GetObjectForNativeVariant_MethodGroup:
        def __getitem__(self, t:typing.Type[GetObjectForNativeVariant_1_T1]) -> GetObjectForNativeVariant_1[GetObjectForNativeVariant_1_T1]: ...

        GetObjectForNativeVariant_1_T1 = typing.TypeVar('GetObjectForNativeVariant_1_T1')
        class GetObjectForNativeVariant_1(typing.Generic[GetObjectForNativeVariant_1_T1]):
            GetObjectForNativeVariant_1_T = Marshal.GetObjectForNativeVariant_MethodGroup.GetObjectForNativeVariant_1_T1
            def __call__(self, pSrcNativeVariant: int) -> GetObjectForNativeVariant_1_T:...

        def __call__(self, pSrcNativeVariant: int) -> typing.Any:...

    # Skipped GetObjectsForNativeVariants due to it being static, abstract and generic.

    GetObjectsForNativeVariants : GetObjectsForNativeVariants_MethodGroup
    class GetObjectsForNativeVariants_MethodGroup:
        def __getitem__(self, t:typing.Type[GetObjectsForNativeVariants_1_T1]) -> GetObjectsForNativeVariants_1[GetObjectsForNativeVariants_1_T1]: ...

        GetObjectsForNativeVariants_1_T1 = typing.TypeVar('GetObjectsForNativeVariants_1_T1')
        class GetObjectsForNativeVariants_1(typing.Generic[GetObjectsForNativeVariants_1_T1]):
            GetObjectsForNativeVariants_1_T = Marshal.GetObjectsForNativeVariants_MethodGroup.GetObjectsForNativeVariants_1_T1
            def __call__(self, aSrcNativeVariant: int, cVars: int) -> Array_1[GetObjectsForNativeVariants_1_T]:...

        def __call__(self, aSrcNativeVariant: int, cVars: int) -> Array_1[typing.Any]:...

    # Skipped OffsetOf due to it being static, abstract and generic.

    OffsetOf : OffsetOf_MethodGroup
    class OffsetOf_MethodGroup:
        def __getitem__(self, t:typing.Type[OffsetOf_1_T1]) -> OffsetOf_1[OffsetOf_1_T1]: ...

        OffsetOf_1_T1 = typing.TypeVar('OffsetOf_1_T1')
        class OffsetOf_1(typing.Generic[OffsetOf_1_T1]):
            OffsetOf_1_T = Marshal.OffsetOf_MethodGroup.OffsetOf_1_T1
            def __call__(self, fieldName: str) -> int:...

        def __call__(self, t: typing.Type[typing.Any], fieldName: str) -> int:...

    # Skipped PtrToStringAnsi due to it being static, abstract and generic.

    PtrToStringAnsi : PtrToStringAnsi_MethodGroup
    class PtrToStringAnsi_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> str:...
        @typing.overload
        def __call__(self, ptr: int, len: int) -> str:...

    # Skipped PtrToStringAuto due to it being static, abstract and generic.

    PtrToStringAuto : PtrToStringAuto_MethodGroup
    class PtrToStringAuto_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> str:...
        @typing.overload
        def __call__(self, ptr: int, len: int) -> str:...

    # Skipped PtrToStringUni due to it being static, abstract and generic.

    PtrToStringUni : PtrToStringUni_MethodGroup
    class PtrToStringUni_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> str:...
        @typing.overload
        def __call__(self, ptr: int, len: int) -> str:...

    # Skipped PtrToStringUTF8 due to it being static, abstract and generic.

    PtrToStringUTF8 : PtrToStringUTF8_MethodGroup
    class PtrToStringUTF8_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> str:...
        @typing.overload
        def __call__(self, ptr: int, byteLen: int) -> str:...

    # Skipped PtrToStructure due to it being static, abstract and generic.

    PtrToStructure : PtrToStructure_MethodGroup
    class PtrToStructure_MethodGroup:
        def __getitem__(self, t:typing.Type[PtrToStructure_1_T1]) -> PtrToStructure_1[PtrToStructure_1_T1]: ...

        PtrToStructure_1_T1 = typing.TypeVar('PtrToStructure_1_T1')
        class PtrToStructure_1(typing.Generic[PtrToStructure_1_T1]):
            PtrToStructure_1_T = Marshal.PtrToStructure_MethodGroup.PtrToStructure_1_T1
            @typing.overload
            def __call__(self, ptr: int) -> PtrToStructure_1_T:...
            @typing.overload
            def __call__(self, ptr: int, structure: PtrToStructure_1_T) -> None:...

        @typing.overload
        def __call__(self, ptr: int, structureType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, ptr: int, structure: typing.Any) -> None:...

    # Skipped ReadByte due to it being static, abstract and generic.

    ReadByte : ReadByte_MethodGroup
    class ReadByte_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> int:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int) -> int:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int) -> int:...

    # Skipped ReadInt16 due to it being static, abstract and generic.

    ReadInt16 : ReadInt16_MethodGroup
    class ReadInt16_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> int:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int) -> int:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int) -> int:...

    # Skipped ReadInt32 due to it being static, abstract and generic.

    ReadInt32 : ReadInt32_MethodGroup
    class ReadInt32_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> int:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int) -> int:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int) -> int:...

    # Skipped ReadInt64 due to it being static, abstract and generic.

    ReadInt64 : ReadInt64_MethodGroup
    class ReadInt64_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> int:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int) -> int:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int) -> int:...

    # Skipped ReadIntPtr due to it being static, abstract and generic.

    ReadIntPtr : ReadIntPtr_MethodGroup
    class ReadIntPtr_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int) -> int:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int) -> int:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int) -> int:...

    # Skipped SizeOf due to it being static, abstract and generic.

    SizeOf : SizeOf_MethodGroup
    class SizeOf_MethodGroup:
        def __getitem__(self, t:typing.Type[SizeOf_1_T1]) -> SizeOf_1[SizeOf_1_T1]: ...

        SizeOf_1_T1 = typing.TypeVar('SizeOf_1_T1')
        class SizeOf_1(typing.Generic[SizeOf_1_T1]):
            SizeOf_1_T = Marshal.SizeOf_MethodGroup.SizeOf_1_T1
            @typing.overload
            def __call__(self) -> int:...
            @typing.overload
            def __call__(self, structure: SizeOf_1_T) -> int:...

        @typing.overload
        def __call__(self, t: typing.Type[typing.Any]) -> int:...
        @typing.overload
        def __call__(self, structure: typing.Any) -> int:...

    # Skipped StructureToPtr due to it being static, abstract and generic.

    StructureToPtr : StructureToPtr_MethodGroup
    class StructureToPtr_MethodGroup:
        def __getitem__(self, t:typing.Type[StructureToPtr_1_T1]) -> StructureToPtr_1[StructureToPtr_1_T1]: ...

        StructureToPtr_1_T1 = typing.TypeVar('StructureToPtr_1_T1')
        class StructureToPtr_1(typing.Generic[StructureToPtr_1_T1]):
            StructureToPtr_1_T = Marshal.StructureToPtr_MethodGroup.StructureToPtr_1_T1
            def __call__(self, structure: StructureToPtr_1_T, ptr: int, fDeleteOld: bool) -> None:...

        def __call__(self, structure: typing.Any, ptr: int, fDeleteOld: bool) -> None:...

    # Skipped ThrowExceptionForHR due to it being static, abstract and generic.

    ThrowExceptionForHR : ThrowExceptionForHR_MethodGroup
    class ThrowExceptionForHR_MethodGroup:
        @typing.overload
        def __call__(self, errorCode: int) -> None:...
        @typing.overload
        def __call__(self, errorCode: int, errorInfo: int) -> None:...

    # Skipped UnsafeAddrOfPinnedArrayElement due to it being static, abstract and generic.

    UnsafeAddrOfPinnedArrayElement : UnsafeAddrOfPinnedArrayElement_MethodGroup
    class UnsafeAddrOfPinnedArrayElement_MethodGroup:
        def __getitem__(self, t:typing.Type[UnsafeAddrOfPinnedArrayElement_1_T1]) -> UnsafeAddrOfPinnedArrayElement_1[UnsafeAddrOfPinnedArrayElement_1_T1]: ...

        UnsafeAddrOfPinnedArrayElement_1_T1 = typing.TypeVar('UnsafeAddrOfPinnedArrayElement_1_T1')
        class UnsafeAddrOfPinnedArrayElement_1(typing.Generic[UnsafeAddrOfPinnedArrayElement_1_T1]):
            UnsafeAddrOfPinnedArrayElement_1_T = Marshal.UnsafeAddrOfPinnedArrayElement_MethodGroup.UnsafeAddrOfPinnedArrayElement_1_T1
            def __call__(self, arr: Array_1[UnsafeAddrOfPinnedArrayElement_1_T], index: int) -> int:...

        def __call__(self, arr: Array, index: int) -> int:...

    # Skipped WriteByte due to it being static, abstract and generic.

    WriteByte : WriteByte_MethodGroup
    class WriteByte_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int, val: int) -> None:...

    # Skipped WriteInt16 due to it being static, abstract and generic.

    WriteInt16 : WriteInt16_MethodGroup
    class WriteInt16_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int, val: str) -> None:...
        @typing.overload
        def __call__(self, ptr: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int, val: str) -> None:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int, val: str) -> None:...

    # Skipped WriteInt32 due to it being static, abstract and generic.

    WriteInt32 : WriteInt32_MethodGroup
    class WriteInt32_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int, val: int) -> None:...

    # Skipped WriteInt64 due to it being static, abstract and generic.

    WriteInt64 : WriteInt64_MethodGroup
    class WriteInt64_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int, val: int) -> None:...

    # Skipped WriteIntPtr due to it being static, abstract and generic.

    WriteIntPtr : WriteIntPtr_MethodGroup
    class WriteIntPtr_MethodGroup:
        @typing.overload
        def __call__(self, ptr: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: int, ofs: int, val: int) -> None:...
        @typing.overload
        def __call__(self, ptr: typing.Any, ofs: int, val: int) -> None:...



class MarshalAsAttribute(Attribute):
    @typing.overload
    def __init__(self, unmanagedType: UnmanagedType) -> None: ...
    @typing.overload
    def __init__(self, unmanagedType: int) -> None: ...
    ArraySubType : UnmanagedType
    IidParameterIndex : int
    MarshalCookie : str
    MarshalType : str
    MarshalTypeRef : typing.Type[typing.Any]
    SafeArraySubType : VarEnum
    SafeArrayUserDefinedSubType : typing.Type[typing.Any]
    SizeConst : int
    SizeParamIndex : int
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> UnmanagedType: ...


class MarshalDirectiveException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class MemoryMarshal(abc.ABC):
    @staticmethod
    def TryGetString(memory: ReadOnlyMemory_1[str], text: clr.Reference[str], start: clr.Reference[int], length: clr.Reference[int]) -> bool: ...
    # Skipped AsBytes due to it being static, abstract and generic.

    AsBytes : AsBytes_MethodGroup
    class AsBytes_MethodGroup:
        def __getitem__(self, t:typing.Type[AsBytes_1_T1]) -> AsBytes_1[AsBytes_1_T1]: ...

        AsBytes_1_T1 = typing.TypeVar('AsBytes_1_T1')
        class AsBytes_1(typing.Generic[AsBytes_1_T1]):
            AsBytes_1_T = MemoryMarshal.AsBytes_MethodGroup.AsBytes_1_T1
            @typing.overload
            def __call__(self, span: Span_1[AsBytes_1_T]) -> Span_1[int]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[AsBytes_1_T]) -> ReadOnlySpan_1[int]:...


    # Skipped AsMemory due to it being static, abstract and generic.

    AsMemory : AsMemory_MethodGroup
    class AsMemory_MethodGroup:
        def __getitem__(self, t:typing.Type[AsMemory_1_T1]) -> AsMemory_1[AsMemory_1_T1]: ...

        AsMemory_1_T1 = typing.TypeVar('AsMemory_1_T1')
        class AsMemory_1(typing.Generic[AsMemory_1_T1]):
            AsMemory_1_T = MemoryMarshal.AsMemory_MethodGroup.AsMemory_1_T1
            def __call__(self, memory: ReadOnlyMemory_1[AsMemory_1_T]) -> Memory_1[AsMemory_1_T]:...


    # Skipped AsRef due to it being static, abstract and generic.

    AsRef : AsRef_MethodGroup
    class AsRef_MethodGroup:
        def __getitem__(self, t:typing.Type[AsRef_1_T1]) -> AsRef_1[AsRef_1_T1]: ...

        AsRef_1_T1 = typing.TypeVar('AsRef_1_T1')
        class AsRef_1(typing.Generic[AsRef_1_T1]):
            AsRef_1_T = MemoryMarshal.AsRef_MethodGroup.AsRef_1_T1
            @typing.overload
            def __call__(self, span: Span_1[int]) -> clr.Reference[AsRef_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[int]) -> clr.Reference[AsRef_1_T]:...


    # Skipped Cast due to it being static, abstract and generic.

    Cast : Cast_MethodGroup
    class Cast_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Cast_2_T1], typing.Type[Cast_2_T2]]) -> Cast_2[Cast_2_T1, Cast_2_T2]: ...

        Cast_2_T1 = typing.TypeVar('Cast_2_T1')
        Cast_2_T2 = typing.TypeVar('Cast_2_T2')
        class Cast_2(typing.Generic[Cast_2_T1, Cast_2_T2]):
            Cast_2_TFrom = MemoryMarshal.Cast_MethodGroup.Cast_2_T1
            Cast_2_TTo = MemoryMarshal.Cast_MethodGroup.Cast_2_T2
            @typing.overload
            def __call__(self, span: Span_1[Cast_2_TFrom]) -> Span_1[Cast_2_TTo]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[Cast_2_TFrom]) -> ReadOnlySpan_1[Cast_2_TTo]:...


    # Skipped CreateFromPinnedArray due to it being static, abstract and generic.

    CreateFromPinnedArray : CreateFromPinnedArray_MethodGroup
    class CreateFromPinnedArray_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateFromPinnedArray_1_T1]) -> CreateFromPinnedArray_1[CreateFromPinnedArray_1_T1]: ...

        CreateFromPinnedArray_1_T1 = typing.TypeVar('CreateFromPinnedArray_1_T1')
        class CreateFromPinnedArray_1(typing.Generic[CreateFromPinnedArray_1_T1]):
            CreateFromPinnedArray_1_T = MemoryMarshal.CreateFromPinnedArray_MethodGroup.CreateFromPinnedArray_1_T1
            def __call__(self, array: Array_1[CreateFromPinnedArray_1_T], start: int, length: int) -> Memory_1[CreateFromPinnedArray_1_T]:...


    # Skipped CreateReadOnlySpan due to it being static, abstract and generic.

    CreateReadOnlySpan : CreateReadOnlySpan_MethodGroup
    class CreateReadOnlySpan_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateReadOnlySpan_1_T1]) -> CreateReadOnlySpan_1[CreateReadOnlySpan_1_T1]: ...

        CreateReadOnlySpan_1_T1 = typing.TypeVar('CreateReadOnlySpan_1_T1')
        class CreateReadOnlySpan_1(typing.Generic[CreateReadOnlySpan_1_T1]):
            CreateReadOnlySpan_1_T = MemoryMarshal.CreateReadOnlySpan_MethodGroup.CreateReadOnlySpan_1_T1
            def __call__(self, reference: clr.Reference[CreateReadOnlySpan_1_T], length: int) -> ReadOnlySpan_1[CreateReadOnlySpan_1_T]:...


    # Skipped CreateReadOnlySpanFromNullTerminated due to it being static, abstract and generic.

    CreateReadOnlySpanFromNullTerminated : CreateReadOnlySpanFromNullTerminated_MethodGroup
    class CreateReadOnlySpanFromNullTerminated_MethodGroup:
        @typing.overload
        def __call__(self, value: clr.Reference[str]) -> ReadOnlySpan_1[str]:...
        @typing.overload
        def __call__(self, value: clr.Reference[int]) -> ReadOnlySpan_1[int]:...

    # Skipped CreateSpan due to it being static, abstract and generic.

    CreateSpan : CreateSpan_MethodGroup
    class CreateSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateSpan_1_T1]) -> CreateSpan_1[CreateSpan_1_T1]: ...

        CreateSpan_1_T1 = typing.TypeVar('CreateSpan_1_T1')
        class CreateSpan_1(typing.Generic[CreateSpan_1_T1]):
            CreateSpan_1_T = MemoryMarshal.CreateSpan_MethodGroup.CreateSpan_1_T1
            def __call__(self, reference: clr.Reference[CreateSpan_1_T], length: int) -> Span_1[CreateSpan_1_T]:...


    # Skipped GetArrayDataReference due to it being static, abstract and generic.

    GetArrayDataReference : GetArrayDataReference_MethodGroup
    class GetArrayDataReference_MethodGroup:
        def __getitem__(self, t:typing.Type[GetArrayDataReference_1_T1]) -> GetArrayDataReference_1[GetArrayDataReference_1_T1]: ...

        GetArrayDataReference_1_T1 = typing.TypeVar('GetArrayDataReference_1_T1')
        class GetArrayDataReference_1(typing.Generic[GetArrayDataReference_1_T1]):
            GetArrayDataReference_1_T = MemoryMarshal.GetArrayDataReference_MethodGroup.GetArrayDataReference_1_T1
            def __call__(self, array: Array_1[GetArrayDataReference_1_T]) -> clr.Reference[GetArrayDataReference_1_T]:...

        def __call__(self, array: Array) -> clr.Reference[int]:...

    # Skipped GetReference due to it being static, abstract and generic.

    GetReference : GetReference_MethodGroup
    class GetReference_MethodGroup:
        def __getitem__(self, t:typing.Type[GetReference_1_T1]) -> GetReference_1[GetReference_1_T1]: ...

        GetReference_1_T1 = typing.TypeVar('GetReference_1_T1')
        class GetReference_1(typing.Generic[GetReference_1_T1]):
            GetReference_1_T = MemoryMarshal.GetReference_MethodGroup.GetReference_1_T1
            @typing.overload
            def __call__(self, span: Span_1[GetReference_1_T]) -> clr.Reference[GetReference_1_T]:...
            @typing.overload
            def __call__(self, span: ReadOnlySpan_1[GetReference_1_T]) -> clr.Reference[GetReference_1_T]:...


    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        def __getitem__(self, t:typing.Type[Read_1_T1]) -> Read_1[Read_1_T1]: ...

        Read_1_T1 = typing.TypeVar('Read_1_T1')
        class Read_1(typing.Generic[Read_1_T1]):
            Read_1_T = MemoryMarshal.Read_MethodGroup.Read_1_T1
            def __call__(self, source: ReadOnlySpan_1[int]) -> Read_1_T:...


    # Skipped ToEnumerable due to it being static, abstract and generic.

    ToEnumerable : ToEnumerable_MethodGroup
    class ToEnumerable_MethodGroup:
        def __getitem__(self, t:typing.Type[ToEnumerable_1_T1]) -> ToEnumerable_1[ToEnumerable_1_T1]: ...

        ToEnumerable_1_T1 = typing.TypeVar('ToEnumerable_1_T1')
        class ToEnumerable_1(typing.Generic[ToEnumerable_1_T1]):
            ToEnumerable_1_T = MemoryMarshal.ToEnumerable_MethodGroup.ToEnumerable_1_T1
            def __call__(self, memory: ReadOnlyMemory_1[ToEnumerable_1_T]) -> IEnumerable_1[ToEnumerable_1_T]:...


    # Skipped TryGetArray due to it being static, abstract and generic.

    TryGetArray : TryGetArray_MethodGroup
    class TryGetArray_MethodGroup:
        def __getitem__(self, t:typing.Type[TryGetArray_1_T1]) -> TryGetArray_1[TryGetArray_1_T1]: ...

        TryGetArray_1_T1 = typing.TypeVar('TryGetArray_1_T1')
        class TryGetArray_1(typing.Generic[TryGetArray_1_T1]):
            TryGetArray_1_T = MemoryMarshal.TryGetArray_MethodGroup.TryGetArray_1_T1
            def __call__(self, memory: ReadOnlyMemory_1[TryGetArray_1_T], segment: clr.Reference[ArraySegment_1[TryGetArray_1_T]]) -> bool:...


    # Skipped TryGetMemoryManager due to it being static, abstract and generic.

    TryGetMemoryManager : TryGetMemoryManager_MethodGroup
    class TryGetMemoryManager_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[TryGetMemoryManager_2_T1], typing.Type[TryGetMemoryManager_2_T2]]) -> TryGetMemoryManager_2[TryGetMemoryManager_2_T1, TryGetMemoryManager_2_T2]: ...

        TryGetMemoryManager_2_T1 = typing.TypeVar('TryGetMemoryManager_2_T1')
        TryGetMemoryManager_2_T2 = typing.TypeVar('TryGetMemoryManager_2_T2')
        class TryGetMemoryManager_2(typing.Generic[TryGetMemoryManager_2_T1, TryGetMemoryManager_2_T2]):
            TryGetMemoryManager_2_T = MemoryMarshal.TryGetMemoryManager_MethodGroup.TryGetMemoryManager_2_T1
            TryGetMemoryManager_2_TManager = MemoryMarshal.TryGetMemoryManager_MethodGroup.TryGetMemoryManager_2_T2
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[TryGetMemoryManager_2_T], manager: clr.Reference[TryGetMemoryManager_2_TManager]) -> bool:...
            @typing.overload
            def __call__(self, memory: ReadOnlyMemory_1[TryGetMemoryManager_2_T], manager: clr.Reference[TryGetMemoryManager_2_TManager], start: clr.Reference[int], length: clr.Reference[int]) -> bool:...


    # Skipped TryRead due to it being static, abstract and generic.

    TryRead : TryRead_MethodGroup
    class TryRead_MethodGroup:
        def __getitem__(self, t:typing.Type[TryRead_1_T1]) -> TryRead_1[TryRead_1_T1]: ...

        TryRead_1_T1 = typing.TypeVar('TryRead_1_T1')
        class TryRead_1(typing.Generic[TryRead_1_T1]):
            TryRead_1_T = MemoryMarshal.TryRead_MethodGroup.TryRead_1_T1
            def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[TryRead_1_T]) -> bool:...


    # Skipped TryWrite due to it being static, abstract and generic.

    TryWrite : TryWrite_MethodGroup
    class TryWrite_MethodGroup:
        def __getitem__(self, t:typing.Type[TryWrite_1_T1]) -> TryWrite_1[TryWrite_1_T1]: ...

        TryWrite_1_T1 = typing.TypeVar('TryWrite_1_T1')
        class TryWrite_1(typing.Generic[TryWrite_1_T1]):
            TryWrite_1_T = MemoryMarshal.TryWrite_MethodGroup.TryWrite_1_T1
            def __call__(self, destination: Span_1[int], value: clr.Reference[TryWrite_1_T]) -> bool:...


    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        def __getitem__(self, t:typing.Type[Write_1_T1]) -> Write_1[Write_1_T1]: ...

        Write_1_T1 = typing.TypeVar('Write_1_T1')
        class Write_1(typing.Generic[Write_1_T1]):
            Write_1_T = MemoryMarshal.Write_MethodGroup.Write_1_T1
            def __call__(self, destination: Span_1[int], value: clr.Reference[Write_1_T]) -> None:...




class NativeLibrary(abc.ABC):
    @staticmethod
    def Free(handle: int) -> None: ...
    @staticmethod
    def GetExport(handle: int, name: str) -> int: ...
    @staticmethod
    def SetDllImportResolver(assembly: Assembly, resolver: DllImportResolver) -> None: ...
    @staticmethod
    def TryGetExport(handle: int, name: str, address: clr.Reference[int]) -> bool: ...
    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        @typing.overload
        def __call__(self, libraryPath: str) -> int:...
        @typing.overload
        def __call__(self, libraryName: str, assembly: Assembly, searchPath: typing.Optional[DllImportSearchPath]) -> int:...

    # Skipped TryLoad due to it being static, abstract and generic.

    TryLoad : TryLoad_MethodGroup
    class TryLoad_MethodGroup:
        @typing.overload
        def __call__(self, libraryPath: str, handle: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, libraryName: str, assembly: Assembly, searchPath: typing.Optional[DllImportSearchPath], handle: clr.Reference[int]) -> bool:...



class NativeMemory(abc.ABC):
    @staticmethod
    def AlignedAlloc(byteCount: UIntPtr, alignment: UIntPtr) -> clr.Reference[None]: ...
    @staticmethod
    def AlignedFree(ptr: clr.Reference[None]) -> None: ...
    @staticmethod
    def AlignedRealloc(ptr: clr.Reference[None], byteCount: UIntPtr, alignment: UIntPtr) -> clr.Reference[None]: ...
    @staticmethod
    def Free(ptr: clr.Reference[None]) -> None: ...
    @staticmethod
    def Realloc(ptr: clr.Reference[None], byteCount: UIntPtr) -> clr.Reference[None]: ...
    # Skipped Alloc due to it being static, abstract and generic.

    Alloc : Alloc_MethodGroup
    class Alloc_MethodGroup:
        @typing.overload
        def __call__(self, byteCount: UIntPtr) -> clr.Reference[None]:...
        @typing.overload
        def __call__(self, elementCount: UIntPtr, elementSize: UIntPtr) -> clr.Reference[None]:...

    # Skipped AllocZeroed due to it being static, abstract and generic.

    AllocZeroed : AllocZeroed_MethodGroup
    class AllocZeroed_MethodGroup:
        @typing.overload
        def __call__(self, byteCount: UIntPtr) -> clr.Reference[None]:...
        @typing.overload
        def __call__(self, elementCount: UIntPtr, elementSize: UIntPtr) -> clr.Reference[None]:...



class NFloat(ISpanFormattable, IEquatable_1[NFloat], IComparable_1[NFloat], IComparable_0):
    # Constructor .ctor(value : Double) was skipped since it collides with above method
    def __init__(self, value: float) -> None: ...
    @classmethod
    @property
    def Epsilon(cls) -> NFloat: ...
    @classmethod
    @property
    def MaxValue(cls) -> NFloat: ...
    @classmethod
    @property
    def MinValue(cls) -> NFloat: ...
    @classmethod
    @property
    def NaN(cls) -> NFloat: ...
    @classmethod
    @property
    def NegativeInfinity(cls) -> NFloat: ...
    @classmethod
    @property
    def PositiveInfinity(cls) -> NFloat: ...
    @classmethod
    @property
    def Size(cls) -> int: ...
    @property
    def Value(self) -> float: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def IsFinite(value: NFloat) -> bool: ...
    @staticmethod
    def IsInfinity(value: NFloat) -> bool: ...
    @staticmethod
    def IsNaN(value: NFloat) -> bool: ...
    @staticmethod
    def IsNegative(value: NFloat) -> bool: ...
    @staticmethod
    def IsNegativeInfinity(value: NFloat) -> bool: ...
    @staticmethod
    def IsNormal(value: NFloat) -> bool: ...
    @staticmethod
    def IsPositiveInfinity(value: NFloat) -> bool: ...
    @staticmethod
    def IsSubnormal(value: NFloat) -> bool: ...
    def __add__(self, left: NFloat, right: NFloat) -> NFloat: ...
    # Operator not supported op_Decrement(value: NFloat)
    def __truediv__(self, left: NFloat, right: NFloat) -> NFloat: ...
    def __eq__(self, left: NFloat, right: NFloat) -> bool: ...
    # Operator not supported op_Explicit(value: Double)
    # Operator not supported op_Explicit(value: Decimal)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    # Operator not supported op_Explicit(value: NFloat)
    def __gt__(self, left: NFloat, right: NFloat) -> bool: ...
    def __ge__(self, left: NFloat, right: NFloat) -> bool: ...
    # Operator not supported op_Implicit(value: Single)
    # Operator not supported op_Implicit(value: Byte)
    # Operator not supported op_Implicit(value: Char)
    # Operator not supported op_Implicit(value: Int16)
    # Operator not supported op_Implicit(value: Int32)
    # Operator not supported op_Implicit(value: Int64)
    # Operator not supported op_Implicit(value: IntPtr)
    # Operator not supported op_Implicit(value: SByte)
    # Operator not supported op_Implicit(value: UInt16)
    # Operator not supported op_Implicit(value: UInt32)
    # Operator not supported op_Implicit(value: UInt64)
    # Operator not supported op_Implicit(value: UIntPtr)
    # Operator not supported op_Implicit(value: NFloat)
    # Operator not supported op_Increment(value: NFloat)
    def __ne__(self, left: NFloat, right: NFloat) -> bool: ...
    def __lt__(self, left: NFloat, right: NFloat) -> bool: ...
    def __le__(self, left: NFloat, right: NFloat) -> bool: ...
    def __mod__(self, left: NFloat, right: NFloat) -> NFloat: ...
    def __mul__(self, left: NFloat, right: NFloat) -> NFloat: ...
    def __sub__(self, left: NFloat, right: NFloat) -> NFloat: ...
    def __neg__(self, value: NFloat) -> NFloat: ...
    def __pos__(self, value: NFloat) -> NFloat: ...
    def TryFormat(self, destination: Span_1[str], charsWritten: clr.Reference[int], format: ReadOnlySpan_1[str] = ..., provider: IFormatProvider = ...) -> bool: ...
    # Skipped CompareTo due to it being static, abstract and generic.

    CompareTo : CompareTo_MethodGroup
    class CompareTo_MethodGroup:
        @typing.overload
        def __call__(self, other: NFloat) -> int:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> int:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: NFloat) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> NFloat:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles) -> NFloat:...
        @typing.overload
        def __call__(self, s: str, provider: IFormatProvider) -> NFloat:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles = ..., provider: IFormatProvider = ...) -> NFloat:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider) -> NFloat:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: str) -> str:...
        @typing.overload
        def __call__(self, provider: IFormatProvider) -> str:...
        @typing.overload
        def __call__(self, format: str, provider: IFormatProvider) -> str:...

    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], result: clr.Reference[NFloat]) -> bool:...
        @typing.overload
        def __call__(self, s: str, result: clr.Reference[NFloat]) -> bool:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[str], style: NumberStyles, provider: IFormatProvider, result: clr.Reference[NFloat]) -> bool:...
        @typing.overload
        def __call__(self, s: str, style: NumberStyles, provider: IFormatProvider, result: clr.Reference[NFloat]) -> bool:...



class OptionalAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class OutAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class PosixSignal(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    SIGTSTP : PosixSignal # -10
    SIGTTOU : PosixSignal # -9
    SIGTTIN : PosixSignal # -8
    SIGWINCH : PosixSignal # -7
    SIGCONT : PosixSignal # -6
    SIGCHLD : PosixSignal # -5
    SIGTERM : PosixSignal # -4
    SIGQUIT : PosixSignal # -3
    SIGINT : PosixSignal # -2
    SIGHUP : PosixSignal # -1


class PosixSignalContext:
    def __init__(self, signal: PosixSignal) -> None: ...
    @property
    def Cancel(self) -> bool: ...
    @Cancel.setter
    def Cancel(self, value: bool) -> bool: ...
    @property
    def Signal(self) -> PosixSignal: ...
    @Signal.setter
    def Signal(self, value: PosixSignal) -> PosixSignal: ...


class PosixSignalRegistration(IDisposable):
    @staticmethod
    def Create(signal: PosixSignal, handler: Action_1[PosixSignalContext]) -> PosixSignalRegistration: ...
    def Dispose(self) -> None: ...


class PreserveSigAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ProgIdAttribute(Attribute):
    def __init__(self, progId: str) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> str: ...


class SafeArrayRankMismatchException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class SafeArrayTypeMismatchException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class SafeBuffer(SafeHandleZeroOrMinusOneIsInvalid):
    @property
    def ByteLength(self) -> int: ...
    @property
    def IsClosed(self) -> bool: ...
    @property
    def IsInvalid(self) -> bool: ...
    def AcquirePointer(self, pointer: clr.Reference[clr.Reference[int]]) -> None: ...
    def ReleasePointer(self) -> None: ...
    # Skipped Initialize due to it being static, abstract and generic.

    Initialize : Initialize_MethodGroup
    class Initialize_MethodGroup:
        def __getitem__(self, t:typing.Type[Initialize_1_T1]) -> Initialize_1[Initialize_1_T1]: ...

        Initialize_1_T1 = typing.TypeVar('Initialize_1_T1')
        class Initialize_1(typing.Generic[Initialize_1_T1]):
            Initialize_1_T = SafeBuffer.Initialize_MethodGroup.Initialize_1_T1
            def __call__(self, numElements: int) -> None:...

        @typing.overload
        def __call__(self, numBytes: int) -> None:...
        @typing.overload
        def __call__(self, numElements: int, sizeOfEachElement: int) -> None:...

    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        def __getitem__(self, t:typing.Type[Read_1_T1]) -> Read_1[Read_1_T1]: ...

        Read_1_T1 = typing.TypeVar('Read_1_T1')
        class Read_1(typing.Generic[Read_1_T1]):
            Read_1_T = SafeBuffer.Read_MethodGroup.Read_1_T1
            def __call__(self, byteOffset: int) -> Read_1_T:...


    # Skipped ReadArray due to it being static, abstract and generic.

    ReadArray : ReadArray_MethodGroup
    class ReadArray_MethodGroup:
        def __getitem__(self, t:typing.Type[ReadArray_1_T1]) -> ReadArray_1[ReadArray_1_T1]: ...

        ReadArray_1_T1 = typing.TypeVar('ReadArray_1_T1')
        class ReadArray_1(typing.Generic[ReadArray_1_T1]):
            ReadArray_1_T = SafeBuffer.ReadArray_MethodGroup.ReadArray_1_T1
            def __call__(self, byteOffset: int, array: Array_1[ReadArray_1_T], index: int, count: int) -> None:...


    # Skipped ReadSpan due to it being static, abstract and generic.

    ReadSpan : ReadSpan_MethodGroup
    class ReadSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[ReadSpan_1_T1]) -> ReadSpan_1[ReadSpan_1_T1]: ...

        ReadSpan_1_T1 = typing.TypeVar('ReadSpan_1_T1')
        class ReadSpan_1(typing.Generic[ReadSpan_1_T1]):
            ReadSpan_1_T = SafeBuffer.ReadSpan_MethodGroup.ReadSpan_1_T1
            def __call__(self, byteOffset: int, buffer: Span_1[ReadSpan_1_T]) -> None:...


    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        def __getitem__(self, t:typing.Type[Write_1_T1]) -> Write_1[Write_1_T1]: ...

        Write_1_T1 = typing.TypeVar('Write_1_T1')
        class Write_1(typing.Generic[Write_1_T1]):
            Write_1_T = SafeBuffer.Write_MethodGroup.Write_1_T1
            def __call__(self, byteOffset: int, value: Write_1_T) -> None:...


    # Skipped WriteArray due to it being static, abstract and generic.

    WriteArray : WriteArray_MethodGroup
    class WriteArray_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteArray_1_T1]) -> WriteArray_1[WriteArray_1_T1]: ...

        WriteArray_1_T1 = typing.TypeVar('WriteArray_1_T1')
        class WriteArray_1(typing.Generic[WriteArray_1_T1]):
            WriteArray_1_T = SafeBuffer.WriteArray_MethodGroup.WriteArray_1_T1
            def __call__(self, byteOffset: int, array: Array_1[WriteArray_1_T], index: int, count: int) -> None:...


    # Skipped WriteSpan due to it being static, abstract and generic.

    WriteSpan : WriteSpan_MethodGroup
    class WriteSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteSpan_1_T1]) -> WriteSpan_1[WriteSpan_1_T1]: ...

        WriteSpan_1_T1 = typing.TypeVar('WriteSpan_1_T1')
        class WriteSpan_1(typing.Generic[WriteSpan_1_T1]):
            WriteSpan_1_T = SafeBuffer.WriteSpan_MethodGroup.WriteSpan_1_T1
            def __call__(self, byteOffset: int, data: ReadOnlySpan_1[WriteSpan_1_T]) -> None:...




class SafeHandle(CriticalFinalizerObject, IDisposable):
    @property
    def IsClosed(self) -> bool: ...
    @property
    def IsInvalid(self) -> bool: ...
    def Close(self) -> None: ...
    def DangerousAddRef(self, success: clr.Reference[bool]) -> None: ...
    def DangerousGetHandle(self) -> int: ...
    def DangerousRelease(self) -> None: ...
    def Dispose(self) -> None: ...
    def SetHandleAsInvalid(self) -> None: ...


class SEHException(ExternalException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def ErrorCode(self) -> int: ...
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
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    def CanResume(self) -> bool: ...


class StandardOleMarshalObject(MarshalByRefObject):
    pass


class StructLayoutAttribute(Attribute):
    @typing.overload
    def __init__(self, layoutKind: LayoutKind) -> None: ...
    @typing.overload
    def __init__(self, layoutKind: int) -> None: ...
    CharSet : CharSet
    Pack : int
    Size : int
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> LayoutKind: ...


class SuppressGCTransitionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class TypeIdentifierAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, scope: str, identifier: str) -> None: ...
    @property
    def Identifier(self) -> str: ...
    @property
    def Scope(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class UnknownWrapper:
    def __init__(self, obj: typing.Any) -> None: ...
    @property
    def WrappedObject(self) -> typing.Any: ...


class UnmanagedCallConvAttribute(Attribute):
    def __init__(self) -> None: ...
    CallConvs : Array_1[typing.Type[typing.Any]]
    @property
    def TypeId(self) -> typing.Any: ...


class UnmanagedCallersOnlyAttribute(Attribute):
    def __init__(self) -> None: ...
    CallConvs : Array_1[typing.Type[typing.Any]]
    EntryPoint : str
    @property
    def TypeId(self) -> typing.Any: ...


class UnmanagedFunctionPointerAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, callingConvention: CallingConvention) -> None: ...
    BestFitMapping : bool
    CharSet : CharSet
    SetLastError : bool
    ThrowOnUnmappableChar : bool
    @property
    def CallingConvention(self) -> CallingConvention: ...
    @property
    def TypeId(self) -> typing.Any: ...


class UnmanagedType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Bool : UnmanagedType # 2
    I1 : UnmanagedType # 3
    U1 : UnmanagedType # 4
    I2 : UnmanagedType # 5
    U2 : UnmanagedType # 6
    I4 : UnmanagedType # 7
    U4 : UnmanagedType # 8
    I8 : UnmanagedType # 9
    U8 : UnmanagedType # 10
    R4 : UnmanagedType # 11
    R8 : UnmanagedType # 12
    Currency : UnmanagedType # 15
    BStr : UnmanagedType # 19
    LPStr : UnmanagedType # 20
    LPWStr : UnmanagedType # 21
    LPTStr : UnmanagedType # 22
    ByValTStr : UnmanagedType # 23
    IUnknown : UnmanagedType # 25
    IDispatch : UnmanagedType # 26
    Struct : UnmanagedType # 27
    Interface : UnmanagedType # 28
    SafeArray : UnmanagedType # 29
    ByValArray : UnmanagedType # 30
    SysInt : UnmanagedType # 31
    SysUInt : UnmanagedType # 32
    VBByRefStr : UnmanagedType # 34
    AnsiBStr : UnmanagedType # 35
    TBStr : UnmanagedType # 36
    VariantBool : UnmanagedType # 37
    FunctionPtr : UnmanagedType # 38
    AsAny : UnmanagedType # 40
    LPArray : UnmanagedType # 42
    LPStruct : UnmanagedType # 43
    CustomMarshaler : UnmanagedType # 44
    Error : UnmanagedType # 45
    IInspectable : UnmanagedType # 46
    HString : UnmanagedType # 47
    LPUTF8Str : UnmanagedType # 48


class VarEnum(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    VT_EMPTY : VarEnum # 0
    VT_NULL : VarEnum # 1
    VT_I2 : VarEnum # 2
    VT_I4 : VarEnum # 3
    VT_R4 : VarEnum # 4
    VT_R8 : VarEnum # 5
    VT_CY : VarEnum # 6
    VT_DATE : VarEnum # 7
    VT_BSTR : VarEnum # 8
    VT_DISPATCH : VarEnum # 9
    VT_ERROR : VarEnum # 10
    VT_BOOL : VarEnum # 11
    VT_VARIANT : VarEnum # 12
    VT_UNKNOWN : VarEnum # 13
    VT_DECIMAL : VarEnum # 14
    VT_I1 : VarEnum # 16
    VT_UI1 : VarEnum # 17
    VT_UI2 : VarEnum # 18
    VT_UI4 : VarEnum # 19
    VT_I8 : VarEnum # 20
    VT_UI8 : VarEnum # 21
    VT_INT : VarEnum # 22
    VT_UINT : VarEnum # 23
    VT_VOID : VarEnum # 24
    VT_HRESULT : VarEnum # 25
    VT_PTR : VarEnum # 26
    VT_SAFEARRAY : VarEnum # 27
    VT_CARRAY : VarEnum # 28
    VT_USERDEFINED : VarEnum # 29
    VT_LPSTR : VarEnum # 30
    VT_LPWSTR : VarEnum # 31
    VT_RECORD : VarEnum # 36
    VT_FILETIME : VarEnum # 64
    VT_BLOB : VarEnum # 65
    VT_STREAM : VarEnum # 66
    VT_STORAGE : VarEnum # 67
    VT_STREAMED_OBJECT : VarEnum # 68
    VT_STORED_OBJECT : VarEnum # 69
    VT_BLOB_OBJECT : VarEnum # 70
    VT_CF : VarEnum # 71
    VT_CLSID : VarEnum # 72
    VT_VECTOR : VarEnum # 4096
    VT_ARRAY : VarEnum # 8192
    VT_BYREF : VarEnum # 16384


class VariantWrapper:
    def __init__(self, obj: typing.Any) -> None: ...
    @property
    def WrappedObject(self) -> typing.Any: ...

