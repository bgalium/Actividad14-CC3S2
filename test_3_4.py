import os
from iac_patterns.builder import InfrastructureBuilder
from iac_patterns.singleton import ConfigSingleton

PATH_TF_DIR = "terraform"
PATH_15 = os.path.join(PATH_TF_DIR, "main_15.tf.json")
PATH_150 = os.path.join(PATH_TF_DIR, "main_150.tf.json")

def generate_file(count: int, path: str):

    print(f"--- Generando archivo con {count} recursos en: {path} ---")
    
    ConfigSingleton._instances = {}
    
    builder = InfrastructureBuilder(env_name=f"fleet_{count}")
    builder.build_null_fleet(count=count)
    builder.export(path=path)

generate_file(15, PATH_15)
generate_file(150, PATH_150)

print("\nArchivos generados!")
