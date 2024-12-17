import sys
from smalig import app, help, cls

if __name__ == "__main__":
    args = sys.argv[1:]

    if "-h" in args or "--help" in args:
        help()
        sys.exit(0)

    if "-m" in args:
        exact_match = False
    else:
        exact_match = True

    if "-o" in args:
        try:
            output_file = args[args.index("-o") + 1]
        except IndexError:
            output_file = None
    else:
        output_file = None

    try:
        if "-f" in args:
            try:
                file_path = args[args.index("-f") + 1]
            except IndexError:
                file_path = None
        else:
            file_path = input(f"Enter the path to the file: ")

        if "-t" in args:
            try:
                target = args[args.index("-t") + 1]
            except IndexError:
                target = ""
        else:
            target = input(f"Enter Query: ")
            cls()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

    if "-j" in args:
        json = True
    else:
        if output_file and output_file.endswith(".json"):
            json = True
        else:
            json = False

    if target == "":
        raise Exception("Query is empty")

    if file_path == "":
        raise Exception("File path is empty")

    app(file_path=file_path, target=target, json=json, out=output_file, exact_match=exact_match)
