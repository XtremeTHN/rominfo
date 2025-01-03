import typing, clr
from System import ReadOnlySpan_1, Span_1, Array_1
from System.Runtime.Intrinsics import Vector128_1
from System.Security.Cryptography import CipherMode
from LibHac.Common import Buffer16

class AesCbcMode:
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int], isDecrypting: bool) -> None: ...


class AesCbcModeNi:
    Iv : Vector128_1[int]
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int], isDecrypting: bool) -> None: ...


class AesCore:
    def Initialize(self, key: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int], mode: CipherMode, isDecrypting: bool) -> None: ...
    # Skipped Decrypt due to it being static, abstract and generic.

    Decrypt : Decrypt_MethodGroup
    class Decrypt_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, input: Array_1[int], output: Array_1[int], length: int) -> int:...

    # Skipped Encrypt due to it being static, abstract and generic.

    Encrypt : Encrypt_MethodGroup
    class Encrypt_MethodGroup:
        @typing.overload
        def __call__(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, input: Array_1[int], output: Array_1[int], length: int) -> int:...



class AesCoreNi:
    @property
    def RoundKeys(self) -> ReadOnlySpan_1[Vector128_1[int]]: ...
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> None: ...
    def DecryptBlocks8(self, in0: Vector128_1[int], in1: Vector128_1[int], in2: Vector128_1[int], in3: Vector128_1[int], in4: Vector128_1[int], in5: Vector128_1[int], in6: Vector128_1[int], in7: Vector128_1[int], out0: clr.Reference[Vector128_1[int]], out1: clr.Reference[Vector128_1[int]], out2: clr.Reference[Vector128_1[int]], out3: clr.Reference[Vector128_1[int]], out4: clr.Reference[Vector128_1[int]], out5: clr.Reference[Vector128_1[int]], out6: clr.Reference[Vector128_1[int]], out7: clr.Reference[Vector128_1[int]]) -> None: ...
    def DecryptInterleaved8(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> None: ...
    def EncryptBlocks8(self, in0: Vector128_1[int], in1: Vector128_1[int], in2: Vector128_1[int], in3: Vector128_1[int], in4: Vector128_1[int], in5: Vector128_1[int], in6: Vector128_1[int], in7: Vector128_1[int], out0: clr.Reference[Vector128_1[int]], out1: clr.Reference[Vector128_1[int]], out2: clr.Reference[Vector128_1[int]], out3: clr.Reference[Vector128_1[int]], out4: clr.Reference[Vector128_1[int]], out5: clr.Reference[Vector128_1[int]], out6: clr.Reference[Vector128_1[int]], out7: clr.Reference[Vector128_1[int]]) -> None: ...
    def EncryptInterleaved8(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key: ReadOnlySpan_1[int], isDecrypting: bool) -> None: ...
    # Skipped DecryptBlock due to it being static, abstract and generic.

    DecryptBlock : DecryptBlock_MethodGroup
    class DecryptBlock_MethodGroup:
        @typing.overload
        def __call__(self, input: Vector128_1[int]) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, input: Vector128_1[int], key: Vector128_1[int]) -> Vector128_1[int]:...

    # Skipped EncryptBlock due to it being static, abstract and generic.

    EncryptBlock : EncryptBlock_MethodGroup
    class EncryptBlock_MethodGroup:
        @typing.overload
        def __call__(self, input: Vector128_1[int]) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, input: Vector128_1[int], key: Vector128_1[int]) -> Vector128_1[int]:...



class AesCtrMode:
    Iv : Buffer16
    def Initialize(self, key: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int]) -> None: ...
    def Transform(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...


class AesCtrModeNi:
    Iv : Vector128_1[int]
    def Initialize(self, key: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int]) -> None: ...
    def Transform(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...


class AesEcbMode:
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key: ReadOnlySpan_1[int], isDecrypting: bool) -> None: ...


class AesEcbModeNi:
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key: ReadOnlySpan_1[int], isDecrypting: bool) -> None: ...


class AesXtsMode:
    Iv : Buffer16
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key1: ReadOnlySpan_1[int], key2: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int], isDecrypting: bool) -> None: ...


class AesXtsModeNi:
    Iv : Vector128_1[int]
    def Decrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Encrypt(self, input: ReadOnlySpan_1[int], output: Span_1[int]) -> int: ...
    def Initialize(self, key1: ReadOnlySpan_1[int], key2: ReadOnlySpan_1[int], iv: ReadOnlySpan_1[int], decrypting: bool) -> None: ...


class HashState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Initial : HashState # 0
    Initialized : HashState # 1
    Done : HashState # 2


class Sha256Impl:
    def GetHash(self, hashBuffer: Span_1[int]) -> None: ...
    def Initialize(self) -> None: ...
    def Update(self, data: ReadOnlySpan_1[int]) -> None: ...

