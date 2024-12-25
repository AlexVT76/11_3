import inspect
def introspection_info(obj):
    info={'type':type(obj),'attributes': inspect.getmembers(obj),
          "methods": inspect.ismethod(obj),'module':inspect.getmodule(obj) }
    return info



number_info = introspection_info(42)
print(number_info)