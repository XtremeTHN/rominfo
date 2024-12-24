import typing, clr, abc
from System import ReadOnlySpan_1, Span_1, Array_1, IDisposable
from LibHac.Common import U8Span

class Alignment(abc.ABC):
    # Skipped AlignDown due to it being static, abstract and generic.

    AlignDown : AlignDown_MethodGroup
    class AlignDown_MethodGroup:
        def __call__(self, value: int, alignment: int) -> int:...
        # Method AlignDown(value : Int32, alignment : UInt32) was skipped since it collides with above method
        # Method AlignDown(value : Int64, alignment : UInt32) was skipped since it collides with above method

    # Skipped AlignDownPow2 due to it being static, abstract and generic.

    AlignDownPow2 : AlignDownPow2_MethodGroup
    class AlignDownPow2_MethodGroup:
        def __call__(self, value: int, alignment: int) -> int:...
        # Method AlignDownPow2(value : Int32, alignment : UInt32) was skipped since it collides with above method
        # Method AlignDownPow2(value : Int64, alignment : UInt32) was skipped since it collides with above method
        # Method AlignDownPow2(value : Int64, alignment : Int64) was skipped since it collides with above method

    # Skipped AlignUp due to it being static, abstract and generic.

    AlignUp : AlignUp_MethodGroup
    class AlignUp_MethodGroup:
        def __call__(self, value: int, alignment: int) -> int:...
        # Method AlignUp(value : Int32, alignment : UInt32) was skipped since it collides with above method
        # Method AlignUp(value : Int64, alignment : UInt32) was skipped since it collides with above method

    # Skipped AlignUpPow2 due to it being static, abstract and generic.

    AlignUpPow2 : AlignUpPow2_MethodGroup
    class AlignUpPow2_MethodGroup:
        def __call__(self, value: int, alignment: int) -> int:...
        # Method AlignUpPow2(value : Int32, alignment : UInt32) was skipped since it collides with above method
        # Method AlignUpPow2(value : Int64, alignment : UInt32) was skipped since it collides with above method

    # Skipped IsAligned due to it being static, abstract and generic.

    IsAligned : IsAligned_MethodGroup
    class IsAligned_MethodGroup:
        def __call__(self, value: int, alignment: int) -> bool:...
        # Method IsAligned(value : Int32, alignment : UInt32) was skipped since it collides with above method
        # Method IsAligned(value : Int64, alignment : UInt32) was skipped since it collides with above method

    # Skipped IsAlignedPow2 due to it being static, abstract and generic.

    IsAlignedPow2 : IsAlignedPow2_MethodGroup
    class IsAlignedPow2_MethodGroup:
        def __getitem__(self, t:typing.Type[IsAlignedPow2_1_T1]) -> IsAlignedPow2_1[IsAlignedPow2_1_T1]: ...

        IsAlignedPow2_1_T1 = typing.TypeVar('IsAlignedPow2_1_T1')
        class IsAlignedPow2_1(typing.Generic[IsAlignedPow2_1_T1]):
            IsAlignedPow2_1_T = Alignment.IsAlignedPow2_MethodGroup.IsAlignedPow2_1_T1
            @typing.overload
            def __call__(self, buffer: ReadOnlySpan_1[IsAlignedPow2_1_T], alignment: int) -> bool:...
            @typing.overload
            def __call__(self, pointer: clr.Reference[IsAlignedPow2_1_T], alignment: int) -> bool:...

        def __call__(self, value: int, alignment: int) -> bool:...
        # Method IsAlignedPow2(value : Int32, alignment : UInt32) was skipped since it collides with above method
        # Method IsAlignedPow2(value : Int64, alignment : UInt32) was skipped since it collides with above method



