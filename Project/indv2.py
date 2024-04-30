import argparse
import os


def list_files(startpath, output_file=None):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        if output_file:
            with open(output_file, "a") as f:
                f.write("{}{}/\n".format(indent, os.path.basename(root)))
                subindent = " " * 4 * (level + 1)
                for file in files:
                    f.write("{}{}\n".format(subindent, file))
        else:
            print("{}{}/".format(indent, os.path.basename(root)))
            subindent = " " * 4 * (level + 1)
            for file in files:
                print("{}{}".format(subindent, file))


def main():
    parser = argparse.ArgumentParser(
        description="Analog of the tree utility in Linux"
    )
    parser.add_argument(
        "directory", nargs="?", default=".", help="Directory to display"
    )
    parser.add_argument(
        "-o", "--output", help="Output file to save the tree structure"
    )
    args = parser.parse_args()

    if args.output:
        list_files(args.directory, args.output)
    else:
        list_files(args.directory)


if __name__ == "__main__":
    main()
