from django.urls import path
from .views import ViewCart, ViewWishlist

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('', ViewWishlist.as_view(), name='wishlist'),
]

