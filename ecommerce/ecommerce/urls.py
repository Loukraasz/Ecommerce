from django.contrib import admin
from ecommerceApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login, name="login"),
    path('cad/',views.cad , name="cad"),
    path("platform/",views.platform, name="platform"),
    path("passwordChange/", views.passwordChange, name="passwordChange"),
    path("passwordChange/confirmedEmail/", views.confirmedEmail, name="confirmedEmail"),
    path("passwordChange/newPassword/", views.newPassword, name="newPassword"),
    path("platform/court/", views.court, name="court"),
    path("platform/downshifter/", views.downshifter, name="downshifter"),
    path("platform/max/", views.max, name="max"),
    path("platform/revolution/", views.revolution, name="revolution"),
    path("platform/excee/", views.excee, name="excee"),
    path("platform/court/specs", views.court_specs, name="court_specs"),
    path("platform/excee/specs", views.excee_specs, name="excee_specs"),
    path("platform/max/specs", views.max_specs, name="max_specs"),
    path("platform/downshifter/specs", views.downshifter_specs, name="downshifter_specs"),
    path("platform/revolution/specs", views.revolution_specs, name="revolution_specs"),
]
