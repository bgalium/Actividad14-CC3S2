"""Patrón Composite
Permite tratar múltiples recursos Terraform como una única unidad lógica o módulo compuesto.
"""

from typing import List, Dict, Any

class CompositeModule:
    """
    Clase que agrega múltiples diccionarios de recursos Terraform como un módulo lógico único.
    Sigue el patrón Composite, donde se unifican estructuras individuales en una sola jerarquía.
    """

    def __init__(self) -> None:
        """
        Inicializa la estructura compuesta como una lista vacía de recursos hijos.
        Cada hijo será un diccionario que contiene bloques Terraform.
        """
        self._children: List[Dict[str, Any]] = []

    def add(self, resource_dict: Dict[str, Any]) -> None:
        """
        Agrega un diccionario de recurso (por ejemplo, con una clave 'resource') al módulo.

        Args:
            resource_dict: Diccionario que representa un recurso Terraform.
        """
        self._children.append(resource_dict)

    def export(self) -> Dict[str, Any]:
        """
        Exporta todos los recursos agregados a un único diccionario.
        Esta estructura se puede serializar directamente a un archivo Terraform JSON válido.

        Returns:
            Un diccionario con todos los recursos combinados bajo la clave "resource".
        """
        aggregated: Dict[str, Any] = {"resource": {}, "module": {}}
        for child_dict in self._children:
            if "resource" in child_dict:
                resources = child_dict.get("resource", [{}])[0]
                for res_type, res_block in resources.items():
                    if res_type not in aggregated["resource"]:
                        aggregated["resource"][res_type] = []
                    aggregated["resource"][res_type].extend(res_block)

            if "module" in child_dict:
                modules = child_dict.get("module", [{}])[0]
                for mod_name, mod_block in modules.items():
                    if mod_name not in aggregated["module"]:
                        aggregated["module"][mod_name] = []
                    aggregated["module"][mod_name].extend(mod_block)

        if not aggregated["resource"]:
            del aggregated["resource"]
        if not aggregated["module"]:
            del aggregated["module"]
        return aggregated
