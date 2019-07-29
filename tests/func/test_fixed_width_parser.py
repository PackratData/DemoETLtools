"""Placeholder test file."""
from decimal import Decimal
from datetime import datetime

from app.utilities import to_bytes
from app.data.entities.vehicles import VehicleRepairRecord
from app.extract.fixedwidth.parsers import FixedWidthParser


def test_unpack_with_parsing_rules1():
    """"""

    fixed_width_parser = FixedWidthParser(source_data_type='vehicle_repairs')

    fixed_width_record = '211103/27/2015 12:00:00 AM14415X01917      28213    SNOW BREAKDOWN                        HYD LEAKSENT TO CAT TO REPAIR/REPLACE MAIN HYDRAULIC CONTROL VALVE AND ASSYHO PENNINVOICE WOCE0581604$9,083.02                                                                                                 9083.0209083.02'

    parsed_data = fixed_width_parser.parse_textdata(to_bytes(fixed_width_record))
    parsed_record = VehicleRepairRecord(*parsed_data)

    assert parsed_record.dept == 2111
    assert parsed_record.jobdate == datetime.strptime('2015-03-27 00:00:00', '%Y-%m-%d %H:%M:%S')
    assert parsed_record.jobno == 14415
    assert parsed_record.vehicleid == 'X01917'
    assert parsed_record.unitno == 282
    assert '13    SNOW BREAKDOWN' in parsed_record.reason
    assert 'HYD LEAKSENT TO CAT' in parsed_record.notes
    assert parsed_record.costparts == Decimal('9083.02')
    assert parsed_record.costlabor == Decimal('0')
    assert parsed_record.costtotal == Decimal('9083.02')

    # Additional Data
    assert parsed_record.yearmon == '2015-03'


def test_unpack_with_parsing_rules2():
    """"""

    fixed_width_parser = FixedWidthParser(source_data_type='vehicle_repairs')

    fixed_width_record = '211103/26/2015 12:00:00 AM14735B31276      17713    SNOW BREAKDOWN                        CHECK NOISE IN REAR- END (DIFF)TOWED FROM VEHICLE MAINTENANCE TO INTERSTATE FORD IN MILFORDBILLS TOWING, INVOICE 165003$250.00GABRIELLI FORDREPLACE REAR , BEARINGS, SEALSU-JOINTSINVOICE 85031MS      $4570.804820.8 04820.8 '

    parsed_data = fixed_width_parser.parse_textdata(to_bytes(fixed_width_record))
    parsed_record = VehicleRepairRecord(*parsed_data)

    assert parsed_record.dept == 2111
    assert parsed_record.jobdate == datetime.strptime('2015-03-26 00:00:00', '%Y-%m-%d %H:%M:%S')
    assert parsed_record.jobdate.strftime('%Y-%m-%d %H:%M:%S') == '2015-03-26 00:00:00'
    assert parsed_record.jobdate != '2015-03-26 00:00:00'
    assert parsed_record.jobno == 14735
    assert parsed_record.jobno != '14735'
    assert parsed_record.vehicleid == 'B31276'
    assert parsed_record.unitno != '177'
    assert '13    SNOW BREAKDOWN' in parsed_record.reason
    assert 'TOWED FROM VEHICLE MAINTENANCE' in parsed_record.notes
    assert parsed_record.costparts == Decimal('4820.80')
    assert parsed_record.costlabor == Decimal('0')
    assert parsed_record.costlabor == 0
    assert parsed_record.costtotal == Decimal('4820.80')
    assert parsed_record.costtotal != 4820.8

    # Additional Data
    assert parsed_record.yearmon == '2015-03'
