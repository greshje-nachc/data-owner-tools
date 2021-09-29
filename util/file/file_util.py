import os
import definitions
from pathlib import Path


def get_file_name(rel_path):
    return str(Path(definitions.ROOT_DIR, rel_path).resolve())


def get_dirs(path):
    dirs = os.listdir(path)
    return dirs
