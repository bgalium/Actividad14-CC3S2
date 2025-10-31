import json, os
from iac_patterns.factory import TimestampedNullResourceFactory

FORMATO_FECHA = '%Y%m%d'
PATH_TF_JSON = 'terraform/main.tf.json'

print('--- Generando JSON para Ejercicio 2.2 ---')
recurso = TimestampedNullResourceFactory.create('recurso_formato', fmt=FORMATO_FECHA)
os.makedirs(os.path.dirname(PATH_TF_JSON), exist_ok=True)
with open(PATH_TF_JSON, 'w') as f:
    json.dump(recurso, f, indent=4)
print(f'Archivo generado en {PATH_TF_JSON}')