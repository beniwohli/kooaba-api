# -*- coding: utf-8 -*-

EOL = b"\n"

def to_hashable(data):
    """ Convert data to a hashable type. """
    if isinstance(data, bytes):
        return data
    else:
        return str(data).encode()

def ascii_to_hashable(data):
    """ Convert ASCII text data to a hashable type. """
    if isinstance(data, bytes):
        return data
    else:
        return str(data).encode('ascii')

__all__ = ['to_hashable', 'ascii_to_hashable', 'EOL']