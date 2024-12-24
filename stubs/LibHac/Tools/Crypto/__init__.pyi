import typing, clr, abc
from LibHac.Common import Validity
from System import Array_1, ReadOnlySpan_1, Span_1
from System.Security.Cryptography import RSAParameters

class CryptoOld(abc.ABC):
    @staticmethod
    def Rsa2048Pkcs1Verify(data: Array_1[int], signature: Array_1[int], modulus: Array_1[int]) -> Validity: ...
    @staticmethod
    def Rsa2048PssVerify(data: Array_1[int], signature: Array_1[int], modulus: Array_1[int]) -> Validity: ...
    # Skipped DecryptRsaOaep due to it being static, abstract and generic.

    DecryptRsaOaep : DecryptRsaOaep_MethodGroup
    class DecryptRsaOaep_MethodGroup:
        @typing.overload
        def __call__(self, data: Array_1[int], rsaParams: RSAParameters) -> Array_1[int]:...
        @typing.overload
        def __call__(self, data: ReadOnlySpan_1[int], destination: Span_1[int], rsaParams: RSAParameters, bytesWritten: clr.Reference[int]) -> bool:...


