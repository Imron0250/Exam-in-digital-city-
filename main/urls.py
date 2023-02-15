from django.urls import path
from .views import *

urlpatterns = [
    # path("login/", login_view),
    path("get-slider/", get_slider),
    path("get_category/", get_category),
    path('get_product/', get_product),
    path("get-service/", get_service),
    path('login/', login_view),
    path('register/', register),
    path('clearcard/', clearcard),
    path("get-ad-product/", get_ad_product),
    path("get-product-by-category/<int:pk>/", get_product_by_category),
    path("get-blog/", get_blog),
    path("get-single-product/<int:pk>/", get_single_product),
    path('get-team/', get_team),
    path('get-client-say/', get_client_say),
    path('get-partner/', get_partner),
    path('create-emails/', create_emails),
    path('get-info/', get_info),
    path('get-product-by-price/', get_product_by_price),
    path('get-faq/', get_faq),
    path('serach-product/', search_producy),
    path('get-product-by-reating/', get_product_by_reating),
    path('send-message/', send_message),
    path('register/', register),
    path('add-wishlist/', add_wishlist),
    path('delete-wishlist/<int:pk>/', wishlist_delete),
    path('add-card/', add_card),
    path('card-delete/<int:pk>/', card_delete),
    path('card-edit/<int:pk>/', card_edit),
    path('create-order/', create_order),
    path('get-order/', get_order),
    path('get-order-items/<int:pk>/', get_order_items),
    path('get-wishlist/', get_wishlist),
    path('edit-user-info/', edit_user_info),

    
]

create_order
get_order
get_order_items
edit_user_info