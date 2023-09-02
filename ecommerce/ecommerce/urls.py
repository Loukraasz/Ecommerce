from django.contrib import admin
from ecommerceApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('login/',views.login , name="login"),
    path('cad/',views.cad , name="cad"),
]
