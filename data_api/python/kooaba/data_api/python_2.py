# -*- coding: utf-8 -*-

EOL = "\n"

def to_hashable(data):
    """ Convert data to a hashable type. """
    return str(data)

def ascii_to_hashable(data):
    """ Convert ASCII text data to a hashable type. """
    return str(data)

__all__ = ['to_hashable', 'ascii_to_hashable', 'EOL']