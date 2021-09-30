import os
import time
import util.garble.garble_util as gu
import util.file.file_util as fu

ROOT_DIR = "C:\\test\\synthea-patients\\test-sets\\test-set-001"


def main():
    print("Starting test...")
    print("ROOT_DIR: " + ROOT_DIR)
    csv_dir = os.path.join(str(ROOT_DIR), "csv")
    secret_file = os.path.join(str(ROOT_DIR), "secret-file.txt")
    output_root = os.path.join(str(ROOT_DIR), "garbled")
    schema_dir = os.path.join(str(ROOT_DIR), "schema")
    files = fu.get_files(csv_dir)
    times = []
    for source_file in files:
        short_name = fu.get_file_prefix(source_file)
        output_dir = os.path.join(output_root, short_name)
        print("Running test for: " + source_file + " (" + short_name + ")")
        print("Outdir: " + output_dir)
        fu.rmdir(output_dir)
        fu.mkdirs(output_dir)
        output_zip = os.path.join(output_dir, short_name + ".zip")
        start = time.time()
        gu.do_garble(source_file, secret_file, output_dir, schema_dir, output_zip)
        end = time.time()
        elapsed = (end - start)
        print("ELAPSED: " + str(elapsed))
        times.append(short_name + "," + str(elapsed))
        print("----------------------------")
        print("Times:")
        for row in times:
            print(row)
        print("\n")
    print("Done.")


if __name__ == "__main__":
    main()
