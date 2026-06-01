from ..models import unitModel

def list_units():
    return unitModel.getAllUnits()
