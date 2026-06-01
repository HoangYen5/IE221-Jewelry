from ..models import supplierModel

def get_suppliers():
    return supplierModel.getAllSuppliers()

def get_supplier(supplier_id):
    return supplierModel.getSupplierById(supplier_id)

def create_supplier(data: dict):
    return supplierModel.createSupplier(data)

def update_supplier(supplier_id, data: dict):
    return supplierModel.updateSupplier(supplier_id, data)

def delete_supplier(supplier_id):
    return supplierModel.deleteSupplier(supplier_id)
