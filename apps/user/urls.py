from django.urls import path
from .views import *

urlpatterns = [
    path("pincode/", GetPincodeDetails.as_view(), name="pincode"),
    path("product-models/", GetProductTypeModelsView.as_view(), name="product-models"),
    path("register/", CustomerRegistrationView.as_view(), name="register"),
    path("login/", CustomerLoginView.as_view(), name="login"),
    path('logout/', CustomerLogoutView.as_view(), name='logout'),
    path("dashboard/", CustomerDashboardView.as_view(), name="customer-dashboard"),
    path("profile/", CustomerProfileView.as_view(), name="customer-profile"),
    path("orders/", CustomerOrdersView.as_view(), name="customer-orders"),
    path("address/", CustomerAddressView.as_view(), name="customer-address"),
    path("track/<str:order_id>", CustomerOrderTrackView.as_view(), name="customer-order-track"),
    path("change-password/", CustomerChangePasswordView.as_view(), name="change-password"),
    # path("enquiry/", EnquiryView.as_view(), name="enquiry")
]
