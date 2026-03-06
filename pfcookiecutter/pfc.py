from pathlib import Path

from cookiecutter.main import cookiecutter
from pydantic import BaseModel

from pfcookiecutter.renamer import rename_templates
from pfcookiecutter.renamer import update_string

MAPPED = {
    '_11': '{{cookiecutter.',
    '11_': '}}',
}

TEMPLATE_FOLDER = '_11cookiecutter_source_name11_'
WORKDIR = Path(__file__).parent.absolute()

def pfc(
    template_path: Path,
    template_folder: str,
    content: BaseModel,
    mapped: dict[str, str] | None = None,
) -> None:
    if mapped is None:
        mapped = MAPPED
    anti_mapped = {
        val: key
        for key, val in mapped.items()
    }
    try:
        rename_templates(
            mapped=mapped,
            workdir=template_path,
            template_folder=template_folder,
        )

        cookiecutter(
            str(template_path.absolute()),
            overwrite_if_exists=True,
        )
    finally:
        rename_templates(
            mapped=anti_mapped,
            workdir=template_path,
            template_folder=update_string(template_folder, mapped=mapped),
        )

