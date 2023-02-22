from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CartItemShop, Cart, Product


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


class ViewCartBuy(View):
   def get(self, request, product_id):
       product = get_object_or_404(Product, id=product_id)
       cart_user = get_object_or_404(Cart, user=request.user)
       cart_item = CartItemShop(cart=cart_user, product=product)
       cart_item.save()
       return redirect('cart_shop:cart')


class ViewCartDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemShop, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')


class ViewCartAdd(View):
   def get(self, request, product_id):
       product = get_object_or_404(Product, id=product_id)
       cart_user = get_object_or_404(Cart, user=request.user)
       cart_item = CartItemShop(cart=cart_user, product=product)
       cart_item.save()
       return redirect('home:index')


class ViewWishlist(View):
   def get(self, request):
       return render(request, 'cart_shop/wishlist.html')