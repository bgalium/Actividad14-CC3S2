import json
import os
from iac_patterns.builder import InfrastructureBuilder

PATH_TF_JSON = "terraform/main.tf.json"
print("Ejercicio 3.2")

builder = InfrastructureBuilder(env_name="adapter-test")

builder.add_adapted_bucket(name="mi_bucket_adaptado")

builder.export(path=PATH_TF_JSON)

print(f"Archivo JSON con 'mock_cloud_bucket' generado en: {PATH_TF_JSON}")
