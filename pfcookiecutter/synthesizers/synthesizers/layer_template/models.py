from pydantic import BaseModel


class LayerSynthesizerContent(BaseModel):
    source_name: str = 'app'
    layer_name: str
    LayerName: str
