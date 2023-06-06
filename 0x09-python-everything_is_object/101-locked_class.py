#!/usr/bin/python3
"""Represents a class."""


class LockedClass:
    """
    LockedClass is a class that prevents the user from dynamically 
    creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    
    def __setattr__(self, name, value):
        """
        Overrides the setattr() method to control the assignment 
        of instance attributes.

        Args:
            name (str): The name of the attribute.
            value (Any): The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute being set is not 
            'first_name' or if it is not an existing attribute.
        """
        if name == 'first_name' or name in self.__dict__:
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
