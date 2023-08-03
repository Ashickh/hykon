import json
from apps.catalogue.models import Category
from apps.order.models import Cart


def main_product_categories(request):
    categories = Category.objects.filter(domestic_corporate__in=[1, 2]
                                         ).order_by('priority')
    domestic_categories = [category for category in categories if category.domestic_corporate == 1]
    corporate_categories = [category for category in categories if category.domestic_corporate == 2]
    return {'domestics': domestic_categories, 'corporates': corporate_categories}


def user_logged_in(request):
    if request.user.is_authenticated:
        cart_count = len(Cart.objects.filter(user=request.user, placed=False))
        return {'user_logged_in': True, 'name': request.user.first_name, 'cart_count': cart_count}
    else:
        print (request.COOKIES.get('cart_id', []), type(request.COOKIES.get('cart_id', [])))
        cart_id = request.COOKIES.get('cart_id', [])
        if cart_id:
            cart_id = json.loads(cart_id)
        cart_count = len(Cart.objects.filter(id__in=cart_id, placed=False))
        return {'user_logged_in': False, 'cart_count': cart_count}
