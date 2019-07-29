import attr

from dateutil.parser import parse
from datetime import datetime
from decimal import Decimal
from app.utilities import to_str

###########################################################
# Data Classes for Vehicle Repairs
#
# Developer Notes:
# * Use these data classes to store data
###########################################################
@attr.s
class VehicleRepairRecord(object):
    """

    Reference
    https://catalog.data.gov/dataset/vehicle-repairs
    Dept,JobDate,jobno,Vehicleid,UnitNo,Reason,Notes,CostParts,CostLabor,CostTotal
    """

    # Declare attributes of Vehicle Repair object
    dept = attr.ib(converter=int)
    jobdate = attr.ib()
    jobno = attr.ib(converter=int)
    vehicleid = attr.ib()
    unitno = attr.ib(converter=int)
    reason = attr.ib()
    notes = attr.ib()
    costparts = attr.ib()
    costlabor = attr.ib()
    costtotal = attr.ib()

    def __attrs_post_init__(self):
        """
        This step is required to convert input data to proper data types
        This is awkward, but then again this is only a demo
        """

        self.jobdate = parse(to_str(self.jobdate).strip())
        self.vehicleid = to_str(self.vehicleid).strip()
        self.reason = to_str(self.reason).strip()
        self.notes = to_str(self.notes).strip()
        self.costparts = Decimal(to_str(self.costparts).strip())
        self.costlabor = Decimal(to_str(self.costlabor).strip())
        self.costtotal = Decimal(to_str(self.costtotal).strip())

        # Apply additional data transformations
        self.yearmon = datetime.strftime(self.jobdate, '%Y-%m')
