import os
import yaml

from io import StringIO
from typing import List, Dict

cls = lambda: print("\033c", end="")


class YamlReader:
    def __init__(self, filename: str | StringIO):
        if isinstance(filename, str):
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} not found!")
            elif os.path.isdir(filename):
                raise IsADirectoryError(f"{filename} is a directory!")
            file_object = open(filename, "r", encoding="utf-8")
        else:
            file_object = filename
        self.yamlf = file_object
        self.data: List[Dict] = self.read_yaml()

    def read_yaml(self) -> List[Dict]:
        return yaml.load(self.yamlf, Loader=yaml.FullLoader)


class InstructionFetch:
    def __init__(self, instructions: List[Dict], target: str):
        self.instructions = instructions
        self.target: str = target
        self.result: Dict = self.fetch()
        self.name: str = self.result["name"]
        self.opcode: int = self.result["opcode"]
        self.format: str = self.result["format"]
        self.format_id: str = self.result["format_id"]
        self.syntax: str = self.result["syntax"]
        self.args_info: str = self.result["args_info"]
        self.short_desc: str = self.result["short_desc"]
        self.long_desc: str = self.result["long_desc"]
        self.note: str = self.result["note"]
        self.example: str = self.result["example"]
        self.example_desc: str = self.result["example_desc"]

    def __str__(self):
        results = f"Opcode: {self.opcode}\n"
        results += f"Name: {self.name}\n"
        results += f"Format: {self.format}\n"
        results += f"Format ID: {self.format_id}\n"
        results += f"Syntax: {self.syntax}\n"
        results += f"Args: {self.args_info}\n"
        results += f"Short Info: {self.short_desc}\n"
        results += f"Detailed Info: {self.long_desc}\n"
        results += f"Note: {self.note}\n" if self.note else ""
        results += f"Example: {self.example}\n"
        results += f"  Desc: {self.example_desc}"
        return results

    def __repr__(self):
        return f"InstructionFetch(instructions={self.instructions}, target={self.target}, name={self.name}, opcode={self.opcode}, format={self.format}, format_id={self.format_id}, syntax={self.syntax}, args_info={self.args_info}, short_desc={self.short_desc}, long_desc={self.long_desc}, note={self.note}, example={self.example}, example_desc={self.example_desc})"

    def fetch(self) -> Dict:
        for instruction in self.instructions:
            if instruction["opcode"] == self.target:
                return instruction
        for instruction in self.instructions:
            if instruction["name"] == self.target:
                return instruction
        return {}

    def fetch_opcode(self) -> Dict:
        for instruction in self.instructions:
            if instruction["opcode"] == self.target:
                return instruction
        return {}

    def fetch_inst(self) -> Dict:
        for instruction in self.instructions:
            if instruction["name"] == self.target:
                return instruction
        return {}
