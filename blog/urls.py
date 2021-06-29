from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    url(r'^', include('product.urls')),

]