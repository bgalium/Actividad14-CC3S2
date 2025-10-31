import json
import os
from iac_patterns.builder import InfrastructureBuilder

PATH_TF_JSON = "terraform/main.tf.json"
print("--- Probando Ejercicio 2.5: Builder Personalizado (build_group) ---")

builder = InfrastructureBuilder(env_name="prod-group")

builder.build_group(name="web_servers", size=3)

builder.export(path=PATH_TF_JSON)

print(f"Archivo JSON generado en: {PATH_TF_JSON}")
print("¡Valida inspeccionando el anidamiento del JSON!")