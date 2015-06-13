"""
Test to make sure it is possible to print all structs.
"""

from __future__ import print_function

import sdl

def test_struct():
    for name in dir(sdl):
        value = getattr(sdl, name)
        try:
            if isinstance(value, type) and value != sdl.Struct:
                print(name, value())
        except TypeError as e:
            print("TypeError", e)
        except Exception as e:
            print("Exception", e)
            
if __name__ == "__main__":
    test_struct()
