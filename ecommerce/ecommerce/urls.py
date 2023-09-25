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
    path("court/specs", views.court_specs, name="court_specs"),
    path("excee/specs", views.excee_specs, name="excee_specs"),
    path("max/specs", views.max_specs, name="max_specs"),
    path("downshifter/specs", views.downshifter_specs, name="downshifter_specs"),
    path("revolution/specs", views.revolution_specs, name="revolution_specs"),
]
