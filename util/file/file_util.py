import os
import definitions
from pathlib import Path


def get_file_name(rel_path):
    return str(Path(definitions.ROOT_DIR, rel_path).resolve())


def is_true(foo):
    return True


def get_dirs(path):
    files = os.listdir(path)
    rtn = []
    for file in files:
        cur = os.path.join(str(path), file)
        if os.path.isdir(cur):
            rtn.append(cur)
    return rtn


def get_files(path):
    files = os.listdir(path)
    rtn = []
    for file in files:
        cur = os.path.join(str(path), file)
        if os.path.isdir(cur) == False:
            rtn.append(cur)
    return rtn


