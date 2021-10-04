import util.garble.garble_util as gu
import util.file.file_util as fu
from types import SimpleNamespace


def test_household():
    print("\n\nStarting test...")
    do_test("hospital_001")
    do_test("hospital_002")
    do_test("hospital_003")
    print("\n\nDone.")


def do_test(name):
    print("-----------------------------------")
    print("Doing test for: " + name)
    source_file = fu.get_file_name("test-data/data-owner/small/"+name+"/"+name+".csv")
    secret_file = fu.get_file_name("test-data/data-owner/small/"+name+"/secret-file.txt")
    output_dir = fu.get_file_name("test-data/data-owner/small/"+name+"/out")
    schemafile = fu.get_file_name("test-data/data-owner/small/schema/household-schema/fn-phone-addr-zip.json")
    output_zip = name+".zip"
    mappingfile = str(output_dir + "/households.csv")
    gu.do_garble_household(source_file, secret_file, output_dir, schemafile, output_zip, mappingfile)


