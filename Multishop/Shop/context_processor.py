from .models import Catagory,Cart,Wishlist

def cat_context(request):
    cat_data = Catagory.objects.all()
    total = 0
    cart_data = 0
    wish_data = 0
    if request.user.is_authenticated:
        cart_data = Cart.objects.filter(u_id=request.user)
        wish_data = Wishlist.objects.filter(u_id=request.user)
        for i in cart_data:
            total += i.sub_total()
        print(total)
        cart_data = cart_data.count()
        wish_data = wish_data.count()


    return {'cat_data':cat_data,'cart_data':cart_data,'total':total,'wish_data':wish_data}