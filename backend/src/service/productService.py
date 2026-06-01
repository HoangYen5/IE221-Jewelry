from ..models import productModel

def list_products():
    return productModel.getAllProducts()

def list_categories():
    return productModel.getAllCategories()

def get_product(product_id):
    return productModel.getProductById(product_id)

def create_product(data: dict):
    return productModel.createProduct(data)

def update_product(product_id, data: dict):
    return productModel.updateProduct(product_id, data)

def delete_product(product_id):
    return productModel.deleteProduct(product_id)

def activate_product(product_id):
    return productModel.activateProduct(product_id)

def delete_products(product_ids):
    return productModel.deleteProducts(product_ids)

