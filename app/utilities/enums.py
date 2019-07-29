from enum import Enum


class EtlDataEntities(Enum):
    """
    Enumerated lists of Data Entities
    """
    VEHICLE_REPAIRS = 'vehicle_repairs'
    HEALTHCARE_PAYMENTS = 'healthcare_payments'


class EtlFileTypes(Enum):
    """
    Enumerated lists of File Types.
    """
    TXT = 'txt'     # Fixed Width Format Text File
    CSV = 'csv'     # CSV Delimited Text File
    XML = 'xml'     # XML File
    JSON = 'json'   # JSON File


class ContentTypes(Enum):
    """
    Enumerated lists of Mime Content Types.
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types
    """
    CSS = 'text/css'
    CSV = 'text/csv'
    JAVASCRIPT = 'application/javascript'
    JSON = 'application/json'
    HTML = 'text/html'
    PDF = 'application/pdf'
