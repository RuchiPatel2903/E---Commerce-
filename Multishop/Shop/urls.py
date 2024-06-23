from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.cart,name='cart'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('catagory/<int:id>',views.cat_prod,name='cat_prod'),
    path('prod-details/<int:id>',views.prod_details,name='prod_details'),
    path('add-cart/<int:id>',views.add_cart,name='add_cart'),
    path('delete-cart/<int:id>',views.delete_cart,name='delete_cart'),
    path('minus-cart/<int:id>',views.minus_cart,name='minus_cart'),
    path('plus-cart/<int:id>',views.plus_cart,name='plus_cart'),
    path('wish-list/',views.wish_list,name='wish_list'),
    path('add-wish/<int:id>',views.add_wish,name='add_wish'),
    path('delete-wish/<int:id>',views.delete_wish,name='delete_wish'),
    path('confirm-order/<int:id>',views.confirm_order,name='confirm_order'),
    path('order-history/',views.order_history,name='order_history'),
    path('search/', views.search, name='search'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
