class VariableDescriptor:
    def __init__(self, variable_factory):
        self.variable_factory = variable_factory
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if self.name not in obj.__dict__:
            obj.__dict__[self.name] = self.variable_factory()
        
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        raise AttributeError("can't set attribute")


class VariableValueDescriptor:
    def __init__(self, linked_descriptor: VariableDescriptor):
        self.linked_descriptor = linked_descriptor
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return self.linked_descriptor.__get__(obj).get()
    
    def __set__(self, obj, value):
        self.linked_descriptor.__get__(obj).set(value)


def tk_variable(variable_factory):
    var = VariableDescriptor(variable_factory)
    return var, VariableValueDescriptor(var)
