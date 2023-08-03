from django.urls import path
from .views import *

urlpatterns = [
    path("add-cart/", AddProductToCartView.as_view(), name="add-cart"),
    path("remove-cart/", RemoveProductFromCartView.as_view(), name="remove-cart"),
    path("carts/", CartListView.as_view(), name="carts"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("checkout-summary/", CheckoutSummaryView.as_view(), name="checkout-summary"),
    path("review-product/", ReviewProductView.as_view(), name="review-product"),
  
]
