from django.shortcuts import render
from django.views import View
from .models import CartItemShop


class ViewCart(View):
   def get(self, request):
       cart_items = CartItemShop.objects.filter(cart__user=request.user)
       data = list(cart_items)
       total_price_no_discount = sum(item.product.price * item.quantity for item in data)
       total_discount = sum(item.product.price * item.product.discount * item.quantity for item in data if item.product.discount is not None) / 100
       total_sum = total_price_no_discount - total_discount
       context = {'cart_items': data,
                  'total_price_no_discount': total_price_no_discount,
                  'total_discount': total_discount,
                  'total_sum': total_sum,
                  }
       return render(request, 'cart_shop/cart.html', context)

class ViewWishlist(View):
   def get(self, request):
       return render(request, 'cart_shop/wishlist.html')