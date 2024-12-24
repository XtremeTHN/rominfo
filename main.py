import pythonnet

pythonnet.set_runtime("coreclr")

import clr
clr.AddReference("LibHac")

from LibHac.Common.Keys import ExternalKeyReader
from LibHac.Tools.FsSystem import StreamStorage, StorageStream
from LibHac.Fs import FileStorage, OpenMode
from LibHac.FsSystem import PartitionFileSystem
from LibHac.Ncm import ContentMetaType, ContentType
from LibHac.Tools.Ncm import Cnmt, CnmtContentEntry
from LibHac.Tools.FsSystem import NxFileStream
from LibHac.Tools.FsSystem.RomFs import RomFsFileSystem
from LibHac.Tools.FsSystem.NcaUtils import Nca
from LibHac.Tools.FsSystem import IntegrityCheckLevel

from System.IO import FileStream, FileMode, FileAccess, StreamReader
from System import BitConverter

keys = ExternalKeyReader.ReadKeyFile("prod.keys")

stream = FileStream("smpj.nsp", FileMode.Open, FileAccess.Read)
storage = StreamStorage(stream, True)

pfs = PartitionFileSystem(storage)

def processCmnt(file):
    file = StorageStream(file, FileAccess.Read, True)
    reader = StreamReader(file)
    content = reader.ReadToEnd()
    reader.Dispose()
    file.Dispose()
    print(content)

def processCnmtNca(nca: Nca):
    ncaPfs = PartitionFileSystem(nca.OpenStorage(0, IntegrityCheckLevel.ErrorOnInvalid, True))
    for pfile in ncaPfs.Files:
        stream = NxFileStream(ncaPfs.OpenFile(pfile, OpenMode.Read), True)
        cnmt = Cnmt(stream)
        print(cnmt.TitleVersion.Version)
        print(cnmt.Type)

        biggestNca, controlNca = None, None
        entries: list[CnmtContentEntry] = cnmt.ContentEntries
        for cEntry in entries:
            print(cEntry.Type)
            if cnmt.Type in [ContentMetaType.Application, ContentMetaType.Patch]:
                if cEntry.Type == ContentType.Program:
                    biggestNca = BitConverter.ToString(cEntry.NcaId).replace("-", "").lower() + ".nca"
                elif cEntry.Type == ContentType.Control:
                    controlNca = BitConverter.ToString(cEntry.NcaId).replace("-", "").lower() + ".nca"

        # print(biggestNca, controlNca)
        stream.Close()
        stream.Dispose()

    ncaPfs.Dispose()
    return biggestNca, controlNca

def processControlNca(nca: Nca):
    romfs = RomFsFileSystem(nca.OpenStorage(0, IntegrityCheckLevel.ErrorOnInvalid))
    print(romfs.FileTable)
    # print(BitConverter.ToString(romfs.FileTable.GetFileEntries()))

def processNacpXml(file):
    stream = StorageStream(file, FileAccess.Read, True)
    reader = StreamReader(stream)
    content = reader.ReadToEnd()
    reader.Dispose()
    stream.Dispose()
    print(content)

for pfile in pfs.Files:
    if pfile.Name.endswith(".cnmt.xml"):
        processCmnt(pfs.OpenFile(pfile))
    elif pfile.Name.endswith(".cnmt.nca"):
        nca = Nca(keys, FileStorage(pfs.OpenFile(pfile, OpenMode.Read)))
        _, control = processCnmtNca(nca)
        for control_pfile in pfs.Files:
            if control_pfile.Name == control:
                controlNca = Nca(keys, FileStorage(pfs.OpenFile(control_pfile, OpenMode.Read)))
                processControlNca(controlNca)
    elif pfile.Name.endswith(".nacp.xml"):
        processNacpXml(pfs.OpenFile(pfile))


pfs.Dispose()
storage.Dispose()
stream.Close()
stream.Dispose()