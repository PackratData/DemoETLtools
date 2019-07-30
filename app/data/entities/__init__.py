from app.utilities.enums import EtlDataEntities
from app.data.entities import (
    healthcare,
    vehicles,
)


def get_data_entity_class(etl_data_entity_type):

    if etl_data_entity_type == EtlDataEntities.VEHICLE_REPAIRS.value:
        data_entity = vehicles.VehicleRepairRecord

    else:
        raise TypeError("{} is not a supported data entity type".format(etl_data_entity_type))

    return data_entity
