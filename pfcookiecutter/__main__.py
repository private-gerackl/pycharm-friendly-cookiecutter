from pathlib import Path

from pfcookiecutter.pfc import pfc

pfc(
    template_path=Path().parent / 'pfcookiecutter' / 'templates' / 'postgres_template',
    template_folder='_11source_name11_',
)

class PostgreSQLTemplateBuilder:
    pass