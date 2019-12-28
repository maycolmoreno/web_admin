from django.conf.urls import url, include
from . import views


from django.conf.urls import url  # (,include) le quite
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout_then_login
from iglesia import views

urlpatterns = [
    # url(r'^admin/usuario/', Personalist.as_view(), name='listapersona'),
    url(r'^register/$', views.mostrar_register, name='register'),

    
]
