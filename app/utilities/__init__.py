from .enums import EtlDataEntities, EtlFileTypes


def get_data_entity_type(filename):
    if filename.lower().startswith('vehicle_repairs.'):
        return EtlDataEntities.VEHICLE_REPAIRS.value

    else:
        return TypeError("{} is not a supported data entity".format(filename))


def get_file_type(filename):

    if filename.lower().endswith('.csv'):
        return EtlFileTypes.CSV.value

    elif filename.lower().endswith('.txt'):
        return EtlFileTypes.TXT.value

    elif filename.lower().endswith('.xml'):
        return EtlFileTypes.XML.value

    elif filename.lower().endswith('.json'):
        return EtlFileTypes.JSON.value

    else:
        return TypeError("{} is not a supported file type".format(filename))


def to_bytes(bytes_or_str):

    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')    # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value    # Instance of bytes


def to_str(bytes_or_str):

    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')    # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value    # Instance of str
