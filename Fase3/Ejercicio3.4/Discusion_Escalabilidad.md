# Fase 3.4: Discusión sobre Escalabilidad de JSON en IaC

La generación de archivos main.tf.json usando python presenta algunos problemas de escalabilidad, se ve en el tamaño de los archivos generados, ya que crece linealmente con la cantidad de recursos usados. Este crecimiento va a ser contraproducente a los pipelines de CI/CD.

Va a afectar los tiempos de parseo ya que un pipeline debe ejecutar terraform plan y el tiempo que se necesita para leer y procesar un archivo JSON masivo puede aumentar drásticamente, ralentizando los despliegues. Tambieén impactará en los límites de Git/storage.

Lo que se puede hacer es establecer estrategias de mitigación como la de fragmentación. Primero Módulos de terraform separados, El Builder no debería generar recursos sino bloques modules que apunten a definiciones de modulos más pequeñas y reutilizables. Otra estrategiua es generar HCL en vez de JSON, si bien JSON es más facil de generar HCL (lenguaje antivo de terraform) puede resultar en archivos más legibles, el problema es que es más complejo la programación.