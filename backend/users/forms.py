from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["documento", "first_name", "last_name","email"]  # Incluye el campo 'documento' en el formulario de creación
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ["documento", "first_name", "last_name","email"]  # Incluye el campo 'documento' en el formulario de cambio
        error_class = "error"
