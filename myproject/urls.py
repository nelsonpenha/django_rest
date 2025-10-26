from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import EstudianteViewSet, CarreraViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet, basename='estudiante')
router.register(r'carreras', CarreraViewSet, basename='carrera')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # OpenAPI schema (JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # --- NUEVOS ENDPOINTS DE AUTENTICACIÓN ---
    # INICIO DE SESIÓN (LOGIN): Obtiene access y refresh tokens
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # REFRESCAR TOKEN: Obtiene un nuevo access token usando el refresh token
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # RUTAS DE USUARIOS (Registro, Logout, Test Protegido)
    # Incluimos el users/urls.py bajo el prefijo /api/auth/
    path('api/auth1/', include('users.urls')),
    # ---------------------------------------
]
