import typing
from System import SystemException, Exception, Array_1
from System.Collections import IDictionary
from System.Reflection import MethodBase

class CipherMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    CBC : CipherMode # 1
    ECB : CipherMode # 2
    OFB : CipherMode # 3
    CFB : CipherMode # 4
    CTS : CipherMode # 5


class CryptographicException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, format: str, insert: str) -> None: ...
    @typing.overload
    def __init__(self, hr: int) -> None: ...
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


class RSAParameters:
    D : Array_1[int]
    DP : Array_1[int]
    DQ : Array_1[int]
    Exponent : Array_1[int]
    InverseQ : Array_1[int]
    Modulus : Array_1[int]
    P : Array_1[int]
    Q : Array_1[int]

