from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
import re

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Debes proporcionar un correo electrónico válido"))
        
    def create_user(self, documento, password=None, **extra_fields):
        if not documento:
            raise ValueError(_("El campo de documento es obligatorio."))
        
        if not re.match(r'^\S*[0-9]\S*$', documento):
            raise ValidationError(_("El campo de documento debe contener al menos un número válido y no debe tener espacios en blanco."))
        
        user = self.model(
            documento=documento,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)

        return user
    
    def create_superuser(self, documento, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Los superusuarios deben tener is_superuser=True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Los superusuarios deben tener is_staff=True"))
        
        if not password:
            raise ValueError(_("Los superusuarios deben tener una contraseña"))

        user = self.create_user(documento, password, **extra_fields)
        user.save()

        return user
