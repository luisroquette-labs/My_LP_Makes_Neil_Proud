from pathlib import Path
import subprocess
import sys

from pygments import lex
from pygments.lexers import BashLexer, PythonLexer, YamlLexer
from pygments.token import Comment


LEXERS = {".py": PythonLexer, ".sh": BashLexer, ".yaml": YamlLexer, ".yml": YamlLexer}


def comment_lines(source: str, suffix: str) -> list[int]:
    lines = []
    line = 1
    for token, value in lex(source, LEXERS[suffix.lower()]()):
        required_directive = (
            suffix.lower() in {".py", ".sh"} and line == 1 and value.startswith("#!")
        )
        if token in Comment and not required_directive:
            lines.append(line)
        line += value.count("\n")
    return lines


def gitignore_comment_lines(source: str) -> list[int]:
    return [line for line, value in enumerate(source.splitlines(), 1) if value.lstrip().startswith("#")]


def main() -> int:
    tracked = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
    failures = [
        f"{path}:{line}"
        for path in tracked
        if path and Path(path).suffix.lower() in LEXERS
        for line in comment_lines(Path(path).read_text(), Path(path).suffix)
    ]
    if Path(".gitignore").exists():
        failures.extend(f".gitignore:{line}" for line in gitignore_comment_lines(Path(".gitignore").read_text()))
    if failures:
        print("Comments are forbidden:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    print("Comment ratchet: zero comments in tracked Python, shell, YAML and gitignore files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
