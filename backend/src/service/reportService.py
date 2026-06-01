from ..models import reportModel

def get_report(params=None):
    return reportModel.getReport(params)
