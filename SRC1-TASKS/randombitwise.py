def toggle_string(s: str) -> str:
    return_s = ...
    for c in s:
        return_s += chr(ord(s)^0x20)
    return return_s


print(toggle_string('S'))