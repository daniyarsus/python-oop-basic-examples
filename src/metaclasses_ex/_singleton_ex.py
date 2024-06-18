class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


instance1 = SingletonClass(10)
instance2 = SingletonClass(20)

print(instance1.value)
print(instance2.value)
print(instance1 is instance2)
