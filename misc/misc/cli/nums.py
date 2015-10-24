# -*- coding:utf-8 -*-
from handofcats import as_command
import random
import json
import sys
from misc.utils import (
    FileOrPortOpener
)

# 実行結果を揃えるためにseedを指定
random.seed(1)


# 本来はmisc.nums的なものをimport
def generate(N):
    result = []
    for _ in range(N):
        i = random.random()
        if random.random() > 0.5:
            i = -i
        result.append(i)
    return result


@as_command
def main(nums=10, items=5, outfile=None):
    items = int(items)
    nums = int(nums)
    open_file_or_stdout = FileOrPortOpener(outfile)
    for i in range(1, items + 1):
        result = generate(nums)
        filename = "{0:03}.json".format(i)
        with open_file_or_stdout(filename, "w") as wf:
            wf.write(json.dumps(result, ensure_ascii=False, indent=2))
        sys.stderr.write(".")
