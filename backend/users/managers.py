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
        
    def create_user(self, documento,first_name, last_name, email, password=None, **extra_fields):
        if not first_name:
            raise ValueError(_("Los usuarios deben proporcionar nombre"))
        
        if not last_name:
            raise ValueError(_("Los usuarios deben proporcionar apellido"))
        
        if not documento:
            raise ValueError(_("El campo de documento es obligatorio."))
        
        if not re.match(r'^\S*[0-9]\S*$', documento):
            raise ValidationError(_("El campo de documento debe contener al menos un número válido y no debe tener espacios en blanco."))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Se requiere una dirección de correo electrónico."))
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            documento=documento,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)

        return user
    
    def create_superuser(self, documento, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Los superusuarios deben tener is_superuser=True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Los superusuarios deben tener is_staff=True"))
        
        if not password:
            raise ValueError(_("Los superusuarios deben tener una contraseña"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Se requiere una dirección de correo electrónico."))
        
        user = self.create_user(first_name, last_name, email, documento, password, **extra_fields)
        user.save()

        return user
