from pfcookiecutter.synthesizer_builder import SynthesizerBuilder
from pfcookiecutter.synthesizers.synthesizers.layer_template.models import LayerSynthesizerContent
from pfcookiecutter.synthesizers.synthesizers.layer_template.synthesizer import LayerSynthesizer
from pfcookiecutter.synthesizers.synthesizers.postgres_infra_template.models import PostgresInfraSynthesizerContent
from pfcookiecutter.synthesizers.synthesizers.postgres_infra_template.synthesizer import PostgresInfraSynthesizer


def app_builder_factory(
    source_name: str = 'app',
    integration_layer_name: str = 'integrations',
    service_layer_name: str = 'services',
) -> SynthesizerBuilder:
    return SynthesizerBuilder(
        SynthesizerBuilder(
            LayerSynthesizer(
                content=LayerSynthesizerContent(
                    source_name=source_name,
                    layer_name=integration_layer_name,
                    LayerName=integration_layer_name.capitalize()[:-1],
                )
            ),
            PostgresInfraSynthesizer(
                content=PostgresInfraSynthesizerContent(
                    source_name=source_name,
                    integration_name='postgresql',
                    IntegrationName='PSQL',
                    BaseIntegrationClass=f'Base{integration_layer_name.capitalize()[:-1]}',
                    base_integration_class_module=f'{source_name}.{integration_layer_name}.base',
                )
            ),
        ),
        SynthesizerBuilder(
            LayerSynthesizer(
                content=LayerSynthesizerContent(
                    source_name=source_name,
                    layer_name=service_layer_name,
                    LayerName=service_layer_name.capitalize()[:-1],
                )
            )
        )
    )


app_builder = app_builder_factory()
app_builder.pfc()