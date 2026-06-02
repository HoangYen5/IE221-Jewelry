from ..models import productTypeModel

def get_types():
    return productTypeModel.getAllProductTypes()

def create_type(data: dict):
    return productTypeModel.createProductType(data)

def update_type(type_id, data: dict):
    return productTypeModel.updateProductType(type_id, data)

def delete_type(type_id):
    return productTypeModel.deleteProductType(type_id)
