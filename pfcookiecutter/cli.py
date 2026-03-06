from pathlib import Path

import typer
from cookiecutter.main import cookiecutter

from pfcookiecutter.renamer import rename_templates, update_string

app = typer.Typer()

MAPPED = {
    '_11cookiecutter_': '{{cookiecutter.',
    '11_': '}}',
}

TEMPLATE_FOLDER = '_11cookiecutter_source_name11_'
WORKDIR = Path(__file__).parent.absolute()

@app.command()
def hello():
    try:
        rename_templates(
            mapped=MAPPED,
            workdir=WORKDIR,
            template_folder=TEMPLATE_FOLDER,
        )

        cookiecutter(
            '/home/gerackl/mine/apps/pycharm/pycharm-projects/my-projects/pycharm-friendly-cookiecutter/pfcookiecutter',
            overwrite_if_exists=True,
        )
    finally:
        anti_mapped = {
            val: key
            for key, val in MAPPED.items()
        }
        rename_templates(
            mapped=anti_mapped,
            workdir=WORKDIR,
            template_folder=update_string(TEMPLATE_FOLDER, mapped=MAPPED),
        )

@app.command()
def goodbye(name: str):
    typer.echo(f"Goodbye {name}")


if __name__ == "__main__":
    app()