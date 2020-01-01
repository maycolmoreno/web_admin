from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout_then_login
from iglesia import views

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    # url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.mostrar_inicio, name='index'),
    url(r'^admin', views.mostrar_administracion, name='administracion'),

    url(r'login', login, {'template_name': 'login/login.html'}, name='auth_login'),
    
    url(r'', include('iglesia.urls')),
]
