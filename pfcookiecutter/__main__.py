from pathlib import Path

from pfcookiecutter.pfc import pfc

pfc(
    template_path=Path().parent / 'pfcookiecutter' / 'templates' / 'postgres_template',
    template_folder='_11source_name11_',

)

class PostgreSQLTemplateBuilder:
    def __init__(
        self,
        template_path: Path,
        template_folder: str,
    ):
        self._template_path = template_path
        self._template_folder = template_folder

    def pfc(
        self,

    ):