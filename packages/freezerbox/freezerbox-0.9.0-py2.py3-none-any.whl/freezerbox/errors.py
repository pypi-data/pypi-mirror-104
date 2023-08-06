#!/usr/bin/env python3

import functools
from tidyexc import Error

class Po4Error(Error):

    @property
    def brief_str(self):
        brief_str = super().brief_str
        culprit = self.data.get('culprit')

        if culprit:
            culprit = getattr(culprit, '_tag', None) or culprit
            brief_str = f"{culprit}: {brief_str}"

        return brief_str


class LoadError(Po4Error):
    # For errors relating to loading the database.
    pass

class QueryError(Po4Error):
    # For errors relating to looking up information from the database.
    pass

class ParseError(QueryError):
    # For errors relating to parsing a value from the database, e.g. a unit.
    pass

class CheckError(Po4Error):
    # For errors found when checking the database for self-consistency.
    pass



class only_raise:
    """
    Guarantee that the decorated function can only raise the given type of 
    exception.

    Any unhandled exception raised by the decorated function will be caught and 
    re-raised using an exception of the given type. 
    """

    def __init__(self, err_cls):
        self.err_cls = err_cls

    def __call__(self, f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except self.err_cls as err:
                raise err from None
            except Exception as err:
                raise self.err_cls(str(err)) from err

        return wrapper
