from ..models import unitModel

def list_units():
    return unitModel.getAllUnits()

def get_unit(unit_id):
    return unitModel.getUnitById(unit_id)

def search_units(keyword):
    return unitModel.searchUnits(keyword)

def get_next_code():
    return unitModel.getNextCode()

def create_unit(data: dict):
    return unitModel.createUnit(data)

def update_unit(unit_id, data: dict):
    return unitModel.updateUnit(unit_id, data)

def delete_unit(unit_id):
    return unitModel.deleteUnit(unit_id)
