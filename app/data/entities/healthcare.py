import attr
from decimal import decimal

from app.data.validators import (
    check_longitude,
    check_latitude,
)


###########################################################
# Data Classes for Health Data Records
#
# Developer Notes:
# * Use these data classes to store data loaded from
#   Health Data Records at https://healthdata.gov/search
###########################################################
@attr.s
class EHRPaymentRecord(object):
    """

    Reference
    https://healthdata.gov/dataset/electronic-health-record-ehr-incentive-program-payments-eligible-providers
    """

    # Declare core attributes of EHR Payment Record
    x = attr.ib(validator=[attr.validators.instance_of(decimal), check_longitude])              # longitude
    y = attr.ib(validator=[attr.validators.instance_of(decimal), check_latitude])               # latitude
    provider_name = attr.ib(validator=attr.validators.instance_of(str))
    npi = attr.ib(converter=int)
    medicaid_ep_hospital_type = attr.ib(validator=attr.validators.instance_of(str))
    specialty = attr.ib(validator=attr.validators.instance_of(str))
    business_street_address = attr.ib(validator=attr.validators.instance_of(str))
    business_city = attr.ib(validator=attr.validators.instance_of(str))
    business_county = attr.ib(validator=attr.validators.instance_of(str))
    business_zip_code = attr.ib(validator=attr.validators.instance_of(str))
    business_state_territory = attr.ib(validator=attr.validators.instance_of(str))
    program_year = attr.ib(converter=int)
    payment_year = attr.ib(converter=int)
    payment_year_number = attr.ib(converter=int)
    payment_criteria_medicaid_only = attr.ib(validator=attr.validators.instance_of(str))
    payee_name = attr.ib(validator=attr.validators.instance_of(str))
    payee_npi = attr.ib(converter=int)
    disbursement_amount = attr.ib(converter=int)
    total_payments = attr.ib(converter=int)
    longitude = attr.ib(validator=[attr.validators.instance_of(decimal), check_longitude])      # longitude
    latitude = attr.ib(validator=[attr.validators.instance_of(decimal), check_latitude])        # latitude
    fid = attr.ib(converter=int)
