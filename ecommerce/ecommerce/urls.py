from django.contrib import admin
from ecommerceApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('login/',views.login , name="login"),
    path('cad/',views.cad , name="cad"),
    path("platform/",views.platform, name="platform"),
    path("passwordChange/", views.passwordChange, name="passwordChange"),
    path("passwordChange/confirmedEmail", views.confirmedEmail, name="confirmedEmail"),
    path("passwordChange/newPassword", views.newPassword, name="newPassword")
]
