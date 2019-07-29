import struct
from .rules import ParsingRules


###########################################################
# Use FixedWidthParser to split textdata into
# relevant data fields
###########################################################

class FixedWidthParser(object):

    def __init__(self, source_data_type, excluded_fields=None):
        self.source_data_type = source_data_type
        self.excluded_fields = excluded_fields if excluded_fields else list()
        self.parsing_rules = ParsingRules.get(self.source_data_type)

        # DEVELOPER NOTES
        # Create fixed_width_parser for any shortname variable not listed in optional excluded_fields
        #  * Use the 'struct' module to operate on binary data
        #  * Assumes that fixed format text file is not UTF8 encoded, so 100 bytes will always be 100 characters
        fmtstring = ' '.join('{}{}'.format(pr.length, 'x' if pr.shortname in self.excluded_fields else 's') for pr in self.parsing_rules)
        # print("fmtstring text string is: '{}'".format(fmtstring))

        # Instantiate a Struct object   https://docs.python.org/3.6/library/struct.html#struct.Struct
        struct_parser = struct.Struct(fmtstring)
        self.fixed_width_parser = struct_parser.unpack_from
        # print('fmtstring: {!r}, recsize: {} chars'.format(fmtstring, struct_parser.size))

    def parse_textdata(self, textdata):
        """

        :param textdata:
        :return:
        """
        return self.fixed_width_parser(textdata)
