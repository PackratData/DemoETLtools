

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8') # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value # Instance of bytes

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8') # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value # Instance of str
