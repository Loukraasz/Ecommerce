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
    path("passwordChange/confirmedEmail/", views.confirmedEmail, name="confirmedEmail"),
    path("passwordChange/newPassword/", views.newPassword, name="newPassword"),
    path("court/", views.court, name="court"),
    path("downshifter/", views.downshifter, name="downshifter"),
    path("max/", views.max, name="max"),
    path("revolution/", views.revolution, name="revolution"),
    path("excee/", views.excee, name="excee"),
    path("teste/", views.teste, name="teste")
]
