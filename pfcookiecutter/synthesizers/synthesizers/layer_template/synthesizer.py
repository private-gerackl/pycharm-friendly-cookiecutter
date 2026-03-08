from pathlib import Path

from pfcookiecutter.pfc import pfc
from pfcookiecutter.synthesizers.base import BaseSynthesizer
from pfcookiecutter.synthesizers.synthesizers.layer_template.models import LayerSynthesizerContent


class LayerSynthesizer(BaseSynthesizer):
    template_path: Path = Path().parent / 'pfcookiecutter' / 'templates' / 'layer_template'
    template_folder: str = 'pfct_source_name11'

    def __init__(
        self,
        content: LayerSynthesizerContent,
    ):
        self.content = content

    def pfc(self) -> None:
        pfc(
            template_path=self.template_path,
            template_folder=self.template_folder,
            content=self.content,
        )
