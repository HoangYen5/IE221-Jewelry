from ..models import customerModel

def get_customers():
    return customerModel.getAllCustomers()

def get_customer(customer_id):
    return customerModel.getCustomerById(customer_id)

def create_customer(data: dict):
    return customerModel.createCustomer(data)

def update_customer(customer_id, data: dict):
    return customerModel.updateCustomer(customer_id, data)

def delete_customer(customer_id):
    return customerModel.deleteCustomer(customer_id)
