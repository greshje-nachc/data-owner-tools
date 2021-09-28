import definitions
import util.file.file_util as fu


def get_project_root_test():
    print("Getting project root...")
    print("Project Root: \n" + definitions.ROOT_DIR)
    print("Done.\n")


def get_file_test():
    print("Getting file...")
    file_name = fu.get_file_name("test")
    print(file_name)
    print("Done.\n")


def main():
    get_project_root_test()
    get_file_test()


if __name__ == "__main__":
    main()
