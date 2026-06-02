from ..models import serviceTypeModel

def list_service_types():
    return serviceTypeModel.getAllServiceTypes()

def create_service_type(data: dict):
    return serviceTypeModel.createServiceType(data)

def update_service_type(type_id, data: dict):
    return serviceTypeModel.updateServiceType(type_id, data)

def delete_service_type(type_id):
    return serviceTypeModel.deleteServiceType(type_id)
