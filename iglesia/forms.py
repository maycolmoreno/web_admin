# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ('id_persona', 'nombre', 'apellido',
		          'cedula', 'direccion', 'telefono')
		widgets = {'id_persona': forms.HiddenInput()}

# class ClienteForm(forms.ModelForm):
# 	class Meta:
# 		model = Cliente
# 		fields = ('id_cliente','nombre','apellidos', 'cedula','direccion','telefono','estado','nacionalidad','email')

# 		widgets = {'id_cliente': forms.HiddenInput()}



class UsuarioForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('id','username', 'password', 'email')
		widgets = {'id': forms.HiddenInput(),'password': forms.PasswordInput(),}

class RegistroForm(UserCreationForm):
	email = forms.EmailField(required=True)
    	class Meta:
    		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2',
				'groups',
				'is_superuser',
				'is_active',
			]
		labels ={
				'username':'Nombre de Usuario',
				'first_name':'Nombre' ,
				'last_name':'Apellidos',
				'email': 'Correo',
				'groups': 'Rol',
				# 'is_superuser': 'SuperUser',
				'is_active': 'Estado',
			}
		def save(self, commit=True):
					user = super(RegistroForm, self).save(commit=False)
					user.email = self.cleaned_data["email"]
					if commit:
						user.save()
					return user
# class ProductoForm(forms.ModelForm):
# 	class Meta:
# 		model = Producto
# 		fields = [
# 			'nombre','marca','stock','precio_compra','precio_venta','categoria']
# 		labels ={
# 			'nombre': 'Nombre del producto',
# 			'marca': 'Marca del producto',
# 			'stock': 'Stock',
# 			'precio_compra': 'Precio compra',
# 			'precio_venta': 'Precio venta',
# 			'fecha' : 'Fecha',
# 			'categoria': 'Categoria',
#  		}
# 		widgets = {
# 			'nombre': forms.TextInput(attrs={'class':'form-control'}),
# 			'marca': forms.TextInput(attrs={'class':'form-control'}),
# 			'stock': forms.TextInput(attrs={'class':'form-control'}),
# 			'precio_compra': forms.TextInput(attrs={'class':'form-control'}),
# 			'precio_venta': forms.TextInput(attrs={'class':'form-control'}),
# 			'fecha': forms.DateInput(),
# 		}
# class TipoProductoForm(forms.ModelForm):
# 	class Meta:
# 		model = Categoria_Producto

# 		fields = [
# 			'tipo_prod'
# 		]
# 		labels ={
# 			'tipo_prod': 'Categoria'
# 		}
# 		widgets = {
# 			'tipo_prod': forms.TextInput(attrs={'class':'form-control'}),
# 		}

# class HabitacionForm(forms.ModelForm):
#     	class Meta:
# 		model = Habitacion
# 		fields = [
# 			'numero_habitacion','piso_habitacion','estado_habitacion','tipohabitacion']
# 		labels ={
# 			'numero_habitacion': 'Numero habitacion',
# 			'piso_habitacion': 'Piso habitacion',
# 			 'estado_habitacion': 'Estado habitacion',
# 			'tipohabitacion': 'Tipo habitacion'

# 		}
# 		widgets = {
# 			'numero_habitacion': forms.TextInput(attrs={'class':'form-control'}),
# 			'piso_habitacion': forms.TextInput(attrs={'class':'form-control'}),
# 		}
# class Tipo_HabitacionForm(forms.ModelForm):
#     	class Meta:
# 		model = TipoHabitacion
# 		fields = [
# 			'nombre_tipo','precio_tipo', 'imagen', 'nro_personas','descripcion']
# 		labels ={
# 			'nombre_tipo': 'Nombre',
# 			'precio_tipo': 'Precio',

# 		}
# 		widgets = {
# 			'nombre_tipo': forms.TextInput(attrs={'class':'form-control'}),
# 			'precio_tipo': forms.TextInput(attrs={'class':'form-control'}),
# 			'imagen': forms.FileInput(attrs={'class':'form-control'}),
# 		}

# class RegModelForm(forms.ModelForm):
# 	class Meta:

# 		fields = ["nombre","apellidos","cedula_identidad","email","telefono","direccion"]

# 		def clean_email(self):
# 			email = self.cleaned_data.get("email")
# 			email_base, proveeder = email.split("@")
# 			dominio, extension = proveeder.split(".")
# 			if not extension == "com":
# 				raise forms.ValidationError("Por favor utiliza un email con la extension .com")
# 			return email


# 		def clean_nombre(self):
# 			nombre = self.cleaned_data.get("nombre")
# 			return nombre

# class ContactForm(forms.Form):
# 	nombre = forms.CharField(required=False)
# 	email = forms.EmailField()
# 	mensaje = forms.CharField(widget=forms.Textarea)

# class GestiocontenidoForm(forms.ModelForm):
#     	class Meta:
# 		model = GestionContenido

# 		fields = '__all__'
# 		labels ={
# 			'image': 'Imagen',
# 			'titulo': 'Titulo',
# 			'descipcion': 'Descripcion',
# 		}
# 		widgets = {
# 			'titulo': forms.TextInput(attrs={'class':'form-control'}),
# 			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
# 		}


# class VentaForm(forms.ModelForm):

# 	class Meta:
# 		model = Venta

# 		fields = [ 'fecha', 'id_reserva', 'subtotal', 'iva','descuento','total', 'numero_factura', 'estado_factura', 'id_persona'
# 		]

# 		labels ={
# 		'numero_factura':'Nro Venta',
# 		'estado_factura':'Estado',
# 		'fecha':'Fecha',
# 		'id_reserva':'Reserva',
# 		'id_persona':'Cliente',
# 		'subtotal':'subtotal',
# 		'iva':'IVA',
# 		'descuento': 'Descuento',
# 		'total':'Total',

# 		}

# 		widgets = {
# 		'nro_venta': forms.TextInput(attrs={'class':'form-control'}),
# 		'fecha_venta': forms.DateInput(),
# 		}
# class ImageForm(forms.ModelForm):
# 	class Meta:
# 		model = GestionContenido
# 		fields = '__all__'


