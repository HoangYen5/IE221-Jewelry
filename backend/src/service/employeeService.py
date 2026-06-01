from ..models import employeeModel

def get_employees():
    return employeeModel.getAllEmployees()

def get_employee(employee_id):
    return employeeModel.getEmployeeById(employee_id)

def create_employee(data: dict):
    return employeeModel.createEmployee(data)

def update_employee(employee_id, data: dict):
    return employeeModel.updateEmployee(employee_id, data)

def delete_employee(employee_id):
    return employeeModel.deleteEmployee(employee_id)
