from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError
from .managers import CustomUserManager  # Importa el administrador personalizado

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("Nombre"), max_length=100)
    last_name = models.CharField(_("Apellido"), max_length=100)
    email = models.EmailField(_("Correo Electrónico"), max_length=254, unique=True)
    documento = models.CharField(_("Documento"), max_length=20, unique=True)
    is_staff = models.BooleanField(_("Es parte del Staff"), default=False)
    is_active = models.BooleanField(_("Activo"), default=False)
    date_joined = models.DateTimeField(_("Fecha de Registro"), auto_now_add=True)
    letra_diferenciadora = models.CharField(_("Letra Diferenciadora"), max_length=1, blank=True, null=True)

    USERNAME_FIELD = "documento"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    objects = CustomUserManager()  # Usa el administrador personalizado definido en managers.py

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.documento

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
