import re
from abc import ABC, abstractmethod


class CategoryMap(ABC):
    def __init__(self, source: str, destination: str):
        self._source = source
        self._destination = destination

    def __call__(self, *source_values: int) -> list[int]:
        return [dest_value for source_value in source_values for dest_value in self._map(source_value)]

    def __or__(self, other: "CategoryMap") -> "CategoryMap":
        return ComposedCategoryMap(self, other)

    def __ior__(self, other: "CategoryMap") -> "CategoryMap":
        return self | other

    @abstractmethod
    def _map(self, source_value: int) -> list[int]:
        ...

    @property
    def source(self) -> str:
        return self._source

    @property
    def destination(self) -> str:
        return self._destination


class ComposedCategoryMap(CategoryMap):
    def __init__(self, *mappings: CategoryMap):
        assert len(mappings) > 0, "must have at least one mapping"
        for mapping, next_mapping in zip(mappings[:-1], mappings[1:]):
            assert mapping.destination == next_mapping.source, f"mappings must be composed in order, but {mapping.destination} != {next_mapping.source}"
        super().__init__(mappings[0].source, mappings[-1].destination)
        self._mappings = mappings

    def _map(self, source_value: int) -> list[int]:
        dest_values = [source_value]
        for mapping in self._mappings:
            dest_values = mapping(*dest_values)
        return dest_values


class SingleCategoryMap(CategoryMap):
    def __init__(self, source: str, destination: str, mappings: list[tuple[int, int, int]]):
        super().__init__(source, destination)
        self._mappings = mappings

    def _map(self, source_value: int) -> list[int]:
        for dest_start, source_start, length in self._mappings:
            if source_value in range(source_start, source_start + length):
                return [dest_start + source_value - source_start]
        return [source_value]


class NoOpCategoryMap(CategoryMap):
    def __init__(self, category: str):
        super().__init__(category, category)

    def _map(self, source_value: int) -> list[int]:
        return [source_value]


def main() -> None:
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        lines.append("")  # add a blank line to the end to make parsing easier
    initial_seeds = [int(seed) for seed in lines[0].split()[1:]]
    source, destination, mappings = None, None, []
    mapping = NoOpCategoryMap("seed")
    for line in lines[2:]:
        if match := re.match(r"^(\w+)-to-(\w+) map:$", line):
            source, destination = match.groups()
        elif line == "":
            mapping |= SingleCategoryMap(source, destination, mappings)
            mappings = []
        else:
            dest_start, src_start, length = [int(num) for num in line.split()]
            mappings.append((dest_start, src_start, length))
    print(min(mapping(*initial_seeds)))


if __name__ == '__main__':
    main()
