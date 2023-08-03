from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/<str:slug>/", CategoryView.as_view(), name="category"),
    path("products/<str:slug>/", ProductListView.as_view(), name="products"),
    path("product/<str:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path("news-events/", NewsEventsView.as_view(), name="news-events"),
    path("news/<str:slug>/", NewsDetailView.as_view(), name="news"),
    path("event/<str:slug>/", EventDetailView.as_view(), name="event"),
    path("blog/", BlogsView.as_view(), name="blog"),
    path("blog/<str:slug>/", BlogDetailView.as_view(), name="blog"),
    path("about-us/", AboutView.as_view(), name="about-us"),
    path("career/", CareerView.as_view(), name="career"),
    path("career/career-form/", CareerApplicationView.as_view(), name="career-form"),
    path("warranty/", WarrantyView.as_view(), name="warranty"),
    path("delivery-polices/", DeliveryPolicyView.as_view(), name="delivery-polices"),
    path("enquiry/", EnquiryView, name="enquiry"),
    path("search/", SearchView.as_view(), name="search"),


    path("products/<str:slug>/filter/", FilterProductView.as_view(), name="filter"),
 

  
]
