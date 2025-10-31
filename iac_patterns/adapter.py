# adapter.py
from typing import Dict, Any
class MockBucketAdapter:
    def __init__(self, null_block: Dict[str, Any]):
        self._null_block = null_block

    def to_bucket(self) -> Dict[str, Any]:
        # Mapea triggers a parámetros de bucket simulado
        try:
            null_res_data = self._null_block["resource"][0]["null_resource"][0]
            name = next(iter(null_res_data.keys()))
            triggers = null_res_data[name][0]["triggers"]
        except (KeyError, IndexError, StopIteration):
            return {"error": "Estructura de null_block inválida"}
        return {
            "resource": [{
                "mock_cloud_bucket": [{
                    name: [{
                        "bucket_name": name,
                        "parameters": triggers 
                    }]
                }]
            }]
        }