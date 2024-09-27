"""This module contains dangerous functions!"""
import functions
import ctypes
import warnings
import sys
import binascii
function = type(lambda: None)

if sys.version < (3, 10):
    raise SystemError("this Python script only works in Python 3.10 or above")


def bytes_view(bytes_, /,
                  *, # Keyword-only so parameters can be passed in any order.
                  sep=b' ',
                  prefix = b"", 
                  suffix =  b"",  
                  encoding='latin1', 
                  errors='surrogatepass', 
                  upper=True, 
                  rows: int|None=16) -> str:
    """Shows how a string is represented in encoded bytes."""
    if (rows is not None) or (rows > 0):
        returnée = ""
        groups = [bytes_[i:i+rows] for i in range(0, len(bytes_), rows)]
        new_groups = []
        for i in groups:
            if upper:
                addition = binascii.b2a_hex(i, sep).decode().upper()
            else:
                addition = binascii.b2a_hex(i, sep).decode()
            # Adds "--" for absence of a byte.
            if len(i) < rows:
                addition+=' --'* (rows - len(i))

            new_groups.append(addition)
        print('\n'.join(new_groups)) if bytes_ != b'' else print(' NO DATA '.center(rows*3 - 1, '\u2500'))
        return None
    j = binascii.b2a_hex(bytes_, sep)
##    import re
##    j = j.decode()
##    if re.match('.*[^0-9A-Fa-f]+.*', sep) or not sep
    if upper:
        return (prefix + j + suffix).decode().upper()
    return (prefix + j + suffix)

def pyobject_raw_data(OBJECT, /, *, bytes_ = False) -> bytes:
    """Returns a true representation of how Python stores objects in memory!"""
    résultat = (ctypes.c_byte * sys.getsizeof(OBJECT)).from_address(id(OBJECT))
    if bytes_:
        return bytes(résultat)
    else:
        return résultat


def PyObject_hex_dump(OBJECT, /, *, metadata = True, position = "top",) -> None:
    """Prints a hex-dump of PyObject.
    if metadata is True, its ID, size, type and value are displayed.
    position indicates if metadata should go before or after data"""
    DATA = ' HEX DUMP OF BYTES '.center(47, '─')
    INFORMATION = f"""\
ID:    0x{id(OBJECT):016X} ({id(OBJECT)})
Size:  {sys.getsizeof(OBJECT)} bytes
Type:  {OBJECT.__class__}
Value: {OBJECT!r}"""
    if metadata:
        if position == "top":
            print(f"""{INFORMATION}\n{DATA}""")
            bytes_view(pyobject_raw_data(OBJECT, bytes_=True))
        elif position == "bottom":
            bytes_view(pyobject_raw_data(OBJECT, bytes_=True))
            print(f"""{DATA}\n{INFORMATION}""" )
        else:
            raise ValueError("position can only be either 'top' or 'bottom'")
    else:
        bytes_view(pyobject_raw_data(OBJECT, bytes_=True))



def ___unicodevalue(Unicode·codepoint, /):
    """Creates a string with a codepoint greater than U+10FFFF (max: 0xFFFF_FFFF).
Warning: some operations (e.g. slicing) won't work properly on these strings.
If 0 <= codepoint <= 0x10FFFF, a normal string is returned."""
    # Prevents bugs, such as (___unicodevalue(126) != '~') == True, with characters between U+0000 and U+10FFFF.
    # It also avoids creating strings that occupy too much memory.
    if 0 <= Unicode·codepoint <= 1114111:
        return chr(Unicode·codepoint) # Avoids comparison bugs with '=='.
    elif Unicode·codepoint == -1:
        return '' # Secret undocumented feature!… Unless you’re one of few people who actually looks at the source code
    elif Unicode·codepoint > 0xFFFF_FFFF:
        raise ValueError(f"codepoint must be ≥ 0 and ≤ 0xFFFF_FFFF ({0xFFFF_FFFF})") # Creates a string with a different ID.
    elif Unicode·codepoint < 0:
        raise ValueError(f"negative Unicode codepoints not allowed") # Creates a string with a different ID.
    else:
        if ___unicodevalue.warn:
            warnings.warn("you’re creating an illegal string!", Warning)
        illegal_character = chr(1114111)
        # If highest codepoint ≥ U+10000, codepoint is internally encoded as UTF-32-LE.
        little_endian = list(Unicode·codepoint.to_bytes(length=4, byteorder='little'))
        # Modifies memory value of PyObject.
        functions.pyobject_raw_data(illegal_character,)[56:60] = little_endian
        return illegal_character
___unicodevalue.my·comments = r"Illegal strings like '\U00110000' CAN be sliced, but it must be sliced like '\U00110000'[0:1] and not like '\U00110000'[0]"
___unicodevalue.warn = True


def negative_positional_argument(negative_int, /, *, code = "pass", name=None, mode='exec', globals={}):
    """\
    Returns a function that accepts a negative amount of positional arguments."""
    if type(negative_int) is not int:
        raise TypeError(f"{type(negative_int).__name__!r} cannot be interpreted as an integer")
    elif negative_int > 0:
          raise ValueError("integer must be ≤ 0")
    dangerǃ =  function(compile(code, '© Mehdical Man! 2024', mode=mode,),   
             globals=globals,                                            # globals
             argdefs=(None,) * -negative_int)               # Multiplies the length of argdefs by -1,
                                                            # function call
    if name is not None:
        dangerǃ.__qualname__ = name 
    return dangerǃ
negative_positional_argument.accept·positive·integer·as·negative = False

##negative_positional_argument.__signature__='(negative·integer, /)'
