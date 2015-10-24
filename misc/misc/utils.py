# -*- coding:utf-8 -*-
import sys
import glob
import os.path
import contextlib


def get_dirpath_and_filepath(path):
    """dirpath, filepathのtupleを返す"""
    if os.path.isdir(path):
        return path, None
    else:
        return os.path.dirname(path), path


def iterate_file_or_directory(path, glob_arg="*"):
    """渡されたdirectory pathまたはfile pathを元にiteratorを生成"""
    if os.path.exists(path):
        if os.path.isdir(path):
            for path in glob.glob(os.path.join(path, glob_arg)):
                yield path
        else:
            yield path


def is_file(outfile):
    return os.path.isfile(outfile) or (os.path.splitext(outfile)[1] != '' and not outfile.endswith("/"))


class FileOrPortOpener(object):
    def __init__(self, outfile=None, port=sys.stdout):
        self.outfile = outfile
        self.port = port
        self.outfile_is_file = outfile is not None and is_file(outfile)
        self.is_first = True

    @contextlib.contextmanager
    def open(self, path, mode="r", **kwargs):
        if self.outfile is None:
            yield self.port
        elif self.outfile_is_file:
            if not self.is_first and mode.startswith("w"):
                mode = "a{}".format(mode[1:])
            with open(self.outfile, mode=mode, **kwargs) as port:
                yield port
        else:
            path = os.path.join(self.outfile, os.path.basename(path))
            with open(path, mode=mode, **kwargs) as port:
                yield port
        if self.is_first:
            self.is_first = False

    __call__ = open
