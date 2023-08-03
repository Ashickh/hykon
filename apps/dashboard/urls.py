from django.urls import path
from .views import *


urlpatterns = [
  
    path("", DashboardView.as_view(), name="dashboard"),
    path("products_dash/", ProductListView.as_view(), name="products_dash"),
    path("order_dash/", OrderDashboardView.as_view(), name="order_dash"),
    path("orders/order_details/<int:id>", OrderDetailView.as_view(), name="order_details"),
    path("orders/track-order/<int:id>", OrderTrackView.as_view(), name="track-order"),
    path("admin_profile/", AdminProfileView.as_view(), name="admin_profile"),
    path("enquiry_dash/", EnquiryDashboardView.as_view(), name="enquiry_dash"),
    path("warranty_dash/", WarrantyListDashboardView.as_view(), name="warranty_dash"),
    


  
]