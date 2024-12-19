<a name="readme-top"></a>
# smalig

Dalvik(Smali) ByteCode info (grammar) fetch tool written in Python.

## Description

`smalig` is a tool designed to fetch information about Dalvik(Smali) bytecode instructions. It allows users to specify a target instruction and retrieve detailed information about it, either in plain text or JSON format. This tool is particularly useful for developers and reverse engineers working with Android bytecode. Although there are many tools & resources available which does same job like [Dalvik Bytecode Reference](https://source.android.com/devices/tech/dalvik/dalvik-bytecode), Some chinese applications like MT Manager, NP, etc. but they all are very limited or little complex to understand and some are even outdated with no new instructions added. This tool is designed to be used from command line and can be integrated with other tools. We created it for our use in RevEngi project and decided to share it in the hope that it will be useful to others.

## Features

- Fetch information for specific Dalvik(Smali) instructions.
- Output results in plain text or JSON format.
- Save output to a specified file or print to the console.
- Interactive mode for prompting user input.


## Installation

To install `smalig`, you can use `pip`:

```sh
pip install smalig
```

or you can install it from source:

```sh
pip install git+https://github.com/RevEngiSquad/smalig.git
```

## Usage/Examples

You can use `smalig` from the command line. Below are some examples of how to use the tool:

```sh
smalig -t "move"  # Fetch information for the 'move' instruction.
smalig -t "invoke-virtual" -j -o output.json # Fetch and save as JSON
smalig -o my_output.txt # Prompts for instruction then saves to my_output.txt
```

**Output:**

```plaintext
Opcode: 01
Name: move
Format: B|A|op
Format ID: 12x
Syntax: move vA, vB
Args: A: destination register (4 bits), B: source register (4 bits)
Short Info: Move the contents of one non-object register to another.
Detailed Info: Moves the content of vB into vA. Both registers must be in the first 16 register range (0-15).
Example: 0110 - move v0, v1
  Desc: Moves the content of v1 into v0.
```

As shown in the above example output, we've gone ahead and provided more detailed information about the instruction. This includes the opcode, format, syntax, arguments, and examples. This information can be useful for understanding the instruction and how it is used in Dalvik bytecode even for beginners.

### Command Line Options

- `-t TARGET`: Specify the Smali instruction to fetch. If omitted, prompts the user for input.
- `-j`: Output the result as JSON. If `-o` is also specified and the `OUTPUT_FILE` ends in `.json`, this flag is automatically set.
- `-o OUTPUT_FILE`: Write the output to the specified file. If omitted, prints to console.

## Contributing
We welcome contribution(s) to `smalig`! They are what makes the open-source community such an amazing place to learn, inspire, and create. Any contribution(s) you make is/are greatly appreciated.

If you have a feature request or found a bug, please create an issue on the repo. You can also simply open an issue with the tag "enhancement" or "bug" and we will look into it.

If you would like to contribute, please follow these steps:

1. **Fork the repository**: Click the "Fork" button in the top right corner of the repository page to create a copy of the repository in your GitHub account.

2. **Create a new branch**: Create a new branch for your feature or bug fix:
    ```sh
    git checkout -b my-feature-branch
    ```

3. **Make your changes**: Implement your feature or bug fix.

4. **Commit your changes**: Commit your changes with a descriptive commit message:
    ```sh
    git commit -m "Description of my changes"
    ```

5. **Push to your fork**: Push your changes to your forked repository:
    ```sh
    git push origin my-feature-branch
    ```

6. **Create a pull request**: Go to the original repository and create a pull request from your forked repository. Provide a clear description of your changes and any related issues.

### Guidelines

- Write clear and concise commit messages.
- Update documentation if necessary.
- Write tests for new features or bug fixes if applicable.

Thank you for contributing to `smalig`!

Don't forget to star the repository if you found it useful.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- [Abhi](https://github.com/AbhiTheModder)

<p align="right"><a href="#readme-top">Go to top</a></p>