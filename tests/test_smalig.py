# Tests for smalig
from smalig.utils import YamlReader, InstructionFetch, grammar_yaml


def test_fetch():
    reader = YamlReader(grammar_yaml())
    fetcher = InstructionFetch(reader.data, "move")
    result = fetcher.fetch()
    assert result["opcode"] == "01"
    assert result["name"] == "move"


def test_fetch_fuzzy():
    reader = YamlReader(grammar_yaml())
    fetcher = InstructionFetch(reader.data, "move", exact_match=False)
    result = fetcher.fetch_fuzzy()
    assert len(result) > 0
    assert all("move" in instruction["name"] for instruction in result)


def test_fetch_nonexistent():
    reader = YamlReader(grammar_yaml())
    fetcher = InstructionFetch(reader.data, "nonexistent")
    result = fetcher.fetch()
    assert result == {}


def test_fetch_fuzzy_nonexistent():
    reader = YamlReader(grammar_yaml())
    fetcher = InstructionFetch(reader.data, "nonexistent", exact_match=False)
    result = fetcher.fetch_fuzzy()
    assert result == []
