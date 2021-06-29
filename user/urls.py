from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_view, name='product'),
    path('addproduct/', views.add_product, name='add_product'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('addpost/', views.addpost, name='addpost'),
    path('updatepost/<int:id>/', views.updatepost, name='updatepost'),
    path('deletepost/<int:id>/', views.deletepost, name='deletepost'),

]


