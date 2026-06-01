from ..models import serviceTypeModel

def list_service_types():
    return serviceTypeModel.getAllServiceTypes()
