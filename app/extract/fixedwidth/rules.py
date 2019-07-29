import attr


DATA_TYPES = ['string', 'integer', 'decimal', 'boolean', 'bigint', 'tinyint', 'datetime', 'date', 'double']

###########################################################
# Create Data Classes for parsing fixed width text objects
#
# Developer Notes:
# *
###########################################################

@attr.s
class FixedWidthParsingRule(object):
    """
    A list of FixedWidthParsingRule objects are the rules
    for parsing Fixed Width Data

    # DEVELOPER NOTES
    * field is ignored during parsing
    """

    # Declare core attributes of FixedWidthParsingRule
    shortname = attr.ib(validator=attr.validators.instance_of(str))
    field = attr.ib(validator=attr.validators.instance_of(str))
    displacement = attr.ib(converter=int)
    length = attr.ib(converter=int)
    data_type = attr.ib(validator=attr.validators.instance_of(str))

    # noinspection PyUnusedLocal
    @data_type.validator
    def validate_data_type(self, attribute, value):
        if value.lower() not in DATA_TYPES:
            raise ValueError(str(value) + " is not a supported data type.")

###########################################################
# Create Rules for parsing fixed width text objects
#
# Developer Notes:
# * These rules are used to parse fixed width text
###########################################################

class ParsingRules(object):
    """
    ParsingRules is a reference object that contains metadata used to
    parse Fixed Width text objects

    """

    """
    shortname = attr.ib(validator=attr.validators.instance_of(str))
    field = attr.ib(validator=attr.validators.instance_of(str))
    displacement = attr.ib(converter=int)
    length = attr.ib(converter=int)
    data_type = attr.ib(validator=attr.validators.instance_of(str))
    """

    _rules = {
        # vehicle_repairs
        'vehicle_repairs': (
            FixedWidthParsingRule('dept', 'Department', 1, 4, 'integer'),
            FixedWidthParsingRule('jobdate', 'Job Date', 5, 22, 'date'),
            FixedWidthParsingRule('jobno', 'Job Number', 27, 5, 'integer'),
            FixedWidthParsingRule('vehicleid', 'Vehicle ID', 32, 12, 'integer'),
            FixedWidthParsingRule('unitno', 'Unit Number', 44, 3, 'integer'),
            FixedWidthParsingRule('reason', 'Reason', 47, 44, 'string'),
            FixedWidthParsingRule('notes', 'Notes', 91, 207, 'string'),
            FixedWidthParsingRule('costparts', 'Parts Cost', 298, 7, 'decimal'),
            FixedWidthParsingRule('costlabor', 'Labor Cost', 305, 1, 'decimal'),
            FixedWidthParsingRule('costtotal', 'Total Cost', 306, 7, 'decimal')
        ),
    }

    @classmethod
    def get(cls, source_data_type):
        """Return a created Configs class."""
        c = cls._rules.get(source_data_type)
        if c is None:
            m = "The Fixed Width source_data_type={} has no parsing rules.".format(source_data_type)
            raise TypeError(m)
        return c