class BitUtil(abc.ABC):
    @staticmethod
    def CountLeadingZeros(value: int) -> int: ...
    # Skipped DivideUp due to it being static, abstract and generic.

    DivideUp : DivideUp_MethodGroup
    class DivideUp_MethodGroup:
        def __call__(self, value: int, divisor: int) -> int:...
        # Method DivideUp(value : UInt64, divisor : UInt64) was skipped since it collides with above method
        # Method DivideUp(value : Int32, divisor : Int32) was skipped since it collides with above method
        # Method DivideUp(value : Int64, divisor : Int64) was skipped since it collides with above method

    # Skipped IsPowerOfTwo due to it being static, abstract and generic.

    IsPowerOfTwo : IsPowerOfTwo_MethodGroup
    class IsPowerOfTwo_MethodGroup:
        def __call__(self, value: int) -> bool:...
        # Method IsPowerOfTwo(value : Int64) was skipped since it collides with above method
        # Method IsPowerOfTwo(value : UInt64) was skipped since it collides with above method



class CharacterEncoding(abc.ABC):
    @staticmethod
    def ConvertCharacterUtf32ToUtf8(destination: Span_1[int], source: int) -> CharacterEncodingResult: ...
    @staticmethod
    def ConvertCharacterUtf8ToUtf32(destination: clr.Reference[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult: ...
    @staticmethod
    def PickOutCharacterFromUtf8String(destinationChar: Span_1[int], source: clr.Reference[ReadOnlySpan_1[int]]) -> CharacterEncodingResult: ...
    # Skipped ConvertCharacterUtf16NativeToUtf8 due to it being static, abstract and generic.

    ConvertCharacterUtf16NativeToUtf8 : ConvertCharacterUtf16NativeToUtf8_MethodGroup
    class ConvertCharacterUtf16NativeToUtf8_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[str]) -> CharacterEncodingResult:...

    # Skipped ConvertCharacterUtf8ToUtf16Native due to it being static, abstract and generic.

    ConvertCharacterUtf8ToUtf16Native : ConvertCharacterUtf8ToUtf16Native_MethodGroup
    class ConvertCharacterUtf8ToUtf16Native_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[str], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...

    # Skipped ConvertStringUtf16NativeToUtf8 due to it being static, abstract and generic.

    ConvertStringUtf16NativeToUtf8 : ConvertStringUtf16NativeToUtf8_MethodGroup
    class ConvertStringUtf16NativeToUtf8_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[str]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[str], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped ConvertStringUtf32ToUtf8 due to it being static, abstract and generic.

    ConvertStringUtf32ToUtf8 : ConvertStringUtf32ToUtf8_MethodGroup
    class ConvertStringUtf32ToUtf8_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped ConvertStringUtf8ToUtf16Native due to it being static, abstract and generic.

    ConvertStringUtf8ToUtf16Native : ConvertStringUtf8ToUtf16Native_MethodGroup
    class ConvertStringUtf8ToUtf16Native_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[str], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[str], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped ConvertStringUtf8ToUtf32 due to it being static, abstract and generic.

    ConvertStringUtf8ToUtf32 : ConvertStringUtf8ToUtf32_MethodGroup
    class ConvertStringUtf8ToUtf32_MethodGroup:
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, destination: Span_1[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped GetLengthOfConvertedStringUtf16NativeToUtf8 due to it being static, abstract and generic.

    GetLengthOfConvertedStringUtf16NativeToUtf8 : GetLengthOfConvertedStringUtf16NativeToUtf8_MethodGroup
    class GetLengthOfConvertedStringUtf16NativeToUtf8_MethodGroup:
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[str]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[str], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped GetLengthOfConvertedStringUtf32ToUtf8 due to it being static, abstract and generic.

    GetLengthOfConvertedStringUtf32ToUtf8 : GetLengthOfConvertedStringUtf32ToUtf8_MethodGroup
    class GetLengthOfConvertedStringUtf32ToUtf8_MethodGroup:
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped GetLengthOfConvertedStringUtf8ToUtf16Native due to it being static, abstract and generic.

    GetLengthOfConvertedStringUtf8ToUtf16Native : GetLengthOfConvertedStringUtf8ToUtf16Native_MethodGroup
    class GetLengthOfConvertedStringUtf8ToUtf16Native_MethodGroup:
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...

    # Skipped GetLengthOfConvertedStringUtf8ToUtf32 due to it being static, abstract and generic.

    GetLengthOfConvertedStringUtf8ToUtf32 : GetLengthOfConvertedStringUtf8ToUtf32_MethodGroup
    class GetLengthOfConvertedStringUtf8ToUtf32_MethodGroup:
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int]) -> CharacterEncodingResult:...
        @typing.overload
        def __call__(self, length: clr.Reference[int], source: ReadOnlySpan_1[int], sourceLength: int) -> CharacterEncodingResult:...



