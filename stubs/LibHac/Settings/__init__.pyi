import typing

class Language(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Japanese : Language # 0
    AmericanEnglish : Language # 1
    French : Language # 2
    German : Language # 3
    Italian : Language # 4
    Spanish : Language # 5
    Chinese : Language # 6
    Korean : Language # 7
    Dutch : Language # 8
    Portuguese : Language # 9
    Russian : Language # 10
    Taiwanese : Language # 11
    BritishEnglish : Language # 12
    CanadianFrench : Language # 13
    LatinAmericanSpanish : Language # 14
    SimplifiedChinese : Language # 15
    TraditionalChinese : Language # 16
    BrazilianPortuguese : Language # 17

