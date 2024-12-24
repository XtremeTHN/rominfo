import abc
from LibHac.Gc.Impl import CardId1, CardId2, CardId3
from LibHac.Common.FixedArrays import Array32_1, Array3_1, Array11_1, Array512_1

class GameCardIdSet:
    Id1 : CardId1
    Id2 : CardId2
    Id3 : CardId3


class GameCardStatus:
    CompatibilityType : int
    GameCardAttribute : int
    PackageId : int
    PartitionFsHeaderHash : Array32_1[int]
    PartitionFsHeaderOffset : int
    PartitionFsHeaderSize : int
    Reserved61 : Array3_1[int]
    Reserved65 : Array11_1[int]
    SecureAreaOffset : int
    SecureAreaSize : int
    Size : int
    UpdatePartitionId : int
    UpdatePartitionVersion : int


class RmaInformation:
    Data : Array512_1[int]


class Values(abc.ABC):
    @classmethod
    @property
    def GcAsicFirmwareSize(cls) -> int: ...
    @classmethod
    @property
    def GcCardDeviceIdSize(cls) -> int: ...
    @classmethod
    @property
    def GcCardExistenceResponseDataSize(cls) -> int: ...
    @classmethod
    @property
    def GcCardImageHashSize(cls) -> int: ...
    @classmethod
    @property
    def GcDeviceCertificateSize(cls) -> int: ...
    @classmethod
    @property
    def GcPageSize(cls) -> int: ...

