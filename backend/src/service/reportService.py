from ..models import reportModel


def get_report(params=None):
    return reportModel.getReport(params)


def get_report_by_id(thang: int, nam: int, ma_san_pham: str):
    return reportModel.getReportById(thang, nam, ma_san_pham)


def create_report(data: dict):
    return reportModel.createReport(data)
