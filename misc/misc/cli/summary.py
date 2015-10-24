# -*- coding:utf-8 -*-
import json
import os.path
import sys
from handofcats import as_command
from misc.utils import (
    FileOrPortOpener,
    iterate_file_or_directory,
    get_dirpath_and_filepath
)
from misc import get_summary


@as_command
def main(src, outfile=None):
    dirpath, filepath = get_dirpath_and_filepath(src)
    open_file_or_stdout = FileOrPortOpener(outfile)

    source = filepath or dirpath
    for path in iterate_file_or_directory(source, glob_arg="*.json"):
        with open(path) as rf:
            nums = json.load(rf)

        name = os.path.basename(path)
        result = get_summary(name, nums)
        with open_file_or_stdout(path, "w") as wf:
            wf.write(json.dumps(result, ensure_ascii=False, indent=2))
        sys.stderr.write(".")
