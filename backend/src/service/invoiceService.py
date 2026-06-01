from ..models import invoiceModel

def get_invoices():
    return invoiceModel.getAllInvoices()

def get_invoice(invoice_id):
    return invoiceModel.getInvoiceById(invoice_id)

def create_invoice(data: dict):
    return invoiceModel.createInvoice(data)

def update_invoice(invoice_id, data: dict):
    return invoiceModel.updateInvoice(invoice_id, data)

def delete_invoice(invoice_id):
    return invoiceModel.deleteInvoice(invoice_id)
