from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('category/<int:id_category>/', views.category, name='category'),
    path('product/<int:id_product>/', views.product, name='product'),
    path('product/edit/<int:id_product>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:id_product>/', views.delete_product, name='delete_product'),
    path('product/basket/<int:id_user>/', views.basket, name='basket'),
    # path('product/add_product_to_basket/<int:id_product>/', views.add_product_to_basket, name='add_product_to_basket'),
    # path('product/delete_product_with_basket/<int:id_basket>/', views.delete_product_with_basket, name='delete_product_with_basket'),
    path('logout/', views.logout, name='logout'),
]
