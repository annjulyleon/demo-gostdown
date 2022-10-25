import re
import shutil
import argparse
from pathlib import Path

PATTERNS = [
    {"pattern": "{#(fig|tbl|sec):.+?(?=})}", "replace": "", "desc": "caption"},
    {"pattern": "\[-@(fig|tbl|sec):.+?(?=])]",
     "replace": "", "desc": "reference"},
    {"pattern": "{custom-style.+?(?=})}", "replace": "",
     "desc": "custom style named"},
    {"pattern": "{\..+?(?=})}", "replace": "",
     "desc": "custom style unnamed"},
    {"pattern": "# \[([А-я].+?(?=\]))\]", "replace": r"# \1",
     "desc": "headings brackets"},
    {"pattern": "Table: ", "replace": "_Таблица:_ ",
     "desc": "table caption"}
]


def stripper(patterns: list[dict], file_content) -> str:
    stripped_file_content = file_content
    for pattern in patterns:
        stripped_file_content = re.sub(
            pattern["pattern"], pattern["replace"], stripped_file_content)

    return stripped_file_content


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Gostdown stripper for md files",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-s", "--source", type=str, default="docs_gost",
                        help="Directory in current folder where .md files are stored")
    parser.add_argument("-d", "--destination", type=str, default="docs",
                        help="Name of directory, where stripped files will be placed")
    parser.add_argument("-i", "--ignored", nargs='+',
                        help="Pass ignored files, separated by space, for example: '-i *.png *.bat *.ps1 *.lua end.md begin.md'"),
    parser.add_argument("-a", "--abbreviations", action="store_true",
                        help="Flag if we need to add link to abbreviations file in the end of every md")
    args = vars(parser.parse_args())

    # copy directories with files
    shutil.copytree(args["source"], args["destination"],
                    ignore=shutil.ignore_patterns(*args["ignored"]))

    stripped_dir = args["destination"]
    paths = Path(stripped_dir).rglob("*.md")

    for path in paths:
        try:
            with open(path, 'r', encoding="utf-8") as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f'File "{path}" not found')

        stripped_content = stripper(PATTERNS, file_content)

        with open(path, "w", encoding="utf-8") as file:
            file.write(stripped_content)

        if args["abbreviations"]:
            with open(path, "a+", encoding="utf-8") as file:
                file.seek(0)
                data = file.read(100)
                if len(data) > 0:
                    file.write("\n")
                file.write('--8<-- "includes/abbreviations.md"')
                file.write("\n")
