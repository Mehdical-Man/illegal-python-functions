"""This module contains dangerous functions!"""
import functions
import warnings
function = type(lambda: None)

def ___unicodevalue(Unicode·codepoint, /):
    """Creates a string with a codepoint greater than U+10FFFF (max: 0xFFFF_FFFF).
Warning: some operations (e.g. slicing) won't work properly on these strings.
If 0 <= codepoint <= 0x10FFFF, a normal string is returned."""
    # Prevents bugs, such as (___unicodevalue(126) != '~') == True, with characters between U+0000 and U+10FFFF.
    # It also avoids creating strings that occupy too much memory.
    if 0 <= Unicode·codepoint <= 1114111:
        return chr(Unicode·codepoint) # Avoids comparison bugs with '=='.
    elif Unicode·codepoint == -1:
        return '' # Secret undocumented feature!
    elif Unicode·codepoint > 0xFFFF_FFFF:
        raise ValueError(f"codepoint must be ≥ 0 and ≤ 0xFFFF_FFFF ({0xFFFF_FFFF})") # Creates a string with a different ID.
    elif Unicode·codepoint < 0:
        raise ValueError(f"negative Unicode codepoints not allowed") # Creates a string with a different ID.
    else:
        if ___unicodevalue.warn:
            warnings.warn("You’re creating an illegal string", Warning)
        illegal_character = chr(1114111)
        # If highest codepoint ≥ U+10000, codepoint is internally encoded as UTF-32-LE.
        little_endian = list(Unicode·codepoint.to_bytes(length=4, byteorder='little'))
        # Modifies memory value of PyObject.
        functions.pyobject_raw_data(illegal_character,)[56:60] = little_endian
        return illegal_character
___unicodevalue.my·comments = r"Illegal strings like '\U00110000' CAN be sliced, but it must be sliced like '\U00110000'[0:1] and not like '\U00110000'[0]"
___unicodevalue.warn = True


def negative_positional_argument(negative_int, /, *, code = "pass", name=None, mode='single', globals={}):
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