class CharacterEncodingResult(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Success : CharacterEncodingResult # 0
    InsufficientLength : CharacterEncodingResult # 1
    InvalidFormat : CharacterEncodingResult # 2


class IntUtil(abc.ABC):
    @staticmethod
    def IsIntValueRepresentableAsInt(value: int) -> bool: ...
    @staticmethod
    def IsIntValueRepresentableAsLong(value: int) -> bool: ...
    @staticmethod
    def IsIntValueRepresentableAsUInt(value: int) -> bool: ...
    @staticmethod
    def IsIntValueRepresentableAsULong(value: int) -> bool: ...
    # Skipped CanAddWithoutOverflow due to it being static, abstract and generic.

    CanAddWithoutOverflow : CanAddWithoutOverflow_MethodGroup
    class CanAddWithoutOverflow_MethodGroup:
        def __call__(self, x: int, y: int) -> bool:...
        # Method CanAddWithoutOverflow(x : UInt64, y : UInt64) was skipped since it collides with above method



class Lz4(abc.ABC):
    # Skipped Decompress due to it being static, abstract and generic.

    Decompress : Decompress_MethodGroup
    class Decompress_MethodGroup:
        @typing.overload
        def __call__(self, cmp: Array_1[int], decLength: int) -> Array_1[int]:...
        @typing.overload
        def __call__(self, cmp: ReadOnlySpan_1[int], dec: Span_1[int]) -> None:...



class Optional_GenericClasses(abc.ABCMeta):
    Generic_Optional_GenericClasses_Optional_1_T = typing.TypeVar('Generic_Optional_GenericClasses_Optional_1_T')
    def __getitem__(self, types : typing.Type[Generic_Optional_GenericClasses_Optional_1_T]) -> typing.Type[Optional_1[Generic_Optional_GenericClasses_Optional_1_T]]: ...

Optional : Optional_GenericClasses

Optional_1_T = typing.TypeVar('Optional_1_T')
class Optional_1(typing.Generic[Optional_1_T]):
    @typing.overload
    def __init__(self, value: clr.Reference[Optional_1_T]) -> None: ...
    @typing.overload
    def __init__(self, value: Optional_1_T) -> None: ...
    @property
    def HasValue(self) -> bool: ...
    @property
    def Value(self) -> clr.Reference[Optional_1_T]: ...
    @property
    def ValueRo(self) -> clr.Reference[Optional_1_T]: ...
    def Clear(self) -> None: ...
    # Operator not supported op_Implicit(value: T&)
    # Skipped Set due to it being static, abstract and generic.

    Set : Set_MethodGroup[Optional_1_T]
    Set_MethodGroup_Optional_1_T = typing.TypeVar('Set_MethodGroup_Optional_1_T')
    class Set_MethodGroup(typing.Generic[Set_MethodGroup_Optional_1_T]):
        Set_MethodGroup_Optional_1_T = Optional_1.Set_MethodGroup_Optional_1_T
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, value: Set_MethodGroup_Optional_1_T) -> None:...
        @typing.overload
        def __call__(self, value: clr.Reference[Set_MethodGroup_Optional_1_T]) -> None:...



class Overlap(abc.ABC):
    @staticmethod
    def Contains(start: int, size: int, value: int) -> bool: ...
    @staticmethod
    def HasOverlap(start0: int, size0: int, start1: int, size1: int) -> bool: ...


