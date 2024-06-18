class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = 'This attribute was added dynamically'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Meta):
    pass


print(MyClass.added_attribute)
