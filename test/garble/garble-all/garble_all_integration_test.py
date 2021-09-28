import util.garble.garble_util as gu
import util.file.file_util as fu

def garble_all_integration_test():
    print("Doing test for garble all...")
    path = fu.get_file_name("test-data/data-owner/basic")
    schema_dir_name = "basic-schema"
    gu.garlble_all(path, schema_dir_name)
    print("Done.")


def main():
    garble_all_integration_test()


if __name__ == "__main__":
    main()
