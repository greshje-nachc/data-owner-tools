import util.garble.garble_util as gu
import util.file.file_util as fu


def garble_integration_test():
    name = "hospital_001"
    print("-----------------------------------")
    print("Doing test for: " + name)
    source_file = fu.get_file_name("test-data/data-owner/basic/"+name+"/"+name+".csv")
    secret_file = fu.get_file_name("test-data/data-owner/basic/"+name+"/secret-file.txt")
    output_dir = fu.get_file_name("test-data/data-owner/basic/"+name+"/out")
    schema_dir = fu.get_file_name("test-data/data-owner/basic/basic-schema")
    output_zip = name+".zip"
    gu.do_garble(source_file, secret_file, output_dir, schema_dir, output_zip)
    print("Done.")


def main():
    garble_integration_test()


if __name__ == "__main__":
    main()
