from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label = 'Contaseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contaseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden.')

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Nombre de usuario',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'username'
            }
        )
    )

    password = forms.CharField(
        label = 'Contaseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('El nombre de usuario o la contraseña no es correcta')

        return self.cleaned_data

class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label = 'Contaseña actual',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña actual'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contaseña nueva',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña nueva'
            }
        )
    )

class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            # Verificamos si el codigo y el id son validos
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('El código no es correcto')
        else:
            raise forms.ValidationError('El código no es correcto')