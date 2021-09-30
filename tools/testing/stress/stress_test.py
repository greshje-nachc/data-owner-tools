import os
import util.garble.garble_util as gu
import util.file.file_util as fu

ROOT_DIR = "C:\\test\\synthea-patients\\test-sets\\test-set-001"


def main():
    print("Starting test...")
    print("ROOT_DIR: " + ROOT_DIR)
    csv_dir = os.path.join(str(ROOT_DIR), "csv")
    secret_file = os.path.join(str(ROOT_DIR), "secret-file.txt")
    output_dir = os.path.join(str(ROOT_DIR), "garbled")
    schema_dir = os.path.join(str(ROOT_DIR), "schema")
    files = fu.get_files(csv_dir)
    for source_file in files:
        source_file_name = fu.get_file_name_from_path(source_file)
        print("Running test for: " + source_file + " (" + source_file_name + ")")
        # gu.do_garble(source_file, secret_file, output_dir, schema_dir, output_zip)
    print("Done.")


if __name__ == "__main__":
    main()
