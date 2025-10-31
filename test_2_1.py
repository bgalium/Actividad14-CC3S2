from iac_patterns.singleton import ConfigSingleton
import time

print(' Ejercicio 2.1: Singleton reset')
c1 = ConfigSingleton("dev")
created = c1.created_at
c1.settings["x"] = 1
c1.reset()
assert c1.settings == {}
assert c1.created_at == created
print('El método reset() funciona.')