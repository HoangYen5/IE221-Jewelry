from ..models import purchaseModel

def get_purchases():
    return purchaseModel.getAllPurchases()

def get_purchase(purchase_id):
    return purchaseModel.getPurchaseById(purchase_id)

def create_purchase(data: dict):
    return purchaseModel.createPurchase(data)

def update_purchase(purchase_id, data: dict):
    return purchaseModel.updatePurchase(purchase_id, data)

def delete_purchase(purchase_id):
    return purchaseModel.deletePurchase(purchase_id)
