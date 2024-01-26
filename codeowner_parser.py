"""Parse the CODEOWNERS file."""
import re

import utils


def _parse_line(line):
    """Parse a line from the CODEOWNERS file."""
    if line.startswith("#"):
        return None

    line = line.strip()
    if line == "":
        return None

    parts = re.split(r"(?<!\\)\s+", line)

    pattern = parts[0].replace("\\ ", " ")
    owners = parts[1:]

    return pattern, owners


def parse_codeowners():
    """Parse the CODEOWNERS file."""
    path = utils.get_codeowners_file()
    data = []

    with open(path, encoding="utf-8") as file:
        count = 0
        for line in file:
            count += 1
            line = _parse_line(line)
            if line is None:
                continue
            pattern, owners = line
            data.append((count, line, pattern, owners))

    return data
