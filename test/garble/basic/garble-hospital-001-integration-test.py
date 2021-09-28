import garble
import util.file.file_util as fu
from types import SimpleNamespace


def main():
    print("Starting test...")
    source_file = fu.get_file_name("test-data/data-owner/basic/hospital-001/hospital_001.csv")
    secret_file = fu.get_file_name("test-data/data-owner/basic/hospital-001/secret-file.txt")
    schema_dir = fu.get_file_name("test-data/schemas/default-schema")
    output_dir = fu.get_file_name("test-data/data-owner/basic/hospital-001/out")
    output_zip = "hosp-001.zip"
    args = {
        "sourcefile": source_file,
        "secretfile": secret_file,
        "outputdir":  output_dir,
        "outputzip": output_zip,
        "schemadir": schema_dir
    }
    args = SimpleNamespace(**args)
    print(args)
    clks = garble.garble_pii(args)
    garble.create_clk_zip(clks, args)
    print("Done.")


if __name__ == "__main__":
    main()

