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
from iglesia.views import *

urlpatterns = [
    url(r'^admin/usuario/', views.Personalist, name='listapersona'),
    url(r'^register/', Registro_Usuario.as_view(), name='register'),
    url(r'^about/$', views.mostrar_about, name='about'),
    url(r'^contact/$', views.contacto, name='contact'),
    url(r'^admin/listuser/$', Personalist.as_view(), name='list_usuario'),
    url(r'^admin/createuser/$', Crear_Usuario.as_view(), name='creat_user'),
    url(r'^admin', views.mostrar_administracion, name='administracion'),
    
]
