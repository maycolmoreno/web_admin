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
from iglesia.views import Registro_Usuario

urlpatterns = [
    # url(r'^admin/usuario/', Personalist.as_view(), name='listapersona'),
    url(r'^register/', Registro_Usuario.as_view(), name='register'),
    url(r'^about/$', views.mostrar_about, name='about'),
    url(r'^contact/$', views.contacto, name='contact'),
    url(r'^admin/listuser/$', views.list_usuario, name='list_usuario'),
    
]