class StringUtils(abc.ABC):
    @staticmethod
    def Find(haystack: ReadOnlySpan_1[int], needle: ReadOnlySpan_1[int]) -> int: ...
    @staticmethod
    def IsAlpha(c: int) -> bool: ...
    @staticmethod
    def IsDigit(c: int) -> bool: ...
    @staticmethod
    def IsHexDigit(c: int) -> bool: ...
    @staticmethod
    def NullTerminatedUtf8ToString(value: ReadOnlySpan_1[int]) -> str: ...
    @staticmethod
    def StringToUtf8(value: str) -> ReadOnlySpan_1[int]: ...
    @staticmethod
    def Strlcpy(dest: Span_1[int], source: ReadOnlySpan_1[int], maxLen: int) -> int: ...
    @staticmethod
    def ToBytes(input: str) -> Array_1[int]: ...
    @staticmethod
    def TryFromHexString(chars: ReadOnlySpan_1[str], outputBytes: Span_1[int]) -> bool: ...
    @staticmethod
    def Utf8ToString(value: ReadOnlySpan_1[int]) -> str: ...
    @staticmethod
    def Utf8ZToString(value: ReadOnlySpan_1[int]) -> str: ...
    # Skipped Compare due to it being static, abstract and generic.

    Compare : Compare_MethodGroup
    class Compare_MethodGroup:
        @typing.overload
        def __call__(self, s1: ReadOnlySpan_1[int], s2: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, s1: ReadOnlySpan_1[int], s2: ReadOnlySpan_1[int], maxLen: int) -> int:...

    # Skipped CompareCaseInsensitive due to it being static, abstract and generic.

    CompareCaseInsensitive : CompareCaseInsensitive_MethodGroup
    class CompareCaseInsensitive_MethodGroup:
        @typing.overload
        def __call__(self, s1: ReadOnlySpan_1[int], s2: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, s1: ReadOnlySpan_1[int], s2: ReadOnlySpan_1[int], maxLen: int) -> int:...

    # Skipped Concat due to it being static, abstract and generic.

    Concat : Concat_MethodGroup
    class Concat_MethodGroup:
        @typing.overload
        def __call__(self, dest: Span_1[int], source: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, dest: Span_1[int], source: ReadOnlySpan_1[int], destLength: int) -> int:...

    # Skipped Copy due to it being static, abstract and generic.

    Copy : Copy_MethodGroup
    class Copy_MethodGroup:
        @typing.overload
        def __call__(self, dest: Span_1[int], source: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, dest: Span_1[int], source: ReadOnlySpan_1[int], maxLen: int) -> int:...

    # Skipped FromHexString due to it being static, abstract and generic.

    FromHexString : FromHexString_MethodGroup
    class FromHexString_MethodGroup:
        @typing.overload
        def __call__(self, input: str) -> Array_1[int]:...
        @typing.overload
        def __call__(self, chars: ReadOnlySpan_1[str], outputBytes: Span_1[int]) -> None:...

    # Skipped GetLength due to it being static, abstract and generic.

    GetLength : GetLength_MethodGroup
    class GetLength_MethodGroup:
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[int]) -> int:...
        @typing.overload
        def __call__(self, s: ReadOnlySpan_1[int], maxLen: int) -> int:...

    # Skipped ToHexString due to it being static, abstract and generic.

    ToHexString : ToHexString_MethodGroup
    class ToHexString_MethodGroup:
        @typing.overload
        def __call__(self, bytes: Array_1[int]) -> str:...
        @typing.overload
        def __call__(self, bytes: Span_1[int]) -> str:...
        @typing.overload
        def __call__(self, bytes: ReadOnlySpan_1[int]) -> str:...



class UniqueLock(IDisposable):
    @typing.overload
    def __init__(self, lockObject: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, other: clr.Reference[UniqueLock]) -> None: ...
    @property
    def IsLocked(self) -> bool: ...
    def Dispose(self) -> None: ...
    def Lock(self) -> None: ...
    def Unlock(self) -> None: ...


class Utf8StringUtil(abc.ABC):
    @staticmethod
    def CopyUtf8String(output: Span_1[int], input: ReadOnlySpan_1[int], maxCount: int) -> int: ...
    @staticmethod
    def GetCodePointCountOfUtf8String(str: U8Span) -> int: ...
    @staticmethod
    def VerifyUtf8String(str: U8Span) -> bool: ...

