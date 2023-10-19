from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairView(TokenObtainPairView):
       # Personaliza la respuesta del token de acceso
       def post(self, request, *args, **kwargs):
           response = super().post(request, *args, **kwargs)
           # Personaliza la respuesta aquí si es necesario
           return response

class MyTokenRefreshView(TokenRefreshView):
       # Personaliza la respuesta del token de actualización
       def post(self, request, *args, **kwargs):
           response = super().post(request, *args, **kwargs)
           # Personaliza la respuesta aquí si es necesario
           return response
