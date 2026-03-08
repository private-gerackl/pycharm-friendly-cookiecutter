from pathlib import Path

from cookiecutter.main import cookiecutter
from pydantic import BaseModel

from pfcookiecutter.renamer import rename_templates
from pfcookiecutter.renamer import update_string

MAPPED = {
    'pfct_': '{{cookiecutter.',
    '11': '}}',
}


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
            no_input=True,
            extra_context=content.model_dump(mode='json'),
        )
    finally:
        rename_templates(
            mapped=anti_mapped,
            workdir=template_path,
            template_folder=update_string(template_folder, mapped=mapped),
        )

