# -*- coding: utf-8 -*-

try:
    from django.utils import six
except ImportError:
    try:
        import six
    except ImportError:
        print("Please install external lib:\n\n\tpip install six")
        raise

try:
    from django.utils.encoding import python_2_unicode_compatible
except ImportError:
    def python_2_unicode_compatible(klass):
        """
        A decorator that defines __unicode__ and __str__ methods under Python 2.
        Under Python 3 it does nothing.

        To support Python 2 and 3 with a single code base, define a __str__ method
        returning text and apply this decorator to the class.
        """
        if six.PY2:
            klass.__unicode__ = klass.__str__
            klass.__str__ = lambda self: self.__unicode__().encode('utf-8')
        return klass
