from pathlib import Path

from pfcookiecutter.pfc import pfc
from pfcookiecutter.synthesizers.base import BaseSynthesizer
from pfcookiecutter.synthesizers.synthesizers.postgres_infra_template.models import PostgresInfraSynthesizerContent


class PostgresInfraSynthesizer(BaseSynthesizer):
    template_path: Path = Path().parent / 'pfcookiecutter' / 'templates' / 'postgres_infra_template'
    template_folder: str = 'pfct_source_name11'

    def __init__(
        self,
        content: PostgresInfraSynthesizerContent,
    ):
        self.content = content

    def pfc(self):
        pfc(
            template_path=self.template_path,
            template_folder=self.template_folder,
            content=self.content,
        )
