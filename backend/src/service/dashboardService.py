from ..models import dashboardModel

def get_stats():
    return dashboardModel.getDashboardStats()

def get_revenue():
    return dashboardModel.getRevenue()

def get_category():
    return dashboardModel.getCategory()

def get_order():
    return dashboardModel.getOrder()
