from pfcookiecutter.synthesizers.base import BaseSynthesizer


class SynthesizerBuilder(BaseSynthesizer):

    def __init__(
        self,
        *synthesizers: BaseSynthesizer,
    ):
        self._synthesizers = list(synthesizers)

    def add(
        self,
        synthesizer: BaseSynthesizer,
    ) -> None:
        self._synthesizers.append(synthesizer)

    def pfc(self) -> None:
        for synthesizer in self._synthesizers:
            synthesizer.pfc()