from pfcookiecutter.synthesizer_builder import SynthesizerBuilder
from pfcookiecutter.synthesizers.synthesizers.layer_template.models import LayerSynthesizerContent
from pfcookiecutter.synthesizers.synthesizers.layer_template.synthesizer import LayerSynthesizer
from pfcookiecutter.synthesizers.synthesizers.postgres_infra_template.models import PostgresInfraSynthesizerContent
from pfcookiecutter.synthesizers.synthesizers.postgres_infra_template.synthesizer import PostgresInfraSynthesizer


class AppBuilderFactory:

    def __init__(
        self,
        source_name: str = 'app',
        integration_layer_name: str = 'integrations',
        service_layer_name: str = 'services',
    ):
        self.source_name = source_name
        self.integration_layer_name = integration_layer_name
        self.service_layer_name = service_layer_name

    def build(self) -> SynthesizerBuilder:
        return SynthesizerBuilder(
            self.integration_builder,
            self.service_builder,
        )

    @property
    def integration_builder(self) -> SynthesizerBuilder:
        return SynthesizerBuilder(
            LayerSynthesizer(
                content=LayerSynthesizerContent(
                    source_name=self.source_name,
                    layer_name=self.integration_layer_name,
                    LayerName=self.integration_layer_name_camel_case,
                )
            ),
            PostgresInfraSynthesizer(
                content=PostgresInfraSynthesizerContent(
                    source_name=self.source_name,
                    integration_name='postgresql',
                    IntegrationName='PSQL',
                    BaseIntegrationClass=f'Base{self.integration_layer_name.capitalize()[:-1]}',
                    base_integration_class_module=f'{self.source_name}.{self.integration_layer_name}.base',
                )
            ),
        )

    @property
    def service_builder(self) -> SynthesizerBuilder:
        return SynthesizerBuilder(
            LayerSynthesizer(
                content=LayerSynthesizerContent(
                    source_name=self.source_name,
                    layer_name=self.service_layer_name,
                    LayerName=self.service_layer_name_camel_case,
                )
            )
        )

    @property
    def integration_layer_name_camel_case(self) -> str:
        return self.integration_layer_name.capitalize()[:-1]

    @property
    def service_layer_name_camel_case(self) -> str:
        return self.service_layer_name.capitalize()[:-1]


app_builder = AppBuilderFactory()
app_builder.build().pfc()
