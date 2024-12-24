import pythonnet

pythonnet.set_runtime("coreclr")

import clr
clr.AddReference("LibHac")

from LibHac.Common.Keys import ExternalKeyReader
from LibHac.Tools.FsSystem import StreamStorage, StorageStream
from LibHac.Fs import OpenMode
from LibHac.Fs import FileStorage
from LibHac.FsSystem import PartitionFileSystem
from LibHac.Tools.Ncm import Cnmt
from LibHac.Tools.FsSystem import NxFileStream
from LibHac.Tools.FsSystem.NcaUtils import Nca
from LibHac.Tools.FsSystem import IntegrityCheckLevel

from System.IO import FileStream, FileMode, FileAccess, StreamReader

keys = ExternalKeyReader.ReadKeyFile("prod.keys")

stream = FileStream("smpj.nsp", FileMode.Open, FileAccess.Read)
storage = StreamStorage(stream, True)

pfs = PartitionFileSystem(storage)

def processCmnt(file):
    file = StorageStream(file, FileAccess.Read, True)
    reader = StreamReader(file)
    content = reader.ReadToEnd()
    print(content)

def processCnmtNca(nca: Nca):
    ncaPfs = PartitionFileSystem(nca.OpenStorage(0, IntegrityCheckLevel.ErrorOnInvalid, True))
    print(ncaPfs.Files.Length)
    for pfile in ncaPfs.Files:
        cnmt = Cnmt(NxFileStream(ncaPfs.OpenFile(pfile, OpenMode.Read), OpenMode.Read, True))
        # print(*[f"{k}: {v}" for k, v in cnmt.__dict__.items()], sep="\n")
        for attr in dir(cnmt):
            print(attr, getattr(cnmt, attr))

for pfile in pfs.Files:
    if pfile.Name.endswith(".cnmt.xml"):
        processCmnt(pfs.OpenFile(pfile))
    elif pfile.Name.endswith(".cnmt.nca"):
        print(pfile, type(pfile))
        nca = Nca(keys, FileStorage(pfs.OpenFile(pfile, OpenMode.Read)))
        processCnmtNca(nca)