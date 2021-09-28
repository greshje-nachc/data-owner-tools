import definitions
from pathlib import Path


def get_file_name(rel_path):
    return str(Path(definitions.ROOT_DIR, rel_path).resolve())
