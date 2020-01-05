# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib.auth import login as do_login
from django.views.generic import *
from django.shortcuts import redirect
from django.core.mail import send_mail
from django import forms 
from .forms import *
from .models import *


# FRONTEND.

def mostrar_inicio(request):
	return render(request, 'backend/index.html', {})

def mostrar_about(request):
    return render(request, 'backend/about.html', {})


def mostrar_contact(request):
    return render(request, 'backend/contact.html', {})

def mostrar_administracion(request):
	return render(request, 'admin/index.html', {})
def list_usuario(request):
    return render(request, 'admin/list_usuario.html', {})

def contacto(request):
	titulo = "Contacto"
	formulario = ContactForm(request.POST or None)
	if formulario.is_valid():

		form_email = formulario.cleaned_data.get("email")
		form_mensaje = formulario.cleaned_data.get("mensaje")
		form_nombre = formulario.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)

			# print email, mensaje, nombre
	context = {
		"formulario": formulario,
		"titulo": titulo,
	}
	return render(request, "backend/contact.html", context)
class Registro_Usuario(CreateView):
    model = User
    template_name = "login/registration.html"
    form_class= UserCreationForm
    success_url = reverse_lazy('administracion')
    
class Personalist(ListView):
	model = Persona
	template_name = 'admin/list_usuario.html'
	


class Crear_Usuario(CreateView):
    model = Persona
    template_name = "admin/crear_usuario.html"
    form_class = PersonaForm
    success_url = reverse_lazy('administracion')
