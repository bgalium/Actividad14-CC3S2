import json
import os
from iac_patterns.factory import NullResourceFactory
from iac_patterns.prototype import ResourcePrototype
from typing import Dict, Any

PATH_TF_JSON = "terraform/main.tf.json"

def add_welcome_file(block: Dict[str, Any]) -> None:
  
    block["resource"][0]["null_resource"][0]["app_0"][0]["triggers"]["welcome"] = "¡Hola desde el mutator!"
    block["resource"].append({
        "local_file": [{
            "welcome_txt": [{
                "content": "Bienvenido",
                "filename": "bienvenida.txt"
            }]
        }]
    })

print("--- Probando Ejercicio 2.3: Mutaciones avanzadas (local_file) ---")

base_recurso = NullResourceFactory.create(name="app_0")

proto = ResourcePrototype(base_recurso)

clon_mutado_dict = proto.clone(mutator=add_welcome_file).data

os.makedirs(os.path.dirname(PATH_TF_JSON), exist_ok=True)
with open(PATH_TF_JSON, "w") as f:
    json.dump(clon_mutado_dict, f, indent=4)

print(f"Archivo generado en: {PATH_TF_JSON}")
