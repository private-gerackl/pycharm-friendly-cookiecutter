from pydantic import BaseModel


class PostgresInfraSynthesizerContent(BaseModel):
    source_name: str = 'app'
    integration_name: str = 'postgresql'
    IntegrationName: str = 'PSQL'
    BaseIntegrationClass: str
    base_integration_class_module: str