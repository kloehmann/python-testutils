def property_wrapper(properties: dict) -> object:
    """property_wrapper(properties)

    This will wrap your dict into an object with the dict items as
    properties of the object. This can be handy if you need to emulate
    opjects with properties from a mock.
    """
    return type("", (object,), properties)()


def contextmanagermock(cls):
    """@contextmanagermock decorator

    This decorator add the contextmananager protocol to your mock class.
    Mocks and MagicMocks cannot be used in code that returns the mock as
    context manager. To use this decorator, implement a dummy class and decorate
    it with this decorator.

    You can then just patch the class with your mocks
    """

    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    cls.__init__ = __init__
    cls.__enter__ = __enter__
    cls.__exit__ = __exit__
    return cls
