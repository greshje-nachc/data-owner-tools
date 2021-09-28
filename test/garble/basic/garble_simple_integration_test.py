import garble
import util.file.file_util as fu
from types import SimpleNamespace


def main():
    print("Starting test...")
    do_test("hospital_001")
    do_test("hospital_002")
    do_test("hospital_003")
    print("\n\nDone.")


def do_test(name):
    print("-----------------------------------")
    print("Doing test for: " + name)
    source_file = fu.get_file_name("test-data/data-owner/basic/"+name+"/"+name+".csv")
    secret_file = fu.get_file_name("test-data/data-owner/basic/"+name+"/secret-file.txt")
    schema_dir = fu.get_file_name("test-data/schemas/default-schema")
    output_dir = fu.get_file_name("test-data/data-owner/basic/"+name+"/out")
    output_zip = name+".zip"
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


if __name__ == "__main__":
    main()

