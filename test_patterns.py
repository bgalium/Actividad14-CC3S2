from iac_patterns.singleton import ConfigSingleton
from iac_patterns.factory import NullResourceFactory
from iac_patterns.prototype import ResourcePrototype
from iac_patterns.composite import CompositeModule

# Test 1: Singleton 
def test_singleton_meta():
    ConfigSingleton._instances = {}
    a = ConfigSingleton(env_name="X")
    
    b = ConfigSingleton(env_name="Y") 
    
    assert a is b
    assert a.env_name == "X"
    assert b.env_name == "X" 

# Test 2: Prototype 
def test_prototype_clone_independent():

    proto = ResourcePrototype(NullResourceFactory.create("app"))

    c1_obj = proto.clone(lambda d: d.update({"f1": 1}))
    c2_obj = proto.clone(lambda d: d.update({"b1": 2}))

    c1_data = c1_obj.data
    c2_data = c2_obj.data

    assert "f1" in c1_data
    assert "b1" in c2_data
    assert "f1" not in c2_data
    assert "b1" not in c1_data

# Test 3
def test_factory_creates_resource_structure():

    res = NullResourceFactory.create("test_res")
    assert "resource" in res
    assert "null_resource" in res["resource"][0]
    assert "test_res" in res["resource"][0]["null_resource"][0]

# Test 4: Composite 
def test_composite_export_merges():

    comp = CompositeModule()
    comp.add(NullResourceFactory.create("res1"))
    comp.add(NullResourceFactory.create("res2"))
    
    data = comp.export()
    
    assert len(data["resource"]["null_resource"]) == 2
    assert "res1" in data["resource"]["null_resource"][0]
    assert "res2" in data["resource"]["null_resource"][1]

# Test 5: Singleton Reset 
def test_singleton_reset_method():

    s = ConfigSingleton(env_name="test") 
    s.reset() 
    s.set("key", "value")
    
    assert s.settings["key"] == "value"
    s.reset()
    assert s.settings == {}