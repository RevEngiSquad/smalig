import sys
import json as js
import jsbeautifier
import importlib.resources
import textwrap

from smalig import YamlReader, InstructionFetch, cls


def help() -> None:
    help_message = """
    smalig: Smali ByteCode info (grammar) fetch tool

    Usage: smalig [-t TARGET [-j] [-o OUTPUT_FILE]

    Options:
      -t TARGET  Specify the Smali instruction to fetch.  If omitted, 
                 prompts the user for input.
      -j         Output the result as JSON.  If -o is also specified and the 
                 OUTPUT_FILE ends in '.json', this flag is automatically set.
      -o OUTPUT_FILE Write the output to the specified file.  If omitted, prints to console.

    Examples:
      smalig -t "const-string"  # Fetch information for the 'const-string' instruction.
      smalig -t "invoke-virtual" -j -o output.json # Fetch and save as JSON
      smalig -o my_output.txt # Prompts for instruction then saves to my_output.txt


    If no target is specified using -t, the tool will prompt for input.

    If no -o flag is used, the output goes to stdout.  If a file is specified without a .json extension, plain text output is generated.
    """
    print(textwrap.dedent(help_message))


def app(file_path, target, json, out, exact_match) -> None:
    """
        Base CLI function
    :param file_path: Path to the YAML file containing the Smali instruction data.
    :param target: The Smali instruction to fetch information for.
    :param json: Whether to output the result as JSON.
    :param out: The file to write the output to. If None, prints to console.
    :param exact_match: Whether to perform an exact match on the target instruction.
    :return: None

    This function fetches information for a given Smali instruction from a YAML file and outputs the result.
    If no target is specified, the function prompts for input.
    If no output file is specified, the function prints to console.
    If the json flag is set, the function outputs the result as JSON.
    Otherwise, the function outputs the result as plain text.

    file_path is un-necessary if installed as a package.
    """
    reader = YamlReader(file_path)
    instructions = reader.data
    try:
        result = InstructionFetch(instructions, target, exact_match)
    except KeyError:
        print(f"{target} not found!")
        return
    if json:
        format_code = jsbeautifier.beautify(js.dumps(result.result))
        if out:
            with open(out, "w") as f:
                f.write(format_code)
        else:
            print(format_code)
        return
    if out:
        with open(out, "w") as f:
            f.write(str(result))
    else:
        print(result)
    return


def main() -> None:
    """
    Main function
    """
    args = sys.argv[1:]

    if "-h" in args or "--help" in args:
        help()
        return
    
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

    with importlib.resources.path("smalig", "grammar.yaml") as file_path:
        file_path = str(file_path)

    if "-t" in args:
        try:
            target = args[args.index("-t") + 1]
        except IndexError:
            target = ""
    else:
        try:
            target = input(f"Enter Query: ")
            cls()
        except KeyboardInterrupt:
            print("\nExiting...")
            return

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


if __name__ == "__main__":
    main()
