import json
import os
from iac_patterns.composite import CompositeModule
from iac_patterns.factory import NullResourceFactory

PATH_TF_JSON = "terraform/main.tf.json"
print("Probando Ejercicio 2.4")

network_module = CompositeModule()
network_module.add(NullResourceFactory.create(name="vpc_subnet"))

app_module = CompositeModule()
app_module.add(NullResourceFactory.create(name="app_instance"))

root_module = CompositeModule()

root_module.add({"module": [{"network": [network_module.export()]}]})
root_module.add({"module": [{"app": [app_module.export()]}]})

final_json = root_module.export()

os.makedirs(os.path.dirname(PATH_TF_JSON), exist_ok=True)
with open(PATH_TF_JSON, "w") as f:
    json.dump(final_json, f, indent=4)

print(f"Archivo JSON con submódulos generado en: {PATH_TF_JSON}")
