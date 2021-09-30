import garble
from types import SimpleNamespace
from pathlib import Path


def do_garble(source_file, secret_file, output_dir, schema_dir, output_zip):
    args = {
        "sourcefile": source_file,
        "secretfile": secret_file,
        "schemadir": schema_dir,
        "outputdir":  output_dir,
        "outputzip": output_zip
    }
    args = SimpleNamespace(**args)
    clks = garble.garble_pii(args)
    garble.create_clk_zip(clks, args)


