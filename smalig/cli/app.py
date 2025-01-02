import argparse
import json as js
import jsbeautifier

from smalig import YamlReader, InstructionFetch, cls, grammar_yaml


EXAMPLES = """
examples:
    smalig                                          # Prompts for instruction then fetch it's information.
    smalig -m                                       # Prompts for instruction then fetch it's information with fuzzy match.
    smalig -t "move"                                # Fetch information for the 'move' instruction.
    smalig -t "move" -j                             # Output as JSON
    smalig -t "invoke-virtual" -j -o output.json    # Fetch and save as JSON
    smalig -o my_output.txt                         # Prompts for instruction then saves to my_output.txt
    smalig -t "move" -m                             # Fuzzy match
    smalig -t "move" -o my_output.json              # Save as JSON
    smalig -t "move" -o my_output.txt               # Save as plain text
"""


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


def parse_args():
    parser = argparse.ArgumentParser(
        prog="smalig",
        description="Smali ByteCode info (grammar) fetch tool",
        epilog=EXAMPLES,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-m", action="store_true", help="Enable fuzzy match")
    parser.add_argument(
        "-o",
        metavar="OUTPUT_FILE",
        help="Specify output file. If omitted, prints to console.",
    )
    parser.add_argument(
        "-t",
        metavar="TARGET",
        help="Specify the Smali instruction to fetch. If omitted, prompts the user for input.",
    )
    parser.add_argument(
        "-j",
        action="store_true",
        help="Enable JSON output. If omitted and OUTPUT_FILE ends in '.json', this flag is automatically set.",
    )
    return parser.parse_args()


def get_target(args):
    if args.t:
        return args.t
    else:
        target = input("Search instruction: ")
        cls()
        return target


def get_json(args, output_file):
    if args.j:
        return True
    elif output_file and output_file.endswith(".json"):
        return True
    else:
        return False


def main():
    args = parse_args()
    file_path = grammar_yaml()
    target = get_target(args)
    if not target:
        exit("Query is empty!")
    json_output = get_json(args, args.o)

    app(
        file_path=file_path,
        target=target,
        json=json_output,
        out=args.o,
        exact_match=not args.m,
    )


if __name__ == "__main__":
    main()
