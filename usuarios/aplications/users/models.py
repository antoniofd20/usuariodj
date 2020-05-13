from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
# ¡Checar linea 94 base.py! 

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    username = models.CharField('Nombre de usuario', max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField('Nombre(s)', max_length=30, blank=True)
    apellidos = models.CharField('Apellidos', max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    # Si agrego un campo puedo poner default='algo'
    codregistro = models.CharField(max_length=6, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

    """ Usuarios que he escrito:
        Antonio --> superuser
        Usuario2 --> user """