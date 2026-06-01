from ..models import productTypeModel

def get_types():
    return productTypeModel.getAllProductTypes()
