from pathlib import Path

MAPPED = {
    '_11': '{{',
    '11_': '}}',
}

TEMPLATE_FOLDER = '_11cookiecutter.source_name11_'
WORKDIR = Path(__file__).parent.parent.absolute()


def update_string(string: str, mapped: dict[str, str]) -> str:
    result = string
    for key, val in mapped.items():
        result = result.replace(key, val)
    return result

def rename_templates(
    mapped: dict[str, str],
    workdir: Path,
    template_folder: str,
) -> None:
    paths_for_process = list(
        sorted(
            [(workdir, [template_folder], []), *(workdir / template_folder).walk()],
            key=lambda row: row[0]
        )
    )[::-1]
    for root, dirs, files in paths_for_process:
        for name in files + dirs:
            path = root / name
            if not path.exists():
                continue
            if path.is_file():
                with open(path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    f.seek(0)
                    f.write(update_string(content, mapped))
                    f.truncate()
            new_name = update_string(name, mapped)
            if new_name != name:
                path.rename(root / new_name)