# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.views.generic import ListView
from django.shortcuts import redirect
from django import forms 
from .forms import *
from .models import *


# FRONTEND.

def mostrar_inicio(request):
	return render(request, 'backend/index.html', {})

def mostrar_administracion(request):
	return render(request, 'admin/index.html', {})


# def login(request):
#     return render(request, "login/login.html", {})
def mostrar_register(request):
	form = PersonaForm(request.POST or None)
	user = UsuarioForm(request.POST or None)

	context = {
		"form":form,
		"formu":user
		}

	if request.method == "POST":
		form = PersonaForm(request.POST or None,request.FILES or None, initial = {"id_persona" : "0"})
		formu = UsuarioForm(request.POST or None,  request.FILES or None, initial = {"id" : "0"})
		if form.is_valid() and formu.is_valid():
			print("lleuw aqui")

			user = formu.save()
			print("Guardo")
			#form.user = User.objects.last()
			user.set_password(user.password)
			user.save()
			persona = form.save(commit = False)
			print("Guardoe")
			persona.user = user
			print("Guardo12")
			persona.save()
			return redirect('auth_login')
	else:
		#form = PersonaForm()
		return render(request, "login/registration.html", {'form': form})

class Personalist(ListView):
	model = Persona
	template_name = 'admin/index.html'
=======

# Create your views here.
>>>>>>> 28fbe43d511371f5e8b87cfc926238a44b3c3d84
